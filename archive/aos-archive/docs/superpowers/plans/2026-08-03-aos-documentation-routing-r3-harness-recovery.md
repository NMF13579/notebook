---
status: REFERENCE_ONLY
authority: NONE
archived_reason: SUPERSEDED_BY_SIMPLIFIED_PLANNING_MODEL
---

# AOS Documentation Routing R3 Harness Subject-Binding Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Recover the R3 deterministic harness package from the failed `ROUTING-R3-HARNESS-PACKAGE-VALIDATE-001` binding by making the active `POST_STOP_DOCUMENTATION R6` subject identity canonical, separating six output files from five pinned dependencies, eliminating reviewer-side identity reconstruction, and issuing one new immutable Stage Report under a new execution identity.

**Architecture:** The six mutable package outputs form the only validation subject and use the exact `AOS-SUBJECT-SET-MANIFEST-V1` algorithm from `POST_STOP_DOCUMENTATION R6`. The four read-only agent definitions plus the pinned deterministic-harness plan artifact form a separate five-file technical dependency set; the existing raw `sha256  byte_length  path` algorithm may identify that dependency set but must never be exposed as `subject_set_sha256`. Pinning records exact input bytes and grants no acceptance, activation, implementation, or Git authority. A read-only `freeze-package-binding` command produces one closed canonical binding before report creation; a separate read-only `verify-package-binding` command recomputes that binding and the Stage Report identity so reviewers consume deterministic Evidence instead of manually rebuilding it.

**Tech Stack:** Python 3.9.6 standard library, `unittest`, canonical compact JSON/YAML bytes, SHA-256, UTF-8/LF manifests, Codex CLI strict configuration parser, read-only Git inspection.

## Global Constraints

- Repository: `/Users/muhammed/Documents/GitHub/notebook`, branch `dev`, observed plan-authoring `HEAD` `d733eeb037a517634ecc37e8b19c8421c2d20530`.
- Repository role remains `ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY`; the harness is documentation-routing support tooling, not AOS product runtime code.
- Human recovery-model decision visible text SHA-256: `2b0c0a88d861103a25510381e8cd65773e15b1b532e89d087533037e5f6e0a73` over 140 UTF-8 bytes.
- PLAN authorization visible text SHA-256: `2cfad050992922ae658634569a4ffe8c0b1ce5362b522619adb86d39b393e8f7` over 54 UTF-8 bytes.
- Selected recovery model: `POST_STOP_R6_CANONICAL_SIX_OUTPUT_SUBJECT_PLUS_FIVE_PINNED_DEPENDENCIES_AND_NEW_EXECUTION_ID`.
- This plan creates or modifies only this plan path. It does not authorize the recovery `EXECUTE`, independent `VALIDATE`, safe pilot, acceptance, activation, or Git delivery.
- The R3 package remains pilot-only `DRAFT_CANDIDATE`; it is not active and must not govern mass documentation authoring.
- Primary thread is the only writer. Reviewer agents are bounded read-only, use no nested delegation, perform no same-request retry, and make no human decision.
- Maximum reviewer concurrency is two; semantic review is sequential after current upstream Evidence is normalized.
- Candidate correction and validator/request correction remain distinct. `VALIDATE` never repairs its subject.
- The historical Stage Report at `planning/verification/bootstrap/routing-r3-harness/ROUTING-R3-DETERMINISTIC-HARNESS-EXECUTE-001/stage-report.yaml` is immutable and is never overwritten, renamed, deleted, reused, migrated, or backfilled.
- The recovery execution identity is `ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001`.
- Its only permitted new Stage Report path is `planning/verification/bootstrap/routing-r3-harness/ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001/stage-report.yaml`; it must be absent at authorization preflight and immediately before exclusive creation.
- Commit, Push, Merge, Release, activation, and the next task remain `NOT_RUN` unless separately and exactly authorized.
- No dependency installation, network access, product implementation, database, CI/CD, hook, plugin, or repository-role change is permitted.

---

## Identity Model

### Canonical six-file validation subject

These and only these files form the corrected package subject:

1. `.codex/config.toml`
2. `docs/ideas/AOS_Documentation_Agent_Routing_R1.md`
3. `docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md`
4. `docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md`
5. `tests/test_routing_r3_harness.py`
6. `tools/routing_r3_harness.py`

The exact subject manifest is:

```text
AOS-SUBJECT-SET-MANIFEST-V1<LF>
FILE<TAB><normalized-path><TAB><raw-file-byte-length><TAB><raw-file-sha256><LF>
```

Records are sorted by normalized path UTF-8 bytes. `subject_set_sha256` is the SHA-256 of these complete manifest bytes. No legacy two-space manifest, dependency path, Stage Report path, plan-authority input, Git metadata, chat text, or mtime participates.

### Five pinned package dependencies

These files are immutable inputs to the corrected package:

1. `.codex/agents/contract-analyst.toml`
2. `.codex/agents/mechanical-checker.toml`
3. `.codex/agents/reference-explorer.toml`
4. `.codex/agents/semantic-reviewer.toml`
5. `docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md`

Their dependency manifest retains the existing deterministic record:

```text
<raw-file-sha256><SP><SP><raw-file-byte-length><SP><SP><normalized-path><LF>
```

The digest field is named `pinned_dependency_set_sha256`, never `subject_set_sha256`. This five-file set is distinct from the broader validation-time `authoritative_dependency_set_sha256` required by `POST_STOP_DOCUMENTATION R6`, which also binds the selected profile, current human authorization, and other authoritative inputs.

### Clause-level precedence over the pinned legacy plan

The pinned deterministic-harness plan is immutable historical technical input, not the current recovery contract. For only `ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001`, an accepted hash-bound revision of this recovery plan plus its future exact `EXECUTE` authorization takes precedence over exactly two legacy clauses in `docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md`:

1. its two-space package manifest may identify only `pinned_dependency_set_sha256`; it may not define the R6 six-file `subject_set_sha256`;
2. its closed command list is extended only by `freeze-package-binding` and `verify-package-binding` with the schemas in Task 3.

Every other constraint of the pinned plan remains applicable. No design, routing owner, active profile, repository authority, acceptance, activation, implementation, or Git boundary is superseded. The future recovery `EXECUTE` authorization must bind both plan identities and repeat this exact precedence rule; absent that binding, execution is `BLOCKED/BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH`.

### Validation profile identity

The harness reconstructs section 4.4 exactly:

```text
AOS-VALIDATION-PROFILE-IDENTITY-V1<LF>
PROFILE_ID<TAB>POST_STOP_DOCUMENTATION<LF>
REVISION<TAB>R6<LF>
PATH<TAB>planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md<LF>
SOURCE_SHA256<TAB><raw-profile-source-file-sha256><LF>
```

At plan authoring the source SHA-256 is `b35bf89e503c2cd86393c983ef26108858a5c1e697c09db5d497b8830ca122b9`, producing profile identity `d24e01ea9332ff20152a0502568df678229a350013aaa067b14da57984c9b11a`. Execution and validation must recompute rather than trust these reported plan-time values.

### Validation-time authoritative dependency identity

The five-file `pinned_dependency_set_sha256` is a package-integrity identity only. It never substitutes for the R6 validation-packet dependency identity. Before a separate `VALIDATE`, construct the complete section-4.5 manifest from every authoritative input actually required by the selected profile and exact validation authorization:

```text
AOS-AUTHORITATIVE-DEPENDENCY-MANIFEST-V1<LF>
<kind><TAB><locator><TAB><raw-source-byte-length><TAB><raw-source-sha256><LF>
```

Repository inputs use `FILE` plus the R6 normalized repository-relative locator. The exact current human authorization, when required, uses `INLINE_DECISION` plus `RUNTIME_TURN_ID:<exact-runtime-turn-id>` and binds the complete stored runtime-message text bytes, length, digest, and selector. Records are sorted by UTF-8 bytes of `<kind><TAB><locator>`. Duplicate locators, missing runtime metadata, unavailable bytes, undeclared additions, omitted required inputs, stale bytes, and digest mismatch fail before an `authoritative_dependency_set_sha256` is produced. Final membership is runtime-bound by the accepted profile and exact future validation authorization; this PLAN neither invents that authorization nor precomputes its unknown bytes.

The separate validation packet must carry both `authoritative_dependency_manifest.entries` and its raw-manifest `sha256`, while continuing to carry the six-file subject identity, five-file pinned technical identity, profile identity, and raw Stage Report identity as distinct fields. No one of these digests may be substituted for another.

---

### Task 1: Lock the Recovery Contract with Failing Tests

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Inspect: `planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md`
- Inspect: the exact six subject paths and five dependency paths above

**Interfaces:**

- Consumes: current `run_harness`, `valid_stage_report`, and temporary-root helpers.
- Produces: failing contract tests for `--manifest-profile`, `POST_STOP_R6_SUBJECT`, `R3_PINNED_DEPENDENCY`, `freeze-package-binding`, and `verify-package-binding`.

- [ ] **Step 1: Add exact subject/dependency fixtures**

```python
SUBJECT_PATHS = (
    ".codex/config.toml",
    "docs/ideas/AOS_Documentation_Agent_Routing_R1.md",
    "docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md",
    "docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md",
    "tests/test_routing_r3_harness.py",
    "tools/routing_r3_harness.py",
)

PINNED_DEPENDENCY_PATHS = (
    ".codex/agents/contract-analyst.toml",
    ".codex/agents/mechanical-checker.toml",
    ".codex/agents/reference-explorer.toml",
    ".codex/agents/semantic-reviewer.toml",
    "docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md",
)
```

- [ ] **Step 2: Add a failing canonical R6 manifest test**

```python
def test_post_stop_r6_subject_manifest_is_exact(self) -> None:
    result = run_harness(
        "manifest", "--root", str(root),
        "--manifest-profile", "POST_STOP_R6_SUBJECT",
        "--path", "b.md", "--path", "a.md",
    )
    expected = (
        "AOS-SUBJECT-SET-MANIFEST-V1\n"
        f"FILE\ta.md\t2\t{a_digest}\n"
        f"FILE\tb.md\t2\t{b_digest}\n"
    ).encode("utf-8")
    self.assertEqual(payload["subject_set_sha256"], hashlib.sha256(expected).hexdigest())
    self.assertNotIn("pinned_dependency_set_sha256", payload)
```

- [ ] **Step 3: Add a failing pinned-dependency manifest test**

```python
def test_pinned_dependency_manifest_never_claims_subject_identity(self) -> None:
    result = run_harness(
        "manifest", "--root", str(root),
        "--manifest-profile", "R3_PINNED_DEPENDENCY",
        "--path", "dep.md",
    )
    payload = json.loads(result.stdout)
    self.assertIn("pinned_dependency_set_sha256", payload)
    self.assertNotIn("subject_set_sha256", payload)
```

- [ ] **Step 4: Add failing ambiguity tests**

Require `CONTRACT_VIOLATION/NONE`, `finding_origin: REQUEST_OR_CHECKER_DEFECT`, `repository_mutations: 0`, and `stop: true` for:

- omitted `--manifest-profile`;
- unknown profile;
- a dependency path repeated as a subject path;
- any subject count other than six in `verify-package-binding`;
- any dependency count other than five;
- legacy eleven-file digest supplied as canonical subject identity.

- [ ] **Step 5: Run focused tests and prove RED**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_routing_r3_harness.IdentityTests.test_post_stop_r6_subject_manifest_is_exact \
  tests.test_routing_r3_harness.IdentityTests.test_pinned_dependency_manifest_never_claims_subject_identity -v
```

Expected: both tests fail because `--manifest-profile` is not implemented.

---

### Task 2: Implement Explicit Subject and Dependency Manifests

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Consumes: `normalize_relative_path`, regular-file/symlink checks, `sha256_bytes`.
- Produces:
  - `build_post_stop_r6_subject_manifest(root: Path, paths: Sequence[str]) -> bytes`
  - `build_pinned_dependency_manifest(root: Path, paths: Sequence[str]) -> bytes`
  - explicit `manifest_profile` CLI selection.

- [ ] **Step 1: Extract one regular-file record reader**

```python
def read_manifest_member(root: Path, relative: str) -> bytes:
    """Return exact regular-file bytes after the existing no-symlink walk."""
```

Reuse the current component-by-component `lstat` algorithm. Do not follow symlinks or use Git blob identity.

- [ ] **Step 2: Implement the R6 subject manifest**

```python
def build_post_stop_r6_subject_manifest(root: Path, paths: Sequence[str]) -> bytes:
    records = [b"AOS-SUBJECT-SET-MANIFEST-V1\n"]
    for relative in normalized_unique_sorted(paths):
        data = read_manifest_member(root, relative)
        records.append(
            f"FILE\t{relative}\t{len(data)}\t{sha256_bytes(data)}\n".encode("utf-8")
        )
    return b"".join(records)
```

- [ ] **Step 3: Retain the old algorithm only for pinned dependencies**

```python
def build_pinned_dependency_manifest(root: Path, paths: Sequence[str]) -> bytes:
    return b"".join(
        f"{sha256_bytes(data)}  {len(data)}  {relative}\n".encode("utf-8")
        for relative, data in exact_sorted_members(root, paths)
    )
```

The corresponding response key is `pinned_dependency_set_sha256`. Never emit `subject_set_sha256` for this profile.

- [ ] **Step 4: Make profile selection mandatory**

```python
manifest.add_argument(
    "--manifest-profile",
    required=True,
    choices=("POST_STOP_R6_SUBJECT", "R3_PINNED_DEPENDENCY"),
)
```

- [ ] **Step 5: Run all identity tests and prove GREEN**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_routing_r3_harness.IdentityTests -v
```

Expected: every identity test passes; no repository file changes during test execution.

---

### Task 3: Make Stage Report Membership Lossless

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Consumes: Task 2 manifest builders, existing canonical Stage Report parser, `PRE_R3_BOOTSTRAP` transport.
- Produces: one closed `ROUTING_R3_PACKAGE_BINDING_V1` schema plus `freeze_package_binding_command` and `verify_package_binding_command`.

- [ ] **Step 1: Add the required Stage Report binding fields**

When and only when `create-stage-report` receives `--package-binding-profile ROUTING_R3_RECOVERY_V1`, extend `documentation_validation_extension.output` with one closed machine-produced object:

```python
output.update(
    {
        "package_binding_schema": "ROUTING_R3_PACKAGE_BINDING_V1",
        "package_binding_sha256": package_binding_sha256,
        "package_binding": package_binding,
    }
)
```

`package_binding` is the exact closed object defined in Step 3. `package_binding_sha256` hashes its canonical compact UTF-8 JSON bytes with sorted keys, separators `(',', ':')`, `ensure_ascii=False`, and a terminal LF. The shared binding builder recomputes every nested identity from current bytes; no digest is manually transcribed. Without the explicit package profile, generic Stage Report creation and validation behavior is unchanged.

- [ ] **Step 2: Keep `validate_stage_report` generic**

Preserve the current generic invariant exactly: `expected_paths` and `present_paths` are normalized string lists and a `PASS` report compares them by set equality. This recovery does not add a generic uniqueness or ordering requirement. Do not hard-code the recovery package's six or five paths in `validate_stage_report`, `create-stage-report`, or `verify-stage-report` generic flow.

When `package_binding_schema` is absent, generic acceptance behavior remains unchanged, including the existing set-equality treatment of duplicate path-list members. When it is present, generic validation checks only closed-object shape, supported schema name, digest syntax, and canonical-object hash parity. Exact ordering and uniqueness are intentionally stricter only for the recovery package. The package-specific semantic assertions below belong only to `freeze-package-binding`, the explicitly selected `ROUTING_R3_RECOVERY_V1` creation branch, and `verify-package-binding`:

```python
tuple(output["expected_paths"]) == SUBJECT_PATHS
tuple(output["present_paths"]) == SUBJECT_PATHS
tuple(package_binding["subject_paths"]) == SUBJECT_PATHS
tuple(package_binding["pinned_dependency_paths"]) == PINNED_DEPENDENCY_PATHS
len(set(package_binding["subject_paths"])) == len(SUBJECT_PATHS)
len(set(package_binding["pinned_dependency_paths"])) == len(PINNED_DEPENDENCY_PATHS)
set(package_binding["subject_paths"]).isdisjoint(
    package_binding["pinned_dependency_paths"]
)
```

Require exact ordered equality to the immutable six-file and five-file tuples before digest comparison, thereby rejecting duplicates, omissions, substitutions, and order drift even when counts or sets appear plausible. Require every digest and positive manifest byte length. Reject the historical eleven-file hash as a valid six-file subject binding. Add a regression proving an unrelated generic Stage Report with a different authorized output set still passes generic validation.

- [ ] **Step 3: Add one deterministic freeze-binding producer**

Implement one shared pure builder and one read-only CLI command:

```python
def build_package_binding(
    root: Path,
    subject_paths: Sequence[str],
    dependency_paths: Sequence[str],
    profile_id: str,
    profile_revision: str,
    profile_path: str,
) -> Dict[str, Any]:
    """Return the closed current-byte ROUTING_R3_PACKAGE_BINDING_V1 object."""

def freeze_package_binding_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    """Return canonical read-only Evidence before Stage Report creation."""
```

The closed `package_binding` schema is:

```python
package_binding = {
    "binding_schema": "ROUTING_R3_PACKAGE_BINDING_V1",
    "validated_root": str(validated_root),
    "subject_manifest_profile": "POST_STOP_R6_SUBJECT",
    "subject_paths": list(SUBJECT_PATHS),
    "subject_manifest_byte_length": len(subject_manifest),
    "subject_set_sha256": sha256_bytes(subject_manifest),
    "pinned_dependency_manifest_profile": "R3_PINNED_DEPENDENCY",
    "pinned_dependency_paths": list(PINNED_DEPENDENCY_PATHS),
    "pinned_dependency_manifest_byte_length": len(dependency_manifest),
    "pinned_dependency_set_sha256": sha256_bytes(dependency_manifest),
    "validation_profile": {
        "profile_id": "POST_STOP_DOCUMENTATION",
        "revision": "R6",
        "path": "planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md",
        "source_sha256": profile_source_sha256,
        "validation_profile_sha256": validation_profile_sha256,
    },
}
```

The builder validates the canonical `--root`, exact ordered six/five tuples, manifest bytes, and active profile bytes. Mutable Git status is deliberately excluded from `package_binding` so exclusive Stage Report creation cannot change the frozen package identity; each command instead reports exact repository identity before/after in its outer zero-write Evidence. The freeze command returns `package_binding`, its canonical byte length, and `package_binding_sha256` in a `PASS/NONE` zero-write envelope. This is the only producer of the `freeze` object used later. `create-stage-report --package-binding-profile ROUTING_R3_RECOVERY_V1 --expected-package-binding-sha256 <freeze.package_binding_sha256>` calls the same builder immediately before exclusive creation and fails on subject/dependency/profile drift; it never accepts a caller-authored binding object.

- [ ] **Step 4: Add a single deterministic package verifier**

```python
def verify_package_binding_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    """Verify six-file subject, five pinned dependencies, active profile,
    immutable Stage Report membership, and before/after read-only repository identity."""
```

The implementation constructs the invocation from the exact machine-produced freeze result; no manifest, nested object, hash, length, or path membership is manually reconstructed:

```python
command = [
    "python3", "tools/routing_r3_harness.py", "verify-package-binding",
    "--root", "/Users/muhammed/Documents/GitHub/notebook",
]
for path in SUBJECT_PATHS:
    command.extend(("--subject-path", path))
for path in PINNED_DEPENDENCY_PATHS:
    command.extend(("--dependency-path", path))
command.extend(
    (
        "--expected-package-binding-sha256",
        freeze["package_binding_sha256"],
        "--profile-id", "POST_STOP_DOCUMENTATION",
        "--profile-revision", "R6",
        "--profile-path",
        "planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md",
        "--transport-profile", "PRE_R3_BOOTSTRAP",
        "--task-id", "ROUTING-R3-DETERMINISTIC-HARNESS",
        "--execution-id",
        "ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001",
        "--stage-report-path",
        "planning/verification/bootstrap/routing-r3-harness/"
        "ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001/stage-report.yaml",
        "--expected-stage-report-byte-length", str(stage_report_identity["byte_length"]),
        "--expected-stage-report-sha256", stage_report_identity["sha256"],
    )
)
```

`stage_report_identity` is the direct post-create byte re-read result reported by the primary; it is not part of the pre-create freeze object. The verifier calls the shared binding builder, compares the canonical binding hash to the expected value and the report's nested binding, then enforces the package-only tuple rules from Step 2.

- [ ] **Step 5: Make zero-write Git identity deterministic inside both commands**

Resolve `arguments.root` once with `Path(arguments.root).resolve(strict=True)`, require a directory, run `git -C <resolved-root> rev-parse --show-toplevel`, resolve that returned path, and require exact equality to `<resolved-root>`. Every subsequent repository observation must use this same validated root; a hard-coded repository path or a second independently selected root is forbidden.

Use only these read-only commands through `subprocess.run(..., check=True, stdout=PIPE)` where `<resolved-root>` is the single validated value derived from `--root`:

```text
git -C <resolved-root> branch --show-current
git -C <resolved-root> rev-parse HEAD
git -C <resolved-root> status --short --untracked-files=all
git -C <resolved-root> diff --cached --name-only
```

Capture exact bytes before and after both freeze and verification. Return the validated root plus their byte lengths and SHA-256 values. Any root mismatch or before/after difference returns `BLOCKED/BLOCKED_VALIDATION_SUBJECT_MISMATCH`; any missing Git capability returns `BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY`. Never substitute `--porcelain=v1 -z`, omit `--untracked-files=all`, normalize the output, or observe Git state outside the validated root.

- [ ] **Step 6: Return one canonical read-only success envelope**

```python
return {
    "result": "PASS",
    "reason_code": "NONE",
    "subject_set_sha256": observed_subject_sha256,
    "pinned_dependency_set_sha256": observed_dependency_sha256,
    "validation_profile_sha256": observed_validation_profile_sha256,
    "package_binding_sha256": observed_package_binding_sha256,
    "stage_report_sha256": observed_stage_report_sha256,
    "repository_identity_before": repository_identity_before,
    "repository_identity_after": repository_identity_after,
    "repository_mutations": 0,
    "stop": True,
}
```

- [ ] **Step 7: Add and run focused Stage Report tests**

Cover correct six/five binding, six-versus-eleven mismatch, dependency drift, profile digest drift, missing nested output, wrong report execution ID, report byte drift, Git-status method substitution, and zero writes.

Also cover the future R6 validation-packet dependency boundary: exact complete membership passes; missing, extra, duplicate-locator, stale-byte, mismatched-digest, unavailable-byte, and ambiguous or absent runtime-turn decision inputs fail closed before aggregate readiness. These fixtures test manifest construction and packet binding; they do not synthesize a human authorization.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_routing_r3_harness.StageReportTests -v
```

Expected: all Stage Report tests pass.

---

### Task 4: Reconcile the Four Package Contract Owners

**Files:**

- Modify: `docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md`
- Modify: `docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md`
- Modify: `docs/ideas/AOS_Documentation_Agent_Routing_R1.md`
- Modify: `.codex/config.toml`
- Inspect only: the five pinned dependency paths

**Interfaces:**

- Consumes: exact functions, CLI, schemas, and recovery identity from Tasks 2–3.
- Produces: one identical six-subject/five-dependency contract across design, superseded plan, routing owner, and primary controller.

- [ ] **Step 1: Record the human-selected recovery model**

Each owner must state literally:

```text
POST_STOP_R6_CANONICAL_SIX_OUTPUT_SUBJECT_PLUS_FIVE_PINNED_DEPENDENCIES_AND_NEW_EXECUTION_ID
```

State that the old `2103c2a8805560462c4ba3bbfadbd69da6b766905e182782a126c147422281df` binding and old Stage Report are historical failed-validation Evidence only.

- [ ] **Step 2: Define the three non-interchangeable identities**

Document:

1. `subject_set_sha256`: R6 section-4.3 digest over six output files;
2. `pinned_dependency_set_sha256`: raw two-space digest over five package dependencies;
3. `authoritative_dependency_set_sha256`: validation-time R6 section-4.5 digest over all authoritative inputs.

No field may substitute for another.

- [ ] **Step 3: Replace reviewer reconstruction with the exact command contract**

Record both package-specific commands and their closed shared binding schema. The recovery `EXECUTE` uses `freeze-package-binding` before creation; the later mechanical request `method_contract.exact_algorithm_or_command` names the complete `verify-package-binding` invocation. Reviewer prose, alternate Git-status serialization, direct JSON nesting assumptions, caller-authored binding objects, or hand-built manifest code is forbidden substitution.

Each owner must also reproduce the clause-level precedence rule from the Identity Model: only the pinned legacy plan's manifest-name clause and closed command-list clause are superseded for this exact recovery execution, while every other authority and safety clause remains applicable.

- [ ] **Step 4: Preserve authority and lifecycle boundaries**

State explicitly:

```text
package status: DRAFT_CANDIDATE
static validation: NOT_RUN until separate VALIDATE terminates
safe pilot: NOT_RUN
human acceptance: NOT_RUN
activation: NOT_RUN
mass documentation authoring: FORBIDDEN
implementation authorization: NONE
git authorization: NONE
```

- [ ] **Step 5: Verify derived design SHA references only after final design bytes**

Recompute the modified design SHA-256 and update only its exact derived references in the other three owners. Do not confuse design SHA-256 with subject, dependency, profile, Stage Report, or plan identity.

- [ ] **Step 6: Validate strict configuration and documentation structure**

```bash
codex --strict-config --version
git diff --check
```

Expected: `codex-cli 0.144.5` exits zero, allowing only the existing non-blocking sandbox PATH-alias warning; `git diff --check` emits no output.

---

### Task 5: Close the Failed-Validation Regression Matrix

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Modify only if tests reveal a subject defect: `tools/routing_r3_harness.py`

**Interfaces:**

- Consumes: complete Tasks 2–4 implementation.
- Produces: deterministic regressions for both `VALIDATE-001` subject defects and both reviewer Evidence defects.

- [ ] **Step 1: Add the exact six-versus-eleven regression**

Construct a report whose six expected/present paths bind an eleven-file digest. Require `CONTRACT_VIOLATION/NONE`, `finding_origin: SUBJECT_DEFECT`, no freeze claim, and zero writes.

- [ ] **Step 2: Add the active-profile manifest regression**

Supply the legacy two-space digest as `subject_set_sha256` under `POST_STOP_R6_SUBJECT`. Require rejection before reviewer dispatch.

- [ ] **Step 3: Add reviewer-result schema regressions**

Require `check-result` to reject:

- a result whose `exact_subject` drops one bound token;
- mechanical `reasoning` other than exact configured `medium`;
- `model_binding` without `binding_class: STATIC_CONFIGURATION_BINDING`;
- `git_operations` with any key other than `add`, `commit`, `push`, `merge`, `release`;
- a checker method that substitutes `--porcelain=v1 -z` or reads `output` outside `documentation_validation_extension.output`.

- [ ] **Step 4: Add the deterministic no-loop regression**

Prove one `freeze-package-binding` command produces the closed binding and one valid `verify-package-binding` command recomputes every mechanical identity so the reviewer is not asked to reconstruct status bytes or Stage Report nesting. Require the one canonical field name `validation_profile_sha256` and reject caller-authored binding objects, field renames, and freeze/report drift. A malformed reviewer result remains a checker defect and does not mutate candidate bytes.

- [ ] **Step 5: Add generic-isolation and precedence regressions**

Prove an unrelated authorized generic Stage Report with a non-package output set still passes `validate_stage_report` and `verify-stage-report`, and prove the current generic set-equality behavior for duplicate path-list members remains unchanged. Prove package tuple ordering and uniqueness enforcement occurs only in the explicit recovery profile and `verify-package-binding`. Add a documentation parity assertion that all four mutable owners contain the exact two-clause legacy-plan precedence rule while the pinned legacy plan bytes remain unchanged.

- [ ] **Step 6: Run the complete suite**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_routing_r3_harness.py' -v
```

Expected: all existing 35 tests plus the new recovery tests pass with zero failures and zero errors.

---

### Task 6: Run Internal Gates, Freeze Six Files, and Create One New Report

**Files:**

- Inspect: exact six subject paths
- Inspect: exact five dependency paths
- Create once: `planning/verification/bootstrap/routing-r3-harness/ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001/stage-report.yaml`
- Preserve: historical Stage Report and all unrelated dirty-worktree paths

**Interfaces:**

- Consumes: separately accepted recovery plan and future exact recovery `EXECUTE` authorization.
- Produces: one corrected six-file candidate identity, one five-file dependency identity, one exact profile identity, and one immutable new Stage Report.

- [ ] **Step 1: Re-run exact preflight**

Verify repository root, branch, HEAD, complete worktree/status bytes, empty staging, six allowed path baselines, five dependency hashes, active profile identity, historical report preservation, and required new-report absence.

- [ ] **Step 2: Run required internal reviewers**

Dispatch current-candidate mechanical and contract requests in parallel. Validate their result envelopes with the harness. Only after both normalize to `PASS`, dispatch semantic review over normalized upstream Evidence. Any request/checker defect follows the one-correction loop breaker and never routes to candidate mutation.

- [ ] **Step 3: Run all repository checks**

Run the full harness suite, strict config, Ruby stdlib YAML frontmatter parse, exactly seven canonical docs, structural FTR/LES inventories, Markdown fences/relative links, UTF-8/LF/trailing-whitespace/conflict-marker scan, authority-grant scan, exact five dependency hashes, design-reference count, and `git diff --check`.

- [ ] **Step 4: Freeze the corrected identities**

Run one exact `freeze-package-binding` invocation over the validated root, exact six paths, exact five paths, and R6 profile parameters. It must internally run both manifest builders and profile-identity construction, returning the closed `package_binding`, canonical byte length, and `package_binding_sha256`. Preserve this machine result as task-local Evidence. Invalidate every gate if any bound byte changes; do not hand-assemble or rename any nested field.

- [ ] **Step 5: Recheck new report absence and create exactly once**

Use `create-stage-report --package-binding-profile ROUTING_R3_RECOVERY_V1 --expected-package-binding-sha256 <exact-freeze-digest>` only after all required gates pass. The package branch recomputes the shared binding immediately before exclusive write and rejects drift. The report must carry the complete `package_binding` object, enumerate the exact six subject paths and five dependency paths, record their separate identities, retain `DRAFT_CANDIDATE`, set validation/pilot/acceptance/activation to `NOT_RUN`, and name exactly one next action: authorize separate recovery-package `VALIDATE`.

- [ ] **Step 6: Stop the recovery EXECUTE**

Directly re-read the created Stage Report bytes once. Report its exact byte length/SHA-256, the `package_binding_sha256`, subject digest, dependency digest, `validation_profile_sha256`, changed paths, checks run/not run, repository mutations, and every Git operation `NOT_RUN`. Do not start validation.

---

### Task 7: Separately Validate Without Reviewer Reconstruction

**Files:**

- Read only: exact six subject paths, exact five dependencies, active profile owners, and the new Stage Report
- Modify: none

**Interfaces:**

- Consumes: a new exact `READ_ONLY_NEW_RUN` authorization bound to all corrected identities.
- Produces: one non-durable terminal validation report; no correction.

- [ ] **Step 1: Validate both upstream request envelopes before dispatch**

Bind exact request IDs, current `package_binding_sha256`, its six-file subject digest, five-dependency digest, `validation_profile_sha256`, Stage Report path/length/SHA-256, the complete validation-time `authoritative_dependency_manifest.entries` and `authoritative_dependency_set_sha256`, source boundary, closed output fields, `READ`, forbidden mutations, and retry limit zero. Construct the R6 authoritative-dependency manifest from the exact runtime inputs using the Identity Model above; reject missing, extra, duplicate, unavailable, stale, ambiguous-locator, or digest-mismatched members before dispatch.

- [ ] **Step 2: Run mechanical and contract gates in parallel**

Mechanical must run the exact `verify-package-binding` command with the frozen binding digest and direct post-create Stage Report identity, and report its canonical JSON Evidence. Contract independently verifies identity separation, lifecycle, immutable-report recovery, negative cases, authority, clause-level legacy-plan precedence, and bootstrap sunset.

Both requests must bind the same authoritative-dependency manifest bytes and digest. Each result must echo that identity, and primary normalization rejects omission or mismatch as `CONTRACT_VIOLATION/NONE`; reviewer reconstruction or inferred membership is forbidden.

- [ ] **Step 3: Normalize both results with `check-result` and `check-gate`**

Reject incomplete or stale Evidence. `REQUEST_OR_CHECKER_DEFECT` preserves candidate bytes and follows only the bounded harness-correction route. `SUBJECT_DEFECT` may only be reported for a separately authorized correction.

- [ ] **Step 4: Run semantic review only after upstream PASS**

Verify cross-document provenance, exact six/five separation, active-profile traceability, no false readiness/activation, cold-start usability, and no hidden dependency on chat reconstruction.

- [ ] **Step 5: Aggregate and stop**

Only the primary may return aggregate `PASS/NONE`. All required gates must be current `PASS`, bytes unchanged, material findings empty, and zero-write Evidence exact. Otherwise return the compatible non-PASS result and exactly one bounded next human decision.

- [ ] **Step 6: Keep later stages separate**

Safe pilot, human acceptance, activation, Commit, Push, Merge, Release, and mass documentation authoring remain `NOT_RUN` after static validation and each require separate exact authorization.

---

## Recovery Acceptance Criteria

The recovery implementation is ready for separate validation only when all are true:

1. Six subject paths and five dependency paths are exact, disjoint, and complete.
2. `subject_set_sha256` uses only `POST_STOP_R6_SUBJECT` bytes.
3. `pinned_dependency_set_sha256` cannot be substituted for subject identity.
4. `validation_profile_sha256` is independently reconstructed from R6 section 4.4 and uses that one canonical field name everywhere.
5. The new Stage Report losslessly enumerates all six and five members.
6. The historical Stage Report remains byte-identical and untouched.
7. `freeze-package-binding` is the sole producer of the closed canonical binding, and `verify-package-binding` validates its Stage Report nesting and exact Git status serialization without reviewer reconstruction.
8. All request/result/gate schema regressions pass.
9. The separate R6 validation packet binds a complete authoritative-dependency manifest and digest; missing, extra, duplicate, stale, unavailable, ambiguous-locator, and mismatched members fail closed.
10. Every required internal gate is current `PASS` for the final bytes.
11. Repository mutations outside the exact recovery allowlist equal zero.
12. R3 remains inactive `DRAFT_CANDIDATE`.
13. Validation, safe pilot, acceptance, activation, implementation, and all Git actions remain separately controlled.

## Plan Self-Review Checklist

- [ ] Every selected recovery-model element maps to an implementation task.
- [ ] No deferred implementation wording, ambiguous stand-in value, or inferred authority remains.
- [ ] Function names, CLI arguments, identity fields, manifest formats, and Stage Report fields are consistent across tasks.
- [ ] The six package subject files are never mixed with the five pinned dependencies.
- [ ] The recovery plan itself is an execution authority input, not a package subject/dependency member.
- [ ] The old Stage Report has no mutation or reuse route.
- [ ] Every write is deferred to a separately authorized recovery `EXECUTE`.
- [ ] Every Git mutation remains `NOT_RUN`.

## Terminal PLAN Boundary

This PLAN creates only this decision-ready artifact. It does not consume an implementation authorization, mutate the routing package, create the new Stage Report, run independent validation, run the safe pilot, accept or activate R3, or perform any Git action.

Exactly one next required action after plan review is a hash-bound human decision over this plan:

```text
HUMAN_DECIDE_ROUTING_R3_HARNESS_RECOVERY_PLAN: ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```
