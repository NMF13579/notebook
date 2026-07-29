#!/usr/bin/env python3
"""Materialize AOS feature documents from the bundled deterministic tar.xz archive."""
from __future__ import annotations

import base64
import hashlib
import io
import pathlib
import sys
import tarfile

ROOT = pathlib.Path(__file__).resolve().parent
ARCHIVE_B64 = ROOT / "archive.b64"
TARGET = ROOT / "documents"
EXPECTED_SHA256 = "0d85639e458366cd4290c3fa545a7573fc726c5e05b51fee30bc4a0f83ba2373"


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
    compressed = base64.b64decode(ARCHIVE_B64.read_bytes(), validate=False)
    actual = hashlib.sha256(compressed).hexdigest()
    if actual != EXPECTED_SHA256:
        print(f"Checksum mismatch: expected {EXPECTED_SHA256}, got {actual}", file=sys.stderr)
        return 2

    TARGET.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(compressed), mode="r:xz") as tf:
        tf.extractall(TARGET, members=safe_members(tf), filter="data")

    files = [p for p in TARGET.rglob("*") if p.is_file()]
    print(f"Materialized {len(files)} files into {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
