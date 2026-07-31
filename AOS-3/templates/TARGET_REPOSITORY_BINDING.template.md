---
artifact_id: AOS3-R15-TEMPLATE-TARGET-REPOSITORY-BINDING
artifact_type: TARGET_REPOSITORY_BINDING_TEMPLATE
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: TEMPLATE_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# Target Repository Binding template

Этот record заполняется только direct observation в target repository. Он не
является human approval и не меняет repository role.

```yaml
binding_id: ""
binding_state: TARGET_BOUND_FOR_PLANNING
repository_root: ""
repository_identity: ""
branch: ""
HEAD: ""
baseline: ""
worktree_status: ""
staged_changes: []
unstaged_changes: []
untracked_changes: []
remote: ""
nested_repositories: []
symlinks: []
available_toolchain: []
dependency_state: ""
validation_entrypoints: []
network_state: ""
sandbox_state: ""
observed_at: ""
observation_method: ""
implementation_authorization: NONE
git_authorization: NONE
```

Observation rules:

- record `UNKNOWN`, `NOT_FOUND` or `NOT_RUN` instead of guessing;
- redact credentials from remote information;
- record dirty worktree paths without cleaning them;
- do not run install, mutation or network operations as preflight;
- invalidate the binding when repository identity, branch, HEAD or declared
  baseline materially drifts;
- keep planning state separate from `EXECUTION_BOUND`.
