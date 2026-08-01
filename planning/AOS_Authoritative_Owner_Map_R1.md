---
artifact_id: AOS-AUTHORITATIVE-OWNER-MAP-R1
document_type: AUTHORITATIVE_OWNER_MAP
revision: R1
status: DRAFT
fact_class: SYNTHESIZED
role: NAVIGATION_AND_PROVENANCE_ONLY
authority_effect: NONE
human_acceptance: NOT_RUN
independent_validation: NOT_RUN
source_roadmap:
  path: planning/AOS_Documentation_Task_Sequence_R9.md
  sha256: be91cbffcd2c79a0a632b661157e5e2e7fb7a68d1056ba1c9684f2ea1b549ee7
current_state_owner: planning/CURRENT.md
implementation_authorization: NONE
git_authorization: NONE
output_path: planning/AOS_Authoritative_Owner_Map_R1.md
---

# AOS Authoritative Owner Map R1

## 1. Purpose and boundary

Этот owner map помогает cold-start агенту выбрать authoritative source для
используемого fact class. Он является repository-local navigation и provenance
artifact.

Owner map:

- маршрутизирует к authoritative owner, но не копирует и не переопределяет его
  содержание;
- не владеет current progress state, active interval или next action;
- не создаёт acceptance, activation, execution authorization, implementation
  authorization или Git authorization;
- не повышает supporting, historical, reported, synthesized или proposal
  artifacts до authoritative facts;
- не заменяет direct current repository observation для mutable facts;
- не создаёт product, architecture, feature, authority или human decisions.

`planning/CURRENT.md` является durable owner записанного lifecycle state и
записанного `next_bounded_action`. Current explicit human decision имеет более
высокий приоритет и может сделать persisted state stale до отдельного
разрешённого обновления `planning/CURRENT.md`. Если этот map расходится с
authoritative owner, stale является map, а не owner.

## 2. Source boundary

Authoritative inputs этого map:

```yaml
authoritative_inputs:
  - docs/00_Core.md
  - docs/01_Product.md
  - docs/02_Architecture.md
  - docs/03_Development.md
  - docs/04_Lessons.md
  - docs/05_Reference.md
  - docs/06_Features.md
  - planning/AOS_Documentation_Task_Sequence_R9.md
  - planning/AOS_Documentation_Task_Sequence_R9_Acceptance_Record.md
  - planning/AOS_Documentation_Task_Sequence_R9_Activation_Record.md
  - planning/CURRENT.md
supporting_reference_only:
  - planning/AOS_Documentation_Task_Sequence_R6.md
  - planning/AOS_Documentation_Task_Sequence_R7.md
  - planning/AOS_Documentation_Task_Sequence_R8.md
  - AOS-3/AOS_Core_Roadmap.md
```

Supporting и historical artifacts могут объяснять provenance, но не получают
authority над current documentation sequence.

## 3. Authority precedence

Authority всегда ограничена declared fact class. Использовать следующий
порядок без переноса authority между уровнями:

1. current explicit human decision;
2. human-accepted AOS artifact в declared scope;
3. direct current repository observation для mutable facts;
4. DRAFT-разделы и явно помеченные proposals внутри принятого пакета;
5. historical repository snapshot как reference;
6. chat summary, note, report или assistant analysis;
7. agent inference.

Нижние уровни не отменяют верхние. Repository presence не создаёт authority;
Evidence не создаёт approval; `PASS` не создаёт acceptance; acceptance или
activation не создают execution либо Git authorization.

## 4. Fact-class owner map

Каждая запись назначает не более одного authoritative owner. `supporting_sources`
дают только context, provenance или constraints и не разделяют ownership.

```yaml
owner_map:
  - fact_class: project_identity
    authoritative_owner: docs/00_Core.md
    authority_scope: project identity and repository role of the AOS knowledge baseline
    supporting_sources: [docs/05_Reference.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - new explicit human decision changes project identity or repository role
      - accepted successor artifact supersedes docs/00_Core.md in this fact class
      - exact owner path or identity changes
    conflict_behavior: report CONFLICT and block only the identity-dependent action; do not infer an identity

  - fact_class: authority_and_acceptance_semantics
    authoritative_owner: docs/00_Core.md
    authority_scope: source precedence, fact-class-scoped authority, acceptance boundaries, and human authority
    supporting_sources: [docs/02_Architecture.md, docs/03_Development.md, docs/05_Reference.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - new explicit human authority decision
      - accepted successor artifact in the same fact class
      - competing authority owner is discovered
    conflict_behavior: apply higher precedence, record CONFLICT if same-level owners disagree, and block only the affected authority-bearing action

  - fact_class: canonical_status_vocabulary
    authoritative_owner: docs/00_Core.md
    authority_scope: project-level claim classifications, technical-result semantics, human-decision semantics, and status invariants
    supporting_sources: [docs/02_Architecture.md, docs/03_Development.md, planning/AOS_Documentation_Task_Sequence_R9.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - accepted status-contract revision supersedes the project-level vocabulary
      - a supporting workflow uses an incompatible meaning
      - exact owner path or identity changes
    conflict_behavior: preserve docs/00_Core.md semantics, report the incompatible supporting vocabulary as CONFLICT, and block only its affected use

  - fact_class: minimal_safety_floor
    authoritative_owner: docs/00_Core.md
    authority_scope: always-on minimal safety invariants and protected human decisions
    supporting_sources: [docs/02_Architecture.md, docs/03_Development.md, docs/04_Lessons.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - new explicit human safety decision
      - accepted successor safety artifact
      - a supporting artifact materially contradicts a safety invariant
    conflict_behavior: retain the higher-precedence safety boundary, report CONFLICT, and block only the unsafe affected action

  - fact_class: users_and_problems
    authoritative_owner: docs/01_Product.md
    authority_scope: target users, user problems, and accepted product directions
    supporting_sources: [docs/00_Core.md, docs/06_Features.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - new explicit human product decision
      - accepted successor Product artifact in this fact class
      - product evidence shows the accepted baseline is stale and human review changes it
    conflict_behavior: report CONFLICT and block only the product decision or task that depends on the disputed user or problem

  - fact_class: product_boundaries_and_journeys
    authoritative_owner: docs/01_Product.md
    authority_scope: product boundaries, non-goals, product artifacts, and user journeys
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, docs/06_Features.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - new explicit human product-scope decision
      - accepted successor Product artifact
      - a selected feature contract requires an explicit bounded product decision
    conflict_behavior: report CONFLICT and block only the scope-dependent product or implementation-planning action

  - fact_class: architecture_boundaries_and_ownership
    authoritative_owner: docs/02_Architecture.md
    authority_scope: architecture principles, layer boundaries, shared contract classes, data ownership, and deferred complexity
    supporting_sources: [docs/00_Core.md, docs/01_Product.md, docs/03_Development.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - new explicit human architecture decision
      - accepted ADR or successor Architecture artifact in the same bounded fact class
      - implementation Evidence invalidates an assumption and human review changes the architecture
    conflict_behavior: report CONFLICT; do not select among materially valid architectures; block only the architecture-dependent action

  - fact_class: development_stages_and_task_lifecycle
    authoritative_owner: docs/03_Development.md
    authority_scope: normative PLAN, EXECUTE, VALIDATE, REVIEW boundaries and bounded task workflow
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, planning/AOS_Documentation_Task_Sequence_R9.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - accepted successor workflow artifact
      - new explicit human stage-boundary decision
      - an interval-specific rule conflicts with the normative workflow
    conflict_behavior: report CONFLICT and block only the conflicting stage transition or action; never merge stages by inference

  - fact_class: validation_and_review
    authoritative_owner: docs/03_Development.md
    authority_scope: validation gates, validation protocol, human review content, and separation of verification from acceptance
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, docs/04_Lessons.md, planning/AOS_Documentation_Task_Sequence_R9.md]
    mutable_or_stable: stable_until_superseded
    observation_required: true
    invalidation_conditions:
      - candidate bytes or identity change after freeze
      - validation profile or required checks change
      - accepted successor workflow artifact
      - repository state invalidates a snapshot-bound result
    conflict_behavior: report CONFLICT or UNKNOWN for the affected check, prevent required NOT_RUN from becoming PASS, and block only the affected validation or review claim

  - fact_class: recovery
    authoritative_owner: docs/03_Development.md
    authority_scope: execution failure, validation finding, recovery, resume, correction, and handoff workflow
    supporting_sources: [docs/02_Architecture.md, docs/04_Lessons.md]
    mutable_or_stable: stable_until_superseded
    observation_required: true
    invalidation_conditions:
      - repository or partial-write state changes
      - a new failure changes scope, identity, permissions, or required human decision
      - accepted successor workflow artifact
    conflict_behavior: stop the affected mutation, preserve observed state, report CONFLICT or UNKNOWN, and require one bounded recovery resolution step

  - fact_class: git_boundaries
    authoritative_owner: docs/03_Development.md
    authority_scope: separation and preconditions of Edit, Commit, Push, Merge, and Release
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, docs/04_Lessons.md]
    mutable_or_stable: stable_until_superseded
    observation_required: true
    invalidation_conditions:
      - repository, branch, HEAD, candidate, worktree, remote, or authorization changes
      - new explicit human Git-boundary decision
      - accepted successor workflow artifact
    conflict_behavior: report CONFLICT or UNKNOWN and block only the exact Git action; no permission carries to another Git action

  - fact_class: lessons_and_regression_candidates
    authoritative_owner: docs/04_Lessons.md
    authority_scope: historical failures, lesson inventory, and regression catalog; item policy effect remains decision-bound
    supporting_sources: [docs/03_Development.md, docs/05_Reference.md]
    mutable_or_stable: stable_until_superseded
    observation_required: true
    invalidation_conditions:
      - source locator or historical observation is disproved
      - a new incident changes the lesson candidate
      - item-scoped human decision promotes, rejects, or supersedes a lesson
    conflict_behavior: classify the item as CONFLICT or UNKNOWN, preserve proposal status, and block only promotion or use that depends on the disputed lesson

  - fact_class: research_routing_and_provenance
    authoritative_owner: docs/05_Reference.md
    authority_scope: source provenance, snapshot identity requirements, targeted research routes, and reference authority boundaries
    supporting_sources: [docs/00_Core.md, docs/03_Development.md, docs/04_Lessons.md]
    mutable_or_stable: snapshot_bound
    observation_required: true
    invalidation_conditions:
      - branch, ref, commit, tree, or source path changes
      - source becomes inaccessible or provenance cannot be reproduced
      - accepted successor provenance artifact
    conflict_behavior: report CONFLICT, NOT_FOUND, or UNKNOWN with the exact search boundary and block only the source-dependent claim or action

  - fact_class: feature_inventory
    authoritative_owner: docs/06_Features.md
    authority_scope: feature identities, inventory entries, design-level dossiers, and source crosswalk
    supporting_sources: [docs/01_Product.md, docs/02_Architecture.md, docs/05_Reference.md]
    mutable_or_stable: stable_until_superseded
    observation_required: false
    invalidation_conditions:
      - accepted successor feature inventory
      - feature identity or dossier path changes
      - inventory mirror no longer matches an authoritative item-scoped decision
    conflict_behavior: report CONFLICT and block only inventory-dependent selection or planning; catalog presence must not become feature acceptance

  - fact_class: feature_human_disposition
    authoritative_owner: exact item-scoped human-authored or human-verified feature decision record
    authority_scope: disposition of one exact feature subject only
    supporting_sources: [docs/00_Core.md, docs/06_Features.md, planning/AOS_Documentation_Task_Sequence_R9.md]
    mutable_or_stable: decision_bound
    observation_required: true
    invalidation_conditions:
      - a later exact human decision supersedes the disposition
      - feature subject identity changes
      - docs/06_Features.md mirror differs from the exact decision record
      - actor or decision provenance cannot be verified
    conflict_behavior: the mirror is stale; report CONFLICT and block only the affected feature selection or downstream planning; do not infer disposition

  - fact_class: documentation_interval_sequence
    authoritative_owner: planning/AOS_Documentation_Task_Sequence_R9.md
    authority_scope: exact human-accepted R9 documentation interval order and dependencies only
    supporting_sources: [planning/AOS_Documentation_Task_Sequence_R9_Acceptance_Record.md, planning/AOS_Documentation_Task_Sequence_R9_Activation_Record.md, planning/CURRENT.md]
    mutable_or_stable: stable_until_superseded
    observation_required: true
    invalidation_conditions:
      - R9 bytes no longer match the accepted SHA-256
      - a new exact human-accepted roadmap supersedes R9 in this fact class
      - acceptance record identity is invalid or unavailable
    conflict_behavior: report CONFLICT or UNKNOWN and block only documentation-sequence execution; do not restore R6, R7, or R8 by inference

  - fact_class: roadmap_acceptance
    authoritative_owner: planning/AOS_Documentation_Task_Sequence_R9_Acceptance_Record.md
    authority_scope: human acceptance of the exact SHA-256-bound R9 sequence only
    supporting_sources: [planning/AOS_Documentation_Task_Sequence_R9.md, planning/AOS_Documentation_Task_Sequence_R9_Activation_Record.md]
    mutable_or_stable: decision_bound
    observation_required: true
    invalidation_conditions:
      - accepted R9 subject bytes or SHA-256 change
      - decision actor, subject, or acceptance provenance becomes invalid
      - later explicit human decision supersedes acceptance
    conflict_behavior: report CONFLICT or UNKNOWN and block only actions requiring accepted-roadmap authority; acceptance does not imply activation or authorization

  - fact_class: roadmap_activation
    authoritative_owner: planning/AOS_Documentation_Task_Sequence_R9_Activation_Record.md
    authority_scope: activation of exact accepted R9 and its initial interval pointer
    supporting_sources: [planning/AOS_Documentation_Task_Sequence_R9_Acceptance_Record.md, planning/CURRENT.md]
    mutable_or_stable: decision_bound
    observation_required: true
    invalidation_conditions:
      - activated R9 or acceptance-record identity changes
      - later explicit human activation or deactivation decision
      - activation record no longer matches planning/CURRENT.md
    conflict_behavior: report CONFLICT and block only activation-dependent execution; activation does not create execution, implementation, or Git authorization

  - fact_class: current_progress_state
    authoritative_owner: planning/CURRENT.md
    authority_scope: persisted active roadmap pointer, active interval, lifecycle status, recorded authorization state, and one next bounded action; current explicit human decision retains higher precedence
    supporting_sources: [planning/AOS_Documentation_Task_Sequence_R9_Activation_Record.md, planning/AOS_Documentation_Task_Sequence_R9.md]
    mutable_or_stable: mutable
    observation_required: true
    invalidation_conditions:
      - planning/CURRENT.md bytes or referenced identities change
      - roadmap, interval, verification, human-decision, or external-gate state changes
      - a competing progress owner is discovered
    conflict_behavior: report CONFLICT, treat derived progress views as stale, and block only lifecycle mutation or execution that depends on disputed current state

  - fact_class: mutable_repository_facts
    authoritative_owner: direct current repository observation
    authority_scope: current root, worktree, branch, HEAD, status, diff, paths, staging area, remotes, and candidate identity at the observed snapshot
    supporting_sources: [docs/00_Core.md, docs/03_Development.md, docs/05_Reference.md]
    mutable_or_stable: mutable
    observation_required: true
    invalidation_conditions:
      - any relevant repository, filesystem, branch, HEAD, index, worktree, remote, or candidate change
      - observation boundary or command provenance is incomplete
      - elapsed time or external activity makes the snapshot stale
    conflict_behavior: re-observe read-only; if disagreement remains, report CONFLICT or UNKNOWN and block only the affected mutation or claim

  - fact_class: human_decisions
    authoritative_owner: exact human-authored or human-verified decision record bound to the exact subject
    authority_scope: the declared decision and subject boundary only
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, docs/03_Development.md]
    mutable_or_stable: decision_bound
    observation_required: true
    invalidation_conditions:
      - actor, subject, date, revision, or decision provenance is missing or changes
      - later explicit human decision supersedes it
      - generated or mirror artifact conflicts with the exact decision record
    conflict_behavior: reject generated authority, report CONFLICT or UNKNOWN, and block only the action requiring that human decision

  - fact_class: external_evidence
    authoritative_owner: immutable subject-bound Evidence Record
    authority_scope: observed method, result, locator or digest, temporal scope, and limitations for the exact external subject
    supporting_sources: [docs/02_Architecture.md, docs/03_Development.md, docs/05_Reference.md, planning/AOS_Documentation_Task_Sequence_R9.md]
    mutable_or_stable: snapshot_bound
    observation_required: true
    invalidation_conditions:
      - evidence subject, bytes, locator, digest, method, environment, or temporal scope changes
      - Evidence cannot be reproduced where reproduction is required
      - a competing subject-bound Evidence Record disagrees
    conflict_behavior: report CONFLICT or UNKNOWN, preserve limitations, and block only the Evidence-dependent claim or gate; Evidence never creates approval

  - fact_class: implementation_authorization
    authoritative_owner: exact human-issued Execution Authorization Record bound to the implementation subject
    authority_scope: only the declared task, subject, stage, operations, paths, time boundary, and consumption state
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, docs/03_Development.md, planning/CURRENT.md]
    mutable_or_stable: decision_bound
    observation_required: true
    invalidation_conditions:
      - task, subject, stage, operation, path, expiry, or consumption state changes
      - repository identity no longer matches the authorization binding
      - later explicit human decision revokes or supersedes authorization
    conflict_behavior: default to no implementation authority, report CONFLICT or UNKNOWN, and block only implementation mutation

  - fact_class: git_authorization
    authoritative_owner: exact current explicit human decision bound separately to the exact Commit, Push, Merge, or Release action and subject
    authority_scope: one declared Git action and exact subject only; no authority carries between Git actions
    supporting_sources: [docs/00_Core.md, docs/02_Architecture.md, docs/03_Development.md, planning/CURRENT.md]
    mutable_or_stable: decision_bound
    observation_required: true
    invalidation_conditions:
      - repository, branch, HEAD, candidate, worktree, remote, action, or authorization binding changes
      - later explicit human decision revokes or supersedes permission
      - the requested Git action differs from the authorized action
    conflict_behavior: default to no Git authority, report CONFLICT or UNKNOWN, and block only the exact Git action
```

## 5. Fact classifications

Эти classifications описывают claim status; они не назначают owner и не
повышают authority:

| Classification | Meaning |
|---|---|
| `HUMAN_ACCEPTED_FACT` | Exact human-accepted artifact or claim, authoritative only in its declared fact class. |
| `HUMAN_CONFIRMED_DIRECTION` | Explicit human direction within an exact boundary; not broader acceptance or authorization. |
| `OBSERVED_AT_SNAPSHOT` | Directly observed in an exact repository or external subject at a bounded snapshot. |
| `REPORTED` | Recorded by a source but not reproduced in the current check. |
| `SYNTHESIZED` | Derived from multiple sources; does not become an accepted fact by synthesis. |
| `PROPOSAL` | Explicit candidate or draft awaiting any required decision; not accepted authority. |
| `CONFLICT` | Relevant sources disagree and the disagreement has not been authoritatively resolved. |
| `UNKNOWN` | Available Evidence is insufficient to establish the claim. |
| `NOT_FOUND` | The subject was not found inside the declared search boundary. |
| `NOT_RUN` | The check or operation was not performed. |
| `BLOCKED` | The affected operation stopped at a boundary or unresolved prerequisite. |

`REPORTED`, `SYNTHESIZED` и `PROPOSAL` остаются своими classifications до
отдельного authority-bearing human action; owner map не может повысить их до
`HUMAN_ACCEPTED_FACT`.

## 6. Historical boundary

```yaml
artifact:
  path: AOS-3/AOS_Core_Roadmap.md
  role: HISTORICAL_EVIDENCE_OF_SEPARATE_PORTABLE_PACKAGE
  authority_over_current_documentation_sequence: NONE
  competing_owner: false
```

После acceptance и activation exact R9:

```yaml
planning/AOS_Documentation_Task_Sequence_R6.md:
  authority_over_current_documentation_sequence: NONE
  role: SUPERSEDED_WITHIN_DOCUMENTATION_INTERVAL_SEQUENCE
planning/AOS_Documentation_Task_Sequence_R7.md:
  authority_over_current_documentation_sequence: NONE
  role: UNACCEPTED_DRAFT_INTERMEDIATE_SOURCE
planning/AOS_Documentation_Task_Sequence_R8.md:
  authority_over_current_documentation_sequence: NONE
  role: UNACCEPTED_DRAFT_CORRECTION_SOURCE
```

R6, R7 и R8 не являются current owner документационной последовательности.
Они не могут заменить exact human-accepted R9 при conflict, absence или
uncertainty. Historical `AOS-3/AOS_Core_Roadmap.md` не конкурирует с R9 и не
владеет current documentation progress.

## 7. Conflict and unknown handling

При `CONFLICT`, `UNKNOWN` или `NOT_FOUND` не угадывать owner, claim или решение.
Запись finding должна содержать:

```yaml
finding:
  classification: CONFLICT | UNKNOWN | NOT_FOUND
  confirmed_facts: []
  conflicting_or_missing_claim:
  affected_fact_class:
  affected_action:
  resolution_step:
  blocked_scope:
```

Правила обработки:

1. Сохранить подтверждённые facts отдельно от disputed или missing claim.
2. Назвать один affected fact class и exact affected action.
3. Дать один bounded resolution step: проверить owner, восстановить exact
   source/identity, повторить direct observation или получить explicit human
   decision.
4. Блокировать только affected action. Safe read-only inspection, provenance
   analysis и reporting продолжаются, если они не зависят от disputed claim.
5. `UNKNOWN` не заменять model inference; `NOT_FOUND` не превращать в отсутствие
   вне declared search boundary; `NOT_RUN` не превращать в `PASS`.

Для текущего owner assignment этого R1:

```yaml
owner_assignment_conflicts: []
owner_assignment_unknowns: []
```

## 8. Invalidation and staleness

Entry или весь map становится stale, когда выполняется хотя бы одно применимое
условие:

- принято новое current explicit human decision;
- принят новый artifact в том же fact class;
- изменился exact authoritative source path, revision, hash или identity;
- изменилось repository state для mutable fact;
- owner или owner artifact superseded;
- обнаружен competing owner;
- mirror, derived index, coverage artifact или status view не соответствует
  authoritative source;
- snapshot-bound Evidence потеряла subject binding, freshness или
  reproducibility;
- decision-bound record потерял actor, subject или exact decision provenance.

После invalidation агент возвращается к precedence, проверяет authoritative
owner и direct observation, затем обновляет только affected claim. Этот map не
самообновляется и не может объявить себя fresh.

## 9. Cold-start routing

Cold-start агент действует в следующем порядке:

1. Установить current explicit human decision и его exact subject boundary.
2. Открыть `planning/CURRENT.md` как durable owner persisted lifecycle state и
   непосредственно проверить его current identity. Если более новое explicit
   human decision расходится с записанным state, считать persisted state stale
   до отдельного разрешённого обновления и не исправлять его по inference.
3. Из `planning/CURRENT.md` определить записанные active roadmap, active
   interval и `next_bounded_action`.
4. Использовать этот owner map только для выбора authoritative source нужного
   fact class; затем читать owner content и проверять его identity/freshness.
5. Не использовать owner map как owner progress state, active interval,
   acceptance, activation, authorization или следующего действия.
6. При `UNKNOWN`, `NOT_FOUND` или `CONFLICT` не угадывать; зафиксировать finding
   по разделу 7 и блокировать только affected action.
7. Не выводить execution или Git authorization из acceptance, activation,
   readiness, Evidence, validation result или `PASS`.

Для mutable repository facts всегда выполнить fresh read-only observation
непосредственно перед planning, execution, validation или Git action.

## 10. Owner-map boundary assertion

```yaml
owns_progress_state: false
owns_active_interval: false
owns_next_bounded_action: false
owns_human_decisions: false
creates_acceptance: false
creates_activation: false
creates_execution_authorization: false
creates_implementation_authorization: false
creates_git_authorization: false
redefines_owner_content: false
current_state_owner: planning/CURRENT.md
```
