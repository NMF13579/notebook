# FTR-003 — Specification, Feature Passport, and Slice Contract

```yaml
artifact_role: FEATURE_CONTRACT
fact_class: FEATURE_BEHAVIOR_PROPOSAL
status: DRAFT
authority: NONE
feature_id: FTR-003
human_disposition: SELECT_FOR_X1
evidence_status: SOURCE_BOUND_NOT_AUDITED
implementation_authorization: NONE
git_authorization: NONE
```

## 1. Purpose and boundary

FTR-003 converts confirmed product intent into reviewable product definition, feature behavior, and a decision-ready comparison of the smallest user-visible runtime slice. It preserves human ownership of product scope, first slice, architecture, and exact accepted revision.

This draft defines feature behavior at WHAT level. It does not select the first runtime slice, settle Product Spec↔Feature Passport ownership, freeze a product revision, or authorize implementation.

## 2. Sources and provenance

- Product artifacts, journeys, slice criteria, and acceptance: [docs/01_Product.md](../../docs/01_Product.md), Sections 5–6 and 9–15.
- C-002/C-003 semantics, ownership, state axes, and protected decisions: [docs/02_Architecture.md](../../docs/02_Architecture.md), Sections 5–8 and 16.
- Documentation package requirements and readiness: [docs/03_Development.md](../../docs/03_Development.md), Section 6.
- Feature identity and selected disposition: FTR-003 dossier in [docs/06_Features.md](../../docs/06_Features.md).
- Accepted product foundation and preserved unknowns: [AOS/01_PRODUCT_MODEL.md](../../AOS/01_PRODUCT_MODEL.md), Sections 4–6.
- Exact source digests and dossier byte ranges: [SOURCE_BINDINGS.yaml](SOURCE_BINDINGS.yaml).

Lessons are non-authoritative regression prompts only: LES-002–011, LES-030, LES-032, LES-033, LES-035 and LES-041 in [docs/04_Lessons.md](../../docs/04_Lessons.md).

## 3. Users, trigger, and preconditions

### Primary actor

A product owner or domain expert deciding what product behavior is needed and which exact revision or first slice should be accepted.

### Supporting actors

- an agent that structures product information and compares slice options;
- a reviewer who checks completeness, traceability, owner boundaries, and visible uncertainty;
- a future implementer who may consume only a later human-accepted contract, never this draft by presence alone.

### Trigger

A confirmed or explicitly reviewable intent requires product specification, a feature-specific contract, or comparison of candidate first slices.

### Preconditions

1. Input intent, its maturity, and provenance are explicit.
2. Selected feature IDs and current human dispositions are bound.
3. Accepted product facts are separated from proposals and unknowns.
4. Repository discovery is required only for an existing-project claim; FTR-002 is not admitted automatically.
5. No generated recommendation is treated as a human selection.

## 4. Inputs and outputs

### Inputs

- exact Intent Record revision or equivalent bound product intent;
- accepted product boundaries, actors, journeys, and non-goals;
- selected feature identities and dispositions;
- known dependencies, constraints, conflicts, and research gaps;
- current repository observations only when a claim depends on an existing repository;
- explicit human corrections and decisions.

### Outputs

1. A reviewable Product Spec view covering problem, users/JTBD, goals, non-goals, journeys, boundaries, constraints, dependencies, success signals, acceptance, and open decisions.
2. A full Feature Passport for each feature being proposed, preserving C-002 semantic content: identity, purpose, users, trigger, preconditions, I/O, flow, states/transitions, failures/recovery, dependencies, constraints, authority boundaries, acceptance, negative scenarios, maturity, Evidence status, and human disposition.
3. A slice decision package that compares distinct candidates against the accepted criteria in `docs/01_Product.md` Section 11.
4. Exact provenance and revision identity for any subject presented for human decision.

The Product Spec and Feature Passport may both be drafted before their ownership relationship is chosen, but shared claims must remain linked to their source and cannot silently diverge. Their canonical ownership relationship is an explicit human decision in [X1_DECISION_REQUESTS.md](X1_DECISION_REQUESTS.md).

## 5. Observable flow

1. Bind the exact intent revision and current feature dispositions.
2. Define users/JTBD, problem, goals, non-goals, product boundary, and observable outcome.
3. Draft the Product Spec view and full feature-specific Passports without inventing missing decisions.
4. Detect dependencies, conflicts, authority boundaries, unknowns, and exact research questions.
5. Identify distinct candidate slices that each yield an observable user outcome.
6. Compare candidates on user value, boundary size, dependencies, I/O/states/failures/recovery completeness, learning value, and absence of implicit Git delivery.
7. Present the exact candidate revisions, recommendation if any as `PROPOSAL`, and material unknowns.
8. Obtain an explicit human choice before marking a slice or product revision selected.
9. Bind the chosen exact revision; do not infer implementation authorization.

## 6. Proposed observable states and transitions

| State | Meaning | Permitted transition |
|---|---|---|
| `INPUT_BOUND` | Exact intent and dispositions are known | `SPEC_DRAFT` or `BLOCKED_INPUT` |
| `SPEC_DRAFT` | Product definition is incomplete but source-bound | `PASSPORT_DRAFT`, `SPEC_DRAFT`, or `BLOCKED_INPUT` |
| `PASSPORT_DRAFT` | Required feature behavior fields are visible | `SLICE_OPTIONS_READY` or return to `SPEC_DRAFT` |
| `SLICE_OPTIONS_READY` | Distinct slice options and trade-offs are reviewable | `WAITING_HUMAN_DECISION` |
| `WAITING_HUMAN_DECISION` | Exact decision subject is bound; no option is selected by the agent | `REVISION_SELECTED`, revision correction, or `DEFERRED` |
| `REVISION_SELECTED` | Human selected an exact product/feature revision and, when applicable, a slice | downstream architecture/planning may begin only under separate authority |
| `BLOCKED_INPUT` | A material missing/conflicting upstream fact prevents affected claims | resume after exact source or human decision |
| `DEFERRED` | Human paused the exact subject | resume from the bound revision |

The states are feature-level DRAFT behavior and do not replace the orthogonal document maturity, technical result, human decision, or permission axes.

## 7. Failures and recovery

| Failure | Required behavior | Recovery boundary |
|---|---|---|
| Intent or disposition is missing/stale | Stop affected drafting or selection claim | rebind exact current source |
| Product Spec and Passport make conflicting shared claims | Mark the exact claims `CONFLICT`; do not select an owner implicitly | human chooses ownership relation or corrects a source |
| Feature has no user-visible outcome | Reject it as a valid slice candidate | redefine outcome or remove candidate |
| Slice option lacks I/O, states, failures, recovery, acceptance, or negative cases | Keep it incomplete; do not recommend as ready | fill from authoritative source or expose exact decision gap |
| Generated recommendation appears as `REQUIRED` or selected | Reject the state change | restore proposal and request human choice |
| Legacy presence is used as admission or priority | Reject the rationale | perform targeted research only for an exact gap |
| Candidate revision changes after review binding | Invalidate the old review/decision subject | bind and review the new exact revision |
| Implementation/Git action is inferred | Block that action without blocking safe documentation work | obtain separate downstream authorization |

## 8. Dependencies and boundaries

- FTR-001 is the selected upstream behavior and supplies the intent contract.
- C-002 Feature Passport and C-003 Product Spec define the primary architecture-level content.
- FTR-002 remains `UNDECIDED` and is conditional on an existing-project discovery need.
- FTR-005 is `SUPPORTING_CONTROL_ONLY`; it may support an architecture-need check or DRAFT ADR but is not a separate X1 documentation subject.
- FTR-006, FTR-011, FTR-012, and FTR-013 remain supporting controls; their runtime workflows are not activated by this contract.

FTR-003 does not choose feature priority beyond the current human-selected X1 scope, exact interface, implementation repository, language/toolchain, persistence, Registry implementation, architecture option, Execution Authorization, or Git delivery.

## 9. Acceptance criteria

- `FTR003-AC-01`: Product problem, users/JTBD, goals, non-goals, boundaries, and observable outcomes are reviewable and source-classified.
- `FTR003-AC-02`: Every proposed feature has the full C-002 behavior fields or a visible bounded unknown.
- `FTR003-AC-03`: Dependencies and conditional/out-of-scope dispositions remain visible and are not promoted automatically.
- `FTR003-AC-04`: Slice candidates are distinct and compared against the accepted criteria without a generated selection.
- `FTR003-AC-05`: Product Spec↔Feature Passport ownership ambiguity is presented as an exact decision request and no dependent ownership conclusion is claimed.
- `FTR003-AC-06`: Exact revisions and provenance are bound before human review or selection.
- `FTR003-AC-07`: Human selection is distinct from technical PASS, document readiness, implementation permission, and Git permission.
- `FTR003-AC-08`: A changed revision invalidates prior review/selection binding.

## 10. Negative scenarios

- `FTR003-NEG-01`: A feature without an observable user outcome cannot be declared slice-ready.
- `FTR003-NEG-02`: A legacy feature, file, roadmap, or report cannot create current scope or priority.
- `FTR003-NEG-03`: An agent-generated `REQUIRED`, accepted revision, first-slice choice, or architecture choice is invalid.
- `FTR003-NEG-04`: A Product Spec and Passport cannot both silently own diverging versions of the same accepted claim.
- `FTR003-NEG-05`: A technical PASS cannot become product acceptance.
- `FTR003-NEG-06`: Product acceptance cannot become Execution Authorization or Git delivery.
- `FTR003-NEG-07`: An unbound or mutated revision cannot retain its prior human decision.
- `FTR003-NEG-08`: Supporting-control disposition cannot turn a feature into an independent X1 subject.

## 11. Open decisions and limitations

Material human decisions are isolated in [X1_DECISION_REQUESTS.md](X1_DECISION_REQUESTS.md):

- Product Spec↔Feature Passport ownership relationship;
- exact first Product Runtime vertical slice and resolution of current source ambiguity.

Preserved non-blocking unknowns include exact interface, Registry implementation, acceptance authenticity mechanism, persistence, metrics, language/toolchain, implementation repository, and exact schemas/I/O serialization. Targeted legacy research was `NOT_RUN`; no current behavior claim depends on it.
