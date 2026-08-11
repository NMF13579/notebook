# AOS Lean Portable Documentation Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create one self-contained, audit-ready AOS documentation candidate at `AOS/portable/` without modifying the existing frozen Global Design subject or starting runtime implementation.

**Architecture:** Harmonize the accepted DRAFT-R2 content into eleven package-local Markdown owners, then bind their exact bytes with a deterministic non-self-referential manifest. Audit and human acceptance remain separate gates; the acceptance sidecar is created only after both and is excluded from the manifest.

**Tech Stack:** Markdown, YAML, UTF-8/LF text, SHA-256, Git read-only inspection, Ruby standard-library validation and repository-local shell checks.

## Global Constraints

- Approved design: `docs/superpowers/specs/2026-08-09-aos-lean-portable-package-design.md`, SHA-256 `778d51b7ce176a7e9f39b8f8b74389e15571a5c08f536404ae28087f647d66f0`.
- Primary source candidate: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/CANDIDATE_MANIFEST.txt`, SHA-256 `57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65`.
- Source audit: `workspace/audits/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2_COMPLETENESS_RE_AUDIT.md`, SHA-256 `b6cd639302fb719ab7ef47e894075c791d683c3e46b35291c11a2c591f989cfe`.
- Source acceptance: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2_HUMAN_DECISION_RECORD.yaml`, SHA-256 `0353347d106d1985e7b296f721ade4b9e51a1a26a304468b97dc39b00c7598df`.
- Frozen foundation identity: `b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf`.
- Source commit: `73716e65d6bb4512c58fefbced53d407cec57bca`.
- Writable authoring boundary: create-only `AOS/portable/**`.
- Protected paths: existing `AOS/01_PRODUCT_MODEL.md`, `AOS/02_ARCHITECTURE_CONTRACTS.md`, `AOS/03_ENGINEERING_PIPELINE.md`, `AOS/GLOBAL_DESIGN_FREEZE.md`, `AOS/reviews/**`, `AOS/decisions/**`, `docs/00_Core.md` through `docs/06_Features.md`, accepted workspace sources and prior audits.
- Runtime code, tests, dependencies, CI/CD, deployment and implementation-repository creation are forbidden.
- `PACKAGE_ACCEPTANCE.yaml` is not created during authoring or audit. It is a later sidecar after exact human acceptance.
- Commit, Push, Merge and Release require separate explicit authorization and are not implied by this plan.
- One authoring interval may perform internal harmonization and construction checks without per-document human gates.

---

## File Map

| Path | Responsibility |
|---|---|
| `AOS/portable/AGENTS.md` | Thin package-local routing and authority adapter |
| `AOS/portable/README.md` | Entrypoint, status, inventory, reading order and portability rules |
| `AOS/portable/00_PROJECT_CORE.md` | Identity, vocabulary, precedence and safety semantics |
| `AOS/portable/01_PRODUCT_MODEL.md` | Product problems, users, requirements, capabilities and success |
| `AOS/portable/02_ARCHITECTURE_CONTRACTS.md` | WHAT-level layers, contracts, ownership, trust and recovery |
| `AOS/portable/03_ENGINEERING_WORKFLOW.md` | Future planning/execution/validation/review/recovery semantics |
| `AOS/portable/04_FEATURE_SPECIFICATIONS.md` | Full `FTR-001…FTR-030` design view and dispositions |
| `AOS/portable/05_USER_JOURNEYS_AND_UX.md` | Interface-neutral journeys and UX requirements |
| `AOS/portable/06_PROJECT_ROADMAP.md` | Proposed phases, gates and dependency timing |
| `AOS/portable/07_DECISION_REGISTER.md` | Accepted ledger, safe states and open human decisions |
| `AOS/portable/08_TRACEABILITY.md` | Live trace graph and package coverage without audit history |
| `AOS/portable/MANIFEST.txt` | Deterministic identity for the eleven Markdown content files |
| `AOS/portable/PACKAGE_ACCEPTANCE.yaml` | Post-audit, post-decision sidecar; excluded from manifest |

---

### Task 1: Bind sources and author the portable core

**Files:**
- Create: `AOS/portable/AGENTS.md`
- Create: `AOS/portable/README.md`
- Create: `AOS/portable/00_PROJECT_CORE.md`
- Create: `AOS/portable/01_PRODUCT_MODEL.md`
- Create: `AOS/portable/02_ARCHITECTURE_CONTRACTS.md`
- Create: `AOS/portable/03_ENGINEERING_WORKFLOW.md`
- Read: `docs/superpowers/specs/2026-08-09-aos-lean-portable-package-design.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/{README.md,00_PROJECT_CORE.md,01_PRODUCT_MODEL.md,02_ARCHITECTURE_CONTRACTS.md,03_ENGINEERING_WORKFLOW.md}`
- Read: `AOS/{01_PRODUCT_MODEL.md,02_ARCHITECTURE_CONTRACTS.md,03_ENGINEERING_PIPELINE.md,GLOBAL_DESIGN_FREEZE.md}`

**Interfaces:**
- Consumes: the exact identities in Global Constraints and the accepted content/status classifications in DRAFT-R2.
- Produces: six self-contained Markdown owners with package-local relative links and stable headings used by Tasks 2 and 3.

- [ ] **Step 1: Run the create-only and source-identity preflight**

Run:

```bash
test ! -e AOS/portable
git cat-file -e 73716e65d6bb4512c58fefbced53d407cec57bca^{commit}
shasum -a 256 \
  workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/CANDIDATE_MANIFEST.txt \
  workspace/audits/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2_COMPLETENESS_RE_AUDIT.md \
  workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2_HUMAN_DECISION_RECORD.yaml \
  docs/superpowers/specs/2026-08-09-aos-lean-portable-package-design.md
```

Expected: target absence; the four SHA-256 values exactly match Global Constraints. Any mismatch stops authoring before creating `AOS/portable/`.

- [ ] **Step 2: Snapshot protected identities**

Run SHA-256 over the three frozen subject files, `GLOBAL_DESIGN_FREEZE.md`, seven canonical owners, DRAFT-R2 manifest/audit/acceptance and current Git index. Keep the results as ephemeral construction evidence for the final before/after comparison.

Expected: the ordered three-file frozen subject recomputes to `b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf`.

- [ ] **Step 3: Create the six portable core files**

Use `apply_patch`. Each file must have YAML frontmatter containing package `AOS_LEAN_PORTABLE_DOCUMENTATION`, candidate status `DRAFT`, authority `NONE`, its unique owner role, `implementation_authorization: NONE` and `git_authorization: NONE`.

Required section topology:

```text
AGENTS: purpose → reading routes → ownership → authority → edit/validation/Git boundaries
README: outcome → status → inventory → reading order → portability → identity → exclusions
00: identity → mission → users → source precedence → status/authority → safety → glossary
01: problems → users/JTBD → promise → requirements → capabilities → first slice → success/non-goals
02: goals → layers → C-001…C-014 → ownership → states → trust → recovery → security → open decisions
03: documentation/runtime split → roles → task preparation → stages → validation/Evidence → recovery → Git
```

Do not copy construction history or repository-relative provenance links into operational sections. Preserve source identities concisely in `README.md` and the relevant frontmatter.

- [ ] **Step 4: Check core ownership and portability**

Run:

```bash
rg -n '\]\((\.\./|/)' AOS/portable/{AGENTS.md,README.md,00_PROJECT_CORE.md,01_PRODUCT_MODEL.md,02_ARCHITECTURE_CONTRACTS.md,03_ENGINEERING_WORKFLOW.md}
rg -n 'implementation_authorization: AUTHORIZED|git_authorization: AUTHORIZED' AOS/portable
```

Expected: both searches return zero matches. Manually confirm Product, Architecture and Workflow facts are owned only by `01`, `02` and `03`; navigation files link rather than duplicate.

- [ ] **Step 5: Record the Task 1 checkpoint**

Report six created paths, source identities, focused checks and `AOS/portable/MANIFEST.txt: NOT_CREATED`. Do not stage or commit without separate Git authorization.

---

### Task 2: Author features, journeys, roadmap, decisions and live traceability

**Files:**
- Create: `AOS/portable/04_FEATURE_SPECIFICATIONS.md`
- Create: `AOS/portable/05_USER_JOURNEYS_AND_UX.md`
- Create: `AOS/portable/06_PROJECT_ROADMAP.md`
- Create: `AOS/portable/07_DECISION_REGISTER.md`
- Create: `AOS/portable/08_TRACEABILITY.md`
- Read: `workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT_R2/{04_FEATURE_SPECIFICATIONS.md,05_USER_JOURNEYS_AND_UX.md,06_PROJECT_ROADMAP.md,07_DECISION_REGISTER.md,08_TRACEABILITY_AND_REVIEW.md}`

**Interfaces:**
- Consumes: package vocabulary, contract names and owner relations produced by Task 1.
- Produces: five portable downstream documents with complete feature, journey, phase, decision and trace coverage.

- [ ] **Step 1: Create `04_FEATURE_SPECIFICATIONS.md`**

Preserve exactly one primary section for every `FTR-001…FTR-030`, canonical recommendation/disposition, accepted X1 behavior boundaries, separate Medical/Design profiles under FTR-027 and `selected_domain_profile: null`.

Every feature retains: purpose/users, trigger/preconditions, semantic I/O, flow/states, failures/recovery, dependencies/authority, acceptance/negative cases and unknowns/non-goals.

- [ ] **Step 2: Create `05_USER_JOURNEYS_AND_UX.md`**

Preserve `J-001…J-007`, interface neutrality, Status/Next/Details semantics, accessibility, failure/recovery UX and separation of result, human decision and permission. Supporting journeys remain proposals.

- [ ] **Step 3: Create `06_PROJECT_ROADMAP.md`**

Preserve the accepted FTR-001 first slice and proposed `D0/R0…R9` direction without activating phases or admitting features. Keep the exact nine-decision R0 set identical to Task 2 Step 4.

- [ ] **Step 4: Create `07_DECISION_REGISTER.md`**

Preserve the accepted ledger, including exact `DR-FULL-001: ACCEPT` from the bound R2 acceptance record, `UNASSIGNED` as a safe state, the 21 remaining material open decision contracts with `selected_option: null`, and 23 item-specific `DR-FTR-*` routes. Package-local accepted facts may cite the exact source identities from Global Constraints without linking outside the package.

- [ ] **Step 5: Create `08_TRACEABILITY.md`**

Retain the live 30-row problem→user/JTBD→requirement→journey→feature→contract→acceptance/negative→roadmap→decision graph and package acceptance criteria. Remove R1/R2 construction chronology, old audit state, authoring snapshots and prior next-action ceremony.

- [ ] **Step 6: Run downstream semantic checks**

Run exact-set checks for:

```text
FTR-001…FTR-030: 30 unique primary sections
J-001…J-007: all represented
C-001…C-014: all represented
accepted package decision: DR-FULL-001 = ACCEPT
remaining open material DR records: 21
UNDECIDED item routes: 23 exact DR-FTR IDs
R0 set: DR-PROD-001, DR-PROD-004, DR-ARCH-001…005, DR-POL-001, DR-POL-002
FTR-027 selected_domain_profile: null
```

Expected: exact membership, no duplicates, no selected open option and no changed feature disposition.

- [ ] **Step 7: Record the Task 2 checkpoint**

Report five created paths and the semantic-set results. Continue within the same authoring interval to Task 3 without a human review gate unless a material conflict or new decision was discovered.

---

### Task 3: Harmonize, validate and bind the exact candidate

**Files:**
- Modify: `AOS/portable/AGENTS.md`
- Modify: `AOS/portable/README.md`
- Modify: `AOS/portable/00_PROJECT_CORE.md`
- Modify: `AOS/portable/01_PRODUCT_MODEL.md`
- Modify: `AOS/portable/02_ARCHITECTURE_CONTRACTS.md`
- Modify: `AOS/portable/03_ENGINEERING_WORKFLOW.md`
- Modify: `AOS/portable/04_FEATURE_SPECIFICATIONS.md`
- Modify: `AOS/portable/05_USER_JOURNEYS_AND_UX.md`
- Modify: `AOS/portable/06_PROJECT_ROADMAP.md`
- Modify: `AOS/portable/07_DECISION_REGISTER.md`
- Modify: `AOS/portable/08_TRACEABILITY.md`
- Create: `AOS/portable/MANIFEST.txt`

**Interfaces:**
- Consumes: all eleven mutable content files from Tasks 1 and 2.
- Produces: one coherent, construction-checked, byte-bound candidate ready for separate independent audit.

- [ ] **Step 1: Perform one package-wide harmonization pass**

Check terminology, owner boundaries, internal links, accepted/proposal/unknown classifications, absence of unclassified material claims, R0 set equality, feature dispositions and absence of historical construction narrative. Correct only defects resolvable from the bound sources.

Stop and report if correction would choose product scope, architecture, implementation repository, toolchain, provider, feature disposition or human decision.

- [ ] **Step 2: Run structural checks over all eleven Markdown files**

Before manifest creation, assert that the directory contains exactly the eleven expected Markdown regular files, with no unexpected paths, file types or symlinks. Verify UTF-8, no BOM/CR, final LF, YAML frontmatter with unique keys, balanced fences, required headings and no trailing whitespace/conflict markers. `git diff --no-index --check /dev/null <path>` may exit `1` because each file differs from `/dev/null`; PASS requires empty diagnostics.

- [ ] **Step 3: Validate every package-relative link**

Resolve Markdown links from each source file. Required links must remain under `AOS/portable/`, target an existing file/heading and never use an absolute local path. Expected: broken links `0`, escaping links `0`.

- [ ] **Step 4: Run the full semantic/authority suite**

Repeat the Task 2 exact-set checks and verify:

- exactly eleven Markdown content files before manifest creation;
- one owner per fact class;
- no `implementation_authorization: AUTHORIZED` or `git_authorization: AUTHORIZED`;
- no runtime implementation claims or prescribed reversible HOW;
- frozen/canonical/workspace protected snapshots match Task 1 Step 2;
- candidate-only Git delta is contained in `AOS/portable/**`.

- [ ] **Step 5: Generate deterministic manifest records**

For the eleven Markdown content files, compute exact byte count and SHA-256, sort records by UTF-8 path bytes and format each line as:

```text
<lowercase_sha256>\t<decimal_bytes>\t<package_relative_path>\n
```

Use `apply_patch` to create `AOS/portable/MANIFEST.txt` from the observed exact values. Do not include `MANIFEST.txt` or `PACKAGE_ACCEPTANCE.yaml` in its records.

- [ ] **Step 6: Verify manifest and candidate identity**

Recompute every recorded byte count/hash from disk, assert exact path-set equality, then compute SHA-256 of exact `MANIFEST.txt` bytes. Repeat the full construction suite after manifest creation.

Expected terminal state:

```yaml
construction_result: PASS
candidate_identity: sha256:<observed_manifest_sha256>
independent_audit: NOT_RUN
human_decision: NOT_RUN
PACKAGE_ACCEPTANCE.yaml: ABSENT
implementation_authorization: NONE
git_authorization: NONE
```

- [ ] **Step 7: Stop with an audit-ready handoff**

Report candidate identity, exact inventory, changed paths, checks RUN/NOT_RUN, protected snapshot proof and one next action: separate independent read-only audit. Do not create an audit result, acceptance record, commit or push.

---

### Task 4: Run a separate independent read-only audit

**Files:**
- Read: `AOS/portable/AGENTS.md`
- Read: `AOS/portable/README.md`
- Read: `AOS/portable/00_PROJECT_CORE.md` through `AOS/portable/08_TRACEABILITY.md`
- Read: `AOS/portable/MANIFEST.txt`
- Create: one separately authorized report under `workspace/audits/`

**Interfaces:**
- Consumes: exact manifest identity produced by Task 3.
- Produces: read-only technical result and exact findings bound to that identity.

- [ ] **Step 1: Start a fresh reviewer context**

Bind the manifest path, bytes and SHA-256. Record reviewer independence and limitations. Candidate writes are forbidden.

- [ ] **Step 2: Reproduce identity and construction assertions**

Verify all eleven records, manifest identity, source/frozen bindings, portability, link resolution, exact ID sets, owner boundaries, authority exclusions and absence of implementation HOW.

- [ ] **Step 3: Perform semantic completeness review**

Assess whether the portable package preserves the accepted R2 content while removing only non-operational provenance ceremony. Audit recommendations and open options remain non-authoritative.

- [ ] **Step 4: Emit the audit report and stop**

Valid technical results: `PASS | FAIL | BLOCKED | UNKNOWN`. The report lists findings, checks RUN/NOT_RUN, candidate mutation `NONE`, changed paths and next required action. A finding is not corrected in this task.

---

### Task 5: Record exact human acceptance after audit

**Files:**
- Read: `AOS/portable/MANIFEST.txt`
- Read: exact Task 4 audit report
- Create: `AOS/portable/PACKAGE_ACCEPTANCE.yaml`

**Interfaces:**
- Consumes: an exact audit result and explicit human package decision bound to the same candidate.
- Produces: one non-recursive acceptance sidecar without changing the manifest-bound subject.

- [ ] **Step 1: Present one package-level human decision gate**

Show exact candidate and audit identities, findings/limitations, accepted fact classes and exclusions. Do not repeat per-document review unless material findings or choices require it.

- [ ] **Step 2: Wait for explicit human decision**

Valid values: `ACCEPT | NEEDS_CHANGES | REJECT | DEFER`. Only `ACCEPT` proceeds to sidecar creation. Other values stop or create a separately authorized correction route.

- [ ] **Step 3: Prepare and confirm exact raw acceptance record**

The record contains candidate manifest identity, audit report identity/result, human source locator, accepted fact classes, open decisions left unselected, feature disposition changes `NONE`, frozen foundation unchanged and all implementation/Git authorities `NONE`.

Compute raw byte count/SHA-256 and require exact human confirmation before writing.

- [ ] **Step 4: Create and verify the sidecar**

Use `apply_patch` to create the confirmed bytes at `AOS/portable/PACKAGE_ACCEPTANCE.yaml`. Verify YAML, final LF, byte count and SHA-256. Recompute the candidate manifest identity and prove it remains unchanged.

- [ ] **Step 5: Stop before Git delivery**

Report final portable inventory: eleven Markdown files, one manifest and one acceptance sidecar. Commit, Push, Merge and Release remain `NOT_RUN` until separately authorized.

---

### Task 6: Prepare optional exact Git delivery

**Files:**
- Read: all final `AOS/portable/**` files
- Read: Task 4 audit report
- Read: this plan and the approved design spec

**Interfaces:**
- Consumes: human-accepted final portable package and clean validation evidence.
- Produces: a decision-ready exact path allowlist; no Git mutation without explicit authorization.

- [ ] **Step 1: Reverify final identities and repository state**

Observe repository/branch/HEAD/upstream/status, recompute manifest/audit/acceptance identities and prove no unrelated tracked or untracked state is included.

- [ ] **Step 2: Present the exact proposed commit set**

List every `AOS/portable/**` path plus any provenance/design/plan/audit paths proposed for preservation. Keep portable content separate from repository provenance in the report.

- [ ] **Step 3: Wait for exact Commit authorization**

The user must name the commit action, exact subject/path set and message or approve a proposed message. Without it, staging and commit remain `NOT_RUN`.

- [ ] **Step 4: If authorized, stage and commit exactly once**

Stage only the approved allowlist, verify staged path equality, staged blobs and `git diff --cached --check`, create one commit and reverify the commit tree. Push, Merge and Release remain separate and `NOT_RUN`.
