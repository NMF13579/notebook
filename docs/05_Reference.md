---
package: AOS_Integrated_Knowledge_Package
package_revision: R3-RU
updated: 2026-07-26
status: APPROVED
authority: AUTHORITATIVE
human_review: REQUIRED
human_acceptance: ACCEPTED
implementation_authorization: AUTHORIZED
git_authorization: AUTHORIZED
self_audit: COMPLETED
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
document_language: ru
technical_identifiers_language: en
document_role: REFERENCE_AND_PROVENANCE_REGISTRY
proposed_post_acceptance_role: REFERENCE_AND_PROVENANCE_REGISTRY
proposed_authority_scope:
  - source_provenance
  - snapshot_identity
  - targeted_research_routes
source_files_bound_by_blob_sha: true
---

# 05 — Источники и provenance

## 1. Назначение

Единый provenance и research-routing layer. Не является Product Contract, Architecture Contract или implementation authorization.

```text
reference occurrence ≠ current implementation
historical acceptance ≠ current acceptance
source mapping ≠ target requirement
stored PASS ≠ current PASS
```

## 2. Source classes and authority

| Source class | Use | Authority |
|---|---|---|
| Current project instructions | Agent behavior/safety | Behavior-scoped |
| Explicit human decision | Exact boundary | Human-scoped |
| Accepted project artifact | Fact class | Fact-class scoped |
| Current repository observation | Snapshot facts | Observation only |
| Historical repository | Behavior/failure/reference | None for target |
| Chat summary/note | Intent/lessons/candidates | None |
| Generated synthesis | Navigation/inference | None |

## 3. Bound source-file register

| ID | Path | Роль |
|---|---|---|
| `SRC-AF-00..06` | `AOS-FARM/00_Core.md` … `06_Features.md` | Основной target synthesis и 30 full dossiers |
| `SRC-AG-00..06` | `AgentOS/00_Core.md` … `06_Features.md` | AgentOS-specific evidence, paths, failures и feature crosswalk |
| `REF-AF-REPO` | `NMF13579/AOS-FARM` | Historical implementation reference |
| `REF-A02-REPO` | Historical AOS-02 | Strict loader/CLI/preview/failure reference |

Exact blob SHA сохраняются в repository/audit record при принятии пакета.

## 4. Source roles

`AOS-FARM/` в notebook фактически описывает target AOS synthesis и служит основой объединения. `AgentOS/` содержит source-specific extraction и особенно полезен для Problem Interview, Feature Passport, concrete drift/idle/portability failures, registries и adapters. Ни один из них не имеет target authority автоматически.

## 5. AgentOS path register

```yaml
repository: NMF13579/AgentOS
branch: dev
commit: e3a60a92fbd5e78e583cddb519d39527583f3433
commit_date: 2026-06-05
inspection_mode: static_read_only
commands_tests_build: NOT_RUN
```

| ID | Historical paths | Evidence area |
|---|---|---|
| `AG-RP-01` | `README.md`, `INIT.md` | Identity/onboarding/discovery |
| `AG-RP-02` | `llms.txt`, `ROUTES-REGISTRY.md` | Bootstrap/routes |
| `AG-RP-03` | `core-rules/MAIN.md` | Authority |
| `AG-RP-04` | `state/MAIN.md`, `HANDOFF.md`, `tasks/active-task.md` | State/handoff/idle |
| `AG-RP-05` | `workflow/MAIN.md` | Scope/one-task/lessons |
| `AG-RP-06` | `quality/MAIN.md`, `security/MAIN.md` | Verification/risk |
| `AG-RP-07` | Problem Interview docs/checker | Interview/completeness |
| `AG-RP-08` | Product Spec architecture | Product Spec/depth |
| `AG-RP-09` | Spec-to-task docs/script | Task candidate generation |
| `AG-RP-10` | Task schema/validator | Task/idle bypass |
| `AG-RP-11` | Verification schema/report | Verification/demo |
| `AG-RP-12` | Lessons registry | Incident-to-lesson |
| `AG-RP-13` | RAG-light/index | Context index |
| `AG-RP-14` | Honest PASS checker | False-PASS resistance |
| `AG-RP-15` | Bounded retry | Retry limits |
| `AG-RP-16` | Repo scan/drift reports | Hygiene/drift |
| `AG-RP-17` | `repo-map.md` | Generated map |
| `AG-RP-18` | UI/token docs | NOT_FOUND named artifacts |
| `AG-RP-19` | Maintainability tools | NOT_FOUND dedicated tools |
| `AG-RP-20` | Prompt packs/agent files | Adapter surfaces |

## 6. High-signal inspection order

```text
user-facing docs/commands
→ contracts/schemas
→ tests/negative fixtures
→ implementation paths
→ reports/plans/recovery artifacts
```

## 7. Targeted research record

```yaml
research_id:
feature_id:
question:
repository:
ref_or_branch:
commit_or_tree:
paths: []
methods_or_commands: []
read_only: true
findings:
  - evidence_status:
    statement:
    locator:
    temporal_scope:
useful_contracts: []
useful_negative_cases: []
rejected_legacy_complexity: []
limitations: []
remaining_unknowns: []
```

## 8. Research stop conditions

Stop when question answered, snapshot/path unavailable, conflict changes scope, permission/network expansion needed, protected decision found, research expands beyond selected feature или current state cannot be separated from memory.

## 9. Feature-to-reference routing

| Feature | Первые reference questions |
|---|---|
| `FTR-001..006` | Intake, discovery, spec, install, ADR, Task Brief/auth |
| `FTR-007..012` | Decomposition, status UX, preflight, execution, validation, review |
| `FTR-013..018` | Freeze, recovery, Git closure, memory, search, routing |
| `FTR-019..024` | Trust, Governance, drift, patterns, CI, release |
| `FTR-025..030` | Incidents, plugins, domains, UI, packaging, internal tooling |

## 10. Promotion model

```text
reference idea → feature entry → product-fit review → human disposition
→ Feature Contract → DRAFT architecture → architecture decision
→ Task Brief → Execution Authorization
```

## 11. Current limitations

Byte-complete chat export, historical runtime execution, current test/CI reproduction, independent semantic validation и human canonicalization — `NOT_RUN/NOT_PROVIDED`. Implementation authorization — `NONE`.
