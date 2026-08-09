# AOS Documentation X1 — Review Map

```yaml
artifact_role: PACKAGE_MAP_AND_REVIEW_SUMMARY
fact_class: DERIVED_NAVIGATION
status: DRAFT
authority: DERIVED_NAVIGATION_ONLY
scope: [FTR-001, FTR-003]
authoring_run_id: AOS-DOC-X1-R6-AUTHORING-001
artifact_state: AUTHORING_COMPLETE_CANDIDATE_BOUND
technical_result: NOT_RUN
human_decision: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## 1. Outcome and limits

This X1 package makes the selected FTR-001 and FTR-003 behavior reviewable at Product/Architecture Contract depth. It replaces shared dossier defaults with feature-specific actors, triggers, I/O, flow/states, failures/recovery, constraints, acceptance, negative cases, dependencies, provenance, and bounded unknowns.

It does not accept either feature, choose the first runtime slice, settle Product Spec↔Feature Passport ownership, alter canonical documents or the frozen `AOS/` package, plan implementation, or authorize Git actions.

## 2. Artifact inventory and review order

| Order | Artifact | Role / fact class | Review focus |
|---:|---|---|---|
| 1 | [FTR-001_INTENT_CONTRACT.md](FTR-001_INTENT_CONTRACT.md) | DRAFT feature behavior | intent boundary, questions, states, failures, acceptance |
| 2 | [FTR-003_SPECIFICATION_AND_SLICE_CONTRACT.md](FTR-003_SPECIFICATION_AND_SLICE_CONTRACT.md) | DRAFT feature behavior | Product Spec/Passport outputs, slice comparison, exact selection boundary |
| 3 | [X1_ARCHITECTURE_CONTRACT.md](X1_ARCHITECTURE_CONTRACT.md) | DRAFT architecture relationship | layers, C-001/C-002/C-003 relationships, ownership, state/authority invariants |
| 4 | [X1_DECISION_REQUESTS.md](X1_DECISION_REQUESTS.md) | decision-ready proposal | two human-only choices; no selected option |
| 5 | this file | derived navigation/review map | package coherence and one next action |

Operational continuity and provenance files are not product/architecture artifacts:

- [HUMAN_SELECTION_RECORD.yaml](HUMAN_SELECTION_RECORD.yaml);
- [PROGRAM_RUN_BINDING.yaml](PROGRAM_RUN_BINDING.yaml);
- [SOURCE_BINDINGS.yaml](SOURCE_BINDINGS.yaml).

The derived [CANDIDATE_MANIFEST.txt](CANDIDATE_MANIFEST.txt) will byte-bind the five candidate artifacts and exact source/decision context. It is not part of its own `ARTIFACT` inventory.

## 3. Traceability

| Intent / need | Feature behavior | Architecture contract | Acceptance / decision |
|---|---|---|---|
| Preserve original request and separate outcome from solution | FTR-001 Sections 4–6 | C-001 relationship in X1 Architecture Section 4 | `FTR001-AC-01..07`, `FTR001-NEG-01..07` |
| Make assumptions, unknowns, provenance, and one next route visible | FTR-001 Sections 5–7 | ownership and authority invariants | `FTR001-AC-02..06` |
| Turn intent into reviewable product/feature definition | FTR-003 Sections 4–6 | C-001→C-003/C-002 relationship | `FTR003-AC-01..08` |
| Compare but do not auto-select a first slice | FTR-003 Sections 5–7 | human-decision boundary | `FTR003-NEG-01..08`, `X1-DR-002` |
| Prevent duplicate owners between Product Spec and Passport | FTR-003 Sections 4 and 9 | X1 Architecture Sections 5 and 8 | `X1-DR-001` |
| Keep technical result, human decision, and permission separate | both feature contracts | X1 Architecture Sections 5–7 | package audit then exact human decision |

## 4. Dependency classification

- `FTR-001`, `FTR-003`: selected X1 subjects (`SELECT_FOR_X1`).
- `FTR-005`, `FTR-006`, `FTR-011`, `FTR-012`, `FTR-013`: supporting controls only where referenced; not independent subjects.
- `FTR-002`, `FTR-016`, `FTR-019`: `UNDECIDED`; conditional references do not change disposition.
- No inventory feature outside FTR-001/FTR-003 was added to executable/documentation scope.

## 5. Findings and unknowns

### Material decision requests

1. `X1-DR-001`: Product Spec↔Feature Passport ownership relation.
2. `X1-DR-002`: exact first Product Runtime slice and associated source-status conflict.

The dependent ownership/publication and runtime-slice-selection claims remain blocked. All unaffected documentation is complete enough for exact candidate binding and independent audit.

### Global impact

`X1-GI-001` identifies the first-slice status ambiguity between current canonical/global sources. The package does not mutate any global claim.

### Preserved non-blocking unknowns

Exact interface, Registry implementation, future decision authenticity, persistence/serialization, metrics, provider/privacy policy, implementation repository, language/toolchain, and runtime mechanisms.

## 6. Package review criteria

- exact FTR-001/FTR-003 identity and dispositions are bound;
- each feature contract covers required dossier fields;
- owner/source/status markers are explicit;
- conditional artifacts and supporting dependencies are justified;
- intent→behavior→contract→acceptance traceability is visible;
- unknowns and decision requests do not support dependent conclusions;
- Markdown links/fences are valid;
- no hidden implementation HOW, authority grant, or Git grant exists;
- candidate identity is reproducible from the exact manifest;
- audit is performed in a separate read-only run.

## 7. Status and next action

Authoring content is complete but no technical PASS is claimed. After harmonization and exact candidate binding, the only next action is a separate `AUDIT_RUN` over the bound candidate. Human package acceptance, adoption of feature/architecture facts, implementation planning, Commit, Push, Merge, and Release remain `NOT_RUN`.
