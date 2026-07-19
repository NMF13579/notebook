# AOS Documentation

This directory uses the simplified documentation structure introduced by migration stages M4–M6.

## Canonical structure

- [`00_Core/`](00_Core/README.md) — identity, principles, and the minimum safety floor.
- [`01_Product/`](01_Product/README.md) — product intent, contracts, observable behavior, boundaries, and acceptance criteria.
- [`02_Architecture/`](02_Architecture/README.md) — repository, workspace, agent, and Git foundations.
- [`03_Development/`](03_Development/README.md) — task, execution, validation, recovery, collaboration, and development workflows.
- [`04_Lessons/`](04_Lessons/README.md) — active lessons and anti-patterns, with links to deferred lesson sources.
- [`05_Reference/`](05_Reference/README.md) — deferred Control, Advanced, Research, References, Archive, and reconstruction material.

The central [`MANIFEST.md`](MANIFEST.md) is the only canonical document-location and migration-status manifest. Topic content remains canonical only in the target file assigned to that topic by the manifest.

## Migration boundary

The former `01_Project` through `09_Archive` trees and `00_INDEX.md` are retained unchanged, except for the superseded notice on `00_INDEX.md`, as migration evidence for later destructive review. They are not competing normative sources. Distributed `*_META.yml` files are likewise retained but superseded by `MANIFEST.md`.
