# AOS-3 Notebook Migration Inventory Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to execute this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Создать одну exact, decision-ready карту переноса документации из текущего `NMF13579/notebook` в будущий репозиторий `AOS-3` без создания целевого репозитория и без переноса файлов.

**Architecture:** Read-only inventory связывает каждый релевантный source file с текущей identity, authority class, целевой ролью и одной migration action. Результатом является только `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`; он отделяет current canonical/accepted sources от working history и archived reference, выявляет competing owners и не создаёт target files.

**Tech Stack:** Markdown, Git read-only inspection, `rg`, `find`, `wc`, `shasum -a 256`, Ruby standard library для механических проверок.

## Global Constraints

- Governing repository: `/Users/muhammed/Documents/GitHub/notebook`.
- Accepted design input: `workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md`, 29,895 bytes, SHA-256 `44f495d70c9482192b3f374120198351d11d717c1e348d5c270c7a394ff74839`.
- Root-agent candidate input: `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md`, 16,074 bytes, SHA-256 `e89351a85f191a964d6a33ab7311685c7bee28c57c04656ddcd3824fd3d259e7`.
- Future execution may create only `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md` unless a later human instruction expands the boundary.
- The source repository and every source document are read-only during plan execution.
- Repository `AOS-3` creation, directory scaffolding, source copying, moving, renaming and deletion are forbidden.
- `AOS/portable/` is the starting product-package source; it is not modified during inventory.
- `archive/aos-archive/` has reference authority only and cannot become a target source automatically.
- Each included source file must have exact bytes and SHA-256; group-only claims do not replace the file inventory appendix.
- Each source must receive exactly one action: `MOVE`, `ADAPT`, `REFERENCE` or `EXCLUDE`.
- `MOVE` means byte-preserving target placement is proposed; `ADAPT` means new target bytes and a new review subject will be required.
- No row may claim that historical status, PASS or repository presence creates current authority.
- No technology stack, implementation repository, runtime algorithm implementation or release policy is selected by this plan.
- Human acceptance, implementation authorization and Git authorization remain `NOT_RUN` or `NONE`.
- Commit, Push, Merge and Release are not plan steps.

---

## Planned output

### Only file created during future execution

- Create: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

### Required responsibilities of the map

The map must contain:

1. exact repository snapshot and clean/dirty observation;
2. exact identity of this plan and the accepted design specification;
3. complete file inventory appendix for the inspected source boundary;
4. classification and migration action for every included file;
5. target repository tree at role level;
6. primary source selection for every target owner;
7. duplicate/competing-owner findings;
8. excluded history with concise reasons;
9. open decisions that block actual migration;
10. one next bounded action.

### Required row schema

The inventory appendix must contain exactly one Markdown table between the
literal whole-line markers `<!-- INVENTORY_TABLE_START -->` and
`<!-- INVENTORY_TABLE_END -->`:

```markdown
<!-- INVENTORY_TABLE_START -->
| source_path | source_bytes | source_sha256 | source_status | source_authority | source_role | target_role | proposed_target_path | action | reason | conflict_or_dependency | provenance_required |
|---|---:|---|---|---|---|---|---|---|---|---|---|
<!-- One populated row per inspected regular file; table cells must not contain a literal pipe character. -->
<!-- INVENTORY_TABLE_END -->
```

The explanatory comment is replaced by actual rows during map construction;
it is not retained in a review candidate.

Allowed `source_role` values:

```text
CURRENT_CANONICAL
ACCEPTED_PORTABLE_PRODUCT
ACCEPTED_SUPPORTING_PACKAGE
WORKING_DRAFT
AUDIT_OR_DECISION_EVIDENCE
ARCHIVED_REFERENCE
CONTROLLER_OR_PROCESS_HISTORY
UNIQUE_RESEARCH_OR_LESSON
```

Allowed `target_role` values:

```text
AOS3_ROOT
AOS3_DOCS
AOS_PRODUCT
AOS_PRODUCT_ROOT_PAYLOAD
AOS3_DEVELOPMENT
AOS3_TEST_REFERENCE
PROVENANCE_ONLY
NO_TARGET
```

---

### Task 1: Bind the exact source snapshot and create the map skeleton

**Files:**

- Read: `AGENTS.md`
- Read: `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md`
- Read: `docs/00_Core.md`
- Read: `workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md`
- Create: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

**Interfaces:**

- Consumes: current repository observation and the accepted design specification.
- Produces: map sections `Execution boundary`, `Repository snapshot`, `Classification vocabulary`, `Inventory appendix`, `Findings`, `Open decisions`, `Next action`.

- [ ] **Step 1: Reproduce the design-spec identity**

Run:

```bash
wc -c workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md
shasum -a 256 workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md
```

Expected:

```text
29895 workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md
44f495d70c9482192b3f374120198351d11d717c1e348d5c270c7a394ff74839  workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md
```

Stop with `BLOCKED_SPEC_IDENTITY_MISMATCH` if either value differs.

- [ ] **Step 2: Record repository identity without mutation**

Run each command separately:

```bash
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short --branch
git rev-parse --abbrev-ref --symbolic-full-name @{upstream}
```

Expected: repository root is `/Users/muhammed/Documents/GitHub/notebook`; branch, HEAD, upstream and all pre-existing status paths are copied exactly into the map. A dirty tree is evidence, not automatic permission to modify or clean it.

- [ ] **Step 3: Create the map with explicit safe initial status**

Create `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md` using `apply_patch`. Its frontmatter must contain exactly these safe semantics:

```yaml
document_id: AOS3-NOTEBOOK-MIGRATION-MAP-R1
status: DRAFT
authority: NONE
source_repository: NMF13579/notebook
target_repository: UNCREATED_AOS_3
migration_execution: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Add the required sections listed under `Planned output`. Do not add target content files or empty target directories.

- [ ] **Step 4: Confirm the write boundary immediately**

Run:

```bash
git status --short
```

Expected: the only new path created by this plan execution is `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`; the already-present specification remains unchanged. Stop if any source path changed.

---

### Task 2: Inventory current canonical and repository-rule owners

**Files:**

- Read: `AGENTS.md`
- Read: `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md`
- Read: `docs/00_Core.md`
- Read: `docs/01_Product.md`
- Read: `docs/02_Architecture.md`
- Read: `docs/03_Development.md`
- Read: `docs/04_Lessons.md`
- Read: `docs/05_Reference.md`
- Read: `docs/06_Features.md`
- Modify: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

**Interfaces:**

- Consumes: repository rules and accepted canonical owner set.
- Produces: eight exact `CURRENT_CANONICAL` inventory records, one exact root-agent candidate record and a target-owner recommendation for `AOS3_ROOT` or `AOS3_DOCS`.

- [ ] **Step 1: Enumerate the exact canonical set**

Run:

```bash
find docs -maxdepth 1 -type f -print
```

Expected after bytewise sorting: exactly the seven paths named in this task. Record any extra or missing canonical `.md` path as a finding; do not repair it.

- [ ] **Step 2: Compute exact identities**

Run separately for `AGENTS.md`, the root-agent candidate and the seven
`docs/*.md` files:

```bash
wc -c AGENTS.md workspace/AOS3_ROOT_AGENTS_CANDIDATE.md docs/00_Core.md docs/01_Product.md docs/02_Architecture.md docs/03_Development.md docs/04_Lessons.md docs/05_Reference.md docs/06_Features.md
shasum -a 256 AGENTS.md workspace/AOS3_ROOT_AGENTS_CANDIDATE.md docs/00_Core.md docs/01_Product.md docs/02_Architecture.md docs/03_Development.md docs/04_Lessons.md docs/05_Reference.md docs/06_Features.md
```

Copy the observed bytes and SHA-256 values into individual inventory rows.
The root-agent candidate must reproduce the identity declared in Global
Constraints; otherwise stop with `BLOCKED_ROOT_AGENTS_CANDIDATE_DRIFT`.

- [ ] **Step 3: Classify authority and proposed targets**

Use these mapping rules:

| Source | Proposed target role | Action rule |
|---|---|---|
| `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md` | `AOS3_ROOT` | `MOVE` byte-for-byte to future `AOS-3/AGENTS.md` after target creation is separately authorized |
| `AGENTS.md` | `AOS3_ROOT` | `REFERENCE`, because notebook repository rules cannot be copied as AOS-3 rules and the corrected candidate is the primary source |
| `docs/00_Core.md` | `AOS3_DOCS` | `ADAPT`, retaining project identity/authority semantics but changing repository binding |
| `docs/01_Product.md` | `AOS3_DOCS` | `ADAPT` into AOS product-definition owner |
| `docs/02_Architecture.md` | `AOS3_DOCS` | `ADAPT` into AOS-3 system-architecture owner |
| `docs/03_Development.md` | `AOS3_DOCS` | `ADAPT` into AOS-3 development-process owner |
| `docs/04_Lessons.md` | `AOS3_DEVELOPMENT` | `ADAPT` or `REFERENCE` per lesson relevance; do not copy all lessons automatically |
| `docs/05_Reference.md` | `AOS3_DEVELOPMENT` | `ADAPT` as research routing, excluding notebook-only paths |
| `docs/06_Features.md` | `AOS3_DOCS` | `ADAPT` as product feature source; preserve item dispositions and classifications |

Record these as proposed actions, not completed migration.

- [ ] **Step 4: Record canonical conflicts and open decisions**

At minimum check for:

- notebook-specific repository names and paths;
- `implementation_repository: UNASSIGNED`;
- WHAT/HOW boundary that must be revised only after a separate AOS-3 engineering decision;
- current source precedence that names `docs/` as the active notebook package;
- target root files whose exact content is not selected yet.

Add exact source locators for each finding.

---

### Task 3: Inventory the accepted portable product and its acceptance evidence

**Files:**

- Read: `AOS/portable/AGENTS.md`
- Read: `AOS/portable/README.md`
- Read: `AOS/portable/00_PROJECT_CORE.md`
- Read: `AOS/portable/01_PRODUCT_MODEL.md`
- Read: `AOS/portable/02_ARCHITECTURE_CONTRACTS.md`
- Read: `AOS/portable/03_ENGINEERING_WORKFLOW.md`
- Read: `AOS/portable/04_FEATURE_SPECIFICATIONS.md`
- Read: `AOS/portable/05_USER_JOURNEYS_AND_UX.md`
- Read: `AOS/portable/06_PROJECT_ROADMAP.md`
- Read: `AOS/portable/07_DECISION_REGISTER.md`
- Read: `AOS/portable/08_TRACEABILITY.md`
- Read: `AOS/portable/MANIFEST.txt`
- Read: `AOS/portable/PACKAGE_ACCEPTANCE.yaml`
- Read: `workspace/audits/AOS_PORTABLE_1E3746B4_AUDIT.md`
- Modify: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

**Interfaces:**

- Consumes: accepted exact portable package, manifest, audit and acceptance sidecar.
- Produces: thirteen file records classified as `ACCEPTED_PORTABLE_PRODUCT`, one supporting audit record, reproduced candidate identity and the initial `AOS_PRODUCT` source set.

- [ ] **Step 1: Verify manifest-bound membership**

Run:

```bash
find AOS/portable -maxdepth 1 -type f -print
wc -c AOS/portable/MANIFEST.txt
shasum -a 256 AOS/portable/MANIFEST.txt
```

Expected manifest identity:

```text
bytes: 1015
sha256: 1e3746b4bb6a326d9e93f805cb4ebe8a233c367976189aae1c0d385cde261901
```

The manifest binds eleven Markdown content files and excludes itself and `PACKAGE_ACCEPTANCE.yaml`. If the identity or membership differs, stop with `BLOCKED_PORTABLE_IDENTITY_MISMATCH`.

- [ ] **Step 2: Verify the package acceptance binding**

Inspect `AOS/portable/PACKAGE_ACCEPTANCE.yaml` and reproduce the bound audit:

```bash
wc -c workspace/audits/AOS_PORTABLE_1E3746B4_AUDIT.md
shasum -a 256 workspace/audits/AOS_PORTABLE_1E3746B4_AUDIT.md
```

Expected audit identity:

```text
bytes: 6994
sha256: 1f259d27a0f9456fd7c14880132d1ed6ddaf1a9c33b509727e61fddd0e04f87a
```

Record acceptance as fact-class scoped for the exact package, not as implementation or migration authority.

- [ ] **Step 3: Compute every portable-file identity**

Run:

```bash
find AOS/portable -maxdepth 1 -type f -exec wc -c {} +
find AOS/portable -maxdepth 1 -type f -exec shasum -a 256 {} +
```

Record an individual inventory row for each of the thirteen files. Do not infer file identity only from the package manifest.

- [ ] **Step 4: Assign product migration actions**

Use these rules:

- manifest-bound Markdown content: `MOVE` only for byte-preserving seed placement; otherwise `ADAPT` with new candidate identity required;
- `MANIFEST.txt`: `ADAPT`, because any new `root/`, tools, templates or path set requires regeneration;
- `PACKAGE_ACCEPTANCE.yaml`: `PROVENANCE_ONLY`, not transferable acceptance for changed AOS-3 bytes;
- portable audit: `PROVENANCE_ONLY`;
- embedded `DRAFT`/`NONE` source fields remain historical source fields until a new exact AOS-3 package is reviewed.

Proposed product target root is `AOS-3/aos/`. Do not create it during this task.

---

### Task 4: Inventory accepted supporting design packages without creating competing owners

**Files:**

- Read: `AOS/README.md`
- Read: `AOS/01_PRODUCT_MODEL.md`
- Read: `AOS/02_ARCHITECTURE_CONTRACTS.md`
- Read: `AOS/03_ENGINEERING_PIPELINE.md`
- Read: `AOS/GLOBAL_DESIGN_FREEZE.md`
- Read: `AOS/decisions/GLOBAL_DESIGN_PACKAGE_ACCEPTANCE.md`
- Read: `AOS/reviews/GLOBAL_DESIGN_PACKAGE_REVIEW.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/README.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/CANDIDATE_MANIFEST.txt`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/00_PROJECT_CORE.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/01_PRODUCT_MODEL.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/02_ARCHITECTURE_CONTRACTS.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/03_ENGINEERING_WORKFLOW.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/04_FEATURE_SPECIFICATIONS.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/05_USER_JOURNEYS_AND_UX.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/06_PROJECT_ROADMAP.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/07_DECISION_REGISTER.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/08_TRACEABILITY_AND_REVIEW.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2_HUMAN_DECISION_RECORD.yaml`
- Read: `workspace/audits/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2_COMPLETENESS_RE_AUDIT.md`
- Read: `workspace/AOS_DOCUMENTATION_X1/CANDIDATE_MANIFEST.txt`
- Read: `workspace/AOS_DOCUMENTATION_X1/HUMAN_DECISION_RECORD.yaml`
- Read: `workspace/audits/AOS_DOCUMENTATION_X1_CANDIDATE_1F0D12C3_AUDIT.md`
- Modify: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

**Interfaces:**

- Consumes: global design, full-project R2 and X1 accepted supporting sources.
- Produces: exact supporting-package identities, overlap matrix against `docs/` and `AOS/portable/`, and `REFERENCE`/`PROVENANCE_ONLY` actions unless unique accepted content requires `ADAPT`.

- [ ] **Step 1: Reproduce package identities from their manifests and records**

Run:

```bash
wc -c workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/CANDIDATE_MANIFEST.txt
shasum -a 256 workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/CANDIDATE_MANIFEST.txt
wc -c workspace/AOS_DOCUMENTATION_X1/CANDIDATE_MANIFEST.txt
shasum -a 256 workspace/AOS_DOCUMENTATION_X1/CANDIDATE_MANIFEST.txt
```

Expected identities:

```text
R2 manifest: 5930 bytes, sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
X1 manifest: sha256:1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d
```

If a reported identity is not reproducible, classify it as a finding rather than carrying its status forward.

- [ ] **Step 2: Compute file-level identities for every listed supporting source**

Use `wc -c` and `shasum -a 256` on each exact path in this task. Add individual inventory rows even when a file is already represented by a manifest.

- [ ] **Step 3: Build the overlap matrix**

For each supporting artifact, record whether its fact class is already owned by:

- `docs/00_Core.md`–`docs/06_Features.md`;
- `AOS/01_PRODUCT_MODEL.md`–`AOS/03_ENGINEERING_PIPELINE.md`;
- `AOS/portable/00_PROJECT_CORE.md`–`08_TRACEABILITY.md`.

Select one primary migration source per target fact class. Other sources become `REFERENCE` or `PROVENANCE_ONLY`; do not propose duplicate target owners.

- [ ] **Step 4: Preserve accepted decisions without carrying lifecycle machinery**

Record exact accepted decisions that materially constrain the future product. Classify authoring controllers, correction history and run-state files as `CONTROLLER_OR_PROCESS_HISTORY` unless they contain unique product facts not owned elsewhere.

---

### Task 5: Inspect archived AOS-3 material strictly as reference

**Files:**

- Read: `archive/aos-archive/README.md`
- Read: `archive/aos-archive/development-package/00_Control_and_Source_Precedence.md`
- Read: `archive/aos-archive/development-package/01_Product_and_Core_V1_Scope.md`
- Read: `archive/aos-archive/development-package/02_User_Journeys_and_Workflows.md`
- Read: `archive/aos-archive/development-package/03_Architecture_and_Decisions.md`
- Read: `archive/aos-archive/development-package/04_Runtime_and_Data_Contracts.md`
- Read: `archive/aos-archive/development-package/05_Quality_Recovery_and_Security.md`
- Read: `archive/aos-archive/development-package/06_Traceability_and_Readiness.md`
- Read: `archive/aos-archive/development-package/07_Implementation_Handoff.md`
- Read: `archive/aos-archive/development-package/decisions/DEC-ARCH-002_Architecture_and_Topology.md`
- Read: `archive/aos-archive/development-package/decisions/DEC-ARCH-003_Toolchain_and_Dependencies.md`
- Read: `archive/aos-archive/development-package/decisions/DEC-ARCH-004_Project_Memory.md`
- Read: `archive/aos-archive/development-package/decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md`
- Read: `archive/aos-archive/development-package/adapters/CODEX.md`
- Read: every path returned by `rg --files archive/aos-archive`
- Modify: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

**Interfaces:**

- Consumes: archived AOS-3 documentation and exact historical decisions.
- Produces: complete archive inventory appendix plus a short set of uniquely reusable reference findings; no archived file receives automatic product authority.

- [ ] **Step 1: Enumerate every archived path**

Run:

```bash
rg --files archive/aos-archive
```

Sort paths by UTF-8 bytes in the map appendix. Compute `wc -c` and SHA-256 for every regular file. A large archive may be represented by one inventory appendix, but each file still requires its own row and action.

- [ ] **Step 2: Read the bounded high-value architecture set first**

Read the exact named paths in this task before expanding into feature/function archives. Extract only:

- product constraints still absent from current owners;
- architecture options and their consequences;
- portable installation/update contracts;
- project-memory contracts relevant to `project/`;
- negative fixtures and reusable validation cases;
- unresolved conflicts that must not be silently selected.

- [ ] **Step 3: Classify all archive records**

Default actions:

- historical status, delivery and lifecycle records: `EXCLUDE` or `PROVENANCE_ONLY`;
- architecture/product documents overlapping current owners: `REFERENCE`;
- unique reusable research, lesson or negative fixture: `REFERENCE` with proposed `AOS3_DEVELOPMENT` or `AOS3_TEST_REFERENCE` role;
- archived executable validators/tests: `REFERENCE`, never direct runtime source without separate source audit;
- archived ideas/features/functions: grouped decision index plus file-level `REFERENCE`/`EXCLUDE` records, not automatic product scope.

- [ ] **Step 4: Check for conflict with the accepted Product-in-place design**

Record, without resolving automatically, any archived decision that assumes:

- a different repository topology;
- generated rather than directly maintained product output;
- no `aos/root/` payload;
- a different location for persistent project knowledge;
- selected language/framework/dependencies;
- broader autonomous execution or Git authority.

---

### Task 6: Resolve target-owner proposals and produce the decision table

**Files:**

- Read: all inventory rows created in Tasks 2–5
- Modify: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`

**Interfaces:**

- Consumes: exact file inventory, authority classifications and overlap findings.
- Produces: one proposed source chain for each target role and a decision-ready list of migration blockers.

- [ ] **Step 1: Build the target-role table**

Include these target roles exactly:

```text
AOS-3 root repository rules and navigation
AOS-3 docs product owner
AOS-3 docs system architecture owner
AOS-3 docs development-process owner
AOS-3 docs decisions and provenance
AOS-3 development research/legacy reference
AOS-3 development audits and migration evidence
AOS-3 tests reusable fixtures/reference
AOS-3 aos/ portable product seed
AOS-3 aos/root/ installation payload design source
AOS-3 aos/root/project/ project-documentation templates
```

For every role state one primary source, supporting sources, excluded competitors, migration action and required future review.

For `AOS-3 root repository rules and navigation`, use
`workspace/AOS3_ROOT_AGENTS_CANDIDATE.md` as the primary source and current
notebook `AGENTS.md` as supporting reference. The proposed operation is an exact
byte-preserving placement at `AOS-3/AGENTS.md`, not an edit of notebook root
rules.

- [ ] **Step 2: Enforce one-owner rules**

Flag `MIGRATION_CONFLICT_COMPETING_OWNER` when two sources are proposed as independent owners of the same fact class. Resolve only by recommending one primary source and preserving the other as supporting reference; do not rewrite source documents.

- [ ] **Step 3: Record migration blockers and decisions**

At minimum evaluate:

- exact new repository identity and visibility;
- Git-history strategy;
- license choice;
- root AOS-3 document names;
- exact initial `aos/` inventory;
- exact `aos/root/` payload inventory;
- whether each portable source file can `MOVE` byte-for-byte or needs `ADAPT`;
- which archived negative fixtures merit future test migration;
- implementation/toolchain decisions explicitly deferred by the specification.

Each item must be `RESOLVED_BY_SPEC`, `HUMAN_DECISION_REQUIRED`, `DEFER_TO_IMPLEMENTATION_DESIGN` or `NOT_APPLICABLE`; no blank status is allowed.

- [ ] **Step 4: State the recommended first migration candidate**

The recommendation must remain documentation-only and identify exact proposed source and target paths. It must not describe repository creation or copying as already authorized.

---

### Task 7: Verify completeness, identity and no-mutation evidence

**Files:**

- Read: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md`
- Read: every source path recorded in its inventory appendix
- Modify: `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md` only to correct map defects found before freezing its candidate identity

**Interfaces:**

- Consumes: completed migration-map candidate.
- Produces: mechanically checked map identity, coverage counts, limitations and exact final status proof.

- [ ] **Step 1: Check row completeness**

Run this exact Ruby standard-library checker. It parses the marker-bound
Markdown table and fails unless every row has all twelve required fields, a
unique `source_path`, one allowed `source_role`, one allowed `target_role` and
one allowed action:

```bash
ruby -e 's=File.read(ARGV[0], encoding: "UTF-8"); b=s[/^<!-- INVENTORY_TABLE_START -->\n(.*?)^<!-- INVENTORY_TABLE_END -->$/m,1] or abort("inventory markers missing"); lines=b.lines.map(&:strip).reject(&:empty?); abort("inventory table incomplete") if lines.length < 3; parse=->(line){line.sub(/^\|/,"").sub(/\|$/,"").split("|",-1).map(&:strip)}; header=parse.call(lines[0]); expected=%w[source_path source_bytes source_sha256 source_status source_authority source_role target_role proposed_target_path action reason conflict_or_dependency provenance_required]; abort("header mismatch") unless header==expected; rows=lines.drop(2).map{|line| parse.call(line)}; abort("inventory empty") if rows.empty?; roles=%w[CURRENT_CANONICAL ACCEPTED_PORTABLE_PRODUCT ACCEPTED_SUPPORTING_PACKAGE WORKING_DRAFT AUDIT_OR_DECISION_EVIDENCE ARCHIVED_REFERENCE CONTROLLER_OR_PROCESS_HISTORY UNIQUE_RESEARCH_OR_LESSON]; targets=%w[AOS3_ROOT AOS3_DOCS AOS_PRODUCT AOS_PRODUCT_ROOT_PAYLOAD AOS3_DEVELOPMENT AOS3_TEST_REFERENCE PROVENANCE_ONLY NO_TARGET]; actions=%w[MOVE ADAPT REFERENCE EXCLUDE]; seen={}; rows.each_with_index{|r,i| abort("row #{i+1} field count") unless r.length==12; abort("row #{i+1} blank field") if r.any?(&:empty?); abort("row #{i+1} bytes") unless r[1].match?(/\A\d+\z/); abort("row #{i+1} sha") unless r[2].match?(/\A[0-9a-f]{64}\z/); abort("row #{i+1} role") unless roles.include?(r[5]); abort("row #{i+1} target") unless targets.include?(r[6]); abort("row #{i+1} action") unless actions.include?(r[8]); abort("duplicate source_path #{r[0]}") if seen[r[0]]; seen[r[0]]=true}; puts "inventory_rows=#{rows.length} result=PASS"' workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md
```

Expected: all rows pass. The checker may not mutate or normalize the map.

- [ ] **Step 2: Recompute source identities**

For every inventory row, recompute bytes and SHA-256 from the live source file and compare them with the map. Expected: exact match for all files. Any drift invalidates the affected row and requires reclassification before review.

- [ ] **Step 3: Check target-owner consistency**

Fail the map candidate if:

- a target owner has no primary source;
- a fact class has two primary owners;
- an archived source is classified as current authority;
- an `ADAPT` row claims transferred acceptance;
- `project/` is treated as part of the immutable AOS product;
- `aos/` has a required dependency outside itself;
- actual migration or Git authorization is claimed.

- [ ] **Step 4: Run Markdown and whitespace checks**

Run:

```bash
git diff --no-index --check /dev/null workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md
```

Expected: exit `1` because the untracked file differs from `/dev/null`, with zero diagnostics.

Check UTF-8 validity, BOM absence, CR count `0`, final LF and balanced fenced blocks using Ruby standard library. Expected: all pass.

Run:

```bash
ruby -e 'raw=File.binread(ARGV[0]); abort("BOM present") if raw.byteslice(0,3)==[0xEF,0xBB,0xBF].pack("C*"); abort("CR present") if raw.include?("\r".b); abort("missing final LF") unless raw.end_with?("\n".b); text=raw.dup.force_encoding("UTF-8"); abort("invalid UTF-8") unless text.valid_encoding?; fences=text.lines.count{|line| line.start_with?("```")}; abort("unbalanced fences") unless fences.even?; puts "utf8=PASS bom=ABSENT cr=0 final_lf=PASS fences=#{fences}/#{fences}"' workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md
```

- [ ] **Step 5: Compute exact map identity**

Run:

```bash
wc -c workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md
shasum -a 256 workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md
```

Record the exact bytes and SHA-256 inside the terminal report, not inside the self-bound map.

- [ ] **Step 6: Prove source and Git state were not mutated**

Run the same repository identity and `git status --short --branch` commands used in Task 1. Compare source-file bytes/hashes for all protected inputs. Expected: only the authorized map path was created; no source, index, commit, branch or remote state changed.

- [ ] **Step 7: Stop for human review**

Report:

```yaml
inventory_result: PASS | FAIL | BLOCKED
migration_execution: NOT_RUN
target_repository_creation: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
commit: NOT_RUN
push: NOT_RUN
merge: NOT_RUN
release: NOT_RUN
next_action: HUMAN_REVIEW_OF_EXACT_MIGRATION_MAP
stop: true
```

Do not create `AOS-3`, copy files or start a later plan in the same execution.

---

## Plan completion boundary

This plan is complete when:

1. every inspected source file has an exact identity and one classification;
2. every target role has one proposed primary source;
3. competing owners and required decisions are explicit;
4. the migration map passes its mechanical and semantic consistency checks;
5. repository mutation is limited to the exact authorized map path;
6. human review, migration, implementation and Git operations remain separate later actions.

The plan itself does not authorize its execution.
