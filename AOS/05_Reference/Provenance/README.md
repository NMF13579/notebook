# AOS Migration Provenance

- authority: NONE
- historical_only: true

This directory contains migration and reconstruction evidence. It is not an active Source of Truth and does not define architecture, product scope, lifecycle, approval, Risk Profile, or execution authority.

Active ownership is defined by [AOS/MANIFEST.md](../../MANIFEST.md). Migration provenance is defined by the three registers in this directory. P2 simplified MANIFEST, and stable provenance anchors now exist.

`Legacy_Tree/` has been removed from the current repository tree by separately human-authorized cleanup. It was not canonical navigation. Exact deleted bytes, including the repaired `00_INDEX.md`, remain recoverable from checkpoint commit `346a48076bb998b71b99f20ba74e4e33661273bf`; original historical sources remain recoverable from baseline `b4645d6a6fd6f9e7b2be8c9a85e4c9601a4a68f7`.

## Registers

- [PROVENANCE_REGISTER.md](PROVENANCE_REGISTER.md) — the 79 source-to-target mappings and supplementary legacy artifact inventory.
- [TRANSFORMATION_REGISTER.md](TRANSFORMATION_REGISTER.md) — the 30 authored transformations.
- [LEGACY_METADATA_REGISTER.md](LEGACY_METADATA_REGISTER.md) — historical evidence for all 39 distributed META files.

## Safety boundary

- Provenance registers have authority NONE and are historical and engineering-traceability records only.
- Deletion does not change canonical ownership.
- All 30 transformation validation references remain NOT_PERSISTED; deletion under that evidence boundary was explicitly accepted by a human.
- LEGAL_AUDIT_RETENTION_REQUIREMENT was not established as a general policy. The accepted repository-specific retention decision is `ACCEPT_GIT_AND_REGISTER_RETENTION_FOR_ENGINEERING_USE`.
- P6 execution is complete; independent P6 validation remains NOT_RUN.
- Commit, push, PR, and merge remain unauthorized.
