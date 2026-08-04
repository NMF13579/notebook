---
artifact_id: AOS3-R15-TEMPLATE-FEATURE-CONTRACT
artifact_type: FEATURE_SPECIFIC_PRODUCT_CONTRACT_TEMPLATE
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: TEMPLATE_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# Feature-specific Product Contract template

Generic shared defaults and feature dossiers are inputs for review only. They
must not be copied as exact feature behavior without feature-specific human
review.

## Contract identity

```yaml
contract_id: ""
contract_revision: ""
contract_digest: ""
feature_or_slice_id: ""
selected_slice_decision_id: ""
selected_slice_decision_revision_or_digest: ""
target_repository_binding_id: ""
contract_role: DRAFT_FEATURE_SPECIFIC_PRODUCT_CONTRACT
human_contract_decision: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## Actors, outcome, trigger and preconditions

```yaml
actors:
  primary_users: []
  supporting_actors: []
  protected_actors: []
user_outcome: ""
trigger: ""
preconditions: []
```

## Inputs and outputs

```yaml
input_schemas:
  - schema_id: ""
    revision_or_digest: ""
    required_fields: []
    validation_rules: []
output_schemas:
  - schema_id: ""
    revision_or_digest: ""
    required_fields: []
    validation_rules: []
```

## Behavior and state

```yaml
happy_path: []
states: []
transitions:
  - transition_id: ""
    from: ""
    trigger: ""
    to: ""
    observable_effect: ""
persistence_effects:
  - owner: ""
    write_set: []
    zero_write_conditions: []
```

## Failures, recovery and retry

```yaml
failure_taxonomy:
  - failure_id: ""
    condition: ""
    technical_result: NOT_RUN
    user_visible_result: ""
recovery:
  - failure_id: ""
    recovery_action: ""
    authority_required: ""
retry:
  - failure_id: ""
    allowed: false
    limit: 0
    idempotency_rule: ""
```

## Boundaries

```yaml
authority_boundaries: []
dependencies:
  - dependency_id: ""
    dependency_state: HUMAN_DECISION_REQUIRED
    exact_binding: ""
non_goals: []
required_adrs: []
unresolved_material_decisions: []
```

## Acceptance and executable negative scenarios

```yaml
acceptance_criteria:
  - acceptance_id: AC-FEATURE-000
    observable_condition: ""
    evidence_required: []
negative_scenarios:
  - scenario_id: NEG-FEATURE-000
    precondition: ""
    action: ""
    expected_result: ""
    expected_write_set: []
    executable_fixture_or_command: ""
```

Каждый acceptance ID и negative scenario ID уникален внутри exact contract.
Сценарий без fixture/command и expected result не готов для Task readiness.

## Human decision block

```yaml
human_decision:
  decision: ""
  exact_contract_revision: ""
  exact_contract_digest: ""
  decided_by_human: ""
  decided_at: ""
  limitations: []
```

Пока block не содержит exact human `ACCEPT`, contract остаётся DRAFT и не
может быть input для repository-bound Task Brief.
