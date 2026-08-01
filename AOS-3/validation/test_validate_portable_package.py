#!/usr/bin/env python3
"""Author tests for the DRAFT-R17 portable-package validator."""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = PACKAGE_ROOT / "validation" / "validate_portable_package.py"
FIXTURES = PACKAGE_ROOT / "validation" / "fixtures"
REGISTRY = Path("ACTIVE_SUBJECTS_R17.txt")
MANIFEST = Path("development-package-state/R17_ACTIVE_CONTENT_MANIFEST.sha256")
FULL_CANDIDATE_PATHS = Path(
    "development-package-state/R17_FULL_CANDIDATE_PATHS.txt"
)
FULL_CANDIDATE_MANIFEST = Path(
    "development-package-state/R17_FULL_CANDIDATE_MANIFEST.sha256"
)
COMPOSITE_MANIFEST = Path(
    "development-package-state/R17_COMPOSITE_CONTENT_MANIFEST.sha256"
)
ROOT_MANIFEST = Path("ROOT_FILES_MANIFEST.yaml")
ROOT_PAYLOAD_FILES = {
    "AGENTS.md": "AGENTS.md",
    "README.md": "README.md",
    ".gitignore": ".gitignore",
    ".agents/rules/aos.md": ".agents/rules/aos.md",
}
EXPECTED_R17_CHANGED_PATHS = {
    "ACTIVE_SUBJECTS_R17.txt",
    "AGENTS.md",
    "ROOT_FILES_MANIFEST.yaml",
    "development-package-state/CURRENT.md",
    "development-package-state/R17_ACTIVE_CONTENT_MANIFEST.sha256",
    "development-package-state/R17_AUTHOR_EXECUTION_REPORT.md",
    "development-package-state/R17_FULL_CANDIDATE_MANIFEST.sha256",
    "development-package-state/R17_FULL_CANDIDATE_PATHS.txt",
    "development-package-state/SUBJECT_STATE_REGISTRY_R17.md",
    "development-package/00_Control_and_Source_Precedence.md",
    "development-package/07_Implementation_Handoff.md",
    "root/README.md",
    "validation/test_validate_portable_package.py",
    "validation/validate_portable_package.py",
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
PRODUCT_TARGET_SEQUENCE = (
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


def run_validator(package_root: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "python3",
            str(VALIDATOR),
            "--package-root",
            str(package_root),
            *extra_args,
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def fenced_sequence(lines: tuple[str, ...]) -> str:
    return "```text\n" + "\n".join(lines) + "\n```"


PRODUCT_TARGET_BLOCK = fenced_sequence(PRODUCT_TARGET_SEQUENCE)


def write_manifest(
    package_root: Path,
    manifest: Path,
    paths: list[str],
    excluded_paths: set[str] | None = None,
) -> None:
    excluded = excluded_paths or set()
    records = []
    for relative in sorted(paths, key=lambda value: value.encode("utf-8")):
        if relative in excluded:
            continue
        digest = hashlib.sha256((package_root / relative).read_bytes()).hexdigest()
        records.append(f"{digest}  {relative}\n")
    (package_root / manifest).write_bytes("".join(records).encode("utf-8"))


def regenerate_manifest(package_root: Path) -> None:
    paths = [
        line
        for line in (package_root / REGISTRY).read_text(encoding="utf-8").splitlines()
        if line
    ]
    write_manifest(package_root, MANIFEST, paths)


def regenerate_full_candidate_manifest(package_root: Path) -> None:
    paths = [
        line
        for line in (package_root / FULL_CANDIDATE_PATHS)
        .read_text(encoding="utf-8")
        .splitlines()
        if line
    ]
    write_manifest(
        package_root,
        FULL_CANDIDATE_MANIFEST,
        paths,
        {FULL_CANDIDATE_MANIFEST.as_posix()},
    )


def regenerate_composite_manifest(package_root: Path) -> None:
    records = (package_root / COMPOSITE_MANIFEST).read_text(encoding="utf-8")
    paths = []
    for line in records.splitlines():
        match = re.fullmatch(r"[0-9a-f]{64}  (.+)", line)
        if match is None:
            raise AssertionError(f"invalid composite manifest record: {line!r}")
        paths.append(match.group(1))
    write_manifest(package_root, COMPOSITE_MANIFEST, paths)


def regenerate_candidate_identity(package_root: Path) -> None:
    regenerate_manifest(package_root)
    regenerate_full_candidate_manifest(package_root)
    regenerate_composite_manifest(package_root)


def snapshot_payload(package_root: Path) -> dict[str, str]:
    return {
        relative: hashlib.sha256(
            (package_root / "root" / relative).read_bytes()
        ).hexdigest()
        for relative in ROOT_PAYLOAD_FILES
    }


def simulate_root_materialization(
    package_root: Path, target_root: Path, fail_after_copies: int | None = None
) -> dict[str, object]:
    """Exercise the manifest's preflight/copy/rollback contract in temp roots."""

    source_root = package_root / "root"
    target_root.mkdir(parents=True, exist_ok=True)
    preexisting_files = {
        relative: (target_root / target).read_bytes()
        for relative, target in ROOT_PAYLOAD_FILES.items()
        if (target_root / target).is_file()
    }
    conflicts: list[str] = []
    for source, target in ROOT_PAYLOAD_FILES.items():
        source_path = source_root / source
        target_path = target_root / target
        parent_symlink = False
        parent = target_path.parent
        while True:
            parent_symlink = parent_symlink or parent.is_symlink()
            if parent == target_root:
                break
            parent = parent.parent
        if target_path.is_symlink() or parent_symlink:
            conflicts.append(target)
        elif target_path.exists() and (
            not target_path.is_file()
            or target_path.read_bytes() != source_path.read_bytes()
        ):
            conflicts.append(target)
    if conflicts:
        adoption = any(path in {"README.md", ".gitignore"} for path in conflicts)
        return {
            "technical_result": "BLOCKED",
            "reason_code": (
                "EXISTING_REPOSITORY_ADOPTION_DECISION_REQUIRED"
                if adoption
                else "ROOT_FILE_CONFLICT"
            ),
            "target_mutations": 0,
            "created_target_paths": [],
            "preexisting_paths_modified": [],
        }

    created_files: list[Path] = []
    created_dirs: list[Path] = []
    copies = 0
    try:
        for source, target in ROOT_PAYLOAD_FILES.items():
            source_path = source_root / source
            target_path = target_root / target
            if target_path.exists():
                continue
            missing_dirs = []
            parent = target_path.parent
            while parent != target_root and not parent.exists():
                missing_dirs.append(parent)
                parent = parent.parent
            for directory in reversed(missing_dirs):
                directory.mkdir()
                created_dirs.append(directory)
            target_path.write_bytes(source_path.read_bytes())
            created_files.append(target_path)
            copies += 1
            if fail_after_copies is not None and copies == fail_after_copies:
                raise RuntimeError("SIMULATED_POST_COPY_VALIDATION_FAILURE")
        for source, target in ROOT_PAYLOAD_FILES.items():
            if (target_root / target).read_bytes() != (source_root / source).read_bytes():
                raise RuntimeError("POST_COPY_RAW_BYTES_MISMATCH")
    except Exception as error:  # controlled rollback path under test
        for path in reversed(created_files):
            path.unlink()
        for directory in sorted(created_dirs, key=lambda item: len(item.parts), reverse=True):
            if directory.exists():
                directory.rmdir()
        final_preexisting = {
            relative: (target_root / ROOT_PAYLOAD_FILES[relative]).read_bytes()
            for relative in preexisting_files
        }
        return {
            "technical_result": "FAIL",
            "reason_code": str(error),
            "rollback_required": True,
            "created_target_paths": [],
            "preexisting_paths_modified": [
                relative
                for relative, payload in preexisting_files.items()
                if final_preexisting.get(relative) != payload
            ],
        }
    return {
        "technical_result": "PASS",
        "action": "NOOP" if copies == 0 else "COPY",
        "target_mutations": copies,
        "created_target_paths": [
            path.relative_to(target_root).as_posix() for path in created_files
        ],
        "preexisting_paths_modified": [],
    }


class PortablePackageValidatorTests(unittest.TestCase):
    def run_product_target_variant(
        self, replacement_block: str, extra_prose: str = ""
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(
            prefix="aos3-r17-product-target-order-"
        ) as raw_temp:
            temp_root = Path(raw_temp) / "AOS-3"
            shutil.copytree(PACKAGE_ROOT, temp_root)
            agents_path = temp_root / "AGENTS.md"
            original = agents_path.read_text(encoding="utf-8")
            self.assertIn(PRODUCT_TARGET_BLOCK, original)
            changed = original.replace(
                PRODUCT_TARGET_BLOCK, replacement_block, 1
            )
            if extra_prose:
                changed += f"\n{extra_prose}\n"
            agents_path.write_bytes(changed.encode("utf-8"))
            regenerate_candidate_identity(temp_root)
            return run_validator(temp_root)

    def test_product_target_order_ignores_misleading_prose_outside_fence(
        self,
    ) -> None:
        misleading_prose = "\n".join(reversed(PRODUCT_TARGET_SEQUENCE))
        result = self.run_product_target_variant(
            PRODUCT_TARGET_BLOCK, misleading_prose
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("E_PRODUCT_TARGET_ORDER", result.stdout)

    def test_product_target_order_rejects_non_contiguous_active_sequences(
        self,
    ) -> None:
        missing = PRODUCT_TARGET_SEQUENCE[:5] + PRODUCT_TARGET_SEQUENCE[6:]
        reordered = list(PRODUCT_TARGET_SEQUENCE)
        reordered[4], reordered[5] = reordered[5], reordered[4]
        split = (
            fenced_sequence(PRODUCT_TARGET_SEQUENCE[:5])
            + "\n\n"
            + fenced_sequence(PRODUCT_TARGET_SEQUENCE[5:])
        )
        inserted = (
            PRODUCT_TARGET_SEQUENCE[:5]
            + ("→ unauthorized inserted stage",)
            + PRODUCT_TARGET_SEQUENCE[5:]
        )
        prose_only = (
            fenced_sequence(PRODUCT_TARGET_SEQUENCE[:-1])
            + "\n\n"
            + "\n".join(PRODUCT_TARGET_SEQUENCE)
        )
        historical_only = (
            fenced_sequence(PRODUCT_TARGET_SEQUENCE[:-1])
            + "\n\n<!-- HISTORICAL_R14_APPENDIX_BEGIN -->\n"
            + PRODUCT_TARGET_BLOCK
            + "\n<!-- HISTORICAL_R14_APPENDIX_END -->"
        )
        variants = {
            "missing": fenced_sequence(missing),
            "reordered": fenced_sequence(tuple(reordered)),
            "split": split,
            "extra_inserted": fenced_sequence(inserted),
            "prose_only": prose_only,
            "historical_only": historical_only,
        }
        for name, replacement in variants.items():
            with self.subTest(name=name):
                result = self.run_product_target_variant(replacement)
                self.assertNotEqual(
                    result.returncode, 0, result.stdout + result.stderr
                )
                self.assertIn("E_PRODUCT_TARGET_ORDER", result.stdout)
                self.assertIn("path: AGENTS.md", result.stdout)
                self.assertNotIn("E_MANIFEST_DIGEST", result.stdout)
                self.assertNotIn("E_COMPOSITE_DIGEST", result.stdout)

    def test_r17_lifecycle_and_product_before_target_order(self) -> None:
        current = (
            PACKAGE_ROOT / "development-package-state" / "CURRENT.md"
        ).read_text(encoding="utf-8")
        handoff = (
            PACKAGE_ROOT / "development-package" / "07_Implementation_Handoff.md"
        ).read_text(encoding="utf-8")
        self.assertIn("latest_human_accepted_revision: DRAFT-R16", current)
        self.assertIn("current_candidate_revision: DRAFT-R17", current)
        self.assertIn("DRAFT_R17_independent_validation: NOT_RUN", current)
        self.assertIn(
            "one_next_action: "
            "RUN_SEPARATE_READ_ONLY_INDEPENDENT_VALIDATE_OVER_FROZEN_DRAFT_R17",
            current,
        )
        self.assertLess(
            handoff.index("Obtain exact human first vertical slice selection."),
            handoff.index("Run read-only target repository preflight."),
        )

    def test_r17_validator_reports_composite_identity(self) -> None:
        result = run_validator(PACKAGE_ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("active_path_count: 20", result.stdout)
        self.assertIn("composite_path_count: 40", result.stdout)
        self.assertRegex(
            result.stdout,
            r"composite_content_aggregate_sha256: [0-9a-f]{64}",
        )
        self.assertRegex(result.stdout, r"role_bound_aggregate_sha256: [0-9a-f]{64}")

    maxDiff = None

    def test_valid_package_passes(self) -> None:
        result = run_validator(PACKAGE_ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("technical_result: PASS", result.stdout)

    def test_arbitrary_target_identity_is_deferred(self) -> None:
        text = (
            PACKAGE_ROOT
            / "development-package-state"
            / "PORTABILITY_DIRECTION_2026-07-31.md"
        ).read_text(encoding="utf-8")
        self.assertIn("required_source_repository_name: NONE", text)
        self.assertIn("required_source_branch: NONE", text)
        self.assertIn("required_source_commit: NONE", text)
        self.assertIn(
            "target_repository_identity: OBSERVED_AT_TARGET_PREFLIGHT", text
        )

    def test_no_selected_feature_is_expected_gate(self) -> None:
        text = (
            PACKAGE_ROOT / "development-package-state" / "CURRENT.md"
        ).read_text(encoding="utf-8")
        self.assertIn("human_feature_selection:", text)
        self.assertIn("technical_result: NOT_RUN", text)
        self.assertIn("portable_package_candidate:", text)
        self.assertIn("status: DRAFT", text)
        self.assertIn("readiness_state: BLOCKED_BY_HUMAN_GATE", text)
        self.assertIn("reason: ACCEPTED_FEATURE_CONTRACT_REQUIRED", text)

    def test_portable_unbound_is_not_failure(self) -> None:
        text = (
            PACKAGE_ROOT / "development-package-state" / "CURRENT.md"
        ).read_text(encoding="utf-8")
        self.assertIn("portable_state: PORTABLE_UNBOUND", text)
        result = run_validator(PACKAGE_ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_stale_candidate_metadata_is_historical(self) -> None:
        text = (
            PACKAGE_ROOT / "development-package-state" / "CURRENT.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "current_lifecycle_state_owner: "
            "AOS-3/development-package-state/CURRENT.md",
            text,
        )
        self.assertIn("candidate_internal_state_role: HISTORICAL_SNAPSHOT", text)
        self.assertIn("latest_human_accepted_revision: DRAFT-R16", text)
        self.assertIn("current_candidate_revision: DRAFT-R17", text)

    def test_stored_pass_does_not_grant_acceptance_or_authority(self) -> None:
        text = (
            PACKAGE_ROOT / "development-package-state" / "CURRENT.md"
        ).read_text(encoding="utf-8")
        self.assertIn("revision: DRAFT-R16", text)
        self.assertIn("technical_result: PASS", text)
        self.assertIn("DRAFT_R17_independent_validation: NOT_RUN", text)
        self.assertIn("DRAFT_R17_human_acceptance: NOT_RUN", text)
        self.assertIn("implementation_authorization: NONE", text)
        self.assertIn("git_authorization: NONE", text)

    def test_task_template_is_not_executable(self) -> None:
        portable = (
            PACKAGE_ROOT / "templates" / "PORTABLE_TASK_CANDIDATE.template.md"
        ).read_text(encoding="utf-8")
        brief = (
            PACKAGE_ROOT / "templates" / "TASK_BRIEF.template.md"
        ).read_text(encoding="utf-8")
        self.assertIn("binding_state: PORTABLE_UNBOUND", portable)
        self.assertIn(
            "task_candidate_role: DRAFT_PORTABLE_CANDIDATE", portable
        )
        self.assertIn("human_acceptance: NOT_RUN", portable)
        self.assertIn("human_task_decision: NOT_RUN", brief)
        self.assertIn("implementation_authorization: NONE", portable)
        self.assertIn("implementation_authorization: NONE", brief)

    def check_active_fixture(self, fixture_name: str, expected_code: str) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-validator-test-") as raw_temp:
            temp_root = Path(raw_temp) / "AOS-3"
            shutil.copytree(PACKAGE_ROOT, temp_root)
            injected = Path("validation/fixture-active-subject.md")
            shutil.copyfile(FIXTURES / fixture_name, temp_root / injected)
            with (temp_root / REGISTRY).open("a", encoding="utf-8", newline="\n") as stream:
                stream.write(f"{injected.as_posix()}\n")
            regenerate_manifest(temp_root)
            result = run_validator(temp_root)
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(expected_code, result.stdout)

    def test_status_axis_collision_is_rejected(self) -> None:
        self.check_active_fixture("status_axis_collision.md", "E_STATUS_AXIS_COLLISION")

    def test_external_mandatory_link_is_rejected(self) -> None:
        self.check_active_fixture(
            "external_mandatory_link.md", "E_EXTERNAL_MANDATORY_LINK"
        )

    def test_active_absolute_path_is_rejected(self) -> None:
        self.check_active_fixture("active_absolute_path.md", "E_ACTIVE_ABSOLUTE_PATH")

    def test_modified_subject_cannot_inherit_acceptance_without_proof(self) -> None:
        self.check_active_fixture(
            "modified_accepted_subject.md", "E_ACCEPTANCE_INHERITANCE"
        )

    def test_self_authorized_task_is_rejected(self) -> None:
        result = run_validator(
            PACKAGE_ROOT,
            "--task-brief",
            str(FIXTURES / "self_authorized_task.md"),
        )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("E_SELF_AUTHORIZED_TASK", result.stdout)

    def test_unbound_repository_specific_task_is_rejected(self) -> None:
        result = run_validator(
            PACKAGE_ROOT,
            "--task-brief",
            str(FIXTURES / "unbound_repository_specific_task.md"),
        )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("E_UNBOUND_REPOSITORY_FACT", result.stdout)


class RootPayloadContractTests(unittest.TestCase):
    maxDiff = None

    def test_exact_root_payload_tree(self) -> None:
        files = {
            path.relative_to(PACKAGE_ROOT / "root").as_posix()
            for path in (PACKAGE_ROOT / "root").rglob("*")
            if path.is_file() or path.is_symlink()
        }
        self.assertEqual(files, set(ROOT_PAYLOAD_FILES))

    def test_greenfield_materialization_preserves_source_and_routes(self) -> None:
        before = snapshot_payload(PACKAGE_ROOT)
        with tempfile.TemporaryDirectory(prefix="aos3-r16-greenfield-") as raw_temp:
            target = Path(raw_temp) / "target"
            shutil.copytree(PACKAGE_ROOT, target / "AOS-3")
            result = simulate_root_materialization(target / "AOS-3", target)
            self.assertEqual(result["technical_result"], "PASS", result)
            self.assertEqual(result["target_mutations"], 4, result)
            for source, destination in ROOT_PAYLOAD_FILES.items():
                self.assertEqual(
                    (target / destination).read_bytes(),
                    (target / "AOS-3" / "root" / source).read_bytes(),
                )
            agents = (target / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("AOS-3/AGENTS.md", agents)
            self.assertIn("AOS-3/development-package-state/CURRENT.md", agents)
            readme = (target / "README.md").read_text(encoding="utf-8")
            for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", readme):
                self.assertTrue((target / link).exists(), link)
            rule_path = target / ".agents" / "rules" / "aos.md"
            rule = rule_path.read_text(encoding="utf-8")
            self.assertLess(len(rule), 12_000)
            for reference in re.findall(r"(?m)^@(\S+)$", rule):
                self.assertTrue((rule_path.parent / reference).resolve().is_file())
            self.assertEqual(snapshot_payload(target / "AOS-3"), before)
        self.assertEqual(snapshot_payload(PACKAGE_ROOT), before)

    def test_identical_target_is_noop(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-identical-") as raw_temp:
            target = Path(raw_temp)
            for source, destination in ROOT_PAYLOAD_FILES.items():
                path = target / destination
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((PACKAGE_ROOT / "root" / source).read_bytes())
            before = {
                destination: (target / destination).read_bytes()
                for destination in ROOT_PAYLOAD_FILES.values()
            }
            result = simulate_root_materialization(PACKAGE_ROOT, target)
            self.assertEqual(result["technical_result"], "PASS", result)
            self.assertEqual(result["action"], "NOOP", result)
            self.assertEqual(result["target_mutations"], 0, result)
            self.assertEqual(
                before,
                {
                    destination: (target / destination).read_bytes()
                    for destination in ROOT_PAYLOAD_FILES.values()
                },
            )

    def test_conflict_blocks_before_write(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-conflict-") as raw_temp:
            target = Path(raw_temp)
            conflict = target / ".agents" / "rules" / "aos.md"
            conflict.parent.mkdir(parents=True)
            conflict.write_text("different\n", encoding="utf-8")
            result = simulate_root_materialization(PACKAGE_ROOT, target)
            self.assertEqual(result["technical_result"], "BLOCKED", result)
            self.assertEqual(result["reason_code"], "ROOT_FILE_CONFLICT", result)
            self.assertEqual(result["target_mutations"], 0, result)
            self.assertEqual(result["created_target_paths"], [], result)
            self.assertEqual(result["preexisting_paths_modified"], [], result)
            self.assertEqual(conflict.read_text(encoding="utf-8"), "different\n")

    def test_post_copy_failure_rolls_back_only_current_run(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-rollback-") as raw_temp:
            target = Path(raw_temp)
            existing = target / "README.md"
            existing.write_bytes((PACKAGE_ROOT / "root" / "README.md").read_bytes())
            before = existing.read_bytes()
            source_before = snapshot_payload(PACKAGE_ROOT)
            result = simulate_root_materialization(
                PACKAGE_ROOT, target, fail_after_copies=3
            )
            self.assertEqual(result["technical_result"], "FAIL", result)
            self.assertTrue(result["rollback_required"], result)
            self.assertEqual(result["created_target_paths"], [], result)
            self.assertEqual(result["preexisting_paths_modified"], [], result)
            self.assertEqual(existing.read_bytes(), before)
            self.assertFalse((target / "AGENTS.md").exists())
            self.assertFalse((target / ".gitignore").exists())
            self.assertFalse((target / ".agents").exists())
            self.assertEqual(snapshot_payload(PACKAGE_ROOT), source_before)

    def test_existing_repository_requires_separate_adoption_decision(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-existing-") as raw_temp:
            target = Path(raw_temp)
            (target / "README.md").write_text("existing repository\n", encoding="utf-8")
            result = simulate_root_materialization(PACKAGE_ROOT, target)
            self.assertEqual(result["technical_result"], "BLOCKED", result)
            self.assertEqual(
                result["reason_code"],
                "EXISTING_REPOSITORY_ADOPTION_DECISION_REQUIRED",
                result,
            )
            self.assertEqual(result["target_mutations"], 0, result)

    def check_modified_package(self, relative: str, content: str, code: str) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-contract-") as raw_temp:
            temp_root = Path(raw_temp) / "AOS-3"
            shutil.copytree(PACKAGE_ROOT, temp_root)
            (temp_root / relative).write_bytes(content.encode("utf-8"))
            regenerate_manifest(temp_root)
            result = run_validator(temp_root)
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(code, result.stdout)

    def test_extra_payload_file_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="aos3-r16-extra-") as raw_temp:
            temp_root = Path(raw_temp) / "AOS-3"
            shutil.copytree(PACKAGE_ROOT, temp_root)
            (temp_root / "root" / "GEMINI.md").write_text("extra\n", encoding="utf-8")
            result = run_validator(temp_root)
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("E_ROOT_PAYLOAD_FILE_SET", result.stdout)

    def test_gitignore_broad_rule_is_rejected(self) -> None:
        original = (PACKAGE_ROOT / "root" / ".gitignore").read_text(encoding="utf-8")
        self.check_modified_package(
            "root/.gitignore", original + "*.md\n", "E_ROOT_GITIGNORE_BROAD_RULE"
        )

    def test_manifest_duplicate_target_is_rejected(self) -> None:
        original = (PACKAGE_ROOT / ROOT_MANIFEST).read_text(encoding="utf-8")
        changed = original.replace(
            "target: README.md\n    role: HUMAN_ENTRYPOINT",
            "target: AGENTS.md\n    role: HUMAN_ENTRYPOINT",
        )
        self.check_modified_package(
            ROOT_MANIFEST.as_posix(), changed, "E_ROOT_MANIFEST_TARGET_DUPLICATE"
        )

    def test_manifest_atomic_preflight_change_is_rejected(self) -> None:
        original = (PACKAGE_ROOT / ROOT_MANIFEST).read_text(encoding="utf-8")
        changed = original.replace(
            "writes_before_full_preflight: FORBIDDEN",
            "writes_before_full_preflight: ALLOWED",
        )
        self.check_modified_package(
            ROOT_MANIFEST.as_posix(), changed, "E_ROOT_MANIFEST_ATOMICITY"
        )

    def test_antigravity_activation_promotion_is_rejected(self) -> None:
        original = (PACKAGE_ROOT / ROOT_MANIFEST).read_text(encoding="utf-8")
        changed = original.replace(
            "technical_result: NOT_RUN\n      reason: HUMAN_WORKSPACE_VERIFICATION_REQUIRED",
            "technical_result: PASS\n      reason: AUTOMATICALLY_CONFIRMED",
        )
        self.check_modified_package(
            ROOT_MANIFEST.as_posix(), changed, "E_ANTIGRAVITY_ACTIVATION"
        )

    def test_r16_identity_evidence_is_preserved(self) -> None:
        for relative, expected in R16_EVIDENCE_SHA256.items():
            self.assertEqual(
                hashlib.sha256((PACKAGE_ROOT / relative).read_bytes()).hexdigest(),
                expected,
                relative,
            )

    def test_adapters_are_thin_and_do_not_promote_authority(self) -> None:
        agents = (PACKAGE_ROOT / "root" / "AGENTS.md").read_text(encoding="utf-8")
        readme = (PACKAGE_ROOT / "root" / "README.md").read_text(encoding="utf-8")
        rule = (
            PACKAGE_ROOT / "root" / ".agents" / "rules" / "aos.md"
        ).read_text(encoding="utf-8")
        manifest = (PACKAGE_ROOT / ROOT_MANIFEST).read_text(encoding="utf-8")
        self.assertLess(len(agents), 12_000)
        self.assertLess(len(readme), 12_000)
        self.assertLess(len(rule), 12_000)
        self.assertIn("canonical instruction owner", agents)
        self.assertIn("Не дублируй и не переопределяй", rule)
        self.assertIn("не является Product Contract", readme)
        combined = "\n".join((agents, readme, rule, manifest))
        self.assertNotIn("implementation_authorization: AUTHORIZED", combined)
        self.assertNotIn("implementation_authorization: GRANTED", combined)
        self.assertNotIn("git_authorization: AUTHORIZED", combined)
        self.assertNotIn("git_authorization: GRANTED", combined)
        self.assertIn("implementation_authorization: NONE", manifest)
        self.assertIn("git_authorization: NONE", manifest)

    def test_full_candidate_identity(self) -> None:
        paths_file = (
            PACKAGE_ROOT
            / "development-package-state"
            / "R17_FULL_CANDIDATE_PATHS.txt"
        )
        manifest_file = (
            PACKAGE_ROOT
            / "development-package-state"
            / "R17_FULL_CANDIDATE_MANIFEST.sha256"
        )
        payload = paths_file.read_bytes()
        self.assertNotIn(b"\r", payload)
        self.assertTrue(payload.endswith(b"\n"))
        paths = payload.decode("utf-8").splitlines()
        self.assertEqual(paths, sorted(paths, key=lambda value: value.encode("utf-8")))
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(set(paths), EXPECTED_R17_CHANGED_PATHS)
        manifest_relative = manifest_file.relative_to(PACKAGE_ROOT).as_posix()
        expected_records = []
        for relative in paths:
            if relative == manifest_relative:
                continue
            digest = hashlib.sha256((PACKAGE_ROOT / relative).read_bytes()).hexdigest()
            expected_records.append(f"{digest}  {relative}\n")
        self.assertEqual(
            manifest_file.read_bytes(), "".join(expected_records).encode("utf-8")
        )


if __name__ == "__main__":
    unittest.main()
