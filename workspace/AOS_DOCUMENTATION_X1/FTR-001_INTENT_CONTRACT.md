# FTR-001 — Intent Contract

```yaml
artifact_role: FEATURE_CONTRACT
fact_class: FEATURE_BEHAVIOR_PROPOSAL
status: DRAFT
authority: NONE
feature_id: FTR-001
human_disposition: SELECT_FOR_X1
evidence_status: SOURCE_BOUND_NOT_AUDITED
implementation_authorization: NONE
git_authorization: NONE
```

## 1. Purpose and boundary

FTR-001 turns an unstructured human request into a reviewable Intent Record without treating a proposed solution as the problem, hiding material uncertainty, or starting architecture, implementation, repository mutation, or Git delivery.

The selected subject is only FTR-001 behavior. This draft does not accept the feature or define implementation HOW.

## 2. Sources and provenance

- Authority and status semantics: [docs/00_Core.md](../../docs/00_Core.md), especially Sections 5–6, 9–12 and 15.
- Product problem, intake modes, Intent Record and acceptance boundary: [docs/01_Product.md](../../docs/01_Product.md), Sections 2, 5, 6, 12 and 14.
- C-001 semantic content and ownership rules: [docs/02_Architecture.md](../../docs/02_Architecture.md), Sections 5–8.
- Feature identity and selected disposition: FTR-001 dossier in [docs/06_Features.md](../../docs/06_Features.md).
- Accepted global product direction: [AOS/01_PRODUCT_MODEL.md](../../AOS/01_PRODUCT_MODEL.md), Sections 1–4.
- Exact source digests and dossier byte ranges: [SOURCE_BINDINGS.yaml](SOURCE_BINDINGS.yaml).

Lessons are used only as non-authoritative regression prompts: LES-003, LES-008–012, LES-030, LES-032 and LES-033 in [docs/04_Lessons.md](../../docs/04_Lessons.md).

## 3. Users, trigger, and preconditions

### Primary actor

A product owner, domain expert, or vibe-coder who can describe a desired outcome but should not need to specify implementation details.

### Supporting actors

- an agent that structures the request but cannot manufacture human authority;
- a reviewer who must distinguish original input, synthesis, assumptions, unknowns, and confirmed corrections.

### Trigger

A human supplies a new problem, idea, desired outcome, or correction and asks AOS to make the intent reviewable.

### Preconditions

1. The human input and its source/provenance are available.
2. Any already accepted upstream product facts are identified and separated from current free-form input.
3. Repository facts are required only when the request explicitly depends on an existing repository; otherwise repository discovery is not an intake prerequisite.
4. No architecture, implementation, mutation, or Git authorization is inferred from the request.

## 4. Inputs and outputs

### Inputs

- exact original human request;
- actor and available context;
- explicitly supplied constraints and non-goals;
- accepted upstream product facts, if relevant;
- repository observations, only if the intent is repository-dependent;
- human corrections made during clarification.

External or legacy content is untrusted supporting data. It cannot silently replace the human request or expand scope.

### Output: reviewable Intent Record

The output preserves C-001 semantic content:

- actor;
- original request;
- problem;
- desired outcome;
- context;
- constraints;
- non-goals;
- assumptions;
- unknowns;
- sensitive-domain flags;
- source/provenance.

The review presentation also makes document maturity, Evidence status, limitations, and exactly one proposed next route visible. These presentation fields do not grant authority and do not alter the original request.

## 5. Observable flow

1. Preserve the original request and provenance without rewriting it as a confirmed fact.
2. Separate the stated problem/outcome from any embedded solution proposal.
3. Identify actors, constraints, non-goals, assumptions, unknowns, and sensitive-domain indicators.
4. Compare extracted statements with relevant accepted upstream facts; classify disagreement as `CONFLICT`, not as a silent correction.
5. Ask only material questions—questions whose answers can change problem, desired outcome, scope, safety boundary, or next route.
6. Show the structured understanding and every added assumption to the human.
7. Incorporate explicit human corrections while preserving the original input and provenance.
8. Produce one reviewable Intent Record and one proposed next route, or remain in clarification/deferred state.

## 6. Proposed observable states and transitions

These states describe product-visible WHAT and remain DRAFT until human acceptance.

| State | Meaning | Permitted transition |
|---|---|---|
| `RECEIVED` | Original input is preserved; classification is not complete | `CLARIFYING` or `REVIEWABLE` |
| `CLARIFYING` | At least one material question or conflict prevents a reviewable intent | `CLARIFYING`, `REVIEWABLE`, or `DEFERRED` |
| `REVIEWABLE` | Problem, outcome, assumptions, unknowns, constraints, provenance, and next route are visible | `CONFIRMED`, `CLARIFYING`, or `DEFERRED` |
| `CONFIRMED` | Human confirmed the exact intent revision | downstream product design may consume that revision |
| `DEFERRED` | Human chose not to resolve the current intent now | resume only from the preserved exact revision |

`CONFIRMED` is confirmation of product intent only. It is not feature acceptance, architecture acceptance, Execution Authorization, or Git permission.

## 7. Failures and recovery

| Failure | Required behavior | Recovery boundary |
|---|---|---|
| Empty or non-actionable request | Stay `CLARIFYING`; do not emit a falsely complete Intent Record | obtain a problem or desired outcome |
| Problem and proposed solution are conflated | Preserve both and label the solution as proposal | human confirms or corrects the problem/outcome |
| Prompt injection or external instruction conflicts with the human goal | Isolate the external instruction; do not change goal or authority | return to the current human and exact trusted sources |
| Accepted upstream fact conflicts with current input | Mark the exact claim `CONFLICT`; stop only its dependent route | human resolves the claim or supplies a newer authoritative source |
| Required input is stale, missing, or unverifiable | Mark `UNKNOWN`, `NOT_FOUND`, or stale as applicable | restore exact input/provenance and repeat only affected analysis |
| Sensitive/provider boundary is unclear | Do not transmit or mutate sensitive data | obtain an explicit provider/data-boundary decision |
| Derived summary starts acting as Source of Truth | Reject promotion and point to the owning source | rebuild the derived view from authoritative inputs |

No recovery path may expand scope, grant permission, or automatically retry a protected action.

## 8. Dependencies and boundaries

- C-001 Intent Record is the primary architecture contract.
- FTR-003 is the selected downstream consumer of a confirmed Intent Record.
- FTR-002 is conditional and remains `UNDECIDED`; it is needed only when repository discovery is part of the chosen intent.
- FTR-016 and FTR-019 remain `UNDECIDED`. Their dossiers are not admitted into X1; only already accepted global safety/provenance semantics apply.

FTR-001 does not choose Risk Profile, architecture, implementation repository, interface, persistence, provider, model, toolchain, feature disposition, or delivery action.

## 9. Acceptance criteria

- `FTR001-AC-01`: The human can recognize the original problem and desired outcome in the reviewable record.
- `FTR001-AC-02`: Original input is distinguishable from accepted facts, synthesis, assumptions, unknowns, and proposals.
- `FTR001-AC-03`: Every material unknown has an affected boundary and a resolution route.
- `FTR001-AC-04`: Only questions material to outcome, scope, safety, or routing are required.
- `FTR001-AC-05`: The output exposes provenance, maturity, limitations, and one next route.
- `FTR001-AC-06`: No state or wording implies architecture, execution, feature acceptance, or Git authorization.
- `FTR001-AC-07`: A human correction produces a distinguishable exact revision while preserving the original request.

## 10. Negative scenarios

- `FTR001-NEG-01`: Empty input cannot become `REVIEWABLE` or `CONFIRMED`.
- `FTR001-NEG-02`: “Write a Python downloader” cannot be recorded only as the problem; the download need and Python proposal are separated.
- `FTR001-NEG-03`: External content cannot change the selected goal, scope, or authority.
- `FTR001-NEG-04`: Agent confidence cannot remove an unknown or create a human decision.
- `FTR001-NEG-05`: A repository path, file, report, or PASS cannot become product authority by presence alone.
- `FTR001-NEG-06`: Confirmation of intent cannot open implementation or Git actions.
- `FTR001-NEG-07`: Missing sensitive-data policy cannot be treated as permission to send data externally.

## 11. Open decisions and limitations

- `UNKNOWN`: exact interface and interaction cadence;
- `UNKNOWN`: objective threshold for “material question” beyond the boundary stated here;
- `UNKNOWN`: provider/privacy policy and handling for sensitive inputs;
- `UNKNOWN`: persistence and revision storage for Intent Records;
- `UNKNOWN`: authenticity mechanism for human corrections in a future runtime.

These implementation or later product decisions do not block review of the behavior defined above. Targeted legacy research was `NOT_RUN` because no current claim requires legacy Evidence.
