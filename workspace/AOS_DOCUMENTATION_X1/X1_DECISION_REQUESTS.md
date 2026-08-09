# X1 — Decision Requests

```yaml
artifact_role: HUMAN_DECISION_REQUESTS
fact_class: DECISION_READY_PROPOSAL
status: DRAFT
authority: NONE
scope: [FTR-001, FTR-003]
selected_options: NONE
evidence_status: SOURCE_BOUND_NOT_AUDITED
implementation_authorization: NONE
git_authorization: NONE
```

## 1. Decision boundary

This artifact prepares two human-only decisions. It records no choice, acceptance, feature-disposition mutation, architecture mutation, implementation permission, or Git permission.

The decision subject for each option must bind the exact candidate manifest produced for this package. A later package-level `ACCEPT` is valid only for explicitly named fact classes; it does not fill either `selected_option` unless the human decision record says so.

## 2. X1-DR-001 — Product Spec↔Feature Passport ownership

```yaml
decision_id: X1-DR-001
classification: MATERIAL_PRODUCT_ARCHITECTURE_DECISION
selected_option: null
affected_boundary:
  - FTR-003.output_ownership
  - C-002_C-003_relationship
required_before:
  - canonical_publication_dependent_on_owner_model
  - implementation_planning_dependent_on_owner_model
```

### Question

Which artifact owns shared product facts, and how does a Feature Passport relate to the Product Spec?

### Evidence and constraints

- `docs/01_Product.md` defines both artifacts but lists their relationship as an open product decision.
- `docs/02_Architecture.md` requires one owner per fact class and treats registries/views as derived.
- The accepted Global Design Package preserves Product Spec↔Feature Passport as `UNKNOWN`.
- Duplicate accepted ownership creates drift; one combined artifact may reduce duplication but weakens cross-feature ownership clarity.

### Options

| Option | Contract | Benefits | Costs/risks |
|---|---|---|---|
| `A` | Product Spec owns cross-feature product facts; each Feature Passport owns feature-specific behavior and links to the Product Spec | clear fact-class ownership, reusable product context, less duplicate behavior | requires explicit cross-links and revision compatibility |
| `B` | Every Feature Passport embeds all required product context and is self-contained | simple single-feature handoff | repeated product facts can drift and create competing owners |
| `C` | For the first slice, one combined Product Spec/Feature Passport owns both views; separation is deferred | smallest initial artifact set | later split/migration required; cross-feature ownership remains weak |

### Synthesis recommendation

`PROPOSAL: A`. It best matches the accepted one-owner rule while preserving a complete feature-specific behavior contract. This is not a human decision.

### Exact human response needed

```text
DECIDE X1-DR-001: A
DECIDE X1-DR-001: B
DECIDE X1-DR-001: C
DECIDE X1-DR-001: DEFER
```

## 3. X1-DR-002 — First Product Runtime vertical slice

```yaml
decision_id: X1-DR-002
classification: MATERIAL_PRODUCT_DECISION_AND_SOURCE_CONFLICT
selected_option: null
affected_boundary:
  - first_product_runtime_slice
  - FTR-003.slice_selection_transition
global_impact_finding: X1-GI-001
required_before:
  - first_slice_selection_claim
  - runtime_implementation_planning
```

### Question

Which exact user-visible behavior is the first Product Runtime vertical slice?

### Source status

- `docs/01_Product.md` Section 15 names “Slice 1 (Intake & Definition)” and associates it with an Intent Contract.
- `docs/00_Core.md` Section 17 says first vertical slice remains an open decision protected for the human.
- `AOS/01_PRODUCT_MODEL.md` Section 6 preserves first segment/job/slice as `UNKNOWN`.
- FTR-001 and FTR-003 are both selected for X1, but selection into documentation scope is not runtime slice acceptance.

This is treated as an affected-boundary `CONFLICT`; the package makes no selected-slice claim.

### Options

| Option | User-visible slice | Benefits | Costs/risks |
|---|---|---|---|
| `A` | FTR-001: request → reviewable, human-confirmed Intent Record | smallest observable outcome; minimal dependencies; tests intent clarity and human correction | does not yet produce Product Spec/Feature Passport |
| `B` | FTR-001→FTR-003: request → reviewable Product Spec + Feature Passport + slice decision package | exercises the full definition journey and relation between selected X1 features | larger boundary; blocked ownership relation must be resolved or explicitly constrained |
| `DEFER` | no runtime slice selected now | preserves authority until more product evidence exists | delays implementation planning and dogfood learning |

### Synthesis recommendation

`PROPOSAL: A`, because it is the smallest user-visible outcome satisfying the accepted slice criteria without requiring an implementation repository, Product Registry, or full control plane. This is not a human selection.

### Exact human response needed

```text
DECIDE X1-DR-002: A
DECIDE X1-DR-002: B
DECIDE X1-DR-002: DEFER
```

## 4. Preserved non-blocking unknowns

The following are visible but do not need resolution to review the current WHAT-level package:

- exact interaction surface;
- acceptance-authenticity mechanism for future runtime records;
- Product Feature Registry implementation;
- Intent/Product artifact persistence and serialization;
- metrics and material-question thresholds;
- implementation repository, language, toolchain, dependencies, adapters, and storage;
- provider/privacy/routing policy.

They remain `UNKNOWN`; they are not silently promoted to decisions. Targeted reference research remains `NOT_RUN` until one of these becomes an exact evidence question.
