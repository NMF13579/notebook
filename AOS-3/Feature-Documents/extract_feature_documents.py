#!/usr/bin/env python3
"""Materialize AOS DRAFT feature documents from ordered base64 archive parts."""
from __future__ import annotations

import base64
import hashlib
import io
import pathlib
import sys
import tarfile

ROOT = pathlib.Path(__file__).resolve().parent
PARTS_DIR = ROOT / "archive-parts"
TARGET = ROOT / "documents"
EXPECTED_PART_NAMES = [f"archive.part-{index:02d}.b64" for index in range(23)]
EXPECTED_BASE64_SHA256 = "d0315fd273e953e5043ec74b41ad499e5861ad875460e28df1f54c625ec9e73b"
EXPECTED_ARCHIVE_SHA256 = "0d85639e458366cd4290c3fa545a7573fc726c5e05b51fee30bc4a0f83ba2373"
EXPECTED_EXTRACTED_FILE_COUNT = 141


def fail(message: str, code: int = 2) -> int:
    print(message, file=sys.stderr)
    return code


def safe_members(tf: tarfile.TarFile) -> list[tarfile.TarInfo]:
    members = tf.getmembers()
    target_root = TARGET.resolve()
    for member in members:
        candidate = (TARGET / member.name).resolve()
        if target_root not in candidate.parents and candidate != target_root:
            raise RuntimeError(f"Unsafe archive path: {member.name}")
        if member.issym() or member.islnk():
            raise RuntimeError(f"Links are not allowed: {member.name}")
    return members


def main() -> int:
    parts = sorted(PARTS_DIR.glob("archive.part-*.b64"))
    observed_names = [part.name for part in parts]
    if observed_names != EXPECTED_PART_NAMES:
        return fail(
            "Archive part set mismatch:\n"
            f"expected={EXPECTED_PART_NAMES}\n"
            f"observed={observed_names}"
        )

    encoded = b"".join(part.read_bytes() for part in parts)
    encoded_sha256 = hashlib.sha256(encoded).hexdigest()
    if encoded_sha256 != EXPECTED_BASE64_SHA256:
        return fail(
            "Base64 payload checksum mismatch: "
            f"expected {EXPECTED_BASE64_SHA256}, got {encoded_sha256}"
        )

    try:
        compressed = base64.b64decode(encoded, validate=False)
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        return fail(f"Base64 decode failed: {exc}")

    archive_sha256 = hashlib.sha256(compressed).hexdigest()
    if archive_sha256 != EXPECTED_ARCHIVE_SHA256:
        return fail(
            "Archive checksum mismatch: "
            f"expected {EXPECTED_ARCHIVE_SHA256}, got {archive_sha256}"
        )

    if TARGET.exists() and any(TARGET.iterdir()):
        return fail(
            f"Target is not empty: {TARGET}. "
            "Move or remove it explicitly before materializing again."
        )
    TARGET.mkdir(parents=True, exist_ok=True)

    try:
        with tarfile.open(fileobj=io.BytesIO(compressed), mode="r:xz") as tf:
            members = safe_members(tf)
            try:
                tf.extractall(TARGET, members=members, filter="data")
            except TypeError:  # Python versions without the filter argument
                tf.extractall(TARGET, members=members)
    except Exception as exc:
        return fail(f"Archive extraction failed: {exc}")

    files = [path for path in TARGET.rglob("*") if path.is_file()]
    if len(files) != EXPECTED_EXTRACTED_FILE_COUNT:
        return fail(
            "Extracted file count mismatch: "
            f"expected {EXPECTED_EXTRACTED_FILE_COUNT}, got {len(files)}"
        )

    print(f"Materialized {len(files)} files into {TARGET}")
    print(f"Base64 SHA-256: {encoded_sha256}")
    print(f"Archive SHA-256: {archive_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
