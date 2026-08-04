#!/usr/bin/env python3
"""Deterministic mechanical harness for the AOS routing R3 draft package.

The harness validates byte identity and routing contracts.  It does not make
semantic judgments, dispatch reviewers, aggregate readiness, grant authority,
or perform Git operations.  Only the explicitly named ``create-stage-report``
command may write, and that command uses exclusive creation.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


CONTROL = re.compile(r"[\x00-\x1f\x7f]")
HEX_64 = re.compile(r"[0-9a-f]{64}")
ISO_INSTANT = (
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
    r"(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
)
TEMPORAL_INTERVAL = re.compile(rf"({ISO_INSTANT})/({ISO_INSTANT})")

TECHNICAL_RESULTS = {
    "PASS",
    "FAIL",
    "BLOCKED",
    "CONFLICT",
    "UNKNOWN",
    "NOT_RUN",
    "CONTRACT_VIOLATION",
}
REASON_CODES = {
    "NONE",
    "REVIEWER_EVIDENCE_CONFLICT",
    "BLOCKED_REQUIRED_REVIEW_CAPABILITY",
    "BLOCKED_STAGE_REPORT_PATH_COLLISION",
    "BLOCKED_HUMAN_DECISION_REQUIRED",
    "BLOCKED_UNRESOLVED_CONFLICT",
    "BLOCKED_REFERENCE_ACCESS",
    "BLOCKED_SUBJECT_IDENTITY_MISMATCH",
    "BLOCKED_SCOPE_OR_PROVENANCE",
    "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
    "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
}
CLAIM_CLASSES = {
    "OBSERVED_AT_SNAPSHOT",
    "REPORTED",
    "SYNTHESIZED",
    "CONFLICT",
    "NOT_FOUND",
    "UNKNOWN",
    "NOT_RUN",
    "BLOCKED",
}
ROLE_BINDINGS = {
    "mechanical_checker": ("gpt-5.6-luna", "medium"),
    "contract_analyst": ("gpt-5.6-terra", "high"),
    "semantic_reviewer": ("gpt-5.6-sol", "high"),
    "reference_explorer": ("gpt-5.6-terra", "medium"),
}
FORBIDDEN_OPERATIONS = {
    "WRITE",
    "COMMIT",
    "PUSH",
    "MERGE",
    "RELEASE",
    "NESTED_DELEGATION",
}
GIT_MUTATION_OPERATIONS = {"add", "commit", "push", "merge", "release"}

REQUEST_FIELDS = {
    "task_id",
    "request_id",
    "parent_task_id",
    "task_class",
    "role",
    "exact_subject",
    "subject_sha256",
    "source_boundary",
    "required_output_fields",
    "stop_conditions",
    "allowed_operations",
    "forbidden_operations",
    "retry_limit",
}
RESULT_FIELDS = {
    "task_id",
    "request_id",
    "parent_task_id",
    "task_class",
    "role",
    "model",
    "reasoning",
    "exact_subject",
    "subject_sha256",
    "source_boundary",
    "sources",
    "methods",
    "temporal_scope",
    "classified_claims",
    "conflicts",
    "unknowns",
    "recommendations",
    "checks_run",
    "checks_not_run",
    "limitations",
    "model_binding",
    "repository_mutations",
    "git_operations",
    "result",
    "reason_code",
    "next_required_action",
    "stop",
}
GATE_FIELDS = {
    "gate_id",
    "required",
    "role",
    "request_id",
    "subject_sha256",
    "source_boundary",
    "result",
    "reason_code",
    "finding_ids",
    "limitations",
    "repository_mutations",
    "stop",
}
STAGE_REPORT_FIELDS = {
    "task_id",
    "stage",
    "result",
    "reason_code",
    "starting_identity",
    "ending_identity",
    "changed_paths",
    "checks_run",
    "checks_not_run",
    "findings",
    "limitations",
    "unknowns",
    "out_of_scope_state",
    "authorization_consumed",
    "Git_operations",
    "next_required_action",
    "stop",
    "lifecycle_status",
    "documentation_validation_extension",
}
STAGE_EXTENSION_FIELDS = {
    "report_kind",
    "interval_instance_id",
    "authorization",
    "output",
    "validation_profile",
    "readiness",
    "zero_write_evidence",
    "verification_identity",
    "human_decision",
    "implementation_authorization",
    "git_authorization",
}
STAGE_OUTPUT_FIELDS = {
    "expected_paths",
    "present_paths",
    "absent_paths",
    "partial_paths",
    "subject_kind",
    "subject_set_sha256_or_absent_marker",
    "final_candidate_frozen",
}
SUBJECT_KINDS = {
    "OUTPUT_ARTIFACT_AND_STAGE_REPORT",
    "PARTIAL_ARTIFACT_AND_STAGE_REPORT",
    "STAGE_REPORT_ONLY",
}


class HarnessError(Exception):
    """A deterministic terminal harness result."""

    def __init__(
        self,
        exit_code: int,
        result: str,
        reason_code: str,
        message: str,
        finding_origin: Optional[str] = None,
        repository_mutations: int = 0,
    ) -> None:
        super().__init__(message)
        self.exit_code = exit_code
        self.result = result
        self.reason_code = reason_code
        self.message = message
        self.finding_origin = finding_origin
        self.repository_mutations = repository_mutations


class HarnessHelp(Exception):
    """Return argparse help through the canonical stdout envelope."""

    def __init__(self, help_text: str) -> None:
        super().__init__(help_text)
        self.help_text = help_text


class CanonicalArgumentParser(argparse.ArgumentParser):
    """Route CLI contract defects through the canonical result envelope."""

    def error(self, message: str) -> None:
        raise contract_error(f"invalid CLI invocation: {message}")

    def print_help(self, file: Any = None) -> None:
        del file
        raise HarnessHelp(self.format_help())


def canonical_json_bytes(value: Dict[str, Any]) -> bytes:
    """Return stable UTF-8 JSON bytes with one terminal LF."""

    validate_closed_json_domain(value)
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")


def validate_closed_json_domain(value: Any) -> None:
    if value is None or isinstance(value, bool) or isinstance(value, int):
        return
    if isinstance(value, float):
        raise contract_error("floating-point JSON values are forbidden")
    if isinstance(value, str):
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as error:
            raise contract_error("JSON string contains a lone surrogate") from error
        return
    if isinstance(value, list):
        for item in value:
            validate_closed_json_domain(item)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise contract_error("JSON object keys must be strings")
            validate_closed_json_domain(key)
            validate_closed_json_domain(item)
        return
    raise contract_error(f"unsupported JSON value type: {type(value).__name__}")


def reject_duplicate_keys(pairs: Sequence[Sequence[Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise contract_error(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value: str) -> Any:
    raise contract_error(f"non-finite JSON number is forbidden: {value}")


def load_json_object(path_value: str) -> Dict[str, Any]:
    path = Path(path_value)
    if path.is_symlink() or not path.is_file():
        raise contract_error("JSON input must be a regular non-symlink file")
    try:
        data = path.read_bytes()
    except OSError as error:
        raise contract_error(f"unable to read JSON input: {error}") from error
    return parse_json_object_bytes(data)


def parse_json_object_bytes(data: bytes) -> Dict[str, Any]:
    try:
        text = data.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=reject_duplicate_keys,
            parse_constant=reject_nonfinite,
        )
    except HarnessError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise contract_error(f"invalid UTF-8 JSON input: {error}") from error
    if not isinstance(value, dict):
        raise contract_error("JSON input must contain one object")
    validate_closed_json_domain(value)
    return value


def emit(payload: Dict[str, Any]) -> None:
    sys.stdout.buffer.write(canonical_json_bytes(payload))


def contract_error(message: str) -> HarnessError:
    return HarnessError(
        3,
        "CONTRACT_VIOLATION",
        "NONE",
        message,
        "REQUEST_OR_CHECKER_DEFECT",
    )


def subject_error(message: str) -> HarnessError:
    return HarnessError(2, "FAIL", "NONE", message, "SUBJECT_DEFECT")


def execution_error(message: str, repository_mutations: int = 0) -> HarnessError:
    return HarnessError(
        2,
        "FAIL",
        "NONE",
        message,
        repository_mutations=repository_mutations,
    )


def blocked_error(reason_code: str, message: str, exit_code: int = 4) -> HarnessError:
    if reason_code not in REASON_CODES or not reason_code.startswith("BLOCKED_"):
        raise AssertionError(f"invalid internal blocker reason: {reason_code}")
    return HarnessError(exit_code, "BLOCKED", reason_code, message)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def normalize_relative_path(value: str) -> str:
    if (
        not value
        or value.startswith("/")
        or "\\" in value
        or CONTROL.search(value) is not None
    ):
        raise contract_error("path must be a normalized repository-relative POSIX path")
    if unicodedata.normalize("NFC", value) != value:
        raise contract_error("path must use NFC normalization")
    parts = value.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise contract_error("path contains an empty or ambiguous component")
    return value


def normalize_path_component(value: str, field: str) -> str:
    normalized = normalize_relative_path(value)
    if "/" in normalized:
        raise contract_error(f"{field} must be one path component")
    return normalized


def require_fields(value: Dict[str, Any], fields: set, label: str) -> None:
    missing = sorted(fields.difference(value))
    if missing:
        raise contract_error(f"{label} missing required fields: {','.join(missing)}")


def require_nonempty_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise contract_error(f"{field} must be one non-empty exact string")
    return value


def require_sha256(value: Any, field: str) -> str:
    text = require_nonempty_string(value, field)
    if HEX_64.fullmatch(text) is None:
        raise contract_error(f"{field} must be lowercase 64-hex SHA-256")
    return text


def require_string_list(value: Any, field: str, allow_empty: bool = True) -> List[str]:
    if not isinstance(value, list) or (not allow_empty and not value):
        raise contract_error(f"{field} must be a list of strings")
    if any(not isinstance(item, str) or not item for item in value):
        raise contract_error(f"{field} must contain non-empty strings only")
    if len(set(value)) != len(value):
        raise contract_error(f"{field} must not contain duplicates")
    return value


def validate_role_binding(role: Any, expected_role: str, expected_model: str) -> None:
    if role != expected_role or role not in ROLE_BINDINGS:
        raise contract_error("role does not match the bound configured role")
    configured_model, _ = ROLE_BINDINGS[role]
    if expected_model != configured_model:
        raise contract_error("expected model does not match the static role binding")


def validate_result_reason(result: Any, reason_code: Any) -> None:
    if result not in TECHNICAL_RESULTS or reason_code not in REASON_CODES:
        raise contract_error("unknown technical result or reason_code")
    if result == "CONFLICT" and reason_code != "REVIEWER_EVIDENCE_CONFLICT":
        raise contract_error("CONFLICT requires REVIEWER_EVIDENCE_CONFLICT")
    if result == "BLOCKED" and not str(reason_code).startswith("BLOCKED_"):
        raise contract_error("BLOCKED requires a closed blocker reason")
    if result not in {"CONFLICT", "BLOCKED"} and reason_code != "NONE":
        raise contract_error("non-CONFLICT/non-BLOCKED result requires NONE")


def parse_iso_instant(value: str) -> dt.datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError as error:
        raise contract_error("temporal_scope contains an invalid ISO-8601 instant") from error
    if parsed.tzinfo is None:
        raise contract_error("temporal_scope instants require timezone offsets")
    return parsed


def validate_temporal_scope(value: Any) -> None:
    if not isinstance(value, str) or not value or value.strip() != value:
        raise contract_error("temporal_scope must be one non-empty scalar")
    if value == "CURRENT_SNAPSHOT":
        return
    match = TEMPORAL_INTERVAL.fullmatch(value)
    if match is None:
        raise contract_error("temporal_scope must be CURRENT_SNAPSHOT or an exact interval")
    start = parse_iso_instant(match.group(1))
    end = parse_iso_instant(match.group(2))
    if start > end:
        raise contract_error("temporal_scope interval start exceeds end")


def validate_claim_classes(value: Any) -> None:
    if isinstance(value, list):
        for item in value:
            validate_claim_classes(item)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "claim_class" and item not in CLAIM_CLASSES:
                raise contract_error(f"unknown claim class: {item}")
            validate_claim_classes(item)


def validate_request(
    request: Dict[str, Any],
    expected_subject_sha256: str,
    expected_role: str,
    expected_model: str,
) -> None:
    require_fields(request, REQUEST_FIELDS, "request")
    for field in ("task_id", "request_id", "parent_task_id", "task_class"):
        require_nonempty_string(request[field], field)
    require_sha256(expected_subject_sha256, "expected_subject_sha256")
    require_sha256(request["subject_sha256"], "subject_sha256")
    if request["subject_sha256"] != expected_subject_sha256:
        raise contract_error("request subject_sha256 is stale or mismatched")
    validate_role_binding(request["role"], expected_role, expected_model)
    if request["exact_subject"] in (None, "", [], {}):
        raise contract_error("exact_subject must be non-empty")
    if request["source_boundary"] in (None, "", [], {}):
        raise contract_error("source_boundary must be non-empty")
    require_string_list(request["required_output_fields"], "required_output_fields", False)
    require_string_list(request["stop_conditions"], "stop_conditions", False)
    if request["allowed_operations"] != ["READ"]:
        raise contract_error("allowed_operations must equal [READ]")
    forbidden = require_string_list(
        request["forbidden_operations"], "forbidden_operations", False
    )
    if set(forbidden) != FORBIDDEN_OPERATIONS:
        raise contract_error("forbidden_operations must equal the closed mutation set")
    if isinstance(request["retry_limit"], bool) or request["retry_limit"] != 0:
        raise contract_error("retry_limit must equal integer zero")

    if request["role"] == "mechanical_checker":
        require_fields(
            request,
            {"invariant_semantics", "method_contract"},
            "deterministic request",
        )
        if not isinstance(request["invariant_semantics"], dict) or not request[
            "invariant_semantics"
        ]:
            raise contract_error("invariant_semantics must be a non-empty mapping")
        method = request["method_contract"]
        if not isinstance(method, dict):
            raise contract_error("method_contract must be a mapping")
        method_fields = {
            "preflight_observed_capability",
            "exact_algorithm_or_command",
            "expected_success_shape",
            "forbidden_substitutions",
        }
        require_fields(method, method_fields, "method_contract")
        for field in (
            "preflight_observed_capability",
            "exact_algorithm_or_command",
            "expected_success_shape",
        ):
            require_nonempty_string(method[field], f"method_contract.{field}")
        require_string_list(
            method["forbidden_substitutions"],
            "method_contract.forbidden_substitutions",
            False,
        )


def validate_result(
    result: Dict[str, Any],
    request: Dict[str, Any],
    expected_subject_sha256: str,
    expected_role: str,
    expected_model: str,
) -> None:
    validate_request(request, expected_subject_sha256, expected_role, expected_model)
    require_fields(result, RESULT_FIELDS, "reviewer result")
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
        if result[field] != request[field]:
            raise contract_error(f"reviewer result {field} does not match request")
    validate_role_binding(result["role"], expected_role, expected_model)
    configured_model, configured_reasoning = ROLE_BINDINGS[expected_role]
    if result["model"] != configured_model or result["reasoning"] != configured_reasoning:
        raise contract_error("reviewer model or reasoning does not match static binding")
    binding = result["model_binding"]
    if not isinstance(binding, dict):
        raise contract_error("model_binding must be a mapping")
    if binding.get("configured_model") != configured_model:
        raise contract_error("model_binding configured_model is mismatched")
    if binding.get("binding_class") != "STATIC_CONFIGURATION_BINDING":
        raise contract_error(
            "model_binding must report STATIC_CONFIGURATION_BINDING"
        )
    if expected_role == "mechanical_checker":
        if binding.get("preferred_model") != "gpt-5.3-codex-spark":
            raise contract_error("mechanical model_binding preferred_model is mismatched")
        require_nonempty_string(binding.get("reason"), "model_binding.reason")
    validate_temporal_scope(result["temporal_scope"])
    for field in (
        "sources",
        "methods",
        "classified_claims",
        "conflicts",
        "unknowns",
        "recommendations",
        "checks_run",
        "checks_not_run",
        "limitations",
    ):
        if not isinstance(result[field], list):
            raise contract_error(f"{field} must be a list")
    validate_claim_classes(result["sources"])
    validate_claim_classes(result["classified_claims"])
    if isinstance(result["repository_mutations"], bool) or result[
        "repository_mutations"
    ] != 0:
        raise contract_error("repository_mutations must equal integer zero")
    git_operations = result["git_operations"]
    if not isinstance(git_operations, dict) or set(git_operations) != GIT_MUTATION_OPERATIONS:
        raise contract_error("git_operations must contain the complete closed mutation set")
    if any(value != "NOT_RUN" for value in git_operations.values()):
        raise contract_error("every Git mutation must equal NOT_RUN")
    validate_result_reason(result["result"], result["reason_code"])
    require_nonempty_string(result["next_required_action"], "next_required_action")
    if result["stop"] is not True:
        raise contract_error("reviewer result stop must be true")


def validate_gate(
    gate: Dict[str, Any],
    expected_subject_sha256: str,
    expected_role: str,
    expected_request_id: str,
) -> None:
    require_fields(gate, GATE_FIELDS, "gate")
    require_nonempty_string(gate["gate_id"], "gate_id")
    require_sha256(expected_subject_sha256, "expected_subject_sha256")
    if gate["required"] is not True:
        raise contract_error("normalized gate required must be true")
    if gate["role"] != expected_role or expected_role not in ROLE_BINDINGS:
        raise contract_error("gate role does not match expected configured role")
    if gate["request_id"] != expected_request_id:
        raise contract_error("gate request_id does not match expected request")
    if gate["subject_sha256"] != expected_subject_sha256:
        raise contract_error("gate subject_sha256 is stale or mismatched")
    if gate["source_boundary"] in (None, "", [], {}):
        raise contract_error("gate source_boundary must be non-empty")
    if not isinstance(gate["finding_ids"], list) or not isinstance(
        gate["limitations"], list
    ):
        raise contract_error("gate finding_ids and limitations must be lists")
    if isinstance(gate["repository_mutations"], bool) or gate[
        "repository_mutations"
    ] != 0:
        raise contract_error("gate repository_mutations must equal integer zero")
    validate_result_reason(gate["result"], gate["reason_code"])
    if gate["stop"] is not True:
        raise contract_error("gate stop must be true")


def validate_stage_report(
    report: Dict[str, Any], expected_task_id: str, expected_execution_id: str
) -> None:
    require_fields(report, STAGE_REPORT_FIELDS, "Stage Report")
    if report["task_id"] != expected_task_id:
        raise contract_error("Stage Report task_id does not match the exact task")
    if report["stage"] != "EXECUTE":
        raise contract_error("Stage Report stage must equal EXECUTE")
    validate_result_reason(report["result"], report["reason_code"])
    if not isinstance(report["starting_identity"], dict) or not isinstance(
        report["ending_identity"], dict
    ):
        raise contract_error("Stage Report identities must be mappings")
    for field in (
        "changed_paths",
        "checks_run",
        "checks_not_run",
        "findings",
        "limitations",
        "unknowns",
        "out_of_scope_state",
    ):
        if not isinstance(report[field], list):
            raise contract_error(f"Stage Report {field} must be a list")
    changed_paths = require_string_list(report["changed_paths"], "changed_paths")
    for path in changed_paths:
        normalize_relative_path(path)
    if report["authorization_consumed"] is not True:
        raise contract_error("Stage Report authorization_consumed must be true")
    git_operations = report["Git_operations"]
    if not isinstance(git_operations, dict) or set(git_operations) != GIT_MUTATION_OPERATIONS:
        raise contract_error("Stage Report Git_operations is incomplete")
    if any(value != "NOT_RUN" for value in git_operations.values()):
        raise contract_error("Stage Report Git mutations must all equal NOT_RUN")
    require_nonempty_string(report["next_required_action"], "next_required_action")
    if report["stop"] is not True:
        raise contract_error("Stage Report stop must be true")
    if report["lifecycle_status"] != "DRAFT_CANDIDATE":
        raise contract_error("Stage Report lifecycle_status must remain DRAFT_CANDIDATE")

    extension = report["documentation_validation_extension"]
    if not isinstance(extension, dict):
        raise contract_error("documentation_validation_extension must be a mapping")
    require_fields(extension, STAGE_EXTENSION_FIELDS, "documentation validation extension")
    if extension["report_kind"] != "DOCUMENTATION_STAGE_REPORT":
        raise contract_error("extension report_kind is invalid")
    interval_instance_id = require_nonempty_string(
        extension["interval_instance_id"], "interval_instance_id"
    )
    if interval_instance_id != f"{expected_task_id}.{expected_execution_id}":
        raise contract_error("interval_instance_id does not match task and execution")
    authorization = extension["authorization"]
    if not isinstance(authorization, dict):
        raise contract_error("extension authorization must be a mapping")
    require_fields(
        authorization,
        {"authorization_id", "authorization_state"},
        "extension authorization",
    )
    authorization_id = require_nonempty_string(
        authorization["authorization_id"], "authorization_id"
    )
    if authorization_id != expected_execution_id:
        raise contract_error("authorization_id does not match exact execution")
    if authorization["authorization_state"] != "CONSUMED_ONE_SHOT":
        raise contract_error("authorization_state must equal CONSUMED_ONE_SHOT")
    output = extension["output"]
    if not isinstance(output, dict):
        raise contract_error("extension output must be a mapping")
    require_fields(output, STAGE_OUTPUT_FIELDS, "extension output")
    for field in ("expected_paths", "present_paths", "absent_paths", "partial_paths"):
        paths = require_string_list(output[field], f"output.{field}")
        for path in paths:
            normalize_relative_path(path)
    if output["subject_kind"] not in SUBJECT_KINDS:
        raise contract_error("extension output subject_kind is invalid")
    subject_identity = require_nonempty_string(
        output["subject_set_sha256_or_absent_marker"],
        "subject_set_sha256_or_absent_marker",
    )
    if subject_identity != "ABSENT":
        require_sha256(subject_identity, "subject_set_sha256_or_absent_marker")
    if not isinstance(output["final_candidate_frozen"], bool):
        raise contract_error("final_candidate_frozen must be boolean")
    if extension["readiness"] != "NOT_READY":
        raise contract_error("pre-validation readiness must equal NOT_READY")
    if extension["validation_profile"] is not None:
        raise contract_error("validation_profile must remain null in EXECUTE")
    if extension["verification_identity"] is not None:
        raise contract_error("verification_identity must remain null in EXECUTE")
    if extension["human_decision"] is not None:
        raise contract_error("human_decision must remain null in EXECUTE")
    if extension["implementation_authorization"] != "NONE":
        raise contract_error("implementation_authorization must remain NONE")
    if extension["git_authorization"] != "NONE":
        raise contract_error("git_authorization must remain NONE")

    if report["result"] == "PASS":
        require_sha256(subject_identity, "subject_set_sha256_or_absent_marker")
        if output["final_candidate_frozen"] is not True:
            raise contract_error("PASS Stage Report requires final candidate freeze")
        if output["absent_paths"] or output["partial_paths"]:
            raise contract_error("PASS Stage Report cannot declare absent or partial output")
        if set(output["expected_paths"]) != set(output["present_paths"]):
            raise contract_error("PASS Stage Report expected and present outputs must match")


def expected_transport_path(
    profile: str, task_id: str, execution_id: str
) -> str:
    task = normalize_path_component(task_id, "task_id")
    execution = normalize_path_component(execution_id, "execution_id")
    if profile == "PRE_R3_BOOTSTRAP":
        return (
            "planning/verification/bootstrap/routing-r3-harness/"
            f"{execution}/stage-report.yaml"
        )
    if profile == "R3_ACTIVE":
        return f"planning/verification/runs/{task}/{execution}/stage-report.yaml"
    raise contract_error("unknown Stage Report transport profile")


def validate_transport_path(
    root_value: str,
    profile: str,
    task_id: str,
    execution_id: str,
    relative_value: str,
) -> tuple:
    root = Path(root_value)
    if root.is_symlink() or not root.is_dir():
        raise blocked_error(
            "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
            "repository root must be an existing non-symlink directory",
        )
    relative = normalize_relative_path(relative_value)
    expected = expected_transport_path(profile, task_id, execution_id)
    if relative != expected:
        raise blocked_error(
            "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
            "Stage Report path does not match the exact transport profile",
        )
    current = root
    for component in Path(relative).parts[:-1]:
        current = current / component
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            raise blocked_error(
                "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
                "Stage Report ancestor is not a regular directory",
            )
    return root, relative, root / relative


def create_missing_parents(root: Path, relative: str) -> None:
    current = root
    for component in Path(relative).parts[:-1]:
        current = current / component
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            try:
                os.mkdir(str(current), 0o755)
            except FileExistsError:
                metadata = current.lstat()
                if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
                    raise blocked_error(
                        "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
                        "Stage Report ancestor changed during creation",
                    )
            continue
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
            raise blocked_error(
                "BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH",
                "Stage Report ancestor is not a regular directory",
            )


def path_exists_without_following(path: Path) -> bool:
    return os.path.lexists(str(path))


def write_exclusive(path: Path, data: bytes) -> None:
    if not hasattr(os, "O_NOFOLLOW"):
        raise blocked_error(
            "BLOCKED_REQUIRED_REVIEW_CAPABILITY",
            "os.O_NOFOLLOW is unavailable",
        )
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
    try:
        descriptor = os.open(str(path), flags, 0o644)
    except FileExistsError as error:
        raise blocked_error(
            "BLOCKED_STAGE_REPORT_PATH_COLLISION",
            "Stage Report path already exists",
            exit_code=5,
        ) from error
    written = 0
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise execution_error("new Stage Report is not a regular file", 1)
        while written < len(data):
            count = os.write(descriptor, data[written:])
            if count <= 0:
                raise execution_error("incomplete Stage Report write", 1)
            written += count
        os.fsync(descriptor)
    except HarnessError:
        raise
    except OSError as error:
        raise execution_error(f"Stage Report write failed: {error}", 1) from error
    finally:
        os.close(descriptor)


def read_regular_file(path: Path) -> bytes:
    try:
        metadata = path.lstat()
    except FileNotFoundError as error:
        raise blocked_error(
            "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
            "Stage Report path is absent",
        ) from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise blocked_error(
            "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
            "Stage Report is not a regular non-symlink file",
        )
    try:
        return path.read_bytes()
    except OSError as error:
        raise blocked_error(
            "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
            f"Stage Report cannot be read: {error}",
        ) from error


def build_manifest(root: Path, paths: Sequence[str]) -> bytes:
    normalized = [normalize_relative_path(value) for value in paths]
    if not normalized:
        raise contract_error("at least one subject path is required")
    if len(set(normalized)) != len(normalized):
        raise contract_error("duplicate normalized subject path")

    records: List[bytes] = []
    for relative in sorted(normalized, key=lambda value: value.encode("utf-8")):
        target = root
        components = Path(relative).parts
        for index, component in enumerate(components):
            target = target / component
            try:
                metadata = target.lstat()
            except FileNotFoundError as error:
                raise subject_error(
                    f"subject is not a regular non-symlink file: {relative}"
                ) from error
            if stat.S_ISLNK(metadata.st_mode):
                raise subject_error(
                    f"subject path contains a symlink: {relative}"
                )
            if index < len(components) - 1 and not stat.S_ISDIR(metadata.st_mode):
                raise subject_error(
                    f"subject parent is not a directory: {relative}"
                )
        if not stat.S_ISREG(metadata.st_mode):
            raise subject_error(f"subject is not a regular non-symlink file: {relative}")
        data = target.read_bytes()
        records.append(
            f"{sha256_bytes(data)}  {len(data)}  {relative}\n".encode("utf-8")
        )
    return b"".join(records)


def manifest_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    root = Path(arguments.root)
    if root.is_symlink() or not root.is_dir():
        raise contract_error("root must be an existing regular directory")
    manifest = build_manifest(root, arguments.path)
    return {
        "manifest_byte_length": len(manifest),
        "manifest_hex": manifest.hex(),
        "reason_code": "NONE",
        "repository_mutations": 0,
        "result": "PASS",
        "stop": True,
        "subject_set_sha256": sha256_bytes(manifest),
    }


def check_request_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    request = load_json_object(arguments.input)
    validate_request(
        request,
        arguments.expected_subject_sha256,
        arguments.expected_role,
        arguments.expected_model,
    )
    return {
        "reason_code": "NONE",
        "repository_mutations": 0,
        "result": "PASS",
        "stop": True,
        "validated_request_id": request["request_id"],
    }


def check_result_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    request = load_json_object(arguments.request)
    result = load_json_object(arguments.input)
    validate_result(
        result,
        request,
        arguments.expected_subject_sha256,
        arguments.expected_role,
        arguments.expected_model,
    )
    return {
        "reason_code": "NONE",
        "repository_mutations": 0,
        "result": "PASS",
        "stop": True,
        "validated_reason_code": result["reason_code"],
        "validated_request_id": result["request_id"],
        "validated_reviewer_result": result["result"],
    }


def check_gate_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    gate = load_json_object(arguments.input)
    validate_gate(
        gate,
        arguments.expected_subject_sha256,
        arguments.expected_role,
        arguments.expected_request_id,
    )
    return {
        "reason_code": "NONE",
        "repository_mutations": 0,
        "result": "PASS",
        "stop": True,
        "validated_gate_id": gate["gate_id"],
        "validated_gate_result": gate["result"],
    }


def create_stage_report_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    root, relative, target = validate_transport_path(
        arguments.root,
        arguments.transport_profile,
        arguments.task_id,
        arguments.execution_id,
        arguments.output,
    )
    if path_exists_without_following(target):
        raise blocked_error(
            "BLOCKED_STAGE_REPORT_PATH_COLLISION",
            "Stage Report path already exists",
            exit_code=5,
        )
    report = load_json_object(arguments.input)
    validate_stage_report(report, arguments.task_id, arguments.execution_id)
    if relative not in report["changed_paths"]:
        raise contract_error("Stage Report path must be present in changed_paths")
    data = canonical_json_bytes(report)
    create_missing_parents(root, relative)
    if path_exists_without_following(target):
        raise blocked_error(
            "BLOCKED_STAGE_REPORT_PATH_COLLISION",
            "Stage Report path appeared before exclusive creation",
            exit_code=5,
        )
    write_exclusive(target, data)
    observed = read_regular_file(target)
    if observed != data:
        raise execution_error("Stage Report bytes differ after creation", 1)
    return {
        "reason_code": "NONE",
        "repository_mutations": 1,
        "result": "PASS",
        "stage_report_byte_length": len(observed),
        "stage_report_path": relative,
        "stage_report_sha256": sha256_bytes(observed),
        "stop": True,
    }


def verify_stage_report_command(arguments: argparse.Namespace) -> Dict[str, Any]:
    _, relative, target = validate_transport_path(
        arguments.root,
        arguments.transport_profile,
        arguments.task_id,
        arguments.execution_id,
        arguments.path,
    )
    expected_sha256 = require_sha256(arguments.expected_sha256, "expected_sha256")
    if isinstance(arguments.expected_byte_length, bool) or arguments.expected_byte_length < 1:
        raise contract_error("expected_byte_length must be a positive integer")
    before = read_regular_file(target)
    if len(before) != arguments.expected_byte_length or sha256_bytes(before) != expected_sha256:
        raise blocked_error(
            "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
            "Stage Report byte identity does not match validation binding",
        )
    report = parse_json_object_bytes(before)
    validate_stage_report(report, arguments.task_id, arguments.execution_id)
    if relative not in report["changed_paths"]:
        raise contract_error("Stage Report path must be present in changed_paths")
    after = read_regular_file(target)
    if after != before:
        raise blocked_error(
            "BLOCKED_VALIDATION_SUBJECT_MISMATCH",
            "Stage Report bytes changed during verification",
        )
    return {
        "reason_code": "NONE",
        "repository_mutations": 0,
        "result": "PASS",
        "stage_report_byte_length": len(after),
        "stage_report_path": relative,
        "stage_report_sha256": sha256_bytes(after),
        "stop": True,
    }


def add_request_binding_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--input", required=True)
    parser.add_argument("--expected-subject-sha256", required=True)
    parser.add_argument("--expected-role", required=True)
    parser.add_argument("--expected-model", required=True)


def build_parser() -> argparse.ArgumentParser:
    parser = CanonicalArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    manifest = subparsers.add_parser("manifest")
    manifest.add_argument("--root", required=True)
    manifest.add_argument("--path", action="append", required=True)
    manifest.set_defaults(handler=manifest_command)

    check_request = subparsers.add_parser("check-request")
    add_request_binding_arguments(check_request)
    check_request.set_defaults(handler=check_request_command)

    check_result = subparsers.add_parser("check-result")
    add_request_binding_arguments(check_result)
    check_result.add_argument("--request", required=True)
    check_result.set_defaults(handler=check_result_command)

    check_gate = subparsers.add_parser("check-gate")
    check_gate.add_argument("--input", required=True)
    check_gate.add_argument("--expected-subject-sha256", required=True)
    check_gate.add_argument("--expected-role", required=True)
    check_gate.add_argument("--expected-request-id", required=True)
    check_gate.set_defaults(handler=check_gate_command)

    create_report = subparsers.add_parser("create-stage-report")
    create_report.add_argument("--root", required=True)
    create_report.add_argument("--input", required=True)
    create_report.add_argument("--transport-profile", required=True)
    create_report.add_argument("--task-id", required=True)
    create_report.add_argument("--execution-id", required=True)
    create_report.add_argument("--output", required=True)
    create_report.set_defaults(handler=create_stage_report_command)

    verify_report = subparsers.add_parser("verify-stage-report")
    verify_report.add_argument("--root", required=True)
    verify_report.add_argument("--transport-profile", required=True)
    verify_report.add_argument("--task-id", required=True)
    verify_report.add_argument("--execution-id", required=True)
    verify_report.add_argument("--path", required=True)
    verify_report.add_argument("--expected-byte-length", required=True, type=int)
    verify_report.add_argument("--expected-sha256", required=True)
    verify_report.set_defaults(handler=verify_stage_report_command)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        arguments = build_parser().parse_args(argv)
        emit(arguments.handler(arguments))
        return 0
    except HarnessHelp as help_result:
        emit(
            {
                "help": help_result.help_text,
                "reason_code": "NONE",
                "repository_mutations": 0,
                "result": "PASS",
                "stop": True,
            }
        )
        return 0
    except HarnessError as error:
        payload: Dict[str, Any] = {
            "message": error.message,
            "reason_code": error.reason_code,
            "repository_mutations": error.repository_mutations,
            "result": error.result,
            "stop": True,
        }
        if error.finding_origin is not None:
            payload["finding_origin"] = error.finding_origin
        emit(payload)
        return error.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
