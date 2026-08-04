---
artifact_id: AOS3-R15-TEMPLATE-FIRST-VERTICAL-SLICE
artifact_type: FIRST_VERTICAL_SLICE_SELECTION_TEMPLATE
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: TEMPLATE_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# First Vertical Slice Selection template

Копия этого template становится decision candidate. Агент не заполняет human
fields, не выбирает feature и не преобразует отсутствие решения в failure.

```yaml
decision_type: FIRST_VERTICAL_SLICE_SELECTION
feature_or_slice_id: ""
included_features: []
excluded_features: []
user_outcome: ""
exact_contract_owner: ""
exact_contract_revision_or_digest: ""
human_disposition: UNDECIDED
target_repository_binding: ""
decision_date: ""
decided_by_human: ""
```

До exact human decision:

```yaml
portable_package_readiness:
  readiness_state: READY
feature_selection:
  technical_result: NOT_RUN
task_derivation:
  readiness_state: BLOCKED_BY_HUMAN_GATE
  reason: FIRST_VERTICAL_SLICE_SELECTION_REQUIRED
implementation_authorization: NONE
git_authorization: NONE
```

Required decision evidence:

- exact selected slice identity;
- explicit inclusions and exclusions;
- observable user outcome;
- exact contract owner/binding;
- human disposition and human identity/date record;
- target binding identity when the decision depends on target facts.

`UNDECIDED` is a feature-disposition value, not a technical failure and not
permission to infer a default.
