#!/usr/bin/env python3
"""Validate the active DRAFT-R17 portable-package contract with stdlib only.

This helper performs deterministic mechanical author checks. It does not
perform independent semantic validation, human acceptance, repository
mutation, implementation, or Git actions.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


PACKAGE_REVISION = "DRAFT-R17"
REGISTRY_PATH = Path("ACTIVE_SUBJECTS_R17.txt")
MANIFEST_PATH = Path(
    "development-package-state/R17_ACTIVE_CONTENT_MANIFEST.sha256"
)
STATE_REGISTRY_PATH = Path(
    "development-package-state/SUBJECT_STATE_REGISTRY_R17.md"
)
COMPOSITE_MANIFEST_PATH = Path(
    "development-package-state/R17_COMPOSITE_CONTENT_MANIFEST.sha256"
)
ROOT_MANIFEST_PATH = Path("ROOT_FILES_MANIFEST.yaml")
ROOT_PAYLOAD_FILES = {
    "AGENTS.md": ("AGENTS.md", "REPOSITORY_AGENT_ROUTER"),
    "README.md": ("README.md", "HUMAN_ENTRYPOINT"),
    ".gitignore": (".gitignore", "MINIMAL_SHARED_IGNORE_BASE"),
    ".agents/rules/aos.md": (
        ".agents/rules/aos.md",
        "ANTIGRAVITY_WORKSPACE_RULE",
    ),
}
ROOT_MANIFEST_TOP_LEVEL_KEYS = {
    "manifest_id",
    "manifest_class",
    "package_revision",
    "status",
    "target_repository_class",
    "source",
    "target",
    "materialization",
    "materialization_transaction",
    "conflict_policy",
    "canonical_instruction_owner",
    "root_files_role",
    "files",
    "excluded_root_paths",
    "deferred_artifact_classes",
    "root_materialization_preconditions",
    "postconditions",
    "implementation_authorization",
    "git_authorization",
}
R16_EVIDENCE_SHA256 = {
    "ACTIVE_SUBJECTS_R16.txt": (
        "4267ae4dc485c8da314e6b0f41e1c6f677d3785f8f532e59936ff7e09d9186f2"
    ),
    "development-package-state/R16_ACCEPTANCE_AND_DELIVERY.md": (
        "a2d18ac32403e6a20ef39e261ca718d3f20481df13a95b07ac47240268e41416"
    ),
    "development-package-state/R16_ACCEPTANCE_AND_DELIVERY.md.sha256": (
        "409401f44fc7dece76183666bb3dbca62fa39c6bdc791176a7ec74a90acd5e62"
    ),
    "development-package-state/R16_ACTIVE_CONTENT_MANIFEST.sha256": (
        "6f5603cbbca0553b2ec88794a5507064f001c542579c262329d48b4abbed8519"
    ),
    "development-package-state/R16_AUTHOR_EXECUTION_REPORT.md": (
        "5176847f6861c8dcb1ecc4b2f0d2e5e8ab8ff9dfe7aca08a7b3c2c777626ed4d"
    ),
    "development-package-state/R16_COMPOSITE_CONTENT_MANIFEST.sha256": (
        "5ac5b606960fc4f533cdfe7ca3bc95c879c62a3d8f95d1bc10270a469a286a61"
    ),
    "development-package-state/R16_FULL_CANDIDATE_MANIFEST.sha256": (
        "cc66152658e37fd5879c1c4bd258a8ff9f6f5765f9a54862790a61a900eb1a07"
    ),
    "development-package-state/R16_FULL_CANDIDATE_PATHS.txt": (
        "067d4945e0eabd60f50618f3bc911ea4a329e18b60c70d1028000c47408a4e6d"
    ),
    "development-package-state/SUBJECT_STATE_REGISTRY_R16.md": (
        "99b57c57fee38c5cfaed26d05e37621910a117c0483578b9d0359d02a10eab07"
    ),
}
VALIDATION_SUPPORT_PATHS = {
    "validation/fixtures/active_absolute_path.md",
    "validation/fixtures/external_mandatory_link.md",
    "validation/fixtures/modified_accepted_subject.md",
    "validation/fixtures/self_authorized_task.md",
    "validation/fixtures/status_axis_collision.md",
    "validation/fixtures/unbound_repository_specific_task.md",
    "validation/test_validate_portable_package.py",
}
R17_GENERATED_EVIDENCE_ROLES = {
    "development-package-state/R17_ACTIVE_CONTENT_MANIFEST.sha256": "DETACHED_MANIFEST",
    "development-package-state/R17_AUTHOR_EXECUTION_REPORT.md": "AUTHOR_EVIDENCE",
    "development-package-state/R17_FULL_CANDIDATE_MANIFEST.sha256": "DETACHED_MANIFEST",
    "development-package-state/R17_FULL_CANDIDATE_PATHS.txt": "DETACHED_MANIFEST",
}
HISTORICAL_BEGIN = "<!-- HISTORICAL_R14_APPENDIX_BEGIN -->"
HISTORICAL_END = "<!-- HISTORICAL_R14_APPENDIX_END -->"

TECHNICAL_RESULTS = {
    "CONTRACT_VIOLATION",
    "FAIL",
    "BLOCKED",
    "UNKNOWN",
    "NOT_RUN",
    "PASS",
    "HUMAN_REVIEW_REQUIRED",
}
FORBIDDEN_STATUS_TOKENS = {
    "PASS_OR_EXACT_LIMITATION",
    "NOT_APPLICABLE_UNTIL_SELECTION",
    "BLOCKED_BY_EXPECTED_HUMAN_GATE",
}
LOCAL_ABSOLUTE_PATH = re.compile(
    r"(?<![A-Za-z0-9])(?:/Users/|/home/|[A-Za-z]:\\\\)"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
MANIFEST_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")

REQUIRED_FILES = {
    "AGENTS.md",
    "ACTIVE_SUBJECTS_R17.txt",
    "README.md",
    "ROOT_FILES_MANIFEST.yaml",
    "development-package-state/CURRENT.md",
    "development-package-state/PORTABILITY_DIRECTION_2026-07-31.md",
    "development-package-state/SUBJECT_STATE_REGISTRY_R17.md",
    "development-package/00_Control_and_Source_Precedence.md",
    "development-package/07_Implementation_Handoff.md",
    "root/.agents/rules/aos.md",
    "root/.gitignore",
    "root/AGENTS.md",
    "root/README.md",
    "templates/EXECUTION_AUTHORIZATION.template.md",
    "templates/FEATURE_CONTRACT.template.md",
    "templates/FIRST_VERTICAL_SLICE_SELECTION.template.md",
    "templates/PORTABLE_TASK_CANDIDATE.template.md",
    "templates/TARGET_REPOSITORY_BINDING.template.md",
    "templates/TASK_BRIEF.template.md",
    "validation/validate_portable_package.py",
}

TEMPLATE_REQUIREMENTS: Dict[str, Set[str]] = {
    "templates/FIRST_VERTICAL_SLICE_SELECTION.template.md": {
        "decision_type: FIRST_VERTICAL_SLICE_SELECTION",
        "feature_or_slice_id:",
        "included_features:",
        "excluded_features:",
        "user_outcome:",
        "exact_contract_owner:",
        "exact_contract_revision_or_digest:",
        "human_disposition:",
        "target_repository_binding:",
        "decision_date:",
        "decided_by_human:",
        "FIRST_VERTICAL_SLICE_SELECTION_REQUIRED",
    },
    "templates/FEATURE_CONTRACT.template.md": {
        "contract_id:",
        "selected_slice_decision_id:",
        "primary_users:",
        "user_outcome:",
        "trigger:",
        "preconditions:",
        "input_schemas:",
        "output_schemas:",
        "happy_path:",
        "states:",
        "transitions:",
        "persistence_effects:",
        "failure_taxonomy:",
        "recovery:",
        "retry:",
        "authority_boundaries:",
        "dependencies:",
        "non_goals:",
        "acceptance_criteria:",
        "negative_scenarios:",
        "required_adrs:",
        "unresolved_material_decisions:",
        "human_decision:",
    },
    "templates/PORTABLE_TASK_CANDIDATE.template.md": {
        "task_id:",
        "feature_contract_identity:",
        "contract_dependencies:",
        "architecture_dependencies:",
        "acceptance_ids:",
        "negative_scenario_ids:",
        "binding_state: PORTABLE_UNBOUND",
        "task_candidate_role: DRAFT_PORTABLE_CANDIDATE",
        "assigned_Risk_Profile: UNASSIGNED",
        "implementation_authorization: NONE",
        "git_authorization: NONE",
    },
    "templates/TARGET_REPOSITORY_BINDING.template.md": {
        "binding_state: TARGET_BOUND_FOR_PLANNING",
        "repository_root:",
        "repository_identity:",
        "branch:",
        "HEAD:",
        "baseline:",
        "worktree_status:",
        "staged_changes:",
        "unstaged_changes:",
        "untracked_changes:",
        "nested_repositories:",
        "symlinks:",
        "available_toolchain:",
        "dependency_state:",
        "validation_entrypoints:",
        "network_state:",
        "sandbox_state:",
        "observed_at:",
        "observation_method:",
    },
    "templates/TASK_BRIEF.template.md": {
        "task_candidate_role: TARGET_BOUND_DRAFT",
        "feature_selection_decision_id:",
        "feature_contract_identity:",
        "feature_contract_human_decision:",
        "target_binding_id:",
        "target_binding_current:",
        "allowed_paths:",
        "forbidden_paths:",
        "allowed_operations:",
        "forbidden_operations:",
        "acceptance_matrix:",
        "negative_test_matrix:",
        "validation_commands:",
        "expected_results:",
        "recovery:",
        "stop_conditions:",
        "assigned_Risk_Profile: UNASSIGNED",
        "human_task_decision: NOT_RUN",
        "implementation_authorization: NONE",
    },
    "templates/EXECUTION_AUTHORIZATION.template.md": {
        "authorization_class: IMPLEMENTATION_EXECUTION_AUTHORIZATION",
        "issued_by_human:",
        "task_id:",
        "task_brief_revision:",
        "feature_contract_identity:",
        "target_binding_id:",
        "repository_identity:",
        "branch:",
        "HEAD_or_baseline:",
        "authorized_stage: EXECUTE",
        "allowed_operations:",
        "allowed_paths:",
        "forbidden_operations:",
        "forbidden_paths:",
        "single_run: true",
        "authorization_state: GRANTED",
    },
}


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    detail: str


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def read_utf8(path: Path, findings: List[Finding], relative: str) -> Optional[str]:
    try:
        payload = path.read_bytes()
        return payload.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        findings.append(Finding("E_UTF8_READ", relative, str(error)))
        return None


def active_text(text: str, findings: List[Finding], relative: str) -> str:
    has_begin = HISTORICAL_BEGIN in text
    has_end = HISTORICAL_END in text
    if has_begin != has_end:
        findings.append(
            Finding(
                "E_HISTORICAL_BOUNDARY",
                relative,
                "historical appendix markers are unbalanced",
            )
        )
        return text
    if not has_begin:
        return text
    before, remainder = text.split(HISTORICAL_BEGIN, 1)
    _, after = remainder.split(HISTORICAL_END, 1)
    return before + "\n" + after


def fenced_blocks(text: str) -> List[List[str]]:
    blocks: List[List[str]] = []
    current: Optional[List[str]] = None
    fence_character: Optional[str] = None
    fence_length = 0

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if current is None:
            opening = re.match(r"^(`{3,}|~{3,})(.*)$", stripped)
            if opening is not None:
                fence = opening.group(1)
                current = []
                fence_character = fence[0]
                fence_length = len(fence)
            continue

        if (
            fence_character is not None
            and len(stripped) >= fence_length
            and set(stripped) == {fence_character}
        ):
            blocks.append(current)
            current = None
            fence_character = None
            fence_length = 0
            continue

        if stripped:
            current.append(stripped)

    return blocks


def contains_exact_contiguous_sequence(
    block_lines: Sequence[str], ordered_tokens: Sequence[str]
) -> bool:
    if not ordered_tokens or len(block_lines) < len(ordered_tokens):
        return False
    sequence_length = len(ordered_tokens)
    return any(
        tuple(block_lines[start : start + sequence_length]) == tuple(ordered_tokens)
        for start in range(len(block_lines) - sequence_length + 1)
    )


def parse_frontmatter(
    text: str, findings: List[Finding], relative: str
) -> Dict[str, str]:
    if not text.startswith("---\n"):
        findings.append(
            Finding("E_FRONTMATTER", relative, "missing opening YAML delimiter")
        )
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        findings.append(
            Finding("E_FRONTMATTER", relative, "missing closing YAML delimiter")
        )
        return {}
    block = text[4:end]
    if "\t" in block:
        findings.append(
            Finding("E_FRONTMATTER", relative, "tab found in YAML frontmatter")
        )
    result: Dict[str, str] = {}
    for line_number, line in enumerate(block.splitlines(), start=2):
        if not line or line.startswith((" ", "-", "#")):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            findings.append(
                Finding(
                    "E_FRONTMATTER",
                    relative,
                    f"unsupported top-level YAML syntax at line {line_number}",
                )
            )
            continue
        key, value = match.group(1), (match.group(2) or "").strip()
        if key in result:
            findings.append(
                Finding(
                    "E_FRONTMATTER_DUPLICATE_KEY",
                    relative,
                    f"duplicate top-level key {key}",
                )
            )
        result[key] = value
    return result


def load_registry(package_root: Path, findings: List[Finding]) -> List[str]:
    registry = package_root / REGISTRY_PATH
    text = read_utf8(registry, findings, REGISTRY_PATH.as_posix())
    if text is None:
        return []
    if "\r" in text:
        findings.append(
            Finding("E_REGISTRY_LINE_ENDING", REGISTRY_PATH.as_posix(), "CR found")
        )
    if text and not text.endswith("\n"):
        findings.append(
            Finding(
                "E_REGISTRY_FINAL_LF",
                REGISTRY_PATH.as_posix(),
                "registry must end with LF",
            )
        )
    paths = text.splitlines()
    if any(not item for item in paths):
        findings.append(
            Finding(
                "E_REGISTRY_EMPTY_PATH",
                REGISTRY_PATH.as_posix(),
                "empty registry record",
            )
        )
    if any(item.startswith("#") for item in paths):
        findings.append(
            Finding(
                "E_REGISTRY_COMMENT",
                REGISTRY_PATH.as_posix(),
                "comments are forbidden",
            )
        )
    if len(set(paths)) != len(paths):
        findings.append(
            Finding("E_REGISTRY_DUPLICATE", REGISTRY_PATH.as_posix(), "duplicate path")
        )
    expected_order = sorted(paths, key=lambda value: value.encode("utf-8"))
    if paths != expected_order:
        findings.append(
            Finding(
                "E_REGISTRY_ORDER",
                REGISTRY_PATH.as_posix(),
                "paths are not UTF-8 bytewise sorted",
            )
        )
    if MANIFEST_PATH.as_posix() in paths:
        findings.append(
            Finding(
                "E_MANIFEST_RECURSION",
                REGISTRY_PATH.as_posix(),
                "manifest path must not be active",
            )
        )
    root_resolved = package_root.resolve()
    for relative in paths:
        pure = Path(relative)
        if pure.is_absolute() or ".." in pure.parts or "\\" in relative:
            findings.append(
                Finding("E_REGISTRY_PATH", relative, "path is not safe and relative")
            )
            continue
        resolved = (package_root / pure).resolve()
        if not is_within(resolved, root_resolved):
            findings.append(
                Finding("E_REGISTRY_PATH", relative, "path escapes package root")
            )
            continue
        if not (package_root / pure).exists():
            findings.append(Finding("E_ACTIVE_PATH_MISSING", relative, "not found"))
        elif (package_root / pure).is_symlink():
            findings.append(
                Finding("E_ACTIVE_SYMLINK", relative, "active symlink is forbidden")
            )
        elif not (package_root / pure).is_file():
            findings.append(
                Finding("E_ACTIVE_NOT_FILE", relative, "active path is not a file")
            )
    return paths


def expected_manifest(package_root: Path, paths: Sequence[str]) -> bytes:
    records: List[str] = []
    for relative in sorted(paths, key=lambda value: value.encode("utf-8")):
        digest = sha256_bytes((package_root / relative).read_bytes())
        records.append(f"{digest}  {relative}\n")
    return "".join(records).encode("utf-8")


def write_manifest(package_root: Path, paths: Sequence[str]) -> None:
    destination = package_root / MANIFEST_PATH
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(expected_manifest(package_root, paths))


def check_manifest(
    package_root: Path, paths: Sequence[str], findings: List[Finding]
) -> Optional[str]:
    manifest = package_root / MANIFEST_PATH
    if not manifest.exists():
        findings.append(
            Finding("E_MANIFEST_MISSING", MANIFEST_PATH.as_posix(), "not found")
        )
        return None
    payload = manifest.read_bytes()
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as error:
        findings.append(
            Finding("E_MANIFEST_UTF8", MANIFEST_PATH.as_posix(), str(error))
        )
        return None
    if "\r" in text or (text and not text.endswith("\n")):
        findings.append(
            Finding(
                "E_MANIFEST_LINE_ENDING",
                MANIFEST_PATH.as_posix(),
                "manifest must use LF and final LF",
            )
        )
    records: List[str] = []
    for line in text.splitlines():
        match = MANIFEST_LINE.match(line)
        if not match:
            findings.append(
                Finding(
                    "E_MANIFEST_FORMAT",
                    MANIFEST_PATH.as_posix(),
                    f"invalid record: {line}",
                )
            )
        else:
            records.append(match.group(2))
    if records != sorted(paths, key=lambda value: value.encode("utf-8")):
        findings.append(
            Finding(
                "E_MANIFEST_PATH_SET",
                MANIFEST_PATH.as_posix(),
                "manifest paths differ from active registry",
            )
        )
    if payload != expected_manifest(package_root, paths):
        findings.append(
            Finding(
                "E_MANIFEST_DIGEST",
                MANIFEST_PATH.as_posix(),
                "manifest content does not match active raw bytes",
            )
        )
    return sha256_bytes(payload)


def check_composite_manifest(
    package_root: Path, active_paths: Sequence[str], findings: List[Finding]
) -> Tuple[Optional[str], Optional[str], int]:
    manifest = package_root / COMPOSITE_MANIFEST_PATH
    expected_roles: Dict[str, str] = {
        relative: "ACTIVE_NORMATIVE" for relative in active_paths
    }
    expected_roles.update(
        {relative: "VALIDATION_SUPPORT" for relative in VALIDATION_SUPPORT_PATHS}
    )
    expected_roles.update(
        {
            relative: "HISTORICAL_ACCEPTANCE_EVIDENCE"
            for relative in R16_EVIDENCE_SHA256
        }
    )
    expected_roles.update(R17_GENERATED_EVIDENCE_ROLES)
    expected_paths = sorted(expected_roles, key=lambda value: value.encode("utf-8"))
    if len(expected_paths) != 40:
        findings.append(
            Finding(
                "E_COMPOSITE_ROLE_PARTITION",
                STATE_REGISTRY_PATH.as_posix(),
                f"expected role partition has {len(expected_paths)} paths, not 40",
            )
        )
    if not manifest.is_file():
        findings.append(
            Finding("E_COMPOSITE_MISSING", COMPOSITE_MANIFEST_PATH.as_posix(), "not found")
        )
        return None, None, 0
    payload = manifest.read_bytes()
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as error:
        findings.append(
            Finding("E_COMPOSITE_UTF8", COMPOSITE_MANIFEST_PATH.as_posix(), str(error))
        )
        return None, None, 0
    if "\r" in text or (text and not text.endswith("\n")):
        findings.append(
            Finding(
                "E_COMPOSITE_LINE_ENDING",
                COMPOSITE_MANIFEST_PATH.as_posix(),
                "composite manifest must use LF and final LF",
            )
        )
    records: List[Tuple[str, str]] = []
    for line in text.splitlines():
        match = MANIFEST_LINE.match(line)
        if not match:
            findings.append(
                Finding(
                    "E_COMPOSITE_FORMAT",
                    COMPOSITE_MANIFEST_PATH.as_posix(),
                    f"invalid record: {line}",
                )
            )
            continue
        records.append((match.group(1), match.group(2)))
    record_paths = [relative for _, relative in records]
    if record_paths != expected_paths:
        findings.append(
            Finding(
                "E_COMPOSITE_PATH_SET",
                COMPOSITE_MANIFEST_PATH.as_posix(),
                "composite paths differ from exact 40-path role partition",
            )
        )
    role_records: List[str] = []
    for digest, relative in records:
        path = package_root / relative
        if not path.is_file():
            findings.append(Finding("E_COMPOSITE_PATH_MISSING", relative, "not found"))
            continue
        actual = sha256_bytes(path.read_bytes())
        if actual != digest:
            findings.append(
                Finding("E_COMPOSITE_DIGEST", relative, "raw-byte digest mismatch")
            )
        role = expected_roles.get(relative)
        if role is not None:
            role_records.append(f"{digest}  {role}  {relative}\n")
    role_payload = "".join(role_records).encode("utf-8")
    return sha256_bytes(payload), sha256_bytes(role_payload), len(records)


def yaml_section(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*$", text)
    if not match:
        return ""
    result: List[str] = []
    for line in text[match.end() :].splitlines():
        if line and not line[0].isspace():
            break
        result.append(line)
    return "\n".join(result)


def yaml_section_scalar(section: str, key: str) -> Optional[str]:
    match = re.search(rf"(?m)^  {re.escape(key)}:\s*(.*?)\s*$", section)
    return match.group(1).strip().strip("\"'") if match else None


def yaml_section_list(section: str) -> List[str]:
    return [
        match.group(1).strip().strip("\"'")
        for match in re.finditer(r"(?m)^  -\s+(.+?)\s*$", section)
    ]


def root_manifest_file_entries(text: str) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    current: Optional[Dict[str, str]] = None
    for line in yaml_section(text, "files").splitlines():
        source = re.match(r"^  - source:\s*(.+?)\s*$", line)
        if source:
            current = {"source": source.group(1).strip().strip("\"'")}
            entries.append(current)
            continue
        field = re.match(r"^    ([A-Za-z_][A-Za-z0-9_-]*):\s*(.+?)\s*$", line)
        if field and current is not None:
            current[field.group(1)] = field.group(2).strip().strip("\"'")
    return entries


def gitignore_hides_protected(pattern: str) -> bool:
    protected = (
        "AOS-3/package-file",
        "AGENTS.md",
        "README.md",
        ".agents/rules/aos.md",
        "docs/owner.md",
        "tests/test_owner.py",
        "package.lock",
    )
    normalized = pattern.strip().lstrip("/")
    if not normalized or normalized.startswith(("#", "!")):
        return False
    directory_pattern = normalized.endswith("/")
    normalized = normalized.rstrip("/")
    for path in protected:
        if directory_pattern and (
            path == normalized or path.startswith(normalized + "/")
        ):
            return True
        if fnmatch.fnmatchcase(path, normalized):
            return True
        if "/" not in normalized and fnmatch.fnmatchcase(Path(path).name, normalized):
            return True
    return False


def check_materialized_readme_links(
    package_root: Path, text: str, findings: List[Finding]
) -> None:
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().strip("<>").split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        normalized = posixpath.normpath(target)
        if normalized.startswith("../") or normalized.startswith("/"):
            findings.append(
                Finding("E_ROOT_README_LINK", "root/README.md", f"unsafe {target}")
            )
            continue
        if normalized.startswith("AOS-3/"):
            resolved = package_root / normalized[6:]
        else:
            resolved = package_root / "root" / normalized
        if not resolved.is_file():
            findings.append(
                Finding(
                    "E_ROOT_README_LINK",
                    "root/README.md",
                    f"materialized target not found: {target}",
                )
            )


def check_antigravity_references(
    package_root: Path, text: str, findings: List[Finding]
) -> None:
    references = re.findall(r"(?m)^@(\S+)\s*$", text)
    expected = {
        "../../AOS-3/AGENTS.md",
        "../../AOS-3/development-package-state/CURRENT.md",
    }
    if set(references) != expected:
        findings.append(
            Finding(
                "E_ANTIGRAVITY_ROUTE",
                "root/.agents/rules/aos.md",
                "@ references differ from required package owners",
            )
        )
    for reference in references:
        normalized = posixpath.normpath(posixpath.join(".agents/rules", reference))
        if not normalized.startswith("AOS-3/") or not (
            package_root / normalized[6:]
        ).is_file():
            findings.append(
                Finding(
                    "E_ANTIGRAVITY_ROUTE",
                    "root/.agents/rules/aos.md",
                    f"materialized reference does not resolve: {reference}",
                )
            )


def check_root_payload(package_root: Path, findings: List[Finding]) -> None:
    root = package_root / "root"
    actual_files: Set[str] = set()
    if root.is_dir():
        for path in root.rglob("*"):
            if path.is_file() or path.is_symlink():
                actual_files.add(path.relative_to(root).as_posix())
                if path.is_symlink():
                    findings.append(
                        Finding(
                            "E_ROOT_PAYLOAD_SYMLINK",
                            path.relative_to(package_root).as_posix(),
                            "root payload symlinks are forbidden",
                        )
                    )
    if actual_files != set(ROOT_PAYLOAD_FILES):
        findings.append(
            Finding(
                "E_ROOT_PAYLOAD_FILE_SET",
                "root/",
                "payload files differ: "
                + f"expected={sorted(ROOT_PAYLOAD_FILES)} actual={sorted(actual_files)}",
            )
        )

    for relative in sorted(actual_files & set(ROOT_PAYLOAD_FILES)):
        path = root / relative
        payload = path.read_bytes()
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError as error:
            findings.append(
                Finding("E_ROOT_PAYLOAD_UTF8", f"root/{relative}", str(error))
            )
            continue
        if b"\r" in payload or not payload.endswith(b"\n"):
            findings.append(
                Finding(
                    "E_ROOT_PAYLOAD_LINE_ENDING",
                    f"root/{relative}",
                    "payload must use LF with final LF",
                )
            )
        if relative.endswith(".md") and sum(
            1 for line in text.splitlines() if line.lstrip().startswith("```")
        ) % 2:
            findings.append(
                Finding("E_MARKDOWN_FENCE", f"root/{relative}", "unbalanced fence")
            )

    agents_path = root / "AGENTS.md"
    if agents_path.is_file():
        agents = agents_path.read_text(encoding="utf-8")
        for required in (
            "AOS-3/AGENTS.md",
            "AOS-3/development-package-state/CURRENT.md",
            "canonical instruction owner",
            "только repository-wide router",
        ):
            if required not in agents:
                findings.append(
                    Finding(
                        "E_ROOT_AGENTS_ROUTE",
                        "root/AGENTS.md",
                        f"missing required route/boundary: {required}",
                    )
                )

    readme_path = root / "README.md"
    if readme_path.is_file():
        check_materialized_readme_links(
            package_root, readme_path.read_text(encoding="utf-8"), findings
        )

    rule_path = root / ".agents/rules/aos.md"
    if rule_path.is_file():
        rule = rule_path.read_text(encoding="utf-8")
        if len(rule) >= 12_000:
            findings.append(
                Finding(
                    "E_ANTIGRAVITY_RULE_LENGTH",
                    "root/.agents/rules/aos.md",
                    "rule must be shorter than 12000 characters",
                )
            )
        check_antigravity_references(package_root, rule, findings)

    gitignore_path = root / ".gitignore"
    if gitignore_path.is_file():
        for line in gitignore_path.read_text(encoding="utf-8").splitlines():
            if gitignore_hides_protected(line):
                findings.append(
                    Finding(
                        "E_ROOT_GITIGNORE_BROAD_RULE",
                        "root/.gitignore",
                        f"rule can hide protected content: {line}",
                    )
                )

    manifest_path = package_root / ROOT_MANIFEST_PATH
    manifest_text = read_utf8(
        manifest_path, findings, ROOT_MANIFEST_PATH.as_posix()
    )
    if manifest_text is None:
        return
    if "\r" in manifest_text or not manifest_text.endswith("\n") or "\t" in manifest_text:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_FORMAT",
                ROOT_MANIFEST_PATH.as_posix(),
                "manifest must be UTF-8 LF with final LF and no tabs",
            )
        )
    top_keys = {
        match.group(1)
        for match in re.finditer(
            r"(?m)^([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)", manifest_text
        )
    }
    if top_keys != ROOT_MANIFEST_TOP_LEVEL_KEYS:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_SCHEMA",
                ROOT_MANIFEST_PATH.as_posix(),
                f"top-level keys differ: {sorted(top_keys)}",
            )
        )
    top_required = {
        "manifest_id": "AOS-ROOT-FILES-MANIFEST-R3",
        "manifest_class": "ROOT_PAYLOAD_COPY_CONTRACT",
        "package_revision": "DRAFT-R17",
        "status": "DRAFT",
        "canonical_instruction_owner": "AOS-3/AGENTS.md",
        "root_files_role": "THIN_TARGET_ADAPTERS",
        "implementation_authorization": "NONE",
        "git_authorization": "NONE",
    }
    for key, expected in top_required.items():
        match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", manifest_text)
        if not match or match.group(1).strip().strip("\"'") != expected:
            findings.append(
                Finding(
                    "E_ROOT_MANIFEST_SCHEMA",
                    ROOT_MANIFEST_PATH.as_posix(),
                    f"{key} must equal {expected}",
                )
            )

    section_requirements = {
        "target_repository_class": {
            "supported": "GREENFIELD_OR_EMPTY_ROOT",
            "existing_repository_adoption": (
                "SEPARATE_HUMAN_DECISION_AND_TASK_REQUIRED"
            ),
        },
        "source": {
            "root_base": "TARGET_REPOSITORY_ROOT",
            "relative_path": "AOS-3/root/",
        },
        "target": {
            "root_base": "OBSERVED_TARGET_REPOSITORY_ROOT",
            "relative_path": "./",
        },
        "materialization": {
            "mode": "COPY",
            "copy_semantics": "RAW_BYTES",
            "preserve_source": "true",
            "text_encoding": "UTF-8",
            "line_endings": "PRESERVE_SOURCE_LF",
            "create_missing_parent_directories": "true",
            "follow_symlinks": "false",
            "automatic_overwrite": "FORBIDDEN",
            "automatic_merge": "FORBIDDEN",
            "partial_materialization": "FORBIDDEN",
        },
        "conflict_policy": {
            "target_missing": "COPY",
            "target_exists_identical": "NOOP",
            "target_exists_different": "BLOCKED",
            "reason_code": "ROOT_FILE_CONFLICT",
            "human_review_required": "true",
        },
    }
    for section_name, required in section_requirements.items():
        section = yaml_section(manifest_text, section_name)
        for key, expected in required.items():
            if yaml_section_scalar(section, key) != expected:
                findings.append(
                    Finding(
                        "E_ROOT_MANIFEST_SCHEMA",
                        ROOT_MANIFEST_PATH.as_posix(),
                        f"{section_name}.{key} must equal {expected}",
                    )
                )

    transaction = yaml_section(manifest_text, "materialization_transaction")
    atomic_requirements = (
        "  phase_1: PREFLIGHT_ALL_TARGET_PATHS",
        "  writes_before_full_preflight: FORBIDDEN",
        "  conflict_scope: WHOLE_ROOT_PAYLOAD",
        "  on_any_different_target: BLOCK_BEFORE_WRITE",
        "  phase_2: COPY_ONLY_MISSING_PATHS",
        "  identical_target_action: NOOP",
        "  post_copy_validation: REQUIRED",
        "  on_post_copy_failure:",
        "    rollback_required: true",
        "    remove_only_paths_created_by_this_run: true",
        "    modify_preexisting_paths: false",
        "    preserve_source_payload: true",
    )
    if any(item not in transaction for item in atomic_requirements):
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_ATOMICITY",
                ROOT_MANIFEST_PATH.as_posix(),
                "preflight/copy/rollback transaction contract differs",
            )
        )

    entries = root_manifest_file_entries(manifest_text)
    sources = [entry.get("source", "") for entry in entries]
    targets = [entry.get("target", "") for entry in entries]
    if len(sources) != len(set(sources)):
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_SOURCE_DUPLICATE",
                ROOT_MANIFEST_PATH.as_posix(),
                "source paths are not unique",
            )
        )
    if len(targets) != len(set(targets)):
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_TARGET_DUPLICATE",
                ROOT_MANIFEST_PATH.as_posix(),
                "target paths are not unique",
            )
        )
    expected_entries = {
        source: {"target": target, "role": role, "required": "true"}
        for source, (target, role) in ROOT_PAYLOAD_FILES.items()
    }
    actual_entries = {
        entry.get("source", ""): {
            "target": entry.get("target", ""),
            "role": entry.get("role", ""),
            "required": entry.get("required", ""),
        }
        for entry in entries
    }
    if actual_entries != expected_entries or set(sources) != actual_files:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_FILE_SET",
                ROOT_MANIFEST_PATH.as_posix(),
                "manifest files do not exactly match payload files and roles",
            )
        )

    exclusions = yaml_section_list(yaml_section(manifest_text, "excluded_root_paths"))
    if exclusions != ["llms.txt", "GEMINI.md", ".github/**", ".codex/**"]:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_EXCLUSIONS",
                ROOT_MANIFEST_PATH.as_posix(),
                "excluded root paths differ",
            )
        )
    deferred = yaml_section_list(
        yaml_section(manifest_text, "deferred_artifact_classes")
    )
    if deferred != [
        "RUNTIME_MANIFEST",
        "TOOLCHAIN_MANIFEST",
        "CI_CONFIGURATION",
        "CLOUD_CONFIGURATION",
    ]:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_DEFERRED_CLASSES",
                ROOT_MANIFEST_PATH.as_posix(),
                "deferred artifact classes differ",
            )
        )
    preconditions = yaml_section_list(
        yaml_section(manifest_text, "root_materialization_preconditions")
    )
    if preconditions != [
        "ROOT_MATERIALIZATION_PREFLIGHT_COMPLETE",
        "DOCUMENTATION_MUTATION_AUTHORIZATION_GRANTED",
    ]:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_PRECONDITIONS",
                ROOT_MANIFEST_PATH.as_posix(),
                "materialization preconditions differ",
            )
        )
    postconditions = yaml_section_list(yaml_section(manifest_text, "postconditions"))
    expected_postconditions = [
        "SOURCE_PAYLOAD_PRESERVED",
        "TARGET_PATHS_MATCH_SOURCE_RAW_BYTES",
        "ROOT_AGENT_ROUTE_RESOLVES_TO_AOS_3",
        "ANTIGRAVITY_RULE_REFERENCES_RESOLVE",
        "NO_PARTIAL_MATERIALIZATION",
        "NO_IMPLEMENTATION_AUTHORIZATION_CREATED",
        "NO_GIT_AUTHORIZATION_CREATED",
    ]
    if postconditions != expected_postconditions:
        findings.append(
            Finding(
                "E_ROOT_MANIFEST_POSTCONDITIONS",
                ROOT_MANIFEST_PATH.as_posix(),
                "postconditions differ",
            )
        )
    antigravity = next(
        (entry for entry in entries if entry.get("source") == ".agents/rules/aos.md"),
        {},
    )
    antigravity_block = re.search(
        r"(?ms)^  - source: \.agents/rules/aos\.md\n(?P<body>.*?)(?=^  - source:|^[A-Za-z_]|\Z)",
        yaml_section(manifest_text, "files"),
    )
    activation_text = antigravity_block.group("body") if antigravity_block else ""
    if not antigravity or (
        "      technical_result: NOT_RUN" not in activation_text
        or "      reason: HUMAN_WORKSPACE_VERIFICATION_REQUIRED" not in activation_text
    ):
        findings.append(
            Finding(
                "E_ANTIGRAVITY_ACTIVATION",
                ROOT_MANIFEST_PATH.as_posix(),
                "activation must remain NOT_RUN pending human workspace verification",
            )
        )

    for relative, expected in R16_EVIDENCE_SHA256.items():
        path = package_root / relative
        if not path.is_file() or sha256_bytes(path.read_bytes()) != expected:
            findings.append(
                Finding(
                    "E_R16_EVIDENCE_DRIFT",
                    relative,
                    "immutable R16 acceptance Evidence bytes changed",
                )
            )


def extract_superseded_paths(registry_text: str) -> Set[str]:
    result: Set[str] = set()
    current_path: Optional[str] = None
    for line in registry_text.splitlines():
        path_match = re.match(r"^\s+path:\s+(.+?)\s*$", line)
        if path_match:
            current_path = path_match.group(1).strip("\"'")
            continue
        role_match = re.match(r"^\s+normative_role:\s+(\S+)\s*$", line)
        if role_match and role_match.group(1) == "SUPERSEDED" and current_path:
            result.add(current_path)
    return result


def check_markdown(
    package_root: Path,
    relative: str,
    text: str,
    superseded_paths: Set[str],
    findings: List[Finding],
) -> None:
    current = active_text(text, findings, relative)
    if sum(1 for line in current.splitlines() if line.lstrip().startswith("```")) % 2:
        findings.append(
            Finding("E_MARKDOWN_FENCE", relative, "unbalanced fenced code block")
        )
    if LOCAL_ABSOLUTE_PATH.search(current):
        findings.append(
            Finding(
                "E_ACTIVE_ABSOLUTE_PATH",
                relative,
                "machine-local absolute path in active normative content",
            )
        )
    source_dir = (package_root / relative).parent
    root_resolved = package_root.resolve()
    for raw_target in MARKDOWN_LINK.findall(current):
        target = raw_target.strip().strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        target_path = Path(target)
        if target_path.is_absolute():
            findings.append(
                Finding(
                    "E_ACTIVE_ABSOLUTE_PATH",
                    relative,
                    f"absolute Markdown target {target}",
                )
            )
            continue
        resolved = (source_dir / target_path).resolve()
        if not is_within(resolved, root_resolved):
            findings.append(
                Finding(
                    "E_EXTERNAL_MANDATORY_LINK",
                    relative,
                    f"active Markdown link escapes AOS-3: {target}",
                )
            )
            continue
        if not resolved.exists():
            findings.append(
                Finding("E_MARKDOWN_LINK", relative, f"target not found: {target}")
            )
            continue
        rel_target = resolved.relative_to(root_resolved).as_posix()
        if rel_target in superseded_paths:
            findings.append(
                Finding(
                    "E_SUPERSEDED_INBOUND_REFERENCE",
                    relative,
                    f"active normative link targets superseded subject {rel_target}",
                )
            )


def check_status_and_authority(
    relative: str, text: str, frontmatter: Dict[str, str], findings: List[Finding]
) -> None:
    current = (
        active_text(text, findings, relative) if relative.endswith(".md") else text
    )
    for token in sorted(FORBIDDEN_STATUS_TOKENS):
        if re.search(rf"(?m):[ \t]*{re.escape(token)}[ \t]*$", current):
            findings.append(
                Finding("E_STATUS_AXIS_COLLISION", relative, f"forbidden token {token}")
            )
    for match in re.finditer(
        r"(?m)^[ \t]*technical_result:[ \t]*(\S+)[ \t]*$", current
    ):
        value = match.group(1).strip("\"'")
        if value not in TECHNICAL_RESULTS:
            findings.append(
                Finding(
                    "E_STATUS_AXIS_COLLISION",
                    relative,
                    f"invalid technical_result {value}",
                )
            )
    if re.search(
        r"(?m)^[ \t]*human_decision:[ \t]+HUMAN_REVIEW_REQUIRED[ \t]*$", current
    ):
        findings.append(
            Finding(
                "E_STATUS_AXIS_COLLISION",
                relative,
                "HUMAN_REVIEW_REQUIRED placed on human_decision axis",
            )
        )
    if (
        frontmatter.get("package_revision", "").startswith("DRAFT-R")
        and (
            frontmatter.get("status") == "ACCEPTED"
            or "acceptance_inheritance: ALLOWED_WITHOUT_EXACT_PROOF" in current
        )
    ):
        findings.append(
            Finding(
                "E_ACCEPTANCE_INHERITANCE",
                relative,
                "modified/new DRAFT subject claims acceptance without exact proof",
            )
        )
    if relative != "templates/EXECUTION_AUTHORIZATION.template.md":
        for match in re.finditer(
            r"(?m)^\s*implementation_authorization:\s*(\S+)\s*$", current
        ):
            if match.group(1).strip("\"'") != "NONE":
                findings.append(
                    Finding(
                        "E_IMPLEMENTATION_AUTHORIZATION",
                        relative,
                        "active package subject grants implementation authority",
                    )
                )
        for match in re.finditer(
            r"(?m)^\s*git_authorization:\s*(\S+)\s*$", current
        ):
            if match.group(1).strip("\"'") != "NONE":
                findings.append(
                    Finding(
                        "E_GIT_AUTHORIZATION",
                        relative,
                        "active package subject grants Git authority",
                    )
                )


def scalar(text: str, key: str) -> Optional[str]:
    match = re.search(
        rf"(?m)^\s*{re.escape(key)}:\s*(.*?)\s*$",
        text,
    )
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def nonempty_field(text: str, key: str) -> bool:
    value = scalar(text, key)
    if value is None:
        return False
    if value not in {"", "[]", "{}", "NOT_RUN", "UNASSIGNED"}:
        return True
    pattern = re.compile(
        rf"(?m)^\s*{re.escape(key)}:\s*$\n(?P<body>(?:\s{{2,}}.*\n?)*)"
    )
    match = pattern.search(text)
    return bool(match and re.search(r"(?m)^\s+-\s+\S", match.group("body")))


def check_task_brief(path: Path, findings: List[Finding]) -> None:
    relative = path.as_posix()
    text = read_utf8(path, findings, relative)
    if text is None:
        return
    if re.search(r"(?m)^\s*authorization_state:\s+GRANTED\s*$", text) or re.search(
        r"(?m)^\s*implementation_authorization:\s+GRANTED\s*$", text
    ):
        findings.append(
            Finding(
                "E_SELF_AUTHORIZED_TASK",
                relative,
                "Task Brief embeds execution authority",
            )
        )
    binding = scalar(text, "binding_state")
    if binding == "PORTABLE_UNBOUND":
        guessed_fields = []
        for key in (
            "repository_path",
            "repository_root",
            "repository_identity",
            "branch",
            "HEAD",
            "baseline",
            "toolchain",
            "command",
            "rollback_command",
        ):
            value = scalar(text, key)
            if value not in {None, "", "UNASSIGNED", "NOT_RUN", "[]"}:
                guessed_fields.append(key)
        if guessed_fields:
            findings.append(
                Finding(
                    "E_UNBOUND_REPOSITORY_FACT",
                    relative,
                    "PORTABLE_UNBOUND candidate guesses: "
                    + ", ".join(guessed_fields),
                )
            )
        return

    readiness_fields = (
        "feature_selection_decision_id",
        "feature_contract_identity",
        "target_binding_id",
        "repository_identity",
        "branch",
        "HEAD",
        "baseline",
        "allowed_paths",
        "forbidden_paths",
        "allowed_operations",
        "forbidden_operations",
        "acceptance_matrix",
        "negative_test_matrix",
        "validation_commands",
        "expected_results",
        "recovery",
        "stop_conditions",
        "evidence_requirements",
    )
    for key in readiness_fields:
        if not nonempty_field(text, key):
            findings.append(
                Finding("E_TASK_READINESS_FIELD", relative, f"{key} is incomplete")
            )
    if scalar(text, "feature_contract_human_decision") != "ACCEPT":
        findings.append(
            Finding(
                "E_TASK_CONTRACT_NOT_ACCEPTED",
                relative,
                "exact accepted Feature Contract not established",
            )
        )
    if scalar(text, "material_adrs_resolved") != "true":
        findings.append(
            Finding(
                "E_TASK_ADR_UNRESOLVED",
                relative,
                "material ADR resolution not established",
            )
        )
    if scalar(text, "target_binding_current") != "true":
        findings.append(
            Finding(
                "E_TASK_BINDING_STALE",
                relative,
                "target binding is incomplete or not current",
            )
        )
    if scalar(text, "human_task_decision") != "ACCEPT":
        findings.append(
            Finding(
                "E_TASK_HUMAN_DECISION",
                relative,
                "exact human Task decision is absent",
            )
        )
    if scalar(text, "assigned_Risk_Profile") in {None, "", "UNASSIGNED"}:
        findings.append(
            Finding(
                "E_TASK_RISK_UNASSIGNED",
                relative,
                "Risk Profile remains unassigned",
            )
        )
    if scalar(text, "implementation_authorization") != "NONE":
        findings.append(
            Finding(
                "E_SELF_AUTHORIZED_TASK",
                relative,
                "authorization must remain separate from Task Brief",
            )
        )


def validate_package(
    package_root: Path, write: bool, task_brief: Optional[Path]
) -> Tuple[List[Finding], Optional[str], int, Optional[str], Optional[str], int]:
    findings: List[Finding] = []
    package_root = package_root.resolve()
    if not package_root.is_dir():
        return (
            [Finding("E_PACKAGE_ROOT", package_root.as_posix(), "not a directory")],
            None,
            0,
            None,
            None,
            0,
        )

    for relative in sorted(REQUIRED_FILES):
        if not (package_root / relative).is_file():
            findings.append(Finding("E_REQUIRED_FILE", relative, "not found"))

    check_root_payload(package_root, findings)

    paths = load_registry(package_root, findings)
    if write and paths and not any(
        item.code.startswith("E_REGISTRY") or item.code.startswith("E_ACTIVE")
        for item in findings
    ):
        write_manifest(package_root, paths)

    aggregate = check_manifest(package_root, paths, findings) if paths else None
    composite_aggregate, role_bound_aggregate, composite_path_count = (
        check_composite_manifest(package_root, paths, findings)
        if paths
        else (None, None, 0)
    )

    state_registry = package_root / STATE_REGISTRY_PATH
    registry_text = (
        state_registry.read_text(encoding="utf-8") if state_registry.exists() else ""
    )
    superseded_paths = extract_superseded_paths(registry_text)

    artifact_ids: Dict[str, str] = {}
    for relative in paths:
        path = package_root / relative
        if not path.is_file():
            continue
        text = read_utf8(path, findings, relative)
        if text is None:
            continue
        frontmatter: Dict[str, str] = {}
        if relative.endswith(".md") and not relative.startswith("root/"):
            frontmatter = parse_frontmatter(text, findings, relative)
            check_markdown(package_root, relative, text, superseded_paths, findings)
        check_status_and_authority(relative, text, frontmatter, findings)
        artifact_id = frontmatter.get("artifact_id")
        if artifact_id:
            if artifact_id in artifact_ids:
                findings.append(
                    Finding(
                        "E_DUPLICATE_CANONICAL_ID",
                        relative,
                        f"artifact_id {artifact_id} also in {artifact_ids[artifact_id]}",
                    )
                )
            artifact_ids[artifact_id] = relative

    for relative, required_strings in TEMPLATE_REQUIREMENTS.items():
        path = package_root / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for required in sorted(required_strings):
            if required not in text:
                findings.append(
                    Finding(
                        "E_TEMPLATE_GATE",
                        relative,
                        f"required field/contract missing: {required}",
                    )
                )

    portability = package_root / (
        "development-package-state/PORTABILITY_DIRECTION_2026-07-31.md"
    )
    if portability.exists():
        text = portability.read_text(encoding="utf-8")
        if "required_external_operational_files: []" not in text:
            findings.append(
                Finding(
                    "E_EXTERNAL_OPERATIONAL_DEPENDENCY",
                    portability.relative_to(package_root).as_posix(),
                    "external operational files are not empty",
                )
            )

    current = package_root / "development-package-state/CURRENT.md"
    if current.exists():
        current_text = current.read_text(encoding="utf-8")
        for required in (
            "latest_human_accepted_revision: DRAFT-R16",
            "latest_acceptance_sidecar: AOS-3/development-package-state/R16_ACCEPTANCE_AND_DELIVERY.md",
            "accepted_composite_sha256: 5ac5b606960fc4f533cdfe7ca3bc95c879c62a3d8f95d1bc10270a469a286a61",
            "current_candidate_revision: DRAFT-R17",
            "working_baseline_revision: DRAFT-R16",
            "working_baseline_disposition: USE_AS_EXACT_HUMAN_ACCEPTED_BASELINE",
            "previous_independent_validation:",
            "revision: DRAFT-R16",
            "technical_result: PASS",
            "candidate_internal_state_role: HISTORICAL_SNAPSHOT",
            "portable_state: PORTABLE_UNBOUND",
            "active_subject_registry: AOS-3/ACTIVE_SUBJECTS_R17.txt",
            "root_payload_manifest: AOS-3/ROOT_FILES_MANIFEST.yaml",
            "root_payload_target_class: GREENFIELD_OR_EMPTY_ROOT",
            "root_materialization_authorization: SEPARATE_HUMAN_DECISION_REQUIRED",
            "DRAFT_R17_independent_validation: NOT_RUN",
            "DRAFT_R17_human_acceptance: NOT_RUN",
            "human_first_vertical_slice_selection: NOT_RUN",
            "reason: HUMAN_WORKSPACE_VERIFICATION_REQUIRED",
            "reason: HUMAN_FEATURE_SELECTION_NOT_RUN",
            "readiness_state: BLOCKED_BY_HUMAN_GATE",
            "reason: ACCEPTED_FEATURE_CONTRACT_REQUIRED",
            "one_next_action: RUN_SEPARATE_READ_ONLY_INDEPENDENT_VALIDATE_OVER_FROZEN_DRAFT_R17",
        ):
            if required not in current_text:
                findings.append(
                    Finding(
                        "E_CURRENT_STATE",
                        current.relative_to(package_root).as_posix(),
                        f"missing {required}",
                    )
                )

    handoff = package_root / "development-package/07_Implementation_Handoff.md"
    root_readme = package_root / "root/README.md"
    agents = package_root / "AGENTS.md"
    ordered_tokens = (
        "human first vertical slice selection",
        "→ feature-specific Product/Feature Contract draft",
        "→ human acceptance of exact Feature Contract",
        "→ minimum Portable Task Candidate",
        "→ exact target repository assignment",
        "→ read-only target preflight and Target Repository Binding",
        "→ Target-Bound Task Brief",
        "→ human Task decision",
        "→ human-assigned Risk Profile",
        "→ separate Execution Authorization",
        "→ one bounded implementation stage",
    )
    for path in (agents, handoff):
        if not path.is_file():
            continue
        active_document = active_text(
            path.read_text(encoding="utf-8"),
            findings,
            path.relative_to(package_root).as_posix(),
        )
        has_valid_sequence = any(
            contains_exact_contiguous_sequence(block, ordered_tokens)
            for block in fenced_blocks(active_document)
        )
        if not has_valid_sequence:
            findings.append(
                Finding(
                    "E_PRODUCT_TARGET_ORDER",
                    path.relative_to(package_root).as_posix(),
                    "product-to-target sequence is missing or out of order",
                )
            )
    if root_readme.is_file():
        text = root_readme.read_text(encoding="utf-8")
        slice_position = text.find("first vertical slice")
        preflight_position = text.find("read-only target preflight")
        if slice_position < 0 or preflight_position < 0 or slice_position > preflight_position:
            findings.append(
                Finding(
                    "E_PRODUCT_TARGET_ORDER",
                    root_readme.relative_to(package_root).as_posix(),
                    "slice selection must precede target preflight",
                )
            )

    acceptance_sidecar = (
        package_root / "development-package-state/R17_ACCEPTANCE_AND_DELIVERY.md"
    )
    if acceptance_sidecar.exists():
        findings.append(
            Finding(
                "E_PREMATURE_R17_ACCEPTANCE",
                acceptance_sidecar.relative_to(package_root).as_posix(),
                "R17 acceptance sidecar is forbidden before human decision",
            )
        )

    if task_brief is not None:
        check_task_brief(task_brief.resolve(), findings)

    return (
        findings,
        aggregate,
        len(paths),
        composite_aggregate,
        role_bound_aggregate,
        composite_path_count,
    )


def print_result(
    package_root: Path,
    findings: Iterable[Finding],
    aggregate: Optional[str],
    path_count: int,
    composite_aggregate: Optional[str],
    role_bound_aggregate: Optional[str],
    composite_path_count: int,
) -> int:
    findings = list(findings)
    print(f"package_root: {package_root.resolve().as_posix()}")
    print(f"active_path_count: {path_count}")
    print(f"active_content_aggregate_sha256: {aggregate or 'NOT_AVAILABLE'}")
    print(f"composite_path_count: {composite_path_count}")
    print(
        "composite_content_aggregate_sha256: "
        f"{composite_aggregate or 'NOT_AVAILABLE'}"
    )
    print(
        f"role_bound_aggregate_sha256: {role_bound_aggregate or 'NOT_AVAILABLE'}"
    )
    print(f"technical_result: {'FAIL' if findings else 'PASS'}")
    print("evidence_class: AUTHOR_SELF_CHECK")
    print("independence: NONE")
    print("human_acceptance_effect: NONE")
    print("independent_validation_effect: NONE")
    if findings:
        print("findings:")
        for finding in findings:
            print(f"  - code: {finding.code}")
            print(f"    path: {finding.path}")
            print(f"    detail: {finding.detail}")
        return 1
    print("findings: []")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--task-brief", type=Path)
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="write the non-recursive active-content manifest before checking it",
    )
    args = parser.parse_args(argv)
    (
        findings,
        aggregate,
        path_count,
        composite_aggregate,
        role_bound_aggregate,
        composite_path_count,
    ) = validate_package(
        args.package_root, args.write_manifest, args.task_brief
    )
    return print_result(
        args.package_root,
        findings,
        aggregate,
        path_count,
        composite_aggregate,
        role_bound_aggregate,
        composite_path_count,
    )


if __name__ == "__main__":
    sys.exit(main())
