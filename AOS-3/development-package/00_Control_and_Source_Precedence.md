---
artifact_id: AOS3-DPKG-DOC-000
artifact_type: CONTROL_AND_SOURCE_PRECEDENCE
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R14
status: DRAFT_R14_ROUTE_A_TRACE_CORRECTION_CANDIDATE_READY_FOR_SEPARATE_VALIDATE
authority: PROPOSAL
exact_subject: Portable contract-first package control, source precedence, accepted G1/G2/C1 decisions, Stage C Task candidate inventory, and agent entrypoint for AOS Core v1
created: '2026-07-30'
document_language: ru
technical_identifiers_language: en
source_repository: NMF13579/notebook
source_branch: dev
source_head_at_stage_a_preflight: e1c3bd27f9417d99b365e88525b9a58a2563ec2a
source_head_at_stage_b_preflight: e1c3bd27f9417d99b365e88525b9a58a2563ec2a
source_head_at_stage_c_preflight: e1c3bd27f9417d99b365e88525b9a58a2563ec2a
canonical_knowledge_path: docs/
implementation_repository: UNASSIGNED
human_acceptance: G1_G2_AND_C1_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
stage_state: CORRECTION_EXECUTE_DRAFT_R14_COMPLETED
provenance:
  - path: ../../docs/00_Core.md
    sha256: 96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c
    use: project identity, authority, source precedence, and safety
  - path: ../../docs/01_Product.md
    sha256: bbbce8e166bc4640f8fd98c9407539159a41d216ab9ee993ad2369f07ac81625
    use: users, problems, journeys, product boundaries, and open product decisions
  - path: ../../docs/02_Architecture.md
    sha256: 3724a3369c78f6504c56a0f6d921839839d7adecc9ca806f1fe9d3e65b11be84
    use: accepted architecture fact classes and unresolved architecture boundaries
  - path: ../../docs/03_Development.md
    sha256: 251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1
    use: stage model, validation, reporting, and Git boundaries
  - path: ../../docs/04_Lessons.md
    sha256: e1edd62ec22f109a2b99ac7c4417e5ce94e4e9a0d0ed4c90161a05670d98e1b6
    use: failure and regression routing
  - path: ../../docs/05_Reference.md
    sha256: e7d0dc9aef509853e0f750aa81286eb4a646e6f36c78fb235c9a0d318162287f
    use: targeted research and provenance routing
  - path: ../../docs/06_Features.md
    sha256: 4f6f0e02bc0f89d6f5707111b675962657872e27f29d83389fc8e07caf547cdd
    use: accepted feature inventory with separate item-level dispositions
  - path: ../AOS_Core_Roadmap.md
    sha256: 03208f742a101819da93b2d215252243012e2fb586b3731a1f57e3bb33a93321
    use: DRAFT RMP-001 through RMP-008 documentation pipeline
upstream_links:
  - ../../docs/00_Core.md
  - ../../docs/01_Product.md
  - ../../docs/03_Development.md
  - ../../docs/06_Features.md
  - ../AOS_Core_Roadmap.md
downstream_links:
  - 01_Product_and_Core_V1_Scope.md
  - 02_User_Journeys_and_Workflows.md
  - 03_Architecture_and_Decisions.md
  - 04_Runtime_and_Data_Contracts.md
  - 05_Quality_Recovery_and_Security.md
  - 06_Traceability_and_Readiness.md
  - 07_Implementation_Handoff.md
  - decisions/DECISION-RECORD-TEMPLATE.md
  - decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md
  - decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
  - decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
  - research/RESEARCH-RECORD-TEMPLATE.md
  - tasks/TASK-TEMPLATE.md
  - tasks/TASK-GRAPH.md
  - tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md
  - tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md
  - adapters/CODEX.md
limitations:
  - The package is a pilot-only DRAFT candidate.
  - G1 is bound to the exact Stage A aggregate SHA-256.
  - G2 decisions are bound to the exact Stage B aggregate SHA-256.
  - The human instructed that no implementation repository be created now and that documentation be formed only in NMF13579/notebook.
  - NMF13579/notebook remains the documentation/knowledge repository and is not an implementation repository.
  - C1 accepted 137 DRAFT-R4 subject definitions; current PSC-A, WFC-A/B/C, and AC-WFC-A-001-01..07 differ from their accepted bytes, so 126 unchanged subjects remain current and eleven C1 bindings are stale.
  - Ten new AC IDs plus SCH-PRODUCT-SPEC-001 and SCH-FEATURE-PASSPORT-001 are DRAFT and have no human acceptance.
  - Task template, graph, and two Task Briefs are DRAFT documentation candidates and are not human-accepted; AOS3-DPKG-TASK-003 is graph-only and blocked.
  - BLK-006 preserves the canonical status-axis conflict and forbids a false TechnicalResult/ResultEnvelope conformance claim.
  - DRAFT-R10 semantic validation failed because its manually maintained forward and reverse requirement-contract relation sets did not round-trip; the mechanical branch remained UNKNOWN because it did not complete all required checks.
  - DRAFT-R11 replaced those two independently edited relation sets with one atomic registry and two derived projections; validation confirmed their equality but found three missing Task-002-to-CTR-002 semantic relations.
  - DRAFT-R12 added those three exact relations and a materialized-Task relation-closure invariant; its validation found one omitted materialized Task projection for REQ-ARCH-003.
  - DRAFT-R13 derived materialized Task projections from existing Task Brief `derived_from` fields and added the omitted Task-002 entry and existing CTR-002 zero-write Evidence path; its separate validation failed on `VAL-R13-001` and `VAL-R13-002`.
  - DRAFT-R14 route A removes the unsupported `REQ-ARCH-009 → CTR-002 → AOS3-DPKG-TASK-002` derivation, retains `REQ-ARCH-009` as a deferred `DEC-ARCH-008` compatibility boundary, and removes the non-derived materialized-Task note from the `REQ-WF-006` forward Task projection; independent validation remains NOT_RUN.
  - No implementation, independent validation, or Git operations are authorized.
documentation_mutation_authorization:
  stage: CORRECTION_EXECUTE_DRAFT_R14_FOR_VAL_R13_001_AND_VAL_R13_002
  source: USER_EXACT_R14_ROUTE_A_CORRECTION_EXECUTE_AUTHORIZATION_2026-07-31
  received_at: '2026-07-31T04:38:14Z'
  exact_authorization_text_sha256: 9e857a410cbc0c710da8f51d6751a2720128d335a6c25f52d034fdf00725cda6
  exact_source_candidate_sha256: 880dfdd3260beb19fa73078c9df50b84172ebbeec9719d62ad23b81c1407044c
  selected_route: R13_FIX_A_REMOVE_UNSUPPORTED_REQ_ARCH_009_DERIVATION_AND_CLEAN_TASK_PROJECTION
  relation_registry:
    registry_id: TRC-REG-001
    owner_path: AOS-3/development-package/06_Traceability_and_Readiness.md
    row_count: 83
    payload_sha256: af15f5e0af1ca667136e1ffc2352e3acc7bf3cb5c037f62f558818889170aa69
    removed_relation: "REQ-ARCH-009<TAB>CTR-002<TAB>REVERSE_ONLY_DRAFT_R10<LF>"
  acceptance_projection_consequence: UNCHANGED_126_CURRENT_11_STALE_12_NEW_DRAFT
  allowed_paths: [AOS-3/development-package/**/*.md]
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  allowed_correction_subject: VAL-R13-001 unsupported REQ-ARCH-009 to CTR-002 to Task-002 Evidence path and VAL-R13-002 non-derived REQ-WF-006 materialized Task projection; remove only those derivations, regenerate registry projections, retain the compatibility boundary as deferred, and propagate receipt/revision/status/validation-history/next-action metadata
  canonical_docs_mutation: FORBIDDEN
  roadmap_mutation: FORBIDDEN
  independent_validation: FORBIDDEN
  consumed_for_this_candidate: true
implementation_authorization: NONE
git_authorization: NONE
---

# 00 — Control and Source Precedence

## 1. Назначение

Это обязательная входная точка переносимого contract-first пакета AOS Core v1. Новый AI-агент начинает здесь и без истории чата определяет:

1. какие sources являются canonical;
2. какой stage и exact candidate активны;
3. какие решения принадлежат человеку;
4. какие artifacts разрешено создавать;
5. что блокирует зависимую работу;
6. какой один следующий шаг разрешён.

```text
Documentation ≠ implementation
DRAFT ≠ human acceptance
Evidence ≠ approval
PASS ≠ approval
Task Brief ≠ Execution Authorization
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

## 2. Текущая identity и authority

```yaml
package:
  id: AOS3-DEVELOPMENT-PACKAGE
  revision: DRAFT-R14
  status: DRAFT_R14_ROUTE_A_TRACE_CORRECTION_CANDIDATE_READY_FOR_SEPARATE_VALIDATE
  authority: PROPOSAL
  role: PORTABLE_CORE_V1_DOCUMENTATION_CANDIDATE
  canonical_knowledge_source: docs/
  implementation_repository: UNASSIGNED
  human_acceptance:
    current_accepted_subjects: 126
    stale_c1_subjects: [PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, AC-WFC-A-001-01..07]
    new_draft_acceptance_ids: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05]
    new_draft_schema_ids: [SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
  task_candidate_acceptance: NOT_RUN
  implementation_authorization: NONE
  git_authorization: NONE
current_stage:
  id: CORRECTION_EXECUTE_DRAFT_R14_FOR_VAL_R13_001_AND_VAL_R13_002
  type: EXECUTE
  result_state: AUTHOR_SELF_CHECK_COMPLETED
  independent_validation:
    DRAFT_R10: FAIL
    DRAFT_R11: FAIL
    DRAFT_R12: FAIL
    DRAFT_R13: FAIL
    DRAFT_R14: NOT_RUN
  next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
  stop: true
```

G1 принят для exact Stage A candidate. G2 принят для exact Stage B candidate `d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d` и разложен в `DEC-ARCH-001..008`.

`G2-OPT-A` принят как logical architecture bundle. Позднее human clarification установило: repository сейчас не создавать, документацию формировать только в `NMF13579/notebook`, а `implementation_repository` сохранить `UNASSIGNED`. Это блокирует physical topology и repository-bound execution, но не portable documentation или будущие portable Task candidates.

Stage C подготовил owners `03..07`, contracts `CTR-001..007`, scenarios `SCN-001..044`, traceability, handoff и Codex adapter. Человек затем принял 137 определённых `REQ`, `PSC/WFC/CTR`, `AC` и `SCN-001..044` exact candidate `00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262`. Решение и стабильный subject digest зафиксированы в [`DEC-CONTRACT-001`](decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md).

Stage D для DRAFT-R5 candidate `c21bf54b62cfe78b4c72527390c834fbe4534acca0ff730bdcde70f5b5316bed` завершился техническим `FAIL`: semantic review обнаружил decision-witness, Task namespace/binding/mapping, WFC completeness, shared-schema, status-axis и stale-routing defects. Этот результат не разрешал correction. Человек отдельно принял package-local namespace и авторизовал exact DRAFT-R6 correction внутри package root.

Отдельная read-only validation exact DRAFT-R6 candidate `0309143fa4d048af18c9bdfdc27acd356e927facf1f7c3add39fcece2f529efe` также завершилась техническим `FAIL` (`VAL-R6-001`). Она обнаружила, что C1 manifest не был материализован, `WFC-A-001` изменился без stale-routing, а Task-003 был создан из stale/new DRAFT upstream. Validation не исправляла candidate и не разрешала correction.

Человек затем авторизовал узкую DRAFT-R7 correction: сохранить byte-exact [`C1_ACCEPTED_SUBJECT_MANIFEST.tsv`](decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv), удалить текущий документ Task-003 и исправить только findings `VAL-R6-001`. После correction переносимые [`TASK-TEMPLATE`](tasks/TASK-TEMPLATE.md), [`TASK-GRAPH`](tasks/TASK-GRAPH.md) и два bounded Task Briefs используют namespace `AOS3-DPKG-TASK-###`. Они имеют repository binding `PORTABLE_UNBOUND`, не приняты человеком и не разрешают implementation, validation или Git actions. `AOS3-DPKG-TASK-003..007` существуют только как graph nodes.

Отдельная read-only validation exact DRAFT-R7 candidate `6a06c761c9c722141efb4d2a900632ec4ab59ef9b921645ae028fb39d51db65b` завершилась техническим `FAIL` (`VAL-R7-001`). Она подтвердила structural integrity, но обнаружила несоответствие `HumanDecisionRecord` собственной схеме, конфликтующие определения одинаковых WFC acceptance IDs, stale `DEC-ARCH-001 R3` locators и неканонические schema-ID aliases. Validation не изменяла candidate и не разрешала correction.

Человек затем выбрал `D1`: закрытый `aos.decision/v1` tagged union для четырёх фактически используемых `subject.kind`; и `A2`: WFC envelopes являются единственными владельцами acceptance definitions, а таблицы — их exact derived mirrors. Поэтому текущие `AC-WFC-A-001-01..07` также stale против C1. Из 137 исторически принятых subjects 127 остаются byte-bound/current, десять stale, а десять `AC-WFC-B/C-*` и два shared schema records являются новыми DRAFT subjects. Task-003 блокируется stale `WFC-A-001`, stale `AC-WFC-A-*` и непринятыми shared schemas; Task-004/007 блокируются соответствующими stale WFC/new AC subjects. Это не отзывает историческое C1 Evidence и не расширяет authority.

Отдельная read-only validation exact DRAFT-R8 candidate `f6443683a12094d1357ae8c44b5937f1aaf4f276e088b9c9c1e99b1dcfc4ac97` завершилась техническим `FAIL` (`VAL-R8-001`). Primary deterministic check обнаружил duplicate YAML mapping key `authority` в `PSC-A-001` и `WFC-A-001`: redundant scalar `PROPOSAL` конфликтовал с operational authority map. Validation не изменяла candidate и не разрешала correction.

Человек затем авторизовал route `Y1`: удалить только два redundant scalar authority fields, сохранить operational authority maps и применить детерминированную acceptance projection `126_CURRENT_11_STALE_12_NEW_DRAFT`. Изменение `PSC-A-001` делает его прежнюю C1 binding stale; Task-003 дополнительно блокируется этим subject. Авторизация не принимает новые bytes и не разрешает independent validation, implementation или Git actions.

Отдельная read-only validation exact DRAFT-R9 candidate `61ebdaa63d4fce3034db1c3fceaa3d86c35e5849cc1fc3f5bdb75e8cf3ea2bad` завершилась техническим `FAIL` (`VAL-R9-001`). Она обнаружила три отсутствующие reverse trace links (`REQ-WF-004 → CTR-001`, `REQ-WF-004 → CTR-004`, `REQ-WF-008 → CTR-002`) и отсутствие scenario mappings для `AC-PSC-A-001-01..08`. Validation не изменяла candidate и не разрешала correction.

Человек затем принял route `T2` и отдельно авторизовал bounded DRAFT-R10 correction: добавить восемь explicit `AC-PSC-A-001-01..08` mappings к уже существующим `SCN-*`, восстановить три reverse links, записать `VAL-R9-001`/authorization receipt и распространить только package revision, status и next-action metadata. Авторизация запрещает изменение accepted requirement/contract/acceptance/scenario definitions, Task derivation/materialization, C1 projection, manifest, `/docs`, Roadmap, implementation и Git.

Отдельная read-only validation exact DRAFT-R10 candidate `8b815b48fc6b3114e6bbaf1b8cfa3ac1cace7bb1b3119929a8f023ea2343b5b6` завершилась общим техническим `FAIL` (`VAL-R10-001`). Semantic branch обнаружил, что вручную поддерживаемые forward и reverse requirement-contract relation sets не round-trip. Mechanical branch остался `UNKNOWN`: требуемые YAML, duplicate-key, A2 и exact acceptance-projection checks не были завершены. Validation не изменяла candidate и не разрешала correction.

Человек затем принял route `R10-TRACE-C` и отдельно авторизовал bounded DRAFT-R11 correction: материализовать exact atomic relation registry `TRC-REG-001` из 81 строки с SHA-256 `d55e8b3603a5bf64f97ef43f9569e7aebfad51fe20f180991cb5c1026b78ba15`, генерировать из него обе requirement-contract projections, добавить deterministic equality invariants, записать `VAL-R10-001`/authorization receipt и распространить только package revision, status, validation history и next-action metadata. Авторизация запрещает изменение requirement/PSC/WFC/CTR/acceptance/scenario definitions, C1 projection/manifest, Task semantics/materialization/derivation, `/docs`, Roadmap, repository assignment, runtime code, implementation и Git.

Отдельная read-only validation exact DRAFT-R11 candidate `88eefc88a9e2a1ebfe06b4be6becec9a807452e7c1ff2092eef60a0d751eb5a4` завершилась общим техническим `FAIL` (`VAL-R11-001`). Registry содержал 81 exact relation, а обе его projections совпадали с registry, но materialized Task-002 выводился из трёх requirements без relation к его derived contract `CTR-002`: `REQ-CV1-009`, `REQ-WF-004`, `REQ-WF-010`. Validation не изменяла candidate и не разрешала correction.

Человек принял design `R11-FIX-A` и отдельно авторизовал bounded DRAFT-R12 correction: добавить три exact semantic-completeness relation, получить registry из 84 строк с SHA-256 `87972f97bafe77c621ce01b90bfd60681dd617e3108de38a13b5ecd03d7c110c`, заново вывести обе projections, добавить materialized-Task relation-closure invariant и распространить только receipt/revision/status/validation-history/next-action metadata. Авторизация запрещает изменение endpoint definitions, C1 projection/manifest, Task content/derivation/materialization/graph semantics, `/docs`, Roadmap, implementation repository, runtime code, independent validation и Git.

Отдельная read-only validation exact DRAFT-R12 candidate `291d3771e0b652cc152a8b706fcdeeb1479ac268c1837fd0cce721d7a11f5a8a` завершилась общим техническим `FAIL` (`VAL-R12-001`). Она подтвердила 84-row `TRC-REG-001`, equality обеих requirement-contract projections и materialized-Task relation closure, но обнаружила, что forward row `REQ-ARCH-003` не содержит materialized `AOS3-DPKG-TASK-002`, хотя Task Brief выводится из `REQ-ARCH-003`/`CTR-002` и reverse projection содержит Task-002. Validation не изменяла candidate и не разрешала correction.

Человек затем авторизовал route `R12-FIX-B` для bounded DRAFT-R13 correction: existing Task Brief `derived_from` fields становятся единственным владельцем materialized Task projections; forward/reverse materialized entries выводятся из них, graph-only mappings остаются отдельно обозначенной проекцией `TASK-GRAPH`, а `REQ-ARCH-003` получает пропущенный Task-002 и существующий zero-write Evidence path `AC-CTR-002-01`/`SCN-005`. `TRC-REG-001`, endpoint definitions, Task derivation/materialization/graph semantics, C1 projection/manifest, `/docs`, Roadmap, implementation, independent validation и Git остаются неизменными или запрещёнными.

Отдельная read-only validation exact DRAFT-R13 candidate `880dfdd3260beb19fa73078c9df50b84172ebbeec9719d62ad23b81c1407044c` завершилась общим техническим `FAIL`. `VAL-R13-001` обнаружил, что путь `REQ-ARCH-009 → CTR-002 → AOS3-DPKG-TASK-002` не имеет executable acceptance/scenario Evidence для unknown-format rejection. `VAL-R13-002` обнаружил, что forward Task cell `REQ-WF-006` дополнительно упоминает materialized `AOS3-DPKG-TASK-001..002`, хотя ни один их `derived_from.requirements` не содержит `REQ-WF-006`. Candidate, C1 manifest, canonical `/docs`, Roadmap, branch и HEAD validation не изменяла.

Человек выбрал route A и отдельно авторизовал bounded DRAFT-R14 correction: удалить `REQ-ARCH-009` и `DEC-ARCH-008` только из Task-002 derivation, удалить exact registry relation `REQ-ARCH-009 → CTR-002`, заново вывести обе registry projections, сохранить `REQ-ARCH-009` как deferred compatibility boundary без текущего contract/Task, удалить non-derived materialized-Task note из `REQ-WF-006`, записать оба findings/authorization receipt и распространить только package revision/status/validation-history/next-action metadata. Accepted endpoint definitions, C1 manifest/projection, Task outcome/scope/contracts/acceptance/scenarios, Task graph, `/docs`, Roadmap, implementation и Git не разрешены к изменению.

Top-level `package_revision` во всех artifacts означает membership в текущем package candidate и поэтому равен `DRAFT-R14`. Исторические Gate G1/G2 revisions and hashes сохраняются в их `candidate_binding`; C1 сохраняет исходный aggregate и отдельный accepted-subject manifest. Собственный `revision` каждого artifact меняется только при изменении его subject content.

## 3. Source precedence

При расхождении утверждений агент использует следующий порядок:

1. current explicit human decision, связанное с exact subject/revision/hash;
2. human-accepted artifact в declared fact class;
3. direct current repository observation для mutable facts;
4. DRAFT/PROPOSAL artifacts;
5. exact reference evidence с authority `NONE`;
6. reports, chat summaries и notes;
7. agent synthesis.

Conflict не разрешается молча. Он получает claim class `CONFLICT` и блокирует только зависимый artifact или action.

Допустимые claim classes:

```text
OBSERVED_AT_SNAPSHOT
REPORTED
SYNTHESIZED
CONFLICT
NOT_FOUND
UNKNOWN
NOT_RUN
BLOCKED
```

## 4. Source inventory

Stage A/Stage B/Stage C source snapshot:

```yaml
snapshot:
  repository_root: /Users/muhammed/Documents/GitHub/notebook
  branch: dev
  head: e1c3bd27f9417d99b365e88525b9a58a2563ec2a
  working_tree_before_stage_a: CLEAN_AT_PREFLIGHT
  target_path_before_execution: NOT_FOUND
  stage_a_candidate_aggregate_sha256: 4fe1a0fcc8493d00e60694f86ac734fac197f005246b6ae7cb2689ab6fd9ce80
  stage_b_candidate_aggregate_sha256: d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d
  stage_c_contract_candidate_aggregate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
  c1_accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
  stage_d_draft_r5_candidate_aggregate_sha256: c21bf54b62cfe78b4c72527390c834fbe4534acca0ff730bdcde70f5b5316bed
  stage_d_draft_r5_result: FAIL
  draft_r6_final_aggregate_sha256: 0309143fa4d048af18c9bdfdc27acd356e927facf1f7c3add39fcece2f529efe
  stage_d_draft_r6_result: FAIL
  draft_r7_final_aggregate_sha256: 6a06c761c9c722141efb4d2a900632ec4ab59ef9b921645ae028fb39d51db65b
  stage_d_draft_r7_result: FAIL
  draft_r8_final_aggregate_sha256: f6443683a12094d1357ae8c44b5937f1aaf4f276e088b9c9c1e99b1dcfc4ac97
  stage_d_draft_r8_result: FAIL
  draft_r9_final_aggregate_sha256: 61ebdaa63d4fce3034db1c3fceaa3d86c35e5849cc1fc3f5bdb75e8cf3ea2bad
  stage_d_draft_r9_result: FAIL
  draft_r10_final_aggregate_sha256: 8b815b48fc6b3114e6bbaf1b8cfa3ac1cace7bb1b3119929a8f023ea2343b5b6
  stage_d_draft_r10_result: FAIL
  draft_r11_final_aggregate_sha256: 88eefc88a9e2a1ebfe06b4be6becec9a807452e7c1ff2092eef60a0d751eb5a4
  stage_d_draft_r11_result: FAIL
  draft_r12_final_aggregate_sha256: 291d3771e0b652cc152a8b706fcdeeb1479ac268c1837fd0cce721d7a11f5a8a
  stage_d_draft_r12_result: FAIL
  draft_r13_final_aggregate_sha256: 880dfdd3260beb19fa73078c9df50b84172ebbeec9719d62ad23b81c1407044c
  stage_d_draft_r13_result: FAIL
  draft_r14_final_aggregate_sha256: COMPUTE_AFTER_FINAL_BYTES_AND_REPORT_EXTERNALLY
  g1_human_confirmation: OBSERVED_AT_SNAPSHOT
  g2_human_confirmation: OBSERVED_AT_SNAPSHOT
  c1_human_confirmation: OBSERVED_AT_SNAPSHOT
  g2_repository_value: OWNER/REPOSITORY
  g2_repository_value_classification: UNRESOLVED_PLACEHOLDER
  latest_repository_clarification: DO_NOT_CREATE_REPOSITORY
  documentation_repository: NMF13579/notebook
  effective_implementation_repository: UNASSIGNED
  inventory_class: OBSERVED_AT_SNAPSHOT
```

| Source | Revision/status | Authority/use | Stage C inspection |
|---|---|---|---|
| [`docs/00_Core.md`](../../docs/00_Core.md) | `R4-RU`, `HUMAN_ACCEPTED_KNOWLEDGE_BASELINE` | Identity, precedence, authority, safety | Relevant content inspected |
| [`docs/01_Product.md`](../../docs/01_Product.md) | `R4-RU`, accepted baseline | Users, problems, journeys, product decisions | Full document inspected |
| [`docs/02_Architecture.md`](../../docs/02_Architecture.md) | `R4-RU`, accepted baseline | Architecture fact classes and decision boundary | Full document inspected |
| [`docs/03_Development.md`](../../docs/03_Development.md) | `R4-RU`, accepted baseline | `PLAN → EXECUTE → VALIDATE → REVIEW → DELIVER` | Full document inspected |
| [`docs/04_Lessons.md`](../../docs/04_Lessons.md) | `R4-RU`, accepted baseline | Failures, lessons, regressions | Full document inspected |
| [`docs/05_Reference.md`](../../docs/05_Reference.md) | `R4-RU`, accepted baseline | Reference provenance and research routing | Full document inspected |
| [`docs/06_Features.md`](../../docs/06_Features.md) | `R4-RU`, accepted inventory | Feature dossiers and item-level disposition | Relevant `FTR-001..014`, `FTR-016`, and `FTR-019` dossiers inspected |
| [`AOS_Core_Roadmap.md`](../AOS_Core_Roadmap.md) | `R3`, `DRAFT`, `PROPOSAL` | `RMP-001..008` documentation pipeline | Full document inspected |

All SHA-256 values are stored in frontmatter. A later stage must recheck mutable facts; this inventory does not remain current automatically.

## 5. Package inventory and owner map

### 5.1 Current DRAFT-R14 correction candidate

```yaml
expected_file_count: 37
expected_markdown_file_count: 36
expected_non_markdown_file_count: 1
allowed_non_markdown_paths:
  - decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
task_namespace: AOS3-DPKG-TASK-###
roadmap_task_namespace: TASK-###
namespace_owner_decision: DEC-CORR-001
```

| Stable ID | Path | Owner subject | Status |
|---|---|---|---|
| `AOS3-DPKG-DOC-000` | `00_Control_and_Source_Precedence.md` | Control, precedence, inventory, gates, and routing | `DRAFT_R14_ROUTE_A_TRACE_CORRECTION_CANDIDATE_READY_FOR_SEPARATE_VALIDATE` |
| `AOS3-DPKG-DOC-001` | `01_Product_and_Core_V1_Scope.md` | Product boundary, A→B→C scope, requirements, first-slice contract | `DRAFT_SOURCE_WITH_PARTIAL_C1_ACCEPTANCE` |
| `AOS3-DPKG-DOC-002` | `02_User_Journeys_and_Workflows.md` | Journeys, states, transitions, failures, recovery, checkpoints | `DRAFT_SOURCE_WITH_PARTIAL_C1_ACCEPTANCE` |
| `AOS3-DPKG-DOC-003` | `03_Architecture_and_Decisions.md` | Accepted architecture boundaries and logical design | `DRAFT_SOURCE_WITH_HUMAN_ARCHITECTURE_AND_C1_ACCEPTED_SUBJECTS` |
| `AOS3-DPKG-DOC-004` | `04_Runtime_and_Data_Contracts.md` | Schemas, I/O, effects, permissions, idempotency, `CTR-001..007` | `DRAFT_SOURCE_WITH_C1_ACCEPTED_SUBJECTS_AND_NEW_DRAFT_SCHEMAS` |
| `AOS3-DPKG-DOC-005` | `05_Quality_Recovery_and_Security.md` | Acceptance, `SCN-001..044`, recovery, privacy, security | `DRAFT_SOURCE_WITH_C1_ACCEPTED_SCENARIOS` |
| `AOS3-DPKG-DOC-006` | `06_Traceability_and_Readiness.md` | Atomic registry, derived requirement-contract and materialized Task projections, and blockers | `DRAFT_R14_ROUTE_A_TRACE_CORRECTION` |
| `AOS3-DPKG-DOC-007` | `07_Implementation_Handoff.md` | Portable implementation/task/validation handoff | `DRAFT_R14_ROUTE_A_TRACE_CORRECTION_HANDOFF_READY_FOR_SEPARATE_VALIDATE` |
| `AOS3-DPKG-TPL-DEC-001` | `decisions/DECISION-RECORD-TEMPLATE.md` | Human decision/ADR record schema | `DRAFT` |
| `AOS3-DPKG-TPL-RSR-001` | `research/RESEARCH-RECORD-TEMPLATE.md` | Targeted reference research schema | `DRAFT` |
| `DEC-PROD-001..006` | `decisions/DEC-PROD-*.md` | Exact G1 product decisions | `HUMAN_DECIDED` |
| `DEC-ARCH-001` | `decisions/DEC-ARCH-001_Implementation_Repository.md` | Documentation-only notebook boundary and deferred implementation repository | `HUMAN_DECIDED_IMPLEMENTATION_REPOSITORY_DEFERRED` |
| `DEC-ARCH-002..008` | `decisions/DEC-ARCH-*.md` | Exact G2 architecture decisions and ADRs | `HUMAN_DECIDED` |
| `DEC-CONTRACT-001` | `decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md` | Exact C1 acceptance and accepted-subject manifest | `HUMAN_DECIDED` |
| `AOS3-C1-SUBJECT-MANIFEST-001` | `decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv` | Byte-exact persisted C1 accepted-subject manifest | `HUMAN_ACCEPTANCE_WITNESS_PAYLOAD` |
| `DEC-CORR-001` | `decisions/DEC-CORR-001_Package_Local_Task_Namespace.md` | Package-local Task namespace and bounded DRAFT-R6 through DRAFT-R14 correction receipts | `HUMAN_DECIDED` |
| `AOS3-DPKG-G2-OPT-001` | `decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md` | Decision-ready G2 architecture alternatives | `DRAFT` |
| `RSR-001` | `research/RSR-001_AgentOS_Interview_and_Product_Spec.md` | Exact AgentOS interview/spec research | `COMPLETED_WITH_LIMITATIONS`, authority `NONE` |
| `RSR-002` | `research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md` | Exact AOS-FARM decision/recovery research | `COMPLETED_WITH_LIMITATIONS`, authority `NONE` |
| `RSR-003` | `research/RSR-003_AgentOS_Task_Authorization_and_Handoff.md` | Exact AgentOS Task/auth/result/handoff research | `COMPLETED_WITH_LIMITATIONS`, authority `NONE` |
| `RSR-004` | `research/RSR-004_AOS_FARM_Candidate_Validation_and_Recovery.md` | Exact AOS-FARM candidate/validation/recovery research | `COMPLETED_WITH_LIMITATIONS`, authority `NONE` |
| `AOS3-DPKG-TPL-TASK-001` | `tasks/TASK-TEMPLATE.md` | Portable bounded Task Brief schema | `DRAFT` |
| `AOS3-DPKG-TASK-GRAPH-001` | `tasks/TASK-GRAPH.md` | Seven-node contract-derived Task graph | `DRAFT_DERIVED_VIEW` |
| `AOS3-DPKG-TASK-001` | `tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md` | Portable Core scaffold candidate | `DRAFT_TASK_CANDIDATE` |
| `AOS3-DPKG-TASK-002` | `tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md` | Portable bootstrap candidate | `DRAFT_TASK_CANDIDATE` |
| `AOS3-DPKG-ADAPTER-CODEX-001` | `adapters/CODEX.md` | Replaceable Codex routing | `DRAFT`, adapter authority only |

### 5.2 Task compilation boundary

`AOS3-DPKG-TASK-001..002` are materialized and derive only from current unchanged C1-accepted upstream IDs; neither depends on the eleven stale or twelve new DRAFT subjects. `AOS3-DPKG-TASK-003..007` are graph-only and have no Task Brief files. Node `003` is blocked by stale `PSC-A-001`, stale `WFC-A-001`, stale `AC-WFC-A-001-01..07`, and two new DRAFT shared schemas; nodes `004` and `007` are blocked by their stale WFC/new AC subjects. All Task artifacts are `PORTABLE_UNBOUND`; human Task acceptance, repository binding, Risk assignment, execution, validation, and Git authority remain `NOT_RUN` or `NONE`.

## 6. Stable ID registry

| Namespace | Subject | Allocation rule |
|---|---|---|
| `AOS3-DPKG-DOC-000..007` | Eight owner documents | Fixed; never reused |
| `DEC-PROD-###`, `DEC-ARCH-###`, `DEC-CORR-###` | Human product, scope, architecture, or correction-scope decision | One exact subject per record |
| `ADR-001..008` | Architecture decision identity paired with `DEC-ARCH-001..008` | One artifact owns both human decision and ADR consequences |
| `RSR-###` | One targeted reference research question | Exact repository/ref/commit/path required |
| `REQ-CV1-###`, `REQ-WF-###`, `REQ-ARCH-###` | Product/workflow/architecture requirement | Effective disposition owned by exact human decision |
| `PSC-*`, `WFC-*` | Product-slice and workflow contracts | Effective disposition and dependency state are separate axes |
| `CTR-001..007` | Implementation-grade portable contract | Must trace to `RMP-*`, requirements, acceptance, and scenarios |
| `SCN-001..044` | Positive, negative, failure, or recovery scenario | Accepted contract behavior; execution remains `NOT_RUN` |
| `AOS3-DPKG-TASK-001..007` | Package-local bounded Task Brief or reserved graph node | Must derive only from current accepted upstream IDs; owned only inside this package |
| Roadmap `TASK-###` | Separate Roadmap Task identity | Owned by `AOS-3/AOS_Core_Roadmap.md`; never populated or inferred by this package |

IDs remain stable across revisions. Status changes never cause renumbering.

## 7. Agent operating contract

An AI-agent must:

1. read this document first;
2. revalidate repository identity and candidate revision before mutation;
3. inspect only relevant canonical owners;
4. distinguish facts, proposals, decisions, Evidence, validation, and Git authority;
5. preserve `UNKNOWN` and `NOT_RUN`;
6. stop at a human gate;
7. create no Task from a `DRAFT` contract;
8. perform no implementation or Git action from documentation authority;
9. use reference repositories only for an exact gap;
10. report one `next_required_action`.

Forbidden automatic transitions:

```text
Stage A → G1
G1 → Stage B
Stage B → G2
G2 → Stage C
Unaccepted Stage C contracts → Task artifacts
Stage C Task compilation → VALIDATE
Stage C → VALIDATE
VALIDATE → REVIEW
REVIEW → Git delivery
```

Each arrow requires the authority stated by the receiving stage.

## 8. Codex routing — hash-bound pilot

The Stage B routing candidate was included in the exact G2-bound aggregate SHA-256 and is used only as a pilot for this Stage C documentation run. It is not a general implementation or multi-agent authorization. The replaceable adapter is [`adapters/CODEX.md`](adapters/CODEX.md).

| Role | Responsibility | Mutation authority |
|---|---|---|
| `documentation_architect` | Primary thread and only writer | Only within an exact human-authorized documentation stage |
| `mechanical_checker` | Deterministic inventories, IDs, links, fences, manifests, checksums | `NONE`, read-only |
| `reference_explorer` | Exact repository/ref/commit/path research | `NONE`, read-only |
| `contract_analyst` | Contracts, contradictions, failures, recovery, negative cases | `NONE`, read-only |
| `semantic_reviewer` | Consistency, traceability, authority, false-readiness review | `NONE`, read-only |

When the current environment and instructions permit delegation, concurrency is limited to at most two read-only subagents. Subagents do not write files, mutate Git, make human decisions, expand scope, retry terminal results, or spawn subagents.

`mechanical_checker` is statically bound to `gpt-5.6-luna` because `gpt-5.3-codex-spark` was absent from the configuration-time model catalog. This is not an observed runtime fallback. Runtime model fallback and same-request retry are forbidden.

## 9. Reference routing

Reference repositories:

- [NMF13579/AOS-FARM — `dev`](https://github.com/NMF13579/AOS-FARM/tree/dev)
- [NMF13579/AgentOS — `dev`](https://github.com/NMF13579/AgentOS/tree/dev)

They are `READ_ONLY_REFERENCE` with authority `NONE`.

Required route:

```text
selected feature
→ explicit knowledge gap
→ narrow research question
→ exact repository/ref/commit/path
→ docs/contracts/tests/code/negative fixtures
→ classified finding with provenance
```

Stage B and Stage C completed four bounded read-only research records at the exact pinned commits:

- [`RSR-001`](research/RSR-001_AgentOS_Interview_and_Product_Spec.md) — [AgentOS `e3a60a9…`](https://github.com/NMF13579/AgentOS/tree/e3a60a92fbd5e78e583cddb519d39527583f3433), interview/Product Spec boundary;
- [`RSR-002`](research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md) — [AOS-FARM `71b87f3…`](https://github.com/NMF13579/AOS-FARM/tree/71b87f3dfb9fe3735c7659c123cd86db3f577201), decision/Risk Profile/recovery boundary.
- [`RSR-003`](research/RSR-003_AgentOS_Task_Authorization_and_Handoff.md) — [AgentOS `e3a60a9…`](https://github.com/NMF13579/AgentOS/tree/e3a60a92fbd5e78e583cddb519d39527583f3433), Task/authorization/result/handoff boundary;
- [`RSR-004`](research/RSR-004_AOS_FARM_Candidate_Validation_and_Recovery.md) — [AOS-FARM `71b87f3…`](https://github.com/NMF13579/AOS-FARM/tree/71b87f3dfb9fe3735c7659c123cd86db3f577201), candidate/validation/unknown-outcome boundary.

No runtime or validators were executed. Reference authority remains `NONE`.

## 10. RMP-001..008 gap register

| Gap ID | Roadmap item | Exact unresolved subject | Claim class | Blocks | Gate |
|---|---|---|---|---|---|
| `GAP-RMP-001-001` | `RMP-001` | First user/job/outcome/slice/scope/non-goals | `OBSERVED_AT_SNAPSHOT` — resolved by `DEC-PROD-001..004` | None for DRAFT contract work | `G1` completed |
| `GAP-RMP-002-001` | `RMP-002` | Exact implementation repository; dependency/OS matrix | repository intentionally `UNASSIGNED`, dependencies `UNKNOWN` | Physical scaffold paths, repository-bound Task enrichment, implementation checks | Future repository binding gate |
| `GAP-RMP-003-001` | `RMP-003` | Exact install roots/commands and implementation Evidence | `UNKNOWN`/`NOT_RUN` | Repository-bound bootstrap execution | Future repository binding plus implementation |
| `GAP-RMP-004-001` | `RMP-004` | Product Spec ↔ Feature Passport and split boundary are decided; current PSC-A-001, WFC-A-001, AC-WFC-A-001-01..07, SCH-PRODUCT-SPEC-001, and SCH-FEATURE-PASSPORT-001 are not C1-current at their new bytes | PSC, WFC, and seven AC C1 bindings `STALE`; schemas `DRAFT` | AOS3-DPKG-TASK-003 materialization | New exact human contract decision after DRAFT-R14 validation/review |
| `GAP-RMP-005-001` | `RMP-005` | Human acceptance of corrected WFC-B-001 and AC-WFC-B-001-01..05 | current definitions `DRAFT`; prior WFC C1 binding `STALE`; ACs new | AOS3-DPKG-TASK-004 materialization and dependent graph progression | New exact human contract decision after DRAFT-R14 validation/review |
| `GAP-RMP-006-001` | `RMP-006` | Runtime proof of authorization/idempotency/recovery contracts | `NOT_RUN` | Execution implementation/readiness | Later implementation/validation |
| `GAP-RMP-007-001` | `RMP-007` | Independent-validation threshold and runtime Evidence persistence proof | `UNKNOWN`/`NOT_RUN` | Validation implementation/readiness | Contract review then implementation |
| `GAP-RMP-008-001` | `RMP-008` | Corrected WFC-C-001/AC acceptance, stabilization metrics/cycle threshold, and runtime recovery Evidence | WFC/AC `DRAFT`; metrics `UNKNOWN`; runtime `NOT_RUN` | AOS3-DPKG-TASK-007 materialization and Stable-Core/automation claim | New contract decision, then later runtime/cycle decisions |

An open gap blocks only the outputs named in `Blocks`.

## 11. Human decision register

Product decisions bind the exact Stage A candidate. Architecture decisions bind the exact Stage B candidate. The later human clarification records that repository creation is not authorized, documentation remains in `notebook`, and implementation-repository binding is deferred.

| Decision ID | Exact subject | Gate | Current state | Downstream effect |
|---|---|---|---|---|
| [`DEC-PROD-001`](decisions/DEC-PROD-001_First_User_and_Job.md) | First user and first job | `G1` | `HUMAN_DECIDED` | Defines actor/problem boundary for `01` and `02` |
| [`DEC-PROD-002`](decisions/DEC-PROD-002_Observable_Outcome.md) | Observable outcome | `G1` | `HUMAN_DECIDED` | Defines success boundary |
| [`DEC-PROD-003`](decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md) | Ordered Core v1 sequence `A → B → C`; A first | `G1` | `HUMAN_DECIDED` | Selects initial contract path |
| [`DEC-PROD-004`](decisions/DEC-PROD-004_Core_V1_Scope_and_Non_Goals.md) | Core v1 scope and non-goals | `G1` | `HUMAN_DECIDED` | Prevents optional capability admission |
| [`DEC-PROD-005`](decisions/DEC-PROD-005_Product_Spec_and_Feature_Passport_Relation.md) | Product Spec ↔ Feature Passport relation | `G1` | `HUMAN_DECIDED` | Defines product artifact ownership |
| [`DEC-PROD-006`](decisions/DEC-PROD-006_RMP_004_005_Boundaries.md) | `RMP-004` and `RMP-005` split boundaries | `G1` | `HUMAN_DECIDED` | Keeps both items unsplit |
| [`DEC-ARCH-001`](decisions/DEC-ARCH-001_Implementation_Repository.md) | Documentation location, repository-creation boundary, and deferred implementation identity | `G2` plus later clarification | `HUMAN_DECIDED_IMPLEMENTATION_REPOSITORY_DEFERRED` | Portable docs continue; physical/repository-bound execution blocked |
| [`DEC-ARCH-002`](decisions/DEC-ARCH-002_Architecture_and_Topology.md) | Local modular monolith, ports/adapters, interaction boundary | `G2` | `HUMAN_DECIDED` | Unblocks logical contracts |
| [`DEC-ARCH-003`](decisions/DEC-ARCH-003_Toolchain_and_Dependencies.md) | Python 3.12+, minimal pinned dependencies | `G2` | `HUMAN_DECIDED` | Toolchain class accepted; exact set awaits repo |
| [`DEC-ARCH-004`](decisions/DEC-ARCH-004_Project_Memory.md) | Repository-relative file Project Memory | `G2` | `HUMAN_DECIDED` | Unblocks DRAFT memory/recovery contract |
| [`DEC-ARCH-005`](decisions/DEC-ARCH-005_Provider_and_Privacy.md) | Local-only provider/privacy boundary | `G2` | `HUMAN_DECIDED` | Unblocks privacy/security contract |
| [`DEC-ARCH-006`](decisions/DEC-ARCH-006_Human_Decision_Authenticity.md) | Local-declared hash-bound Human Decisions | `G2` | `HUMAN_DECIDED` | Unblocks decision/staleness contract |
| [`DEC-ARCH-007`](decisions/DEC-ARCH-007_Risk_Profile_Vocabulary.md) | Minimal human-owned action classes | `G2` | `HUMAN_DECIDED` | Unblocks risk/permission vocabulary |
| [`DEC-ARCH-008`](decisions/DEC-ARCH-008_Compatibility.md) | Greenfield contract compatibility only | `G2` | `HUMAN_DECIDED` | Excludes implicit legacy compatibility |
| [`DEC-CONTRACT-001`](decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md) | Exact 137 requirement/contract/acceptance/scenario subjects | `C1` | `HUMAN_DECIDED` | Allows portable DRAFT Task compilation; grants no Task acceptance or implementation/Git authority |
| [`DEC-CORR-001`](decisions/DEC-CORR-001_Package_Local_Task_Namespace.md) | Package-local Task namespace plus exact DRAFT-R6 through DRAFT-R14 correction scopes | `D1` plus later correction authorizations | `HUMAN_DECIDED` | Separates package Task IDs from Roadmap IDs and records only the bounded documentation grants |

G1 records bind Stage A aggregate SHA-256 `4fe1a0fcc8493d00e60694f86ac734fac197f005246b6ae7cb2689ab6fd9ce80`. G2 records bind Stage B aggregate SHA-256 `d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d`. C1 binds Stage C contract candidate aggregate `00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262` and persisted accepted-subject manifest `2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b`. The namespace decision binds the pre-correction DRAFT-R5 package aggregate `c21bf54b62cfe78b4c72527390c834fbe4534acca0ff730bdcde70f5b5316bed`; the DRAFT-R7 correction authorization binds DRAFT-R6 aggregate `0309143fa4d048af18c9bdfdc27acd356e927facf1f7c3add39fcece2f529efe`; the DRAFT-R8 correction authorization binds DRAFT-R7 aggregate `6a06c761c9c722141efb4d2a900632ec4ab59ef9b921645ae028fb39d51db65b`; the DRAFT-R9 correction authorization binds DRAFT-R8 aggregate `f6443683a12094d1357ae8c44b5937f1aaf4f276e088b9c9c1e99b1dcfc4ac97`; the DRAFT-R10 correction authorization binds DRAFT-R9 aggregate `61ebdaa63d4fce3034db1c3fceaa3d86c35e5849cc1fc3f5bdb75e8cf3ea2bad`; the DRAFT-R11 correction authorization binds DRAFT-R10 aggregate `8b815b48fc6b3114e6bbaf1b8cfa3ac1cace7bb1b3119929a8f023ea2343b5b6`; the DRAFT-R12 correction authorization binds DRAFT-R11 aggregate `88eefc88a9e2a1ebfe06b4be6becec9a807452e7c1ff2092eef60a0d751eb5a4`; the DRAFT-R13 correction authorization binds DRAFT-R12 aggregate `291d3771e0b652cc152a8b706fcdeeb1479ac268c1837fd0cce721d7a11f5a8a`; the DRAFT-R14 correction authorization binds DRAFT-R13 aggregate `880dfdd3260beb19fa73078c9df50b84172ebbeec9719d62ad23b81c1407044c`.

## 12. G1 product options and outcome

The options were presented as decision-ready alternatives. The human accepted all three as an ordered sequence, with Option A as the only first slice.

```text
G1-OPT-A → G1-OPT-B → G1-OPT-C
```

The original option descriptions remain below as decision provenance.

### Option A — Intent to reviewed product draft

```yaml
option_id: G1-OPT-A
first_user: non-programmer or domain expert starting a product/feature
job: turn an ambiguous intent into a reviewable product boundary without losing human authority
observable_outcome: reviewed DRAFT Product Spec and feature-specific passport with visible assumptions, unknowns, scope, and one decision request
first_slice: intake → material clarification → DRAFT Product Spec/Feature Passport → human review stop
primary_rmp: [RMP-001, RMP-004]
dependencies: [DEC-PROD-005]
non_goals:
  - implementation planning
  - task creation
  - repository mutation
  - automatic architecture choice
```

Trade-off: earliest product learning and lowest implementation dependency, but does not yet prove execution or recovery behavior.

### Option B — Accepted contract to bounded Task

```yaml
option_id: G1-OPT-B
first_user: vibe-coder or product builder with an accepted feature contract
job: obtain one bounded and reviewable Task Brief without hidden scope or Git authority
observable_outcome: one Task candidate traceable to accepted requirement, contract, and scenario IDs
first_slice: accepted contract → task eligibility → bounded Task Brief → authorization-required stop
primary_rmp: [RMP-001, RMP-005]
dependencies:
  - accepted upstream product contract
  - DEC-PROD-005
non_goals:
  - task execution
  - automatic activation
  - persistent scheduler
  - Git delivery
```

Trade-off: directly tests handoff quality for coding agents, but cannot start until upstream product contracts are accepted.

### Option C — Existing project to safe next action

```yaml
option_id: G1-OPT-C
first_user: product builder resuming an existing AI-assisted project
job: recover actual project state and identify one safe next action without chat history
observable_outcome: read-only project snapshot with gaps, blockers, authority state, and one human-reviewable next action
first_slice: read-only discovery → state/gap classification → safe next-action proposal → human review stop
primary_rmp: [RMP-001, RMP-004, RMP-008]
dependencies:
  - Project Memory boundary remains optional for the first slice
non_goals:
  - autonomous recovery
  - remediation
  - task execution
  - repository writes
```

Trade-off: tests continuity and immediate practical value, but combines discovery with recovery semantics and may widen the first contract surface.

## 13. Gate G1 decision record

```yaml
gate_id: HUMAN_PRODUCT_GATE_G1
candidate:
  package_revision: DRAFT-R1
  aggregate_sha256: 4fe1a0fcc8493d00e60694f86ac734fac197f005246b6ae7cb2689ab6fd9ce80
decision:
  first_user: non-programmer or domain expert
  first_job: turn ambiguous intent into a reviewable product boundary
  observable_outcome: reviewed DRAFT Product Spec and Feature Passport with visible uncertainty
  selected_directions: [G1-OPT-A, G1-OPT-B, G1-OPT-C]
  ordered_sequence: G1-OPT-A → G1-OPT-B → G1-OPT-C
  first_core_v1_vertical_slice: G1-OPT-A
  product_spec_feature_passport_relation: separate logical owners with reciprocal revision links
  rmp_004_split_decision: KEEP_UNSPLIT_UNTIL_MATERIAL_BOUNDARY
  rmp_005_split_decision: KEEP_UNSPLIT_UNTIL_MATERIAL_BOUNDARY
human_disposition: ACCEPT
implementation_authorization: NONE
git_authorization: NONE
```

Exact subjects are recorded in [`DEC-PROD-001..006`](decisions/DEC-PROD-001_First_User_and_Job.md). G1 does not accept individual `FTR-*`, Stage B DRAFT contracts, implementation, or Git delivery.

## 14. Gate G2 decision record

```yaml
gate_id: HUMAN_ARCHITECTURE_GATE_G2
candidate:
  package_revision: DRAFT-R2
  aggregate_sha256: d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d
decision:
  selected_bundle: G2-OPT-A
  repository_option: G2-REPO-A
  received_exact_repository: OWNER/REPOSITORY
  later_human_repository_creation_decision: DO_NOT_CREATE
  documentation_repository: NMF13579/notebook
  effective_implementation_repository: UNASSIGNED
  architecture_option: G2-ARCH-A
  toolchain_option: G2-TOOL-A
  project_memory_option: G2-MEM-A
  provider_privacy_option: G2-PRIV-A
  human_decision_authenticity_option: G2-AUTH-A
  risk_profile_option: G2-RISK-A
  compatibility_option: G2-COMP-A
  interaction_surface: conversational adapter plus portable text/JSON interface
human_disposition: ACCEPT
implementation_authorization: NONE
git_authorization: NONE
```

The bundle choice and interaction surface are exact human decisions. The supplied repository value is preserved as historical input. The later human clarification supersedes repository creation now, keeps documentation in `notebook`, and leaves implementation binding for a separate future gate. `DEC-ARCH-002..008` continue to support portable Stage C contracts.

## 15. Stage boundaries

| Stage/gate | Allowed result | Explicitly forbidden |
|---|---|---|
| Stage A `EXECUTE` | Control owner, source inventory, G1 options/templates | Contracts, adapters, implementation, Git |
| Gate G1 | Human-bound product decision | Agent selection or simulated acceptance |
| Stage B `EXECUTE` | Owners `01/02`, G1 records, research, G2 option package | Implementation contracts, Tasks |
| Gate G2 | Hash-bound human architecture decision | Agent default architecture/repository/toolchain |
| Stage C contract authoring | Owners `03..07`, contract/scenario candidates, traceability, handoff, adapter | Task artifacts from unaccepted inputs |
| Gate C1 | Accepted requirement/contract/acceptance/scenario IDs bound to the exact Stage C candidate | Generic or agent-inferred acceptance; repository inference |
| Stage C Task compilation | Task template, bounded graph, first DRAFT briefs from accepted IDs | Task acceptance, execution, validation, or Git authority |
| Stage D `VALIDATE` | Read-only exact-candidate report | Correction or candidate mutation |
| DRAFT-R6 correction `EXECUTE` | Fix only the human-approved DRAFT-R5 validation findings inside package root | `/docs` or Roadmap mutation, independent validation, implementation, Git |
| DRAFT-R7 correction `EXECUTE` | Persist the C1 manifest, delete the invalid Task-003 document, and fix only `VAL-R6-001` findings inside package root | `/docs` or Roadmap mutation, independent validation, implementation, Git |
| DRAFT-R8 correction `EXECUTE` | Fix only `VAL-R7-001` findings and human-selected D1/A2 deterministic consequences inside allowed package Markdown paths | Manifest, `/docs`, or Roadmap mutation; independent validation, implementation, Git |
| DRAFT-R9 correction `EXECUTE` | Remove only the redundant scalar authority fields identified by `VAL-R8-001`, preserve operational authority maps, and apply the authorized acceptance projection | Manifest, `/docs`, or Roadmap mutation; independent validation, implementation, Git |
| DRAFT-R10 correction `EXECUTE` | Add eight explicit AC-PSC-to-existing-SCN mappings, restore three reverse trace links, and propagate only revision/status/receipt/next-action metadata | Accepted subject definition, Task derivation/materialization, C1 projection, manifest, `/docs`, Roadmap, independent validation, implementation, Git |
| DRAFT-R11 correction `EXECUTE` | Materialize exact `TRC-REG-001`, derive both requirement-contract projections, add deterministic equality invariants, and propagate only receipt/revision/status/validation-history/next-action metadata | Requirement/PSC/WFC/CTR/acceptance/scenario definitions, Task semantics/derivation/materialization, C1 projection/manifest, `/docs`, Roadmap, repository assignment, runtime code, independent validation, implementation, Git |
| DRAFT-R12 correction `EXECUTE` | Add three exact semantic-completeness relations, regenerate both projections, add the materialized-Task relation-closure invariant, and propagate only receipt/revision/status/validation-history/next-action metadata | Requirement/PSC/WFC/CTR/acceptance/scenario definitions, Task content/semantics/derivation/materialization, C1 projection/manifest, `/docs`, Roadmap, repository assignment, runtime code, independent validation, implementation, Git |
| DRAFT-R13 correction `EXECUTE` | Derive materialized Task projections from existing Task Brief `derived_from`, add the omitted Task-002/REQ-ARCH-003 projection and its existing CTR-002 zero-write Evidence path, keep graph-only mappings separate, add deterministic invariants, and propagate correction metadata | `TRC-REG-001`, endpoint definitions, Task derivation/materialization/outcome/scope/graph semantics, C1 projection/manifest, `/docs`, Roadmap, repository assignment, runtime code, independent validation, implementation, Git |
| DRAFT-R14 correction `EXECUTE` | Remove the unsupported REQ-ARCH-009/CTR-002/Task-002 derivation and the non-derived REQ-WF-006 materialized-Task note; regenerate the exact registry projections; preserve compatibility as a deferred decision boundary; propagate correction metadata | Endpoint definitions, C1 projection/manifest, Task-001, Task-002 outcome/scope/contracts/acceptance/scenarios, Task graph/materialization, `/docs`, Roadmap, repository assignment, runtime code, independent validation, implementation, Git |
| Stage E `REVIEW` | Semantic review and human disposition | Automatic delivery |

## 16. DRAFT-R14 correction-candidate completion criteria

The corrected DRAFT-R14 package candidate can request separate Stage D authorization only if:

1. exactly 37 package files exist: 36 Markdown files plus only `decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv`;
2. G1 and G2 records retain their exact candidate hashes;
3. all 17 `aos.decision/v1` instances conform to the closed D1 tagged union, C1 references the persisted manifest, and `DEC-CORR-001` preserves all nine bounded correction receipts;
4. `DEC-ARCH-001` records documentation-only `notebook`, no repository creation, and `implementation_repository: UNASSIGNED`;
5. YAML frontmatter, Markdown fences, and relative links are valid;
6. document, decision, ADR, research, requirement, contract, acceptance, scenario, schema, component, port, and Task IDs are structurally unique within their registries;
7. `TRC-REG-001` contains exactly 83 unique sorted relations with payload SHA-256 `af15f5e0af1ca667136e1ffc2352e3acc7bf3cb5c037f62f558818889170aa69`, both derived requirement-contract projections expand to exactly that registry, and every materialized Task satisfies the Task relation-closure invariant;
8. forward materialized Task entries exactly invert existing Task Brief `derived_from.requirements`, reverse materialized Task entries exactly project `derived_from.contracts`, graph-only mappings remain separately labelled, every materialized requirement-contract path retains existing acceptance/scenario Evidence, `REQ-ARCH-009` has no current portable-contract or Task derivation, and `REQ-WF-006` has no non-derived materialized Task entry;
9. `RMP-001..008` have bidirectional requirement/contract/scenario traceability;
10. every `CTR-001..007`, corrected `WFC-A-001`, corrected `WFC-B-001`, and corrected `WFC-C-001` declares actor, trigger, preconditions, inputs, outputs, states, side effects, authority, failures, recovery, non-goals, and executable acceptance;
11. positive, negative, failure, and recovery scenarios exist for every `CTR-*`;
12. `TASK-TEMPLATE.md`, Task graph, and materialized `AOS3-DPKG-TASK-001..002` bind the accepted DRAFT-R4 source candidate and derive only from current C1-accepted subjects;
13. no Task Brief exists for corrected PSC-A, corrected WFC-A/B/C, stale AC-WFC-A-001-01..07, the ten new DRAFT AC-WFC-B/C IDs, or the two new DRAFT shared schemas;
14. package-local Task IDs and paths do not collide with or claim Roadmap `TASK-###` ownership;
15. shared Product Spec/Feature Passport schemas are closed DRAFT records outside the frozen `CTR-003` subject;
16. optional capabilities remain deferred/reference-only and outside the Core queue;
17. reference findings retain repository/ref/commit/path and authority `NONE`;
18. canonical `/docs` and `AOS_Core_Roadmap.md` remain byte-identical to their recorded hashes;
19. `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT` remains visible and blocks false schema/readiness claims;
20. no implementation, validation, or Git authorization is claimed;
21. each WFC envelope is the sole definition owner for its `AC-WFC-*` IDs and every acceptance table is an exact derived mirror;
22. current schema references use stable IDs `SCH-PRODUCT-SPEC-001` and `SCH-FEATURE-PASSPORT-001`, and current `DEC-ARCH-001` locators use R4;
23. author self-checks complete and a package-relative DRAFT-R14 aggregate SHA-256 is reported after final bytes.

These are correction author self-checks, not independent Stage D validation or human acceptance.

## 17. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```

Until a separate Stage D request binds the exact DRAFT-R14 package candidate:

- do not mutate the package under validation;
- do not infer an implementation repository;
- do not install dependencies or execute runtime behavior;
- do not begin Stage D automatically;
- do not perform Commit, Push, Merge, or Release.
