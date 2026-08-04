---
artifact_id: AOS3-R15-TEMPLATE-EXECUTION-AUTHORIZATION
artifact_type: IMPLEMENTATION_EXECUTION_AUTHORIZATION_TEMPLATE
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: TEMPLATE_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# Execution Authorization template

Только человек выпускает отдельную заполненную копию для exact Task subject.
Агент не заполняет `issued_by_human`.

```yaml
authorization_id: ""
authorization_class: IMPLEMENTATION_EXECUTION_AUTHORIZATION
issued_by_human: ""
task_id: ""
task_brief_revision: ""
feature_contract_identity: ""
target_binding_id: ""
repository_identity: ""
branch: ""
HEAD_or_baseline: ""
authorized_stage: EXECUTE
allowed_operations: []
allowed_paths: []
forbidden_operations: []
forbidden_paths: []
issued_at: ""
expires_at: ""
single_run: true
authorization_state: GRANTED
```

Contract:

- validation `PASS` does not create authorization;
- empty `issued_by_human` means the template is not issued or valid;
- Commit, Push, Merge and Release are excluded unless the issued record
  contains separate explicit fields for the exact action;
- material drift of Task Brief, Feature Contract, target binding or baseline
  invalidates the authorization;
- terminal execution consumes a single-run authorization;
- a Task Brief cannot embed or simulate this record.
