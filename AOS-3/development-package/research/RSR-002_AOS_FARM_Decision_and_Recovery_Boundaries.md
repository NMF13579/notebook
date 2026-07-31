---
artifact_id: RSR-002
artifact_type: TARGETED_REFERENCE_RESEARCH_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R2
status: COMPLETED_WITH_LIMITATIONS
authority: NONE
exact_subject: Historical AOS-FARM human decision authenticity, Risk Profile, candidate non-approval, and handoff evidence relevant to G2
created: '2026-07-30'
source_repository: NMF13579/AOS-FARM
source_ref: dev
source_commit: 71b87f3dfb9fe3735c7659c123cd86db3f577201
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/05_Reference.md
  - https://github.com/NMF13579/AOS-FARM/tree/71b87f3dfb9fe3735c7659c123cd86db3f577201
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md
downstream_links:
  - ../decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md
  - ../02_User_Journeys_and_Workflows.md
limitations:
  - Evidence was inspected from the exact local Git object at the pinned commit; no network refresh was performed.
  - Validators, negative fixtures, and runtime were not executed.
  - AOS-FARM vocabularies and topology have authority NONE for target AOS.
implementation_authorization: NONE
git_authorization: NONE
---

# RSR-002 — AOS-FARM Decision and Recovery Boundaries

## Research question

Which exact historical constraints and negative examples should inform G2 options for Human Decision authenticity, Risk Profile vocabulary, candidate identity, and Project Memory/recovery without copying legacy policy?

## Source boundary and methods

```yaml
repository_url: https://github.com/NMF13579/AOS-FARM
ref: dev
resolved_commit: 71b87f3dfb9fe3735c7659c123cd86db3f577201
repository_role: READ_ONLY_REFERENCE
authority: NONE
paths:
  - aos/docs/workflow/human-result-acceptance-decision-contract.md
  - aos/schemas/human-decision-witness.schema.json
  - aos/schemas/risk-profile-assignment-record.schema.json
  - aos/reports/examples/evidence-to-backlog/fixtures/negative/candidate-claims-approval.md
  - aos/reports/examples/evidence-to-backlog/fixtures/negative/risk-profile-self-assigned.md
  - aos/templates/handoff/session-handoff-template.md
  - aos/docs/architecture/review/architecture-decision-evidence-packet.md
methods:
  - git ls-tree -r --name-only <commit>
  - git show <commit>:<path>
checks_not_run:
  - schema validation
  - fixture runner
  - runtime
  - tests
  - current remote dev refresh
```

## Classified findings

### `RSR-002-F001` — Human acceptance and lifecycle permissions are separate

`OBSERVED_AT_SNAPSHOT`

The reference contract makes the human result decision explicit and keeps Commit, Push, Merge, Release, next-task start, and lifecycle mutation false.

Evidence:

- [Human Result Acceptance rules](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/workflow/human-result-acceptance-decision-contract.md#L1-L41)
- [Blocked automation claims](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/workflow/human-result-acceptance-decision-contract.md#L43-L61)

Target implication: Human Decision records must declare exact grants and non-grants; product/result acceptance cannot imply implementation or Git authority.

### `RSR-002-F002` — A decision witness needs identity and subject bindings

`OBSERVED_AT_SNAPSHOT`

The historical witness schema records actor reference/role, authentication level, channel, task/baseline/proposal/candidate/operation bindings, value, time, grants, non-grants, expiry, and single-use consumption. It explicitly rejects agent-generated approval and Evidence substitution.

Evidence:

- [Witness identity and binding fields](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/human-decision-witness.schema.json#L7-L47)
- [Witness non-substitution invariants](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/human-decision-witness.schema.json#L48-L71)
- [Required witness fields](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/human-decision-witness.schema.json#L73-L98)

Target implication: G2 must select the minimum authenticity mechanism and binding semantics; a chat claim may be recorded as `LOCAL_DECLARED` but must not be upgraded to stronger authentication.

### `RSR-002-F003` — Risk vocabulary is human-owned and legacy-specific

`OBSERVED_AT_SNAPSHOT`

The historical schema uses four named Risk Profiles and forces `execution_authorized: false`; a negative fixture rejects agent self-assignment.

Evidence:

- [Risk Profile assignment schema](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/risk-profile-assignment-record.schema.json#L1)
- [Risk Profile self-assignment negative fixture](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/reports/examples/evidence-to-backlog/fixtures/negative/risk-profile-self-assigned.md#L8-L33)

Target implication: G2 may reuse the invariant “human-owned and non-authorizing,” but must decide target vocabulary separately instead of copying the four legacy labels.

### `RSR-002-F004` — Candidate must not claim approval

`OBSERVED_AT_SNAPSHOT`

The historical negative fixture blocks a DRAFT candidate that claims approved-task status even while its execution/Git flags are false.

Evidence:

- [Candidate claims approval negative fixture](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/reports/examples/evidence-to-backlog/fixtures/negative/candidate-claims-approval.md#L8-L33)

Target implication: target lifecycle rules must validate both explicit authority fields and natural-language approval claims.

### `RSR-002-F005` — Architecture option packages need human weights

`OBSERVED_AT_SNAPSHOT`

The historical architecture packet keeps all recommendations candidate-only, prohibits default stack selection, and requires unresolved material unknowns and human weights to remain visible.

Evidence:

- [Candidate-only and non-approval boundary](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/architecture/review/architecture-decision-evidence-packet.md#L15-L43)
- [Architecture unknowns and ADR constraints](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/architecture/review/architecture-decision-evidence-packet.md#L73-L91)
- [Candidate-only recommendation and tradeoffs](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/architecture/review/architecture-decision-evidence-packet.md#L126-L149)
- [Human checkpoint questions](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/architecture/review/architecture-decision-evidence-packet.md#L166-L182)

Target implication: Stage B may recommend an option but cannot assign G2 weights or select architecture.

### `RSR-002-F006` — Historical handoff template is insufficient

`SYNTHESIZED`

The inspected handoff template contains only current context, next steps, and uncommitted-state warning. It lacks explicit repository identity, candidate binding, accepted decisions, blockers, checks, authority state, failures, and recovery.

Evidence:

- [Minimal historical session handoff template](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/templates/handoff/session-handoff-template.md#L1-L10)

Target implication: do not copy this template; G2 must choose persistence/authenticity, and Stage C must define the fuller `C-012` Project Memory/Handoff contract.

## Conflicts and unknowns

- `CONFLICT`: none between inspected exact paths for the research question.
- `UNKNOWN`: current remote `dev` may have moved after the pinned commit; no current-remote claim is made.
- `UNKNOWN`: runtime enforcement of the schemas was not reproduced.
- `UNKNOWN`: target Risk Profile vocabulary and decision authenticity remain human G2 decisions.

## Result

```yaml
result: RESEARCH_QUESTION_ANSWERED_WITH_G2_UNKNOWNS
authority: NONE
copied_solution: false
target_decision_made: false
historical_next_action_at_research_time: USE_FINDINGS_TO_BUILD_G2_OPTION_PACKAGE
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
