---
artifact_id: RSR-001
artifact_type: TARGETED_REFERENCE_RESEARCH_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R2
status: COMPLETED_WITH_LIMITATIONS
authority: NONE
exact_subject: Historical AgentOS Problem Interview and Product Spec fields, states, and non-approval boundaries relevant to G1 slice A
created: '2026-07-30'
source_repository: NMF13579/AgentOS
source_ref: dev
source_commit: e3a60a92fbd5e78e583cddb519d39527583f3433
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/05_Reference.md
  - https://github.com/NMF13579/AgentOS/tree/e3a60a92fbd5e78e583cddb519d39527583f3433
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md
downstream_links:
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
limitations:
  - Evidence was inspected from the exact local Git object at the pinned commit; no network refresh was performed.
  - Runtime, scripts, fixtures, and current CI were not executed.
  - Findings are reference evidence with authority NONE and do not select target contracts.
implementation_authorization: NONE
git_authorization: NONE
---

# RSR-001 — AgentOS Interview and Product Spec

## Research question

Which exact historical AgentOS fields, lifecycle boundaries, and negative patterns are useful when documenting the accepted first slice:

```text
intent → clarification → DRAFT Product Spec/Feature Passport → human review stop
```

## Source boundary and methods

```yaml
repository_url: https://github.com/NMF13579/AgentOS
ref: dev
resolved_commit: e3a60a92fbd5e78e583cddb519d39527583f3433
repository_role: READ_ONLY_REFERENCE
authority: NONE
paths:
  - docs/PROBLEM-INTERVIEW-TEMPLATE.md
  - docs/INTERVIEW-GAP-DECISION-CARD.md
  - docs/PRODUCT-SPEC-ARCHITECTURE.md
  - docs/PRODUCT-SPEC-LIFECYCLE.md
  - docs/PRODUCT-SPEC-READINESS-GATE.md
  - schemas/product-spec.schema.json
methods:
  - git ls-tree -r --name-only <commit>
  - git show <commit>:<path>
checks_not_run:
  - scripts
  - schemas against fixtures
  - tests
  - runtime
  - current remote dev refresh
```

## Classified findings

### `RSR-001-F001` — Preserve evidence; do not complete the user's idea

`OBSERVED_AT_SNAPSHOT`

The interview template requires preservation of `source_user_input`, a neutral non-inventing summary, visible unknowns/assumptions, and follow-up questions. Missing information is distinct from an explicit `NONE`.

Evidence:

- [Problem Interview fields and neutral-summary boundary](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PROBLEM-INTERVIEW-TEMPLATE.md#L25-L53)
- [Missing information and `NONE` rules](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PROBLEM-INTERVIEW-TEMPLATE.md#L70-L90)

Target implication: Stage B should require original-input preservation, separate `missing`, `unknown`, `assumption`, and `explicit_none` semantics, and material questions instead of inferred requirements.

### `RSR-001-F002` — Interview completeness has no downstream authority

`OBSERVED_AT_SNAPSHOT`

The reference separates interview evidence from industrial specification and rejects implementation/task/Git authority at the interview stage.

Evidence:

- [Interview status and non-approval boundary](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PROBLEM-INTERVIEW-TEMPLATE.md#L55-L68)
- [Explicit prohibited downstream actions](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PROBLEM-INTERVIEW-TEMPLATE.md#L102-L127)
- [Decision card explains but does not approve](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/INTERVIEW-GAP-DECISION-CARD.md#L25-L40)

Target implication: `READY_FOR_SPEC` may unlock only specification drafting; it cannot create contract acceptance, Task eligibility, execution, or Git authority.

### `RSR-001-F003` — Product and operational states must remain orthogonal

`OBSERVED_AT_SNAPSHOT`

The reference distinguishes product-level `APPROVED` from operational `EXECUTION_READY` and states that approval alone does not authorize execution.

Evidence:

- [Product Spec purpose and exclusions](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PRODUCT-SPEC-ARCHITECTURE.md#L12-L30)
- [Product approval versus execution readiness](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PRODUCT-SPEC-ARCHITECTURE.md#L49-L60)
- [Lifecycle transition authority](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PRODUCT-SPEC-LIFECYCLE.md#L20-L30)
- [Readiness is not approval or execution authorization](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PRODUCT-SPEC-READINESS-GATE.md#L12-L35)

Target implication: AOS must keep document maturity, human decision, downstream eligibility, execution authorization, technical result, and Git authority as separate axes.

### `RSR-001-F004` — Useful minimum Product Spec fields

`OBSERVED_AT_SNAPSHOT`

The reference requires product problem, users, JTBD, goals, non-goals, constraints, risks, success metrics, acceptance criteria, dependencies, and open questions.

Evidence:

- [Canonical Product Spec sections](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PRODUCT-SPEC-ARCHITECTURE.md#L61-L127)
- [Schema required fields](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/schemas/product-spec.schema.json#L60-L76)

Target implication: use these fields as reference input, then retain AOS-specific provenance, authority, limitations, and Product Spec ↔ Feature Passport ownership from `DEC-PROD-005`.

### `RSR-001-F005` — Duplicate lifecycle owners are drift risk

`SYNTHESIZED`

The reference schema requires `lifecycle_status` in both `metadata` and `product_spec`. The architecture document separately warns that document frontmatter status and product lifecycle are different fields.

Evidence:

- [Metadata lifecycle field](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/schemas/product-spec.schema.json#L12-L43)
- [Body lifecycle field](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/schemas/product-spec.schema.json#L60-L89)
- [Frontmatter versus product lifecycle warning](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/PRODUCT-SPEC-ARCHITECTURE.md#L49-L52)

Target implication: the target contract should declare exactly one owner per state axis and derive any duplicate view.

## Conflicts and unknowns

- `CONFLICT`: none between inspected exact paths for the research question.
- `UNKNOWN`: current remote `dev` may have moved after the pinned commit; no current-remote claim is made.
- `UNKNOWN`: reference validators may enforce additional semantics not established because execution was `NOT_RUN`.

## Result

```yaml
result: RESEARCH_QUESTION_ANSWERED
authority: NONE
copied_solution: false
target_decision_made: false
historical_next_action_at_research_time: USE_CLASSIFIED_FINDINGS_AS_NON_AUTHORITATIVE_INPUT_TO_STAGE_B
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
