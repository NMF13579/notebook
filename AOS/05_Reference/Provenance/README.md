# AOS Migration Provenance

- authority: NONE
- historical_only: true

This directory contains migration and reconstruction evidence. It is not an active Source of Truth and does not define architecture, product scope, lifecycle, approval, Risk Profile, or execution authority.

Active ownership is defined by [AOS/MANIFEST.md](../../MANIFEST.md). Migration provenance is defined by the three registers in this directory. P2 simplified MANIFEST, and stable provenance anchors now exist.

`Legacy_Tree/` now exists. It has authority: NONE and is historical_only: true; it is not canonical navigation. All legacy sources remain retained there. `00_INDEX.md` received exactly two bounded relative-link repairs. Deletion remains unauthorized, and P4 validation is required.

## Registers

- [PROVENANCE_REGISTER.md](PROVENANCE_REGISTER.md) — the 79 source-to-target mappings and supplementary legacy artifact inventory.
- [TRANSFORMATION_REGISTER.md](TRANSFORMATION_REGISTER.md) — the 30 authored transformations.
- [LEGACY_METADATA_REGISTER.md](LEGACY_METADATA_REGISTER.md) — historical evidence for all 39 distributed META files.

## Safety boundary

- No deletion is authorized.
- Register validation PASS does not authorize cleanup.
- MOVE ≠ DELETE.
- P4 validation is required before any deletion decision.
- Commit ≠ push ≠ merge.
- Historical material has authority NONE.
