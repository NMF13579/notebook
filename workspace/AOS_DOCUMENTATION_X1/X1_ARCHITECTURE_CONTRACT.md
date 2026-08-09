# X1 — Architecture Contract

```yaml
artifact_role: ARCHITECTURE_CONTRACT
fact_class: ARCHITECTURE_PROPOSAL
status: DRAFT
authority: NONE
scope: [FTR-001, FTR-003]
evidence_status: SOURCE_BOUND_NOT_AUDITED
implementation_authorization: NONE
git_authorization: NONE
```

## 1. Purpose and rationale

This separate artifact is required because X1 crosses material component, contract, state, and ownership boundaries: FTR-001 produces an Intent Record; FTR-003 consumes product intent and produces Product Spec, Feature Passport, and slice-decision subjects; human review and decision must not be simulated by either capability.

It defines WHAT-level relationships only. Exact schemas, storage, APIs, UI, adapters, algorithms, toolchain, repository topology, locks, retries, and persistence are excluded implementation HOW.

## 2. Sources and provenance

- Architecture layers, C-001–C-004, ownership, and orthogonal state axes: [docs/02_Architecture.md](../../docs/02_Architecture.md).
- Product actors, journeys, selected X1 features, and preserved unknowns: [AOS/01_PRODUCT_MODEL.md](../../AOS/01_PRODUCT_MODEL.md).
- Accepted global architecture boundaries: [AOS/02_ARCHITECTURE_CONTRACTS.md](../../AOS/02_ARCHITECTURE_CONTRACTS.md).
- Engineering separation and Evidence/decision semantics: [AOS/03_ENGINEERING_PIPELINE.md](../../AOS/03_ENGINEERING_PIPELINE.md).
- Feature contracts: [FTR-001](FTR-001_INTENT_CONTRACT.md) and [FTR-003](FTR-003_SPECIFICATION_AND_SLICE_CONTRACT.md).
- Exact digests: [SOURCE_BINDINGS.yaml](SOURCE_BINDINGS.yaml).

## 3. Capability boundaries

| Capability | Layer | Owns in this DRAFT | Must not own |
|---|---|---|---|
| Intent interaction | L1 Interaction Surface | presentation of input, questions, uncertainty, and review state | product truth, approval, repository mutation |
| FTR-001 intent capability | L2 Product Runtime | creation of a source-bound C-001 Intent Record candidate | human confirmation, architecture, execution, Git authority |
| FTR-003 specification capability | L2 Product Runtime | creation of C-003/C-002 candidates and slice comparison | generated scope/priority/first-slice decision |
| Review surface | L1 Interaction Surface | display of exact revision, Evidence, unknowns, options | independent Source of Truth or implicit approval |
| Product knowledge | L5 Knowledge / Reference | human-accepted Product/Feature artifacts in their declared fact classes | runtime permission or repository state |
| Safety controls | L4 Minimal Safety / Governance | authority, scope, result, decision, and Git boundaries already accepted globally | product value or autonomous product choice |

FTR-005 may support a decision-ready architecture question under its `SUPPORTING_CONTROL_ONLY` disposition. It does not become an independent X1 subject.

## 4. Contract relationships

```text
human request
→ FTR-001 candidate Intent Record (C-001)
→ human confirmation of exact intent revision
→ FTR-003 Product Spec candidate (C-003)
  + Feature Passport candidate (C-002)
  + first-slice decision package
→ exact human product/architecture decision records
→ separate downstream planning, if later authorized
```

### C-001 — Intent Record

- Proposed producer: FTR-001 intent capability.
- Human-controlled checkpoint: confirmation/correction of exact intent revision.
- Proposed consumer: FTR-003 specification capability.
- Invariant: the original request and added synthesis remain distinguishable.

### C-003 — Product Spec

- Proposed producer: FTR-003 specification capability.
- Content boundary: cross-feature product problem, actors/JTBD, goals/non-goals, journeys, scope, constraints, dependencies, success signals, acceptance, and open decisions.
- Ownership relationship to C-002 is not selected in this draft.

### C-002 — Feature Passport

- Proposed producer: FTR-003 specification capability.
- Content boundary: feature-specific observable behavior and acceptance fields.
- Human-controlled checkpoint: acceptance of an exact feature revision and fact classes.

### C-004 — ADR

A DRAFT ADR is needed only when a material architecture option must be selected. X1 currently identifies one decision boundary—Product Spec↔Feature Passport ownership—but does not create or select an ADR option. The decision-ready question is in [X1_DECISION_REQUESTS.md](X1_DECISION_REQUESTS.md).

## 5. Data ownership

| Fact class | Owner before an X1 decision | Owner after an exact acceptance |
|---|---|---|
| Original human request | source-bound Intent Record revision | same accepted/confirmed exact revision |
| Product requirement | current accepted product owner; X1 text is proposal | exact human-accepted Product artifact in declared fact classes |
| Feature behavior | current accepted feature inventory/dossier within its authority; X1 text is proposal | exact human-accepted Feature Passport in declared fact classes |
| Architecture choice | current accepted architecture owner; unresolved X1 choice remains empty | exact human-accepted ADR/architecture record |
| Human decision | exact human-authored/verified record | same record; never generated by UI/agent |
| Technical Evidence | exact immutable subject-bound record | Evidence only; never approval |
| Repository state | current instrumental observation | current instrumental observation, rechecked when mutable |

Derived package maps, manifests, indexes, status views, and registries never own product or architecture truth.

## 6. State and transition invariants

1. Document maturity, technical result, human decision, feature disposition, and permission remain orthogonal.
2. A reviewable or technically passing artifact does not become human-accepted automatically.
3. Intent confirmation does not accept a feature, architecture, implementation, or Git action.
4. Product/feature acceptance binds exact bytes/revision and declared fact classes.
5. A changed subject invalidates its prior review or decision binding.
6. An unknown blocks only claims/actions that depend on it.
7. Supporting-control features do not gain product-scope admission through dependency references.
8. Runtime implementation begins only after separate downstream planning, repository binding, and authorization.

The proposed feature-visible states are defined in the two feature contracts. This architecture contract does not invent a universal runtime state machine or replace the accepted orthogonal axes.

## 7. Failure and recovery boundaries

- **Stale or missing source:** stop the dependent claim, rebind the exact source, and recompute the affected candidate.
- **Conflicting owners:** mark exact claims `CONFLICT`; no derived artifact chooses the winner.
- **Generated human decision:** reject the transition and retain the prior valid state.
- **Subject mutation after binding:** invalidate review/Evidence/decision for the old subject.
- **Unauthorized mutation request:** block only the mutation; preserve safe read-only/product-design work.
- **Partial future write:** implementation must define atomicity/recovery separately; this design does not prescribe HOW.

## 8. Material architecture decision

`X1-DR-001` asks which artifact owns shared product facts and how Feature Passports reference them. Until the human selects an option:

- both views may exist as DRAFT;
- shared claims must retain source links and explicit status;
- neither view may silently supersede the other;
- no canonical publication or implementation plan may depend on an unselected ownership model.

## 9. Global impact and preserved unknowns

No Global Design Package mutation is proposed. One global/canonical status ambiguity is recorded as `X1-GI-001`: `docs/01_Product.md` Section 15 names a Slice 1 direction, while `docs/00_Core.md` Section 17 and `AOS/01_PRODUCT_MODEL.md` Section 6 preserve first slice as open/unknown. The affected first-runtime-slice claim is not resolved here.

Preserved implementation unknowns: exact interface, repository, language/toolchain/dependencies, persistence, schema/serialization, adapters, Registry implementation, provider/privacy routing, and full transition mechanics.
