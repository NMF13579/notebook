---
artifact_id: AOS3-PORTABILITY-DIRECTION-2026-07-31
artifact_type: HUMAN_CONFIRMED_DIRECTION_RECORD
package_revision: DRAFT-R15
revision: R1
status: DRAFT_R15_MATERIALIZATION_OF_HUMAN_DIRECTION
authority: HUMAN_CONFIRMED_DIRECTION
decision_id: AOS-PORTABLE-PACKAGE-DIRECTION-2026-07-31
decision_class: HUMAN_CONFIRMED_DIRECTION
decision_source: CURRENT_EXPLICIT_HUMAN_PROMPT
portable_package_root: AOS-3/
portable_unit: ENTIRE_AOS_3_DIRECTORY
required_external_operational_files: []
source_repository_binding: NONE
target_repository_binding: DEFERRED_UNTIL_TARGET_PREFLIGHT
first_feature_selection: DEFERRED_TO_EXPLICIT_HUMAN_DECISION
implementation_authorization: NONE
git_authorization: NONE
---

# Portability direction

Этот record материализует exact human direction без product, architecture,
repository или permission expansion.

```yaml
target_usage: >
  Папка AOS-3 копируется целиком в target repository. После копирования
  агент начинает package bootstrap и подготовку сборки AOS, используя
  содержимое AOS-3 как переносимый development package.
mandatory_package_entrypoint: AOS-3/AGENTS.md
source_repository_authority_over_target: NONE
target_repository_facts: DIRECT_OBSERVATION_AT_TARGET_PREFLIGHT_ONLY
human_feature_selection: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## Portability contract

```yaml
portable_root: AOS-3/
copy_granularity: WHOLE_DIRECTORY
required_external_operational_files: []
required_source_repository_name: NONE
required_source_branch: NONE
required_source_commit: NONE
target_repository_identity: OBSERVED_AT_TARGET_PREFLIGHT
runtime_toolchain_binding: DEFERRED
dependency_binding: DEFERRED
implementation_authorization: NONE
git_authorization: NONE
portable_binding_state:
  enum:
    - PORTABLE_UNBOUND
    - TARGET_BOUND_FOR_PLANNING
    - EXECUTION_BOUND
```

- `PORTABLE_UNBOUND`: target facts отсутствуют; package bootstrap и author
  self-check разрешены, repository-bound Task запрещён.
- `TARGET_BOUND_FOR_PLANNING`: target facts непосредственно наблюдены и
  записаны; mutation не разрешена.
- `EXECUTION_BOUND`: exact accepted Task Brief и отдельная valid Execution
  Authorization связаны с exact subject.

`implementation_repository: UNASSIGNED` соответствует `PORTABLE_UNBOUND` и
не является package defect. `human_feature_selection: NOT_RUN` блокирует
только feature contract finalization, Task derivation и implementation
planning.

## Path rules

```yaml
logical_package_paths:
  base: TARGET_REPOSITORY_ROOT
  format: AOS-3/...
markdown_links:
  base: CONTAINING_FILE_DIRECTORY
  format: RELATIVE_AND_RESOLVABLE
absolute_operational_paths:
  active_normative_content: FORBIDDEN
historical_machine_local_literals:
  role: INERT_HISTORICAL_LIMITATION
  current_fact_effect: NONE
  operational_link_effect: NONE
```

Machine-local literals внутри явно classified historical Evidence не являются
current facts. Они не блокируют portability, пока отсутствуют active normative
inbound references и operational use.
