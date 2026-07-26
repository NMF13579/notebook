# 03 — AOS Development


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Назначение

Документ описывает shortest safe development path для новой AOS: от выбранной product feature до human decision и отдельно разрешённой Git delivery. Это workflow candidate, а не execution authorization.

Главная формула:

```text
accepted user problem/outcome
→ sufficiently detailed Feature Dossier
→ targeted reference research where needed
→ DRAFT architecture decision
→ bounded Task Brief
→ repository preflight
→ explicit EXECUTE authorization
→ scoped implementation + targeted checks
→ Stage Report + stop
→ separate VALIDATE
→ separate REVIEW
→ human decision
→ separately authorized Commit / Push / Merge / Release
```

## 2. Entry conditions для реализации feature

До implementation feature должна иметь минимум:

- purpose и user value;
- primary actors;
- trigger и preconditions;
- inputs и observable outputs;
- happy path и decision points;
- states/transitions;
- failures и recovery experience;
- authority/safety boundaries;
- acceptance criteria и negative scenarios;
- dependencies/shared contracts;
- explicit unknowns;
- targeted legacy questions, если reference inspection действительно нужен.

Если этих данных нет, текущий stage — `PLAN` или documentation refinement, а не `EXECUTE`.

## 3. Feature-driven reconstruction protocol

### 3.1 Select one feature family

Выбирается один dossier из `06_Features.md`. Сначала подтверждаются user, problem, outcome и current disposition. Broad idea bank не расширяет scope автоматически.

### 3.2 Formulate explicit gaps

Research question должен быть узким. Допустимые примеры:

- какие inputs/outputs поддерживал historical installer;
- какие exit codes и machine-readable results проверялись doctor tests;
- какие states покрывал candidate freeze;
- как historical review package отделял Evidence от human decision;
- какие failure cases доказаны negative fixtures;
- какие legacy elements были recovery-specific и не нужны greenfield implementation.

Недопустимая формулировка:

```text
понять весь AOS-FARM
```

### 3.3 Bind reference snapshot

Для repository research записать:

```yaml
repository:
ref_or_branch:
commit_or_tree:
paths: []
read_only: true
commands_or_methods: []
limitations: []
```

Chat memory не подтверждает current branch, HEAD, tests или working implementation.

### 3.4 Inspect in high-signal order

```text
user-facing docs and commands
→ contracts/schemas
→ tests and negative fixtures
→ implementation paths
→ reports, plans and recovery artifacts
```

Tests важнее descriptive claims, но historical test PASS не является current PASS или target requirement.

### 3.5 Classify each finding

```text
SOURCE_ASSERTION
VERIFIED_OBSERVATION
INFERENCE
PROPOSAL
UNKNOWN
NOT_FOUND
NOT_RUN
BLOCKED
```

Для capability status дополнительно:

```text
VERIFIED_WORKING | PARTIALLY_WORKING | DESIGN_ONLY | BROKEN |
OBSOLETE | RECOVERY_SPECIFIC | UNKNOWN
```

### 3.6 Update dossier, do not copy topology

Research output должен обновить:

- behavior and edge cases;
- contract candidates;
- acceptance/negative scenarios;
- failure/recovery rules;
- useful implementation patterns;
- explicitly rejected legacy complexity;
- remaining human decisions.

Default:

```text
REIMPLEMENT_FROM_CONTRACT
```

Code reuse требует отдельного license, dependency, security, maintenance и compatibility decision.

## 4. Task decomposition

### 4.1 Decompose only as deep as execution requires

Candidate hierarchy:

```text
Epic
→ Stage
→ Sub-stage only when materially useful
→ executable Task
```

Use lazy decomposition:

- не раскрывать весь future backlog заранее;
- создавать child tasks только когда parent outcome и boundary ясны;
- не превращать каждый check или report в отдельный project stage;
- разделять tasks только по authority boundary, independent validation, material risk, protected operation или distinct acceptance outcome.

### 4.2 Child-parent integrity

Каждый child должен указывать:

- parent objective;
- inherited constraints;
- exact contribution to parent acceptance;
- dependencies;
- terminal result;
- what remains open.

Количество closed children не доказывает completion parent objective.

## 5. Task Brief contract

Минимальный Task Brief:

```yaml
task_id:
title:
goal:
user_outcome:
feature_id:
stage: PLAN | EXECUTE | VALIDATE | REVIEW
repository:
worktree:
branch:
HEAD:
baseline:
candidate_identity_model:
scope:
  allowed_paths: []
  forbidden_paths: []
allowed_operations: []
forbidden_operations: []
assumptions: []
unknowns: []
proposed_Risk_Profile:
assigned_Risk_Profile: UNASSIGNED
sandbox:
network_access:
dependencies:
validation_matrix: []
stop_conditions: []
execution_authorized: false
Git_authorizations:
  commit: false
  push: false
  merge: false
  release: false
```

### Completeness rules

- `PLAN` нужен при incomplete Task Brief, ambiguous scope, unknown baseline, unassigned required Risk Profile, protected/destructive risk, source conflict или permission expansion.
- При complete routine Task Brief planning не повторяется.
- Plan не становится Task Brief автоматически.
- Complete Task Brief не выдаёт execution authorization.
- Task Brief не может сам назначить Risk Profile или расширить repository/network/sandbox.

## 6. Repository preflight

Before any mutation verify directly:

1. repository root and expected identity;
2. worktree path;
3. branch and detached-state condition;
4. HEAD and baseline;
5. staged, unstaged and relevant untracked state;
6. actual diff;
7. nested repositories and symlinks;
8. allowed/forbidden path normalization;
9. interpreter/dependency identity;
10. sandbox/network/remote permissions;
11. temporary-output boundary;
12. stop conditions and candidate identity strategy.

### Dirty-state classification

```text
IN_SCOPE_EXISTING
OUT_OF_SCOPE_USER_STATE
ENVIRONMENT_NOISE
GENERATED_DISPOSABLE
UNKNOWN_MATERIAL
```

Не считать все untracked files автоматическим blocker, но и не скрывать material dirty state. Для bounded work предпочтителен clean isolated worktree.

### Safe remote identity

Не выводить raw remote URL или credential-bearing value. Отчёт может содержать normalized host/repository identity и `credentials_present`, но не секрет.

## 7. Stage model

### PLAN

Read-only. Produces decision-ready Task Brief, risks, validation and stop conditions. Не меняет target artifact.

### EXECUTE

- только exact authorized scope;
- один stage;
- no hidden next stage;
- no parallel writes;
- targeted checks допустимы;
- finding/failure/completion → report and stop;
- no correction after validation because validation is separate.

### VALIDATE

Read-only verification exact candidate. Не исправляет artifact. Required `NOT_RUN` не может стать `PASS`.

### REVIEW

Read-only assessment and recommendation. Не симулирует human acceptance и не начинает correction.

### DELIVER

Handoff/context package. Не является stage и не разрешает Git operation.

## 8. Stage Report contract

Every terminal report should contain:

```yaml
task_id:
stage:
result: PASS | FAIL | UNKNOWN | NOT_RUN | BLOCKED | HUMAN_REVIEW_REQUIRED
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed:
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true
```

Claim ceiling: report wording cannot be stronger than checks actually run.

## 9. Implementation rules

1. Implement observable behavior, not legacy folder structure.
2. Use one owner for shared contract and reference it elsewhere.
3. Separate pure analysis from mutation.
4. Bind preview to apply; changed subject invalidates authorization.
5. Write atomically or journal enough for deterministic reconciliation.
6. Make retries explicit and idempotent.
7. Preserve user-owned state on install/update/remove.
8. Configuration defaults fail closed for authority-bearing fields.
9. Runtime must use the same strict contract validator exercised by tests.
10. CLI failure paths must have stable machine-readable result and non-success exit semantics.
11. `--help` and read-only operations must have zero repository side effects.
12. Optional feature failure must not corrupt core state.
13. No hidden provider/network call.
14. No automatic fallback to a more privileged model/agent/environment.
15. No silent compatibility commitment.

## 10. Test strategy

### 10.1 Unit tests

Pure logic:

- schema/closed vocabulary validation;
- status aggregation;
- path normalization and allowlists;
- state transitions;
- digest/candidate identity;
- conflict detection;
- permission classification;
- idempotency rules.

### 10.2 Contract tests

- Task Brief required fields;
- execution authorization default false;
- unknown status rejected;
- Risk Profile closed vocabulary;
- CLI result and exit codes;
- Human Decision cannot be agent-generated;
- install/update ownership classes;
- stable JSON/text output version;
- Source of Truth and derived-view separation.

### 10.3 Integration tests

- intake → specification;
- discovery → capability/gap map;
- preview → exact apply;
- Task Brief → preflight → executor;
- executor → report → validation;
- Project Memory → resume on changed HEAD;
- install/update → reconciliation;
- review package → human decision record;
- candidate freeze → immutable validation subject.

### 10.4 End-to-end journeys

- first install and first safe command;
- idea to human review;
- interrupted session resume;
- blocked protected action;
- validation with `NOT_RUN` required check;
- update preserving user data;
- commit/push/merge/release boundaries;
- incident → lesson → regression test.

### 10.5 Mandatory negative cases from history

- empty mapping accepted;
- bogus status accepted;
- free-form Risk Profile;
- bool accepted as integer;
- mismatched session ID;
- invalid CLI argument returns success/no final result;
- schema exists but runtime bypasses it;
- allowed paths not enforced;
- stale baseline or changed candidate;
- write-after-freeze;
- self-referential package identity;
- read-only command creates repository file;
- raw remote credential/URL leaks;
- unrelated untracked files staged;
- environment noise causes false blocker;
- required check `NOT_RUN` aggregated as PASS;
- Evidence or review package treated as authorization;
- default `authorized: true`;
- partial mutation without journal/recovery;
- update overwrites project-owned/human-owned state;
- external content treated as instruction;
- UI approval button without decision contract.

## 11. Validation protocol

1. Freeze exact subject identity.
2. Confirm validator imports/runs against subject, not live checkout or wrong environment.
3. Run high-signal targeted checks first.
4. Run wider suite only when relevant and permitted.
5. Record exact commands/methods and result.
6. Preserve required vs optional checks.
7. Classify environment limitation as `NOT_RUN` or `BLOCKED`, not PASS.
8. Inspect diff/scope after checks.
9. Verify validation itself caused no subject mutation.
10. Stop with one next action.

Independent validation is required for first vertical slice, protected/high-risk/architecture-sensitive/release-bound work and any Task Brief that specifies it. It is not automatically required for every reversible routine edit.

## 12. Human review

A compact review package should show:

- task and feature purpose;
- user-visible before/after;
- exact changed paths;
- Evidence summary with full pointers;
- acceptance criteria status;
- negative cases;
- findings and limitations;
- `NOT_RUN` checks;
- architecture/scope deviations;
- decision options: `ACCEPT`, `NEEDS_CHANGES`, `REJECT`, `DEFER`;
- one next action after the human decision.

One-document review is preferred; supporting artifacts remain linked rather than duplicated.

## 13. Recovery, resume and handoff

### Execution failure

```text
stop
→ preserve actual candidate/logs
→ classify partial writes
→ create recovery facts
→ no automatic retry
→ new authorized correction Task Brief
```

### Validation finding

```text
VALIDATE reports finding and stops
→ separate correction EXECUTE
→ separate correction VALIDATE
```

### Session interruption

Minimum handoff:

- repository/worktree/branch/HEAD;
- baseline/candidate identity;
- selected feature and Task Brief;
- completed stage and terminal result;
- actual changes;
- checks and `NOT_RUN`;
- findings/blockers;
- accepted human decisions;
- unconsumed authorizations;
- one next action.

On resume, all mutable repository facts are rechecked.

## 14. Git delivery

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Before each operation re-verify repository, branch, HEAD, candidate, working tree, remote identity and exact human authorization.

- Commit authorization does not authorize push.
- Push does not authorize merge.
- Merge does not authorize release.
- Fast-forward or merge method is a separate decision.
- Candidate accepted before a later mutation must be revalidated or re-bound.

## 15. Automation admission rule

Automation may be introduced only when:

- manual flow succeeded repeatedly;
- repeated work is measurable;
- inputs/outputs/states/failures are stable;
- false-positive/false-negative risk is understood;
- fallback/removal path exists;
- automation does not grant authority;
- benefit exceeds maintenance and context cost.

Registry, model routing, autonomous loops, runtime enforcement and broad RAG are deferred until these conditions are met.

## 16. Definition of documentation-to-implementation readiness

A feature can enter DRAFT architecture when its dossier is understandable and testable. It can enter implementation planning only after relevant human product decisions. It can enter execution only with exact Task Brief and authorization.

```text
Detailed dossier ≠ accepted feature
Accepted feature ≠ accepted architecture
Accepted architecture ≠ Task Brief
Task Brief ≠ execution authorization
Successful implementation ≠ human acceptance
Human acceptance ≠ Git delivery
```
