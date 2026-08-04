---
document_id: AOS-DOCUMENTATION-ROUTING-R3-DETERMINISTIC-HARNESS-PLAN
document_type: IMPLEMENTATION_PLAN
revision: R1
status: DRAFT_CANDIDATE
authority: NONE_UNTIL_EXACT_ARTIFACT_HUMAN_ACCEPTANCE
task_id: ROUTING-R3-DETERMINISTIC-HARNESS-PLAN
stage: PLAN
selected_architecture: DETERMINISTIC_EXECUTABLE_HARNESS
implementation_authorization: NONE
routing_activation: NOT_GRANTED
safe_pilot: NOT_RUN
git_authorization: NONE
output_path: docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md
---

# AOS Documentation Routing R3 Deterministic Executable Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. The primary `documentation_architect` is the only writer; any specialist participation is bounded, independent, read-only review.

**Goal:** Replace the failure-prone manual Base64, checksum, request-envelope, and reviewer-result relay with a deterministic executable harness while preserving every R3 authority, validation, and activation boundary.

**Architecture:** A Python 3.9 standard-library CLI performs byte-exact subject identity, request-envelope, reviewer-result, gate-record, and Stage Report checks. All check commands are read-only; one separately authorized command may create one new Stage Report with exclusive-create semantics. The harness supplies deterministic Evidence to the primary but never dispatches agents, judges semantics, aggregates readiness, accepts or activates R3, or performs Git operations.

**Tech Stack:** Python 3.9 standard library (`argparse`, `dataclasses`, `hashlib`, `json`, `os`, `pathlib`, `re`, `stat`, `subprocess`, `unicodedata`), `unittest`, existing Codex CLI strict configuration parser, Markdown, TOML, and canonical JSON bytes that are also valid YAML 1.2.

## Global Constraints

- Repository: `/Users/muhammed/Documents/GitHub/notebook` on branch `dev`.
- Plan-authoring HEAD: `d733eeb037a517634ecc37e8b19c8421c2d20530`.
- Repository role remains `ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY`; the harness is repository validation tooling, not AOS product runtime code.
- The R3 package remains pilot-only `DRAFT_CANDIDATE`. Static validation, safe pilot, exact hash-bound human acceptance, and activation remain separate and `NOT_RUN` by this PLAN.
- Human architecture decision: `DETERMINISTIC_EXECUTABLE_HARNESS`, exact visible UTF-8 length `81`, SHA-256 `6b975eb7673b763598fa43577fb207897807758b36ffc0ff2f14d8c585bfc7a8`.
- PLAN authorization: `HUMAN_AUTHORIZE_EXACT_ROUTING_R3_DETERMINISTIC_HARNESS_PLAN`, exact visible UTF-8 length `59`, SHA-256 `87ecd7ac69b6c532d7ad1315b3925996b4ae9fccbb2c3c7a8a07e68c46a80c5d`.
- This plan is the only path mutated by the current PLAN stage.
- The current worktree is dirty with pre-existing R3, planning, and first-slice changes. Every later stage must preserve them and must bind fresh hashes rather than reuse hashes in this plan as mutation authority.
- The primary thread remains the only writer and aggregate-verdict owner.
- Required `mechanical_checker`, `contract_analyst`, and `semantic_reviewer` gates remain independent model-based reviews. The harness validates their inputs and outputs; it does not replace them.
- `mechanical_checker` remains statically bound to `gpt-5.6-luna`; no runtime fallback is added.
- Maximum concurrent read-only subagents remains two; maximum delegation depth remains one; same-request retry remains zero.
- Candidate correction and validator-harness correction remain different operations. A request/checker defect never authorizes candidate mutation.
- No historical inline Stage Report is migrated, recreated, backfilled, renamed, or treated as a new durable report.
- `planning/CURRENT.md` remains the sole durable lifecycle-state owner. The harness and its outputs own no lifecycle state or authority.
- `PLAN`, documentation/configuration `EXECUTE`, harness implementation, package `VALIDATE`, safe pilot, human acceptance/activation, and Git delivery are separate stages.
- `Edit != Commit != Push != Merge != Release`; all Git mutation operations remain `NOT_RUN` unless separately and exactly authorized.

## Decision Closure and Rejected Alternatives

The human selected the executable harness because the repeated failures were transport and validator-envelope defects, not repeated subject defects.

Two alternatives are closed for this plan:

1. Prompt-only policing is rejected because it leaves Base64, byte length, SHA-256, temporal scope, and derived-identity assembly dependent on manual relay.
2. `DEFER_R3` is rejected by the current architecture decision because it stops work without creating a completion route.

The selected route eliminates manual reconstruction. A validation request names a repository-relative Stage Report path plus exact length and SHA-256. The validator reads those bytes directly and uses the same harness in read-only mode.

## Authority and Source Precedence

1. Current explicit human decisions and exact stage authorization.
2. [Core authority and safety](../../00_Core.md), [Development workflow](../../03_Development.md), and repository [AGENTS.md](../../../AGENTS.md).
3. The accepted active [post-stop validation contract](../../../planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md) in its declared fact class.
4. The current R3 [design candidate](../specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md).
5. This plan after exact human acceptance of its bytes.
6. The earlier [R3 implementation plan](2026-08-02-aos-documentation-routing-r3-reliability-first.md), only where it does not conflict with the selected executable-harness architecture.

A conflict at a higher boundary stops only the affected future stage. No plan step may infer implementation, acceptance, activation, or Git authority.

## File Map for a Future Authorized Implementation

The later implementation authorization must name an exact allowlist and fresh baseline hashes. The intended code and contract surface is:

| Path | Operation | Responsibility |
|---|---|---|
| `tools/routing_r3_harness.py` | Create | Single standard-library CLI and deterministic contract implementation. |
| `tests/test_routing_r3_harness.py` | Create | Unit, contract, negative, collision, and zero-write tests. |
| `docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md` | Modify | Record the human-selected harness architecture and bootstrap/active transport split. |
| `docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md` | Modify | Mark the no-script implementation approach superseded by this accepted plan. |
| `docs/ideas/AOS_Documentation_Agent_Routing_R1.md` | Modify | Make harness preflight and result normalization part of the R3 routing contract. |
| `.codex/config.toml` | Modify | Require harness checks at the primary controller boundary without activating R3. |

The four `.codex/agents/*.toml` files remain read-only implementation inputs unless a later preflight finds a concrete parity defect that requires a separately expanded allowlist. The harness must validate their existing request/result fields rather than add a second schema vocabulary.

The future implementation authorization must also name exactly one new bootstrap Stage Report path when the implementation `EXECUTE` is expected to end in `PASS`:

```text
planning/verification/bootstrap/routing-r3-harness/<execution_id>/stage-report.yaml
```

That path is a one-run pre-activation transport owned by the already active post-stop validation contract. It is not the R3 active transport, is never reused, and does not backfill any historical report. After exact R3 acceptance and activation, only this existing R3 path contract is permitted:

```text
planning/verification/runs/<task_id>/<execution_id>/stage-report.yaml
```

## Harness Contract

### Commands

```text
python3 tools/routing_r3_harness.py manifest ...
python3 tools/routing_r3_harness.py check-request ...
python3 tools/routing_r3_harness.py check-result ...
python3 tools/routing_r3_harness.py check-gate ...
python3 tools/routing_r3_harness.py create-stage-report ...
python3 tools/routing_r3_harness.py verify-stage-report ...
```

All commands except `create-stage-report` are read-only. The create command is legal only inside a separately authorized primary-writer `EXECUTE`, for its one exact allowlisted output path, after candidate freeze.

### Canonical subject manifest

Paths are normalized repository-relative POSIX paths, rejected if empty, absolute, non-NFC, duplicated, symlinked, or containing `.`, `..`, backslash, control bytes, or ambiguous normalization. Records are sorted by path UTF-8 bytes and encoded as:

```text
<lowercase-file-sha256><SP><SP><decimal-byte-length><SP><SP><normalized-path><LF>
```

`subject_set_sha256` is the SHA-256 of the complete manifest bytes. No locale sort, rendered Markdown, filesystem mtime, Git index metadata, or chat text participates.

### Canonical Stage Report bytes

The harness accepts one UTF-8 JSON object containing the generic Stage Report mapping, validates it, and serializes it with:

```python
json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
```

These bytes are valid JSON and valid YAML 1.2. The `.yaml` suffix remains the repository contract. The harness reports exact byte length and lowercase SHA-256 computed from the bytes written, never from a re-rendered object.

The accepted JSON domain is closed to mappings with string keys, lists, strings,
integers, booleans, and `null`. Floating-point values, non-string mapping keys,
duplicate JSON keys, non-finite numbers, and lone surrogate code points are
rejected before serialization.

### Result and reason algebra

```text
PASS | FAIL | BLOCKED | CONFLICT | UNKNOWN | NOT_RUN | CONTRACT_VIOLATION
```

```text
NONE
REVIEWER_EVIDENCE_CONFLICT
BLOCKED_REQUIRED_REVIEW_CAPABILITY
BLOCKED_STAGE_REPORT_PATH_COLLISION
BLOCKED_HUMAN_DECISION_REQUIRED
BLOCKED_UNRESOLVED_CONFLICT
BLOCKED_REFERENCE_ACCESS
BLOCKED_SUBJECT_IDENTITY_MISMATCH
BLOCKED_SCOPE_OR_PROVENANCE
BLOCKED_VALIDATION_SUBJECT_MISMATCH
BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH
```

`CONFLICT` requires `REVIEWER_EVIDENCE_CONFLICT`; `BLOCKED` requires one `BLOCKED_*` value; every other result requires `NONE`. Invalid pairs are deterministic request/result contract defects and never become subject findings.

### Output and exit contract

Every invocation prints exactly one canonical JSON object to stdout and diagnostics only to stderr.

| Exit | Meaning | Technical mapping |
|---:|---|---|
| `0` | Requested deterministic operation passed | `PASS/NONE` |
| `2` | Subject violates a bound deterministic invariant | `FAIL/NONE`, `SUBJECT_DEFECT` |
| `3` | Request, result, gate, or harness input violates its contract | `CONTRACT_VIOLATION/NONE`, `REQUEST_OR_CHECKER_DEFECT` |
| `4` | Required path identity, capability, or authorization binding is unavailable/mismatched | `BLOCKED` with one closed blocker reason |
| `5` | Existing Stage Report path collision | `BLOCKED/BLOCKED_STAGE_REPORT_PATH_COLLISION` |

No command returns a lifecycle label as a technical result. No command emits human acceptance, routing activation, implementation permission, or Git authority.

---

## Stage A: Reconcile the Approved Design Before Code

### Task 1: Bind the Exact Implementation Authorization and Current State

**Files:**

- Inspect: `AGENTS.md`
- Inspect: `docs/00_Core.md`
- Inspect: `docs/03_Development.md`
- Inspect: `planning/CURRENT.md`
- Inspect: every path in the future implementation File Map
- Modify: none

**Interfaces:**

- Consumes: exact implementation authorization containing task ID, execution ID, allowlist, fresh baseline hashes, correction budget, and exact bootstrap Stage Report path.
- Produces: immutable preflight Evidence for the implementation stage.

- [ ] **Step 1: Re-observe repository identity**

Run:

```bash
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short
git diff --cached --name-only
```

Expected: the exact authorization matches root, branch, HEAD, starting worktree fingerprint, and empty staging state. Preserve all pre-existing changes.

- [ ] **Step 2: Verify exact allowed paths and baseline bytes**

For each path named by the authorization, require the expected existing/absent state, regular-file type where present, and exact SHA-256. An extra or missing path returns `BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH`; byte drift returns `BLOCKED_SUBJECT_IDENTITY_MISMATCH`.

- [ ] **Step 3: Verify bootstrap report collision absence**

Reject an empty execution ID, `.`, `..`, slash, backslash, control byte, non-NFC value, symlinked parent, existing target, or target outside the exact bootstrap namespace. Preflight must also observe `os.O_NOFOLLOW`; if it is unavailable, return `BLOCKED_REQUIRED_REVIEW_CAPABILITY` instead of substituting a weaker open method. Do not inspect, overwrite, rename, reuse, or delete an existing target.

### Task 2: Amend the Current R3 Design and Supersede the No-script Plan

**Files:**

- Modify: `docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md`
- Modify: `docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md`
- Reference: this plan

**Interfaces:**

- Consumes: human decision SHA-256 `6b975eb7673b763598fa43577fb207897807758b36ffc0ff2f14d8c585bfc7a8`.
- Produces: one unambiguous architecture owner and one explicit supersession edge.

- [ ] **Step 1: Record the selected architecture without claiming exact-byte acceptance**

Change the selected approach to `DETERMINISTIC_EXECUTABLE_HARNESS`, keep `status: DRAFT_CANDIDATE`, and record that exact corrected design bytes still require separate human review.

- [ ] **Step 2: Add the harness boundary**

Specify the command set, manifest algorithm, canonical Stage Report serialization, bootstrap-only report namespace, active R3 report namespace, exclusive-create behavior, closed exits, zero authority, and model-review preservation exactly as defined above.

- [ ] **Step 3: Mark the earlier implementation plan as superseded for mechanical architecture**

Add a top-level notice that the earlier `BOUNDED_CONTRACT_AND_CONFIGURATION_UPGRADE` plan remains historical Evidence but is not executable after the current human decision. Point to this plan; do not rewrite historical authorizations or claim the successor is accepted before exact human review.

Expected self-check: the live design no longer says that the selected implementation creates no routing scripts, and the older plan cannot be mistaken for the current executable plan.

---

## Stage B: Implement the Pure Deterministic Core with TDD

### Task 3: Write Failing Identity and Path Tests

**Files:**

- Create: `tests/test_routing_r3_harness.py`
- Test target: `tools/routing_r3_harness.py`

**Interfaces:**

- Consumes: temporary repository roots and ordered/unordered path lists.
- Produces: executable tests for `normalize_relative_path`, `build_manifest`, and `sha256_bytes`.

- [ ] **Step 1: Add the initial test module**

```python
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HARNESS = REPO_ROOT / "tools" / "routing_r3_harness.py"


class IdentityTests(unittest.TestCase):
    def test_manifest_is_utf8_byte_sorted_and_byte_exact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "b.md").write_bytes(b"B\n")
            (root / "a.md").write_bytes(b"A\n")
            result = subprocess.run(
                [sys.executable, str(HARNESS), "manifest", "--root", str(root),
                 "--path", "b.md", "--path", "a.md"],
                check=False, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            a_digest = hashlib.sha256(b"A\n").hexdigest()
            b_digest = hashlib.sha256(b"B\n").hexdigest()
            expected = (
                f"{a_digest}  2  a.md\n"
                f"{b_digest}  2  b.md\n"
            ).encode("utf-8")
            self.assertEqual(payload["manifest_hex"], expected.hex())
            self.assertEqual(payload["subject_set_sha256"], hashlib.sha256(expected).hexdigest())

    def test_parent_component_is_rejected(self) -> None:
        result = subprocess.run(
            [sys.executable, str(HARNESS), "manifest", "--root", str(REPO_ROOT),
             "--path", "../outside"],
            check=False, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 3)
        self.assertEqual(json.loads(result.stdout)["result"], "CONTRACT_VIOLATION")
```

- [ ] **Step 2: Run the focused tests and observe the expected red state**

Run:

```bash
python3 -m unittest tests.test_routing_r3_harness.IdentityTests -v
```

Expected: `FAIL` because `tools/routing_r3_harness.py` does not yet exist.

### Task 4: Implement Path Normalization and Subject Identity

**Files:**

- Create: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Produces: `normalize_relative_path(value: str) -> str`, `sha256_bytes(value: bytes) -> str`, and `build_manifest(root: Path, paths: list[str]) -> bytes`.

- [ ] **Step 1: Add the executable foundation**

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path
from typing import Any, Optional


HEX_64 = re.compile(r"[0-9a-f]{64}")
CONTROL = re.compile(r"[\x00-\x1f\x7f]")


class HarnessError(Exception):
    def __init__(self, exit_code: int, result: str, reason_code: str, message: str,
                 finding_origin: Optional[str] = None) -> None:
        super().__init__(message)
        self.exit_code = exit_code
        self.result = result
        self.reason_code = reason_code
        self.finding_origin = finding_origin


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def normalize_relative_path(value: str) -> str:
    if not value or value.startswith("/") or "\\" in value or CONTROL.search(value):
        raise HarnessError(3, "CONTRACT_VIOLATION", "NONE", "invalid path",
                           "REQUEST_OR_CHECKER_DEFECT")
    if unicodedata.normalize("NFC", value) != value:
        raise HarnessError(3, "CONTRACT_VIOLATION", "NONE", "non-NFC path",
                           "REQUEST_OR_CHECKER_DEFECT")
    parts = value.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise HarnessError(3, "CONTRACT_VIOLATION", "NONE", "ambiguous path",
                           "REQUEST_OR_CHECKER_DEFECT")
    return value


def build_manifest(root: Path, paths: list[str]) -> bytes:
    normalized = [normalize_relative_path(value) for value in paths]
    if len(set(normalized)) != len(normalized):
        raise HarnessError(3, "CONTRACT_VIOLATION", "NONE", "duplicate path",
                           "REQUEST_OR_CHECKER_DEFECT")
    records: list[bytes] = []
    for relative in sorted(normalized, key=lambda value: value.encode("utf-8")):
        target = root / relative
        if target.is_symlink() or not target.is_file():
            raise HarnessError(2, "FAIL", "NONE", f"invalid subject: {relative}",
                               "SUBJECT_DEFECT")
        data = target.read_bytes()
        records.append(f"{sha256_bytes(data)}  {len(data)}  {relative}\n".encode("utf-8"))
    return b"".join(records)
```

- [ ] **Step 2: Add `manifest` CLI output**

Return canonical JSON with `result: PASS`, `reason_code: NONE`, `manifest_hex`, `manifest_byte_length`, `subject_set_sha256`, `repository_mutations: 0`, and `stop: true`.

- [ ] **Step 3: Run the focused tests**

Run the Task 3 command. Expected: both tests `ok`.

---

## Stage C: Implement Envelope and Evidence Validation with TDD

### Task 5: Add Contract Tests for Requests, Results, and Gates

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Test target: `tools/routing_r3_harness.py`

**Interfaces:**

- Consumes: JSON request/result/gate files and an exact current subject SHA-256.
- Produces: failing tests for complete envelopes, `temporal_scope`, model/role binding, result/reason compatibility, zero writes, and stale identity rejection.

- [ ] **Step 1: Add a complete valid reviewer-result factory**

The factory must include every configured R3 field: task/request/parent IDs, class, role, model, reasoning, exact subject, subject SHA-256, source boundary, sources, methods, one scalar `temporal_scope`, classified claims, conflicts, unknowns, recommendations, checks run/not run, limitations, model binding, repository mutations `0`, all Git mutations `NOT_RUN`, result, reason code, exactly one next action, and `stop: true`.

- [ ] **Step 2: Add one negative test per defect class**

Test these exact mutations independently:

- missing `subject_sha256`;
- mismatched current subject SHA-256;
- missing, empty, list-valued, or malformed `temporal_scope`;
- unknown technical result;
- `BLOCKED/NONE`;
- `PASS/BLOCKED_REQUIRED_REVIEW_CAPABILITY`;
- wrong role or configured model binding;
- `repository_mutations: 1`;
- any Git mutation not `NOT_RUN`;
- zero or two `next_required_action` values;
- `stop: false`;
- missing `invariant_semantics` for an exact-count request;
- missing exact command or forbidden substitutions in `method_contract`.

Expected for envelope/checker defects: exit `3`, `CONTRACT_VIOLATION/NONE`, origin `REQUEST_OR_CHECKER_DEFECT`, and no candidate mutation recommendation.

- [ ] **Step 3: Run the new tests and observe the expected red state**

```bash
python3 -m unittest tests.test_routing_r3_harness -v
```

Expected: the new request/result/gate tests fail because their commands are not implemented.

### Task 6: Implement Closed Request, Result, and Gate Validators

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Produces: `validate_request`, `validate_result`, `validate_gate`, and `validate_result_reason`.

- [ ] **Step 1: Add immutable closed vocabularies**

Define `TECHNICAL_RESULTS`, `REASON_CODES`, `CLAIM_CLASSES`, role/model bindings, required result fields, allowed operations `["READ"]`, forbidden operations, and required Git `NOT_RUN` fields exactly from the active R3 contract.

- [ ] **Step 2: Implement result/reason compatibility**

```python
def validate_result_reason(result: str, reason_code: str) -> None:
    if result not in TECHNICAL_RESULTS or reason_code not in REASON_CODES:
        raise contract_error("unknown result or reason_code")
    if result == "CONFLICT" and reason_code != "REVIEWER_EVIDENCE_CONFLICT":
        raise contract_error("CONFLICT requires REVIEWER_EVIDENCE_CONFLICT")
    if result == "BLOCKED" and not reason_code.startswith("BLOCKED_"):
        raise contract_error("BLOCKED requires a closed blocker reason")
    if result not in {"CONFLICT", "BLOCKED"} and reason_code != "NONE":
        raise contract_error("non-CONFLICT/non-BLOCKED requires NONE")
```

- [ ] **Step 3: Implement exact temporal-scope validation**

Accept only the scalar `CURRENT_SNAPSHOT` or a full-match interval `<ISO-8601>/<ISO-8601>`. Reject booleans, numbers, lists, mappings, empty strings, whitespace-padded strings, and open intervals.

- [ ] **Step 4: Bind role, model, source, and current subject identity**

Reject missing or mismatched task/request/parent IDs, role, configured model, exact subject, subject SHA-256, source boundary, sources, methods, repository mutation count, Git state, result, next action, and stop flag. The checker consumes expected values from explicit CLI arguments or a request file; it never fills missing Evidence from chat history.

- [ ] **Step 5: Run the complete unit suite**

Expected: all identity and contract tests pass with no repository writes.

---

## Stage D: Implement Exclusive Stage Report Creation with TDD

### Task 7: Add Stage Report Transport and Collision Tests

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Test target: `tools/routing_r3_harness.py`

**Interfaces:**

- Consumes: one validated Stage Report JSON input, transport profile, repository root, exact task/execution IDs, and exact output path.
- Produces: tests for canonical bytes, direct re-read identity, exclusive creation, collision, symlink rejection, namespace separation, and read-only verification.

- [ ] **Step 1: Test canonical serialization**

Provide the same mapping with different JSON input key orders. Require byte-identical output, one trailing LF, UTF-8 encoding, exact length/SHA-256, and successful `json.loads` of written bytes.

- [ ] **Step 2: Test bootstrap and active namespace separation**

`PRE_R3_BOOTSTRAP` accepts only:

```text
planning/verification/bootstrap/routing-r3-harness/<execution_id>/stage-report.yaml
```

`R3_ACTIVE` accepts only:

```text
planning/verification/runs/<task_id>/<execution_id>/stage-report.yaml
```

Neither profile accepts the other path. Both reject invalid components and symlinked ancestors.

- [ ] **Step 3: Test collision and no-overwrite behavior**

The first authorized create succeeds. A second create against the same path exits `5` with `BLOCKED_STAGE_REPORT_PATH_COLLISION`; original bytes and metadata stay unchanged. The harness never reads the existing report during collision handling.

- [ ] **Step 4: Test direct validator verification**

`verify-stage-report` reads the exact path, confirms regular/non-symlink type, UTF-8, complete mapping, expected byte length, expected SHA-256, and result/reason algebra. A mismatch exits `4` with `BLOCKED_VALIDATION_SUBJECT_MISMATCH` and performs zero writes.

- [ ] **Step 5: Run the tests and observe the expected red state**

Expected: new transport tests fail until Task 8 is implemented.

### Task 8: Implement Canonical Render, Exclusive Create, and Direct Verify

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Produces: `canonical_json_bytes`, `validate_transport_path`, `create_stage_report`, and `verify_stage_report`.

- [ ] **Step 1: Implement canonical bytes**

```python
def canonical_json_bytes(value: dict[str, Any]) -> bytes:
    validate_closed_json_domain(value)
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":")) + "\n").encode("utf-8")
```

`validate_closed_json_domain` recursively enforces the closed JSON domain above
and the JSON loader rejects duplicate object keys with `object_pairs_hook`.

- [ ] **Step 2: Implement safe path validation**

Resolve the repository root once, validate every relative component without following the target, require the expected transport-profile path exactly, and reject any existing or symlinked ancestor that escapes the repository. Do not accept path equivalence after normalization as a substitute for exact normalized input.

- [ ] **Step 3: Implement one-shot file creation**

Create missing in-repository parents only within the exact allowlisted report path. Require the preflight-observed `os.O_NOFOLLOW` capability, then open the target using `os.open` with `O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW`, mode `0o644`; write all bytes, flush, close, then re-open read-only and recompute length/SHA-256. On any incomplete write, report `FAIL/NONE`, preserve the observed partial path for a separate recovery decision, and never retry or delete it.

- [ ] **Step 4: Implement verification with before/after identity**

Snapshot report bytes and repository status before validation, verify, then confirm the report hash and repository/staging status are unchanged. Print `repository_mutations: 0` only from the observed equality, never as a default claim.

- [ ] **Step 5: Run all unit and negative tests**

Expected: all tests pass; the only writes occur inside test-created temporary roots.

---

## Stage E: Integrate the Harness Without Activating R3

### Task 9: Update the Routing Contract and Primary Controller

**Files:**

- Modify: `docs/ideas/AOS_Documentation_Agent_Routing_R1.md`
- Modify: `.codex/config.toml`
- Inspect only: `.codex/agents/mechanical-checker.toml`
- Inspect only: `.codex/agents/contract-analyst.toml`
- Inspect only: `.codex/agents/semantic-reviewer.toml`
- Inspect only: `.codex/agents/reference-explorer.toml`

**Interfaces:**

- Consumes: passing harness tests and current R3 request/result contracts.
- Produces: primary-controller instructions that require deterministic pre-dispatch and post-result checks.

- [ ] **Step 1: Require pre-dispatch request validation**

The primary must run `check-request` against the current subject and exact configured role/model before dispatch. An unsent invalid envelope is corrected locally without consuming a reviewer request; a dispatched terminal result is never retried under the same `request_id`.

- [ ] **Step 2: Require post-result Evidence validation**

The primary must run `check-result` and `check-gate` before using Evidence. Invalid or stale Evidence becomes `CONTRACT_VIOLATION/NONE`, preserves candidate bytes, and routes only to the already bounded harness-correction rule.

- [ ] **Step 3: Require direct-path Stage Report validation**

Normal R3 validation authorizations bind path, byte length, SHA-256, candidate manifest SHA-256, and validation profile. Inline Base64 is not the canonical R3 transport and is never reconstructed by a reviewer. The bootstrap profile remains explicit, one-run, pre-activation, and path-bound.

- [ ] **Step 4: Preserve reviewer and authority boundaries**

State that harness `PASS` is only deterministic Evidence. Required model-based gates, primary synthesis, candidate freeze, Stage Report creation authority, human acceptance/activation, and Git boundaries remain unchanged.

- [ ] **Step 5: Confirm no unnecessary agent-definition edits**

Compare all four agent definitions with the harness field vocabulary. If they already require the same request/result fields, temporal scope, result/reason algebra, zero mutations, Git `NOT_RUN`, one next action, and stop, leave their bytes unchanged. A concrete mismatch requires a new bounded scope decision; do not silently expand the implementation allowlist.

### Task 10: Add CLI Integration and Zero-write Regression Tests

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Test: all implementation candidate paths

**Interfaces:**

- Produces: one end-to-end disposable-root test for manifest -> request -> result -> gate -> Stage Report -> verification.

- [ ] **Step 1: Exercise the positive pipeline**

Use a temporary repository root, two subject files, one complete mechanical request, one valid mechanical result, one normalized gate, and one Stage Report. Require exact identities at every edge and no write outside the exact temporary Stage Report path.

- [ ] **Step 2: Exercise the loop-breaker pipeline**

Run one invalid request/result through harness-correction classification, then a fresh request ID with the same checker defect. Require aggregate input `FAIL/NONE`, exactly one human choice `DEFER_OR_REDESIGN_VALIDATOR`, no candidate mutation, and no further finding-specific recovery suggestion.

- [ ] **Step 3: Exercise candidate drift**

Change one temporary subject byte after a passing gate. Require stale gate rejection, recomputed manifest identity, invalidated dependent Evidence, and no freeze claim.

- [ ] **Step 4: Run the complete tests**

```bash
python3 -m unittest discover -s tests -p 'test_routing_r3_harness.py' -v
```

Expected: all tests pass with zero writes outside disposable temporary roots.

---

## Stage F: Internal Static Checks and Candidate Freeze

### Task 11: Run Deterministic Internal Checks

**Files:**

- Inspect: exact future implementation candidate set
- Modify: none unless a technical defect is corrected within the exact implementation correction budget

- [ ] **Step 1: Compile and test the harness**

```bash
python3 -m py_compile tools/routing_r3_harness.py tests/test_routing_r3_harness.py
python3 -m unittest discover -s tests -p 'test_routing_r3_harness.py' -v
```

Expected: successful compilation and all tests pass.

- [ ] **Step 2: Validate Codex configuration using the observed capability**

```bash
codex --strict-config --version
```

Expected at plan authoring: `codex-cli 0.144.5`. The future run records the freshly observed version. Absence of this required named capability returns `BLOCKED_REQUIRED_REVIEW_CAPABILITY`; no TOML parser substitution is allowed.

- [ ] **Step 3: Run repository documentation invariants**

Verify:

- exactly seven canonical `docs/00_Core.md` through `docs/06_Features.md` files remain;
- YAML frontmatter parses using a preflight-observed parser;
- Markdown fences and relative links resolve;
- structural `FTR-001..030` and `LES-001..042` inventories remain complete and unique under the repository-defined counting semantics;
- forbidden authority grants are absent;
- UTF-8, LF-only bytes, trailing whitespace, conflict markers, and file types pass;
- `git diff --check` passes for tracked changes;
- untracked harness/test bytes receive equivalent direct checks.

- [ ] **Step 4: Run harness-specific negative matrix**

Require passing coverage for malformed paths, duplicate manifest entries, invalid UTF-8, stale SHA-256, missing method contract, temporal-scope defects, result/reason mismatch, role/model mismatch, candidate drift, report collision, symlink ancestor, second create, validation write detection, and repeated checker defect after one correction.

- [ ] **Step 5: Classify every non-PASS deterministic finding**

Only `SUBJECT_DEFECT` can route to candidate correction. `REQUEST_OR_CHECKER_DEFECT` preserves candidate bytes and can consume at most the exact harness-correction budget. If a fresh request repeats the defect, stop with `FAIL/NONE` and one next human choice `DEFER_OR_REDESIGN_VALIDATOR`.

### Task 12: Freeze the Exact Candidate and Create One Bootstrap Stage Report

**Files:**

- Inspect: all exact candidate paths
- Create once: the exact bootstrap Stage Report path from the future authorization

- [ ] **Step 1: Build the final candidate manifest**

Use `manifest` over the exact implementation subject set. Record every path, byte length, file SHA-256, manifest byte length, and `subject_set_sha256`.

- [ ] **Step 2: Confirm all required internal gates are current PASS**

No missing, stale, `NOT_RUN`, `UNKNOWN`, `CONFLICT`, `BLOCKED`, `FAIL`, or `CONTRACT_VIOLATION` required gate may participate in freeze. Recompute candidate identity after the final gate and require unchanged bytes.

- [ ] **Step 3: Recheck exact bootstrap report absence**

If the path exists, return `BLOCKED/BLOCKED_STAGE_REPORT_PATH_COLLISION`, do not inspect or mutate it, and require a new authorization plus execution identity.

- [ ] **Step 4: Create the canonical report exactly once**

Invoke `create-stage-report` as the primary writer. Re-read the new file and report its exact path, byte length, and SHA-256. Do not create an inline Base64 substitute.

- [ ] **Step 5: Stop the implementation stage**

The report must state `lifecycle_status: DRAFT_CANDIDATE`, static validation `NOT_RUN`, safe pilot `NOT_RUN`, human acceptance/activation `NOT_RUN`, all Git mutations `NOT_RUN`, exactly one next action `AUTHORIZE_SEPARATE_ROUTING_R3_HARNESS_PACKAGE_VALIDATE`, and `stop: true`.

---

## Stage G: Separate Independent VALIDATE

This stage is not authorized by implementation. It requires a new read-only authorization bound to the exact candidate manifest, subject-set SHA-256, bootstrap Stage Report path/length/SHA-256, active post-stop profile identity, verifier identity, and zero-write boundary.

### Task 13: Run Independent Mechanical and Contract Gates

- [ ] `mechanical_checker` reads exact candidate and report paths, executes the bound harness commands, and verifies identity, structure, manifests, paths, config parsing, test results, and zero writes.
- [ ] `contract_analyst` independently verifies lifecycle, failure/recovery, collision, retry, correction budget, negative cases, authority, bootstrap sunset, and active-transport boundaries.
- [ ] Both requests use distinct request IDs, exact current subject SHA-256, complete method contracts, retry limit zero, and required result fields.
- [ ] The primary validates both results with the harness before normalization.

### Task 14: Run Sequential Semantic Closure

- [ ] Only after current mechanical and contract Evidence terminate and normalize to `PASS`, dispatch `semantic_reviewer` over the exact current candidate and normalized upstream Evidence.
- [ ] Verify design/plan/routing/config traceability, no parallel lifecycle owner, no false active/readiness claim, no historical report backfill, and cold-start usability without chat history.
- [ ] Any candidate mutation invalidates affected and dependent gates and requires a separately authorized correction `EXECUTE`; `VALIDATE` never repairs.

### Task 15: Compute the Aggregate and Stop

The primary alone computes the aggregate. `PASS` and `final_candidate_frozen: true` are permitted only when all required gates are present, current, and `PASS`, material findings are empty, candidate/report bytes are unchanged, and zero-write Evidence passes. The Verification Report ends with exactly one next action: authorize the safe pilot if `PASS`, otherwise authorize one bounded correction or make the required human decision.

---

## Stage H: Safe Pilot, Acceptance, and Activation Boundaries

### Task 16: Run a Separate Safe Read-only Pilot

The pilot must cover:

1. valid mechanical, contract, semantic, and exact-reference routes;
2. unsent envelope repair without consuming a reviewer request;
3. incomplete reviewer result rejection;
4. missing or malformed temporal scope;
5. result/reason incompatibility;
6. candidate drift and dependent-gate invalidation;
7. Stage Report path collision without inspection or mutation;
8. required reviewer unavailability without fallback;
9. one harness correction followed by a repeated defect and terminal `DEFER_OR_REDESIGN_VALIDATOR`;
10. zero repository/Git mutations by reviewers and validator.

The pilot uses only disposable fixtures and new execution identities. It does not recreate historical inline payloads or perform mass documentation authoring.

### Task 17: Present Exact Human Acceptance and Activation Packet

The packet contains exact design, supersession-plan, current plan, routing/config, harness, tests, unchanged agent-definition hashes, candidate manifest, independent verification, safe-pilot Evidence, limitations, and all `NOT_RUN` states. Human acceptance and activation are two explicit hash-bound decisions. Commit, Push, Merge, Release, implementation-repository selection, and mass documentation authoring remain separately controlled.

## Plan Self-review Checklist

- [ ] The human-selected `DETERMINISTIC_EXECUTABLE_HARNESS` is the only active plan architecture.
- [ ] The harness eliminates manual Base64 relay and validates exact path/length/hash identities.
- [ ] Bootstrap and active R3 Stage Report namespaces cannot be confused.
- [ ] Historical inline Stage Reports are never migrated, recreated, or backfilled.
- [ ] Only one command can write, only under separate exact primary authorization, and it uses exclusive creation.
- [ ] Required model reviewers remain required; harness `PASS` is not semantic acceptance.
- [ ] Request/result/gate schemas, temporal scope, result/reason algebra, claim classes, and role/model bindings match current R3 contracts.
- [ ] Subject defects and request/checker defects have different correction routes.
- [ ] Repeated harness defect stops once at `DEFER_OR_REDESIGN_VALIDATOR`.
- [ ] Candidate drift invalidates stale and dependent gates.
- [ ] `planning/CURRENT.md` remains the sole lifecycle-state owner.
- [ ] R3 remains inactive `DRAFT_CANDIDATE` until separate validation, pilot, acceptance, and activation.
- [ ] No implementation or Git operation is authorized by this plan.
- [ ] No unresolved drafting marker, contradictory status, broken relative link, malformed frontmatter, or unbalanced fence remains.

## PLAN Terminal Report Contract

```yaml
task_id: ROUTING-R3-DETERMINISTIC-HARNESS-PLAN
stage: PLAN
result: PASS
reason_code: NONE
artifact: docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md
lifecycle_status: DRAFT_CANDIDATE
selected_architecture: DETERMINISTIC_EXECUTABLE_HARNESS
changed_paths:
  - docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md
checks_not_run:
  - implementation
  - independent_validation
  - safe_pilot
  - human_acceptance
  - activation
  - commit
  - push
  - merge
  - release
implementation_authorization: NONE
routing_activation: NOT_GRANTED
Git_operations:
  add: NOT_RUN
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: HUMAN_REVIEW_EXACT_ROUTING_R3_DETERMINISTIC_HARNESS_PLAN
stop: true
```
