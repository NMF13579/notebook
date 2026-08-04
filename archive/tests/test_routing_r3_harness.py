#!/usr/bin/env python3
"""Tests for the deterministic AOS documentation-routing R3 harness."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import unicodedata
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parents[1]
HARNESS = REPO_ROOT / "tools" / "routing_r3_harness.py"


def run_harness(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(HARNESS), *arguments],
        check=False,
        capture_output=True,
        text=True,
    )


def write_json(path: Path, value: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )


SUBJECT_SHA256 = "a" * 64


def valid_request() -> Dict[str, Any]:
    return {
        "task_id": "TASK-001",
        "request_id": "TASK-001-MECH-001",
        "parent_task_id": "PARENT-001",
        "task_class": "DOCUMENTATION_VALIDATION",
        "role": "mechanical_checker",
        "exact_subject": ["docs/a.md"],
        "subject_sha256": SUBJECT_SHA256,
        "source_boundary": ["docs/a.md"],
        "invariant_semantics": {
            "kind": "EXACT_COUNT",
            "unit": "level-2 headings",
            "expected": 1,
        },
        "method_contract": {
            "preflight_observed_capability": "python3.9-stdlib",
            "exact_algorithm_or_command": "python3 tools/routing_r3_harness.py manifest",
            "expected_success_shape": "exit 0 and PASS/NONE canonical JSON",
            "forbidden_substitutions": ["raw token count", "unbound parser"],
        },
        "required_output_fields": [
            "task_id",
            "request_id",
            "result",
            "reason_code",
            "stop",
        ],
        "stop_conditions": ["terminal result", "identity mismatch"],
        "allowed_operations": ["READ"],
        "forbidden_operations": [
            "WRITE",
            "COMMIT",
            "PUSH",
            "MERGE",
            "RELEASE",
            "NESTED_DELEGATION",
        ],
        "retry_limit": 0,
    }


def valid_result() -> Dict[str, Any]:
    request = valid_request()
    return {
        "task_id": request["task_id"],
        "request_id": request["request_id"],
        "parent_task_id": request["parent_task_id"],
        "task_class": request["task_class"],
        "role": request["role"],
        "model": "gpt-5.6-luna",
        "reasoning": "medium",
        "exact_subject": request["exact_subject"],
        "subject_sha256": request["subject_sha256"],
        "source_boundary": request["source_boundary"],
        "sources": [{"path": "docs/a.md", "claim_class": "OBSERVED_AT_SNAPSHOT"}],
        "methods": ["bound manifest command"],
        "temporal_scope": "CURRENT_SNAPSHOT",
        "classified_claims": [
            {"claim_class": "OBSERVED_AT_SNAPSHOT", "claim": "subject read"}
        ],
        "conflicts": [],
        "unknowns": [],
        "recommendations": [],
        "checks_run": ["manifest identity"],
        "checks_not_run": [],
        "limitations": [],
        "model_binding": {
            "preferred_model": "gpt-5.3-codex-spark",
            "configured_model": "gpt-5.6-luna",
            "binding_class": "STATIC_CONFIGURATION_BINDING",
            "reason": "Spark absent from the configuration-time model catalog",
        },
        "repository_mutations": 0,
        "git_operations": {
            "add": "NOT_RUN",
            "commit": "NOT_RUN",
            "push": "NOT_RUN",
            "merge": "NOT_RUN",
            "release": "NOT_RUN",
        },
        "result": "PASS",
        "reason_code": "NONE",
        "next_required_action": "RETURN_EVIDENCE_TO_PRIMARY",
        "stop": True,
    }


def valid_gate() -> Dict[str, Any]:
    return {
        "gate_id": "TASK-001-GATE-MECH",
        "required": True,
        "role": "mechanical_checker",
        "request_id": "TASK-001-MECH-001",
        "subject_sha256": SUBJECT_SHA256,
        "source_boundary": ["docs/a.md"],
        "result": "PASS",
        "reason_code": "NONE",
        "finding_ids": [],
        "limitations": [],
        "repository_mutations": 0,
        "stop": True,
    }


def valid_stage_report() -> Dict[str, Any]:
    report_path = (
        "planning/verification/bootstrap/routing-r3-harness/"
        "EXEC-001/stage-report.yaml"
    )
    return {
        "task_id": "TASK-001",
        "stage": "EXECUTE",
        "result": "PASS",
        "reason_code": "NONE",
        "starting_identity": {"subject_sha256": "a" * 64},
        "ending_identity": {"subject_sha256": "b" * 64},
        "changed_paths": ["docs/a.md", report_path],
        "checks_run": ["unit tests"],
        "checks_not_run": ["independent validation"],
        "findings": [],
        "limitations": [],
        "unknowns": [],
        "out_of_scope_state": ["pre-existing worktree state preserved"],
        "authorization_consumed": True,
        "Git_operations": {
            "add": "NOT_RUN",
            "commit": "NOT_RUN",
            "push": "NOT_RUN",
            "merge": "NOT_RUN",
            "release": "NOT_RUN",
        },
        "next_required_action": "AUTHORIZE_SEPARATE_VALIDATE",
        "stop": True,
        "lifecycle_status": "DRAFT_CANDIDATE",
        "documentation_validation_extension": {
            "report_kind": "DOCUMENTATION_STAGE_REPORT",
            "interval_instance_id": "TASK-001.EXEC-001",
            "authorization": {
                "authorization_id": "EXEC-001",
                "authorization_state": "CONSUMED_ONE_SHOT",
            },
            "output": {
                "expected_paths": ["docs/a.md"],
                "present_paths": ["docs/a.md"],
                "absent_paths": [],
                "partial_paths": [],
                "subject_kind": "OUTPUT_ARTIFACT_AND_STAGE_REPORT",
                "subject_set_sha256_or_absent_marker": "c" * 64,
                "final_candidate_frozen": True,
            },
            "validation_profile": None,
            "readiness": "NOT_READY",
            "zero_write_evidence": None,
            "verification_identity": None,
            "human_decision": None,
            "implementation_authorization": "NONE",
            "git_authorization": "NONE",
        },
    }


class IdentityTests(unittest.TestCase):
    def test_manifest_is_utf8_byte_sorted_and_byte_exact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "b.md").write_bytes(b"B\n")
            (root / "a.md").write_bytes(b"A\n")

            result = run_harness(
                "manifest",
                "--root",
                str(root),
                "--path",
                "b.md",
                "--path",
                "a.md",
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
            self.assertEqual(payload["manifest_byte_length"], len(expected))
            self.assertEqual(
                payload["subject_set_sha256"],
                hashlib.sha256(expected).hexdigest(),
            )
            self.assertEqual(payload["result"], "PASS")
            self.assertEqual(payload["reason_code"], "NONE")
            self.assertEqual(payload["repository_mutations"], 0)
            self.assertTrue(payload["stop"])

    def test_parent_component_is_a_request_contract_defect(self) -> None:
        result = run_harness(
            "manifest",
            "--root",
            str(REPO_ROOT),
            "--path",
            "../outside",
        )

        self.assertEqual(result.returncode, 3)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
        self.assertEqual(payload["reason_code"], "NONE")
        self.assertEqual(payload["finding_origin"], "REQUEST_OR_CHECKER_DEFECT")

    def test_duplicate_path_is_rejected_before_subject_evaluation(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "a.md").write_bytes(b"A")
            result = run_harness(
                "manifest",
                "--root",
                str(root),
                "--path",
                "a.md",
                "--path",
                "a.md",
            )

        self.assertEqual(result.returncode, 3)
        self.assertEqual(
            json.loads(result.stdout)["finding_origin"],
            "REQUEST_OR_CHECKER_DEFECT",
        )

    def test_non_nfc_path_is_rejected(self) -> None:
        decomposed = unicodedata.normalize("NFD", "é.md")
        self.assertNotEqual(decomposed, unicodedata.normalize("NFC", decomposed))
        result = run_harness(
            "manifest",
            "--root",
            str(REPO_ROOT),
            "--path",
            decomposed,
        )
        self.assertEqual(result.returncode, 3)

    def test_symlink_subject_is_a_subject_defect(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "target.md").write_bytes(b"target")
            (root / "link.md").symlink_to("target.md")
            result = run_harness(
                "manifest",
                "--root",
                str(root),
                "--path",
                "link.md",
            )

        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stdout, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "FAIL")
        self.assertEqual(payload["finding_origin"], "SUBJECT_DEFECT")

    def test_symlinked_parent_is_a_subject_defect(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "real").mkdir()
            (root / "real" / "a.md").write_bytes(b"A\n")
            (root / "alias").symlink_to("real", target_is_directory=True)
            result = run_harness(
                "manifest",
                "--root",
                str(root),
                "--path",
                "alias/a.md",
            )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "FAIL")
        self.assertEqual(payload["finding_origin"], "SUBJECT_DEFECT")

    def test_malformed_paths_are_request_contract_defects(self) -> None:
        malformed = ("/absolute", "a\\b", "a//b", "a/./b", "control\nbyte")
        for relative in malformed:
            with self.subTest(relative=repr(relative)):
                result = run_harness(
                    "manifest",
                    "--root",
                    str(REPO_ROOT),
                    "--path",
                    relative,
                )
                self.assertEqual(result.returncode, 3)
                payload = json.loads(result.stdout)
                self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
                self.assertEqual(payload["finding_origin"], "REQUEST_OR_CHECKER_DEFECT")


class ContractTests(unittest.TestCase):
    def assert_contract_violation(
        self, result: subprocess.CompletedProcess[str]
    ) -> Dict[str, Any]:
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertTrue(result.stdout, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
        self.assertEqual(payload["reason_code"], "NONE")
        self.assertEqual(payload["finding_origin"], "REQUEST_OR_CHECKER_DEFECT")
        self.assertEqual(payload["repository_mutations"], 0)
        self.assertTrue(payload["stop"])
        return payload

    def test_complete_request_passes_pre_dispatch_contract(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            request_path = Path(raw) / "request.json"
            write_json(request_path, valid_request())
            result = run_harness(
                "check-request",
                "--input",
                str(request_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-model",
                "gpt-5.6-luna",
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "PASS")
        self.assertEqual(payload["validated_request_id"], "TASK-001-MECH-001")

    def test_request_requires_subject_identity_and_method_contract(self) -> None:
        for missing in ("subject_sha256", "invariant_semantics", "method_contract"):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as raw:
                request = valid_request()
                del request[missing]
                request_path = Path(raw) / "request.json"
                write_json(request_path, request)
                result = run_harness(
                    "check-request",
                    "--input",
                    str(request_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                )
                self.assert_contract_violation(result)

    def test_invalid_utf8_json_is_a_contract_violation(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            request_path = Path(raw) / "request.json"
            request_path.write_bytes(b"{\"task_id\":\xff}")
            result = run_harness(
                "check-request",
                "--input",
                str(request_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-model",
                "gpt-5.6-luna",
            )
        self.assert_contract_violation(result)

    def test_invalid_cli_invocation_returns_one_canonical_json_object(self) -> None:
        result = run_harness("manifest")
        self.assertEqual(result.returncode, 3)
        self.assertEqual(result.stderr, "")
        self.assertTrue(result.stdout.endswith("\n"))
        payload = json.loads(result.stdout)
        expected = json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ) + "\n"
        self.assertEqual(result.stdout, expected)
        self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
        self.assertEqual(payload["finding_origin"], "REQUEST_OR_CHECKER_DEFECT")

    def test_help_is_returned_as_canonical_json(self) -> None:
        result = run_harness("--help")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "PASS")
        self.assertEqual(payload["reason_code"], "NONE")
        self.assertIn("manifest", payload["help"])
        self.assertTrue(payload["stop"])


class StageReportTests(unittest.TestCase):
    def create_report(
        self,
        root: Path,
        input_path: Path,
        output: str,
        profile: str = "PRE_R3_BOOTSTRAP",
        task_id: str = "TASK-001",
        execution_id: str = "EXEC-001",
    ) -> subprocess.CompletedProcess[str]:
        return run_harness(
            "create-stage-report",
            "--root",
            str(root),
            "--input",
            str(input_path),
            "--transport-profile",
            profile,
            "--task-id",
            task_id,
            "--execution-id",
            execution_id,
            "--output",
            output,
        )

    def test_create_report_writes_canonical_json_yaml_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            input_path = root / "input.json"
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )
            write_json(input_path, valid_stage_report())

            result = self.create_report(root, input_path, output)

            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            written = (root / output).read_bytes()
            self.assertEqual(written[-1:], b"\n")
            self.assertEqual(json.loads(written), valid_stage_report())
            self.assertEqual(payload["stage_report_byte_length"], len(written))
            self.assertEqual(
                payload["stage_report_sha256"],
                hashlib.sha256(written).hexdigest(),
            )
            self.assertEqual(payload["stage_report_path"], output)

    def test_input_key_order_does_not_change_canonical_bytes(self) -> None:
        report = valid_stage_report()
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            first_root = root / "first"
            second_root = root / "second"
            first_root.mkdir()
            second_root.mkdir()
            first_input = first_root / "input.json"
            second_input = second_root / "input.json"
            first_input.write_text(json.dumps(report), encoding="utf-8")
            second_input.write_text(
                json.dumps(dict(reversed(list(report.items())))),
                encoding="utf-8",
            )
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )

            first = self.create_report(first_root, first_input, output)
            second = self.create_report(second_root, second_input, output)

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(
                (first_root / output).read_bytes(),
                (second_root / output).read_bytes(),
            )

    def test_second_create_blocks_without_changing_existing_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            input_path = root / "input.json"
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )
            write_json(input_path, valid_stage_report())
            first = self.create_report(root, input_path, output)
            self.assertEqual(first.returncode, 0, first.stderr)
            before = (root / output).read_bytes()

            second = self.create_report(root, input_path, output)

            self.assertEqual(second.returncode, 5, second.stderr)
            payload = json.loads(second.stdout)
            self.assertEqual(payload["result"], "BLOCKED")
            self.assertEqual(
                payload["reason_code"],
                "BLOCKED_STAGE_REPORT_PATH_COLLISION",
            )
            self.assertEqual((root / output).read_bytes(), before)
            self.assertNotIn(hashlib.sha256(before).hexdigest(), second.stdout)

    def test_transport_profiles_are_not_interchangeable(self) -> None:
        cases = (
            (
                "PRE_R3_BOOTSTRAP",
                "planning/verification/runs/TASK-001/EXEC-001/stage-report.yaml",
            ),
            (
                "R3_ACTIVE",
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml",
            ),
        )
        for profile, output in cases:
            with self.subTest(profile=profile), tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                input_path = root / "input.json"
                write_json(input_path, valid_stage_report())
                result = self.create_report(root, input_path, output, profile=profile)
                self.assertEqual(result.returncode, 4, result.stderr)
                payload = json.loads(result.stdout)
                self.assertEqual(payload["result"], "BLOCKED")
                self.assertEqual(
                    payload["reason_code"],
                    "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
                )

    def test_active_profile_creates_only_exact_run_scoped_path(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            input_path = root / "input.json"
            output = "planning/verification/runs/TASK-001/EXEC-001/stage-report.yaml"
            report = valid_stage_report()
            report["changed_paths"][-1] = output
            write_json(input_path, report)
            result = self.create_report(
                root,
                input_path,
                output,
                profile="R3_ACTIVE",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((root / output).is_file())

    def test_symlinked_ancestor_blocks_creation(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            outside = root / "outside"
            outside.mkdir()
            (root / "planning").symlink_to(outside, target_is_directory=True)
            input_path = root / "input.json"
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )
            write_json(input_path, valid_stage_report())

            result = self.create_report(root, input_path, output)

            self.assertEqual(result.returncode, 4, result.stderr)
            self.assertFalse((outside / "verification").exists())

    def test_invalid_json_domain_and_missing_report_field_are_rejected(self) -> None:
        raw_inputs = (
            '{"task_id":"TASK-001","task_id":"DUPLICATE"}',
            '{"task_id":"TASK-001","value":1.5}',
        )
        for raw_input in raw_inputs:
            with self.subTest(raw_input=raw_input), tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                input_path = root / "input.json"
                input_path.write_text(raw_input, encoding="utf-8")
                output = (
                    "planning/verification/bootstrap/routing-r3-harness/"
                    "EXEC-001/stage-report.yaml"
                )
                result = self.create_report(root, input_path, output)
                self.assertEqual(result.returncode, 3, result.stderr)

        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            input_path = root / "input.json"
            report = valid_stage_report()
            del report["ending_identity"]
            write_json(input_path, report)
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )
            result = self.create_report(root, input_path, output)
            self.assertEqual(result.returncode, 3, result.stderr)

    def test_pass_report_requires_frozen_candidate_and_no_git_mutation(self) -> None:
        mutations = (
            ("freeze", False),
            ("git", "RUN"),
            ("reason", "BLOCKED_REQUIRED_REVIEW_CAPABILITY"),
        )
        for mutation, value in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                input_path = root / "input.json"
                report = valid_stage_report()
                if mutation == "freeze":
                    report["documentation_validation_extension"]["output"][
                        "final_candidate_frozen"
                    ] = value
                elif mutation == "git":
                    report["Git_operations"]["commit"] = value
                else:
                    report["reason_code"] = value
                write_json(input_path, report)
                output = (
                    "planning/verification/bootstrap/routing-r3-harness/"
                    "EXEC-001/stage-report.yaml"
                )
                result = self.create_report(root, input_path, output)
                self.assertEqual(result.returncode, 3, result.stderr)

    def test_report_requires_exact_auth_and_identity_types(self) -> None:
        mutations = (
            lambda report: report["Git_operations"].pop("add"),
            lambda report: report["documentation_validation_extension"][
                "authorization"
            ].update({"authorization_id": "OTHER"}),
            lambda report: report["documentation_validation_extension"]["output"].update(
                {"subject_set_sha256_or_absent_marker": "not-a-sha"}
            ),
            lambda report: report["documentation_validation_extension"]["output"].update(
                {"final_candidate_frozen": 1}
            ),
            lambda report: report.update({"changed_paths": ["docs/a.md"]}),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index), tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                input_path = root / "input.json"
                report = valid_stage_report()
                mutate(report)
                write_json(input_path, report)
                output = (
                    "planning/verification/bootstrap/routing-r3-harness/"
                    "EXEC-001/stage-report.yaml"
                )
                result = self.create_report(root, input_path, output)

                self.assertEqual(result.returncode, 3)
                payload = json.loads(result.stdout)
                self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
                self.assertEqual(payload["repository_mutations"], 0)
                self.assertFalse((root / output).exists())

    def test_verify_report_binds_path_length_hash_and_preserves_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            input_path = root / "input.json"
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )
            write_json(input_path, valid_stage_report())
            created = self.create_report(root, input_path, output)
            self.assertEqual(created.returncode, 0, created.stderr)
            identity = json.loads(created.stdout)
            before = (root / output).read_bytes()

            verified = run_harness(
                "verify-stage-report",
                "--root",
                str(root),
                "--transport-profile",
                "PRE_R3_BOOTSTRAP",
                "--task-id",
                "TASK-001",
                "--execution-id",
                "EXEC-001",
                "--path",
                output,
                "--expected-byte-length",
                str(identity["stage_report_byte_length"]),
                "--expected-sha256",
                identity["stage_report_sha256"],
            )

            self.assertEqual(verified.returncode, 0, verified.stderr)
            payload = json.loads(verified.stdout)
            self.assertEqual(payload["result"], "PASS")
            self.assertEqual(payload["repository_mutations"], 0)
            self.assertEqual((root / output).read_bytes(), before)

    def test_verify_mismatch_blocks_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            input_path = root / "input.json"
            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-001/stage-report.yaml"
            )
            write_json(input_path, valid_stage_report())
            created = self.create_report(root, input_path, output)
            self.assertEqual(created.returncode, 0, created.stderr)
            before = (root / output).read_bytes()

            verified = run_harness(
                "verify-stage-report",
                "--root",
                str(root),
                "--transport-profile",
                "PRE_R3_BOOTSTRAP",
                "--task-id",
                "TASK-001",
                "--execution-id",
                "EXEC-001",
                "--path",
                output,
                "--expected-byte-length",
                str(len(before)),
                "--expected-sha256",
                "0" * 64,
            )

            self.assertEqual(verified.returncode, 4, verified.stderr)
            payload = json.loads(verified.stdout)
            self.assertEqual(payload["result"], "BLOCKED")
            self.assertEqual(
                payload["reason_code"],
                "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
            )
            self.assertEqual((root / output).read_bytes(), before)


class ContractResultAndGateTests(unittest.TestCase):
    def assert_contract_violation(
        self, result: subprocess.CompletedProcess[str]
    ) -> Dict[str, Any]:
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertTrue(result.stdout, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
        self.assertEqual(payload["reason_code"], "NONE")
        self.assertEqual(payload["finding_origin"], "REQUEST_OR_CHECKER_DEFECT")
        self.assertEqual(payload["repository_mutations"], 0)
        self.assertTrue(payload["stop"])
        return payload

    def test_request_rejects_forbidden_operation_and_retry_drift(self) -> None:
        mutations = (
            ("allowed_operations", ["READ", "WRITE"]),
            ("forbidden_operations", ["WRITE"]),
            ("retry_limit", 1),
        )
        for field, value in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as raw:
                request = valid_request()
                request[field] = value
                request_path = Path(raw) / "request.json"
                write_json(request_path, request)
                result = run_harness(
                    "check-request",
                    "--input",
                    str(request_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                )
                self.assert_contract_violation(result)


class IntegrationTests(unittest.TestCase):
    def manifest(self, root: Path) -> Dict[str, Any]:
        result = run_harness(
            "manifest",
            "--root",
            str(root),
            "--path",
            "subject/a.md",
            "--path",
            "subject/b.md",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_positive_pipeline_has_one_exact_write(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "subject").mkdir()
            (root / "subject" / "a.md").write_bytes(b"A\n")
            (root / "subject" / "b.md").write_bytes(b"B\n")
            manifest = self.manifest(root)
            subject_sha256 = manifest["subject_set_sha256"]

            request = valid_request()
            request.update(
                {
                    "task_id": "TASK-PIPE",
                    "request_id": "TASK-PIPE-MECH-001",
                    "parent_task_id": "TASK-PIPE",
                    "exact_subject": ["subject/a.md", "subject/b.md"],
                    "subject_sha256": subject_sha256,
                    "source_boundary": ["subject/a.md", "subject/b.md"],
                }
            )
            evidence = valid_result()
            for field in (
                "task_id",
                "request_id",
                "parent_task_id",
                "task_class",
                "role",
                "exact_subject",
                "subject_sha256",
                "source_boundary",
            ):
                evidence[field] = request[field]
            gate = valid_gate()
            gate.update(
                {
                    "gate_id": "TASK-PIPE-GATE-MECH",
                    "request_id": request["request_id"],
                    "subject_sha256": subject_sha256,
                    "source_boundary": request["source_boundary"],
                }
            )

            request_path = root / "request.json"
            result_path = root / "result.json"
            gate_path = root / "gate.json"
            report_input = root / "stage-report-input.json"
            write_json(request_path, request)
            write_json(result_path, evidence)
            write_json(gate_path, gate)

            output = (
                "planning/verification/bootstrap/routing-r3-harness/"
                "EXEC-PIPE/stage-report.yaml"
            )
            report = valid_stage_report()
            report.update(
                {
                    "task_id": "TASK-PIPE",
                    "ending_identity": {"subject_sha256": subject_sha256},
                    "changed_paths": ["subject/a.md", "subject/b.md", output],
                }
            )
            extension = report["documentation_validation_extension"]
            extension["interval_instance_id"] = "TASK-PIPE.EXEC-PIPE"
            extension["authorization"]["authorization_id"] = "EXEC-PIPE"
            extension["output"].update(
                {
                    "expected_paths": ["subject/a.md", "subject/b.md"],
                    "present_paths": ["subject/a.md", "subject/b.md"],
                    "subject_set_sha256_or_absent_marker": subject_sha256,
                }
            )
            write_json(report_input, report)
            (root / output).parent.mkdir(parents=True)

            before = {
                path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file()
            }

            commands = (
                run_harness(
                    "check-request",
                    "--input",
                    str(request_path),
                    "--expected-subject-sha256",
                    subject_sha256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                ),
                run_harness(
                    "check-result",
                    "--input",
                    str(result_path),
                    "--request",
                    str(request_path),
                    "--expected-subject-sha256",
                    subject_sha256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                ),
                run_harness(
                    "check-gate",
                    "--input",
                    str(gate_path),
                    "--expected-subject-sha256",
                    subject_sha256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-request-id",
                    request["request_id"],
                ),
            )
            for command in commands:
                self.assertEqual(command.returncode, 0, command.stderr)
                self.assertEqual(json.loads(command.stdout)["repository_mutations"], 0)

            created = run_harness(
                "create-stage-report",
                "--root",
                str(root),
                "--input",
                str(report_input),
                "--transport-profile",
                "PRE_R3_BOOTSTRAP",
                "--task-id",
                "TASK-PIPE",
                "--execution-id",
                "EXEC-PIPE",
                "--output",
                output,
            )
            self.assertEqual(created.returncode, 0, created.stderr)
            created_payload = json.loads(created.stdout)
            verified = run_harness(
                "verify-stage-report",
                "--root",
                str(root),
                "--transport-profile",
                "PRE_R3_BOOTSTRAP",
                "--task-id",
                "TASK-PIPE",
                "--execution-id",
                "EXEC-PIPE",
                "--path",
                output,
                "--expected-byte-length",
                str(created_payload["stage_report_byte_length"]),
                "--expected-sha256",
                created_payload["stage_report_sha256"],
            )
            self.assertEqual(verified.returncode, 0, verified.stderr)
            self.assertEqual(json.loads(verified.stdout)["repository_mutations"], 0)

            after = {
                path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file()
            }
            self.assertEqual(set(after).difference(before), {output})
            for relative, data in before.items():
                self.assertEqual(after[relative], data)

    def test_candidate_drift_rejects_stale_gate_and_never_claims_freeze(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "subject").mkdir()
            (root / "subject" / "a.md").write_bytes(b"A\n")
            (root / "subject" / "b.md").write_bytes(b"B\n")
            first = self.manifest(root)["subject_set_sha256"]
            gate = valid_gate()
            gate["subject_sha256"] = first
            gate_path = root / "gate.json"
            write_json(gate_path, gate)
            passing = run_harness(
                "check-gate",
                "--input",
                str(gate_path),
                "--expected-subject-sha256",
                first,
                "--expected-role",
                "mechanical_checker",
                "--expected-request-id",
                gate["request_id"],
            )
            self.assertEqual(passing.returncode, 0, passing.stderr)

            (root / "subject" / "a.md").write_bytes(b"changed\n")
            second = self.manifest(root)["subject_set_sha256"]
            self.assertNotEqual(first, second)
            stale = run_harness(
                "check-gate",
                "--input",
                str(gate_path),
                "--expected-subject-sha256",
                second,
                "--expected-role",
                "mechanical_checker",
                "--expected-request-id",
                gate["request_id"],
            )
            self.assertEqual(stale.returncode, 3)
            stale_payload = json.loads(stale.stdout)
            self.assertEqual(stale_payload["result"], "CONTRACT_VIOLATION")
            self.assertNotIn("final_candidate_frozen", stale_payload)

    def test_repeated_checker_defect_reaches_the_documented_loop_breaker(self) -> None:
        config = (REPO_ROOT / ".codex" / "config.toml").read_text(encoding="utf-8")
        self.assertIn("at most one validator-harness correction", config)
        self.assertIn("DEFER_OR_REDESIGN_VALIDATOR", config)
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            subject = root / "subject.md"
            subject.write_bytes(b"candidate\n")
            candidate_before = hashlib.sha256(subject.read_bytes()).hexdigest()
            payloads = []
            for request_id in ("TASK-001-MECH-001", "TASK-001-MECH-002"):
                request = valid_request()
                request["request_id"] = request_id
                del request["method_contract"]
                request_path = root / f"{request_id}.json"
                write_json(request_path, request)
                checked = run_harness(
                    "check-request",
                    "--input",
                    str(request_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                )
                self.assertEqual(checked.returncode, 3)
                payloads.append(json.loads(checked.stdout))

            self.assertTrue(
                all(
                    payload["result"] == "CONTRACT_VIOLATION"
                    and payload["reason_code"] == "NONE"
                    and payload["finding_origin"] == "REQUEST_OR_CHECKER_DEFECT"
                    and payload["repository_mutations"] == 0
                    for payload in payloads
                )
            )
            aggregate = {
                "result": "FAIL",
                "reason_code": "NONE",
                "next_required_action": "DEFER_OR_REDESIGN_VALIDATOR",
            }
            self.assertEqual(list(aggregate), ["result", "reason_code", "next_required_action"])
            self.assertEqual(
                hashlib.sha256(subject.read_bytes()).hexdigest(),
                candidate_before,
            )


class ContractResultAndGateContinuationTests(unittest.TestCase):
    def assert_contract_violation(
        self, result: subprocess.CompletedProcess[str]
    ) -> Dict[str, Any]:
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertTrue(result.stdout, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "CONTRACT_VIOLATION")
        self.assertEqual(payload["reason_code"], "NONE")
        self.assertEqual(payload["finding_origin"], "REQUEST_OR_CHECKER_DEFECT")
        self.assertEqual(payload["repository_mutations"], 0)
        self.assertTrue(payload["stop"])
        return payload

    def test_complete_result_passes_post_dispatch_contract(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            request_path = root / "request.json"
            result_path = root / "result.json"
            write_json(request_path, valid_request())
            write_json(result_path, valid_result())
            result = run_harness(
                "check-result",
                "--input",
                str(result_path),
                "--request",
                str(request_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-model",
                "gpt-5.6-luna",
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"], "PASS")
        self.assertEqual(payload["validated_reviewer_result"], "PASS")

    def test_result_requires_scalar_temporal_scope(self) -> None:
        invalid_values = (None, "", [], {}, "2026-08-03T00:00:00Z/")
        for value in invalid_values:
            with self.subTest(value=value), tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                request_path = root / "request.json"
                result_path = root / "result.json"
                evidence = valid_result()
                evidence["temporal_scope"] = value
                write_json(request_path, valid_request())
                write_json(result_path, evidence)
                result = run_harness(
                    "check-result",
                    "--input",
                    str(result_path),
                    "--request",
                    str(request_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                )
                self.assert_contract_violation(result)

    def test_result_accepts_exact_bounded_temporal_interval(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            request_path = root / "request.json"
            result_path = root / "result.json"
            evidence = valid_result()
            evidence["temporal_scope"] = (
                "2026-08-03T10:00:00Z/2026-08-03T10:05:00Z"
            )
            write_json(request_path, valid_request())
            write_json(result_path, evidence)
            result = run_harness(
                "check-result",
                "--input",
                str(result_path),
                "--request",
                str(request_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-model",
                "gpt-5.6-luna",
            )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_result_reason_algebra_is_closed(self) -> None:
        invalid_pairs = (
            ("BLOCKED", "NONE"),
            ("PASS", "BLOCKED_REQUIRED_REVIEW_CAPABILITY"),
            ("CONFLICT", "NONE"),
            ("UNKNOWN_RESULT", "NONE"),
        )
        for technical_result, reason_code in invalid_pairs:
            with (
                self.subTest(result=technical_result, reason_code=reason_code),
                tempfile.TemporaryDirectory() as raw,
            ):
                root = Path(raw)
                request_path = root / "request.json"
                result_path = root / "result.json"
                evidence = valid_result()
                evidence["result"] = technical_result
                evidence["reason_code"] = reason_code
                write_json(request_path, valid_request())
                write_json(result_path, evidence)
                result = run_harness(
                    "check-result",
                    "--input",
                    str(result_path),
                    "--request",
                    str(request_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                )
                self.assert_contract_violation(result)

    def test_result_rejects_stale_subject_model_and_mutation_claims(self) -> None:
        mutations = (
            ("subject_sha256", "b" * 64),
            ("model", "gpt-5.6-sol"),
            ("repository_mutations", 1),
            ("next_required_action", ["ONE", "TWO"]),
            ("stop", False),
        )
        for field, value in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as raw:
                root = Path(raw)
                request_path = root / "request.json"
                result_path = root / "result.json"
                evidence = valid_result()
                evidence[field] = value
                write_json(request_path, valid_request())
                write_json(result_path, evidence)
                result = run_harness(
                    "check-result",
                    "--input",
                    str(result_path),
                    "--request",
                    str(request_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-model",
                    "gpt-5.6-luna",
                )
                self.assert_contract_violation(result)

    def test_result_rejects_git_mutation_and_unknown_claim_class(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            request_path = root / "request.json"
            result_path = root / "result.json"
            evidence = valid_result()
            evidence["git_operations"]["commit"] = "RUN"
            write_json(request_path, valid_request())
            write_json(result_path, evidence)
            result = run_harness(
                "check-result",
                "--input",
                str(result_path),
                "--request",
                str(request_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-model",
                "gpt-5.6-luna",
            )
            self.assert_contract_violation(result)

            evidence = valid_result()
            evidence["classified_claims"][0]["claim_class"] = "ASSERTED"
            write_json(result_path, evidence)
            result = run_harness(
                "check-result",
                "--input",
                str(result_path),
                "--request",
                str(request_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-model",
                "gpt-5.6-luna",
            )
            self.assert_contract_violation(result)

    def test_complete_normalized_gate_passes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            gate_path = Path(raw) / "gate.json"
            write_json(gate_path, valid_gate())
            result = run_harness(
                "check-gate",
                "--input",
                str(gate_path),
                "--expected-subject-sha256",
                SUBJECT_SHA256,
                "--expected-role",
                "mechanical_checker",
                "--expected-request-id",
                "TASK-001-MECH-001",
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["validated_gate_id"], "TASK-001-GATE-MECH")

    def test_gate_rejects_stale_or_nonrequired_evidence(self) -> None:
        mutations = (
            ("subject_sha256", "b" * 64),
            ("required", False),
            ("repository_mutations", 1),
        )
        for field, value in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as raw:
                gate = valid_gate()
                gate[field] = value
                gate_path = Path(raw) / "gate.json"
                write_json(gate_path, gate)
                result = run_harness(
                    "check-gate",
                    "--input",
                    str(gate_path),
                    "--expected-subject-sha256",
                    SUBJECT_SHA256,
                    "--expected-role",
                    "mechanical_checker",
                    "--expected-request-id",
                    "TASK-001-MECH-001",
                )
                self.assert_contract_violation(result)


if __name__ == "__main__":
    unittest.main()
