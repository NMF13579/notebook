---
package: AOS_Integrated_Knowledge_Package
package_revision: R3-RU
updated: 2026-07-26
status: APPROVED
authority: AUTHORITATIVE
human_review: REQUIRED
human_acceptance: ACCEPTED
implementation_authorization: AUTHORIZED
git_authorization: AUTHORIZED
self_audit: COMPLETED
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
document_language: ru
technical_identifiers_language: en
document_role: DEVELOPMENT_WORKFLOW
proposed_post_acceptance_role: CANONICAL_DEVELOPMENT_WORKFLOW
proposed_authority_scope:
  - task_workflow
  - stage_boundaries
  - validation_rules
  - reporting_rules
  - git_action_boundaries
source_files_bound_by_blob_sha: true
---

# 03 — Разработка

## 1. Граница статуса

Документ предлагает normative workflow после human acceptance. Он не является Task Brief и не разрешает конкретную mutation или Git-operation.

## 2. End-to-end model

```text
accepted user problem/outcome
→ detailed Feature Passport
→ targeted reference research if needed
→ DRAFT architecture decision
→ bounded Task Brief
→ repository preflight
→ explicit Execution Authorization
→ smallest scoped implementation
→ Stage Report and stop
→ separate VALIDATE when required
→ REVIEW
→ human decision
→ separate Commit / Push / Merge / Release
→ handoff and lesson proposal
```

## 3. Semantic distinctions

Analysis ≠ execution; Plan ≠ implementation; file presence ≠ behavior; readiness ≠ authorization; execution ≠ verification; test PASS ≠ acceptance; CI PASS ≠ approval; verification ≠ commit permission; Commit ≠ Push ≠ Merge ≠ Release; UNKNOWN ≠ OK; NOT_RUN ≠ PASS.

## 4. Entry conditions

Feature должна иметь purpose/value, actors, trigger/preconditions, I/O, happy path, states, failures/recovery, dependencies, authority boundaries, acceptance, negative scenarios, unknowns и targeted reference questions.

## 5. Risk-scaled flow

### Low / trivial

Scope → one reversible change → focused check → concise report. No redundant architecture chain.

### Medium

Explicit acceptance, short plan, relevant regression и handoff.

### High / protected

Pinned baseline, inventory, protected paths, explicit authorization, rollback, Evidence package и human review.

### Critical / destructive / sensitive

Stop-before-action, least privilege, data/provider boundary, recovery plan и explicit human decision.

## 6. Feature-driven reconstruction

1. Выбрать feature из `06_Features.md`.
2. Подтвердить user/problem/outcome/disposition.
3. Сформулировать exact gaps.
4. Bind legacy repository/ref/SHA/paths read-only.
5. Inspect docs/commands → contracts/schemas → tests/negative fixtures → implementation → reports/plans.
6. Classify findings.
7. Обновить Feature Passport.
8. Не копировать legacy topology.
9. Stop when question answered or scope expands.

## 7. Lazy decomposition

```text
Epic → Stage → Sub-stage only when material → executable Task
```

Child создаётся только по authority boundary, independent validation, material risk, protected operation, distinct acceptance или dependency. Closed children не доказывают parent completion.

## 8. Task Brief и Execution Authorization

Task Brief описывает goal/scope/constraints/validation. Authorization создаётся отдельно человеком, bind к exact task/subject, ограничен stage/operations/paths, имеет expiry/consumption и не разрешает Git actions.

## 9. Repository preflight

Проверить root, worktree, branch, HEAD, baseline, staged/unstaged/untracked, diff, nested repos, symlinks, paths, interpreter/dependencies, sandbox/network/remote, temp boundary, stop conditions, candidate identity, source/destination и credentials/data boundary.

```text
IN_SCOPE_EXISTING | OUT_OF_SCOPE_USER_STATE | ENVIRONMENT_NOISE | GENERATED_DISPOSABLE | UNKNOWN_MATERIAL
```

## 10. Stage model

### PLAN
Read-only. Decision-ready Task Brief, risks, validation, stop conditions.

### EXECUTE
Exact authorized scope, one stage, no hidden next stage, no unrelated cleanup; terminal result → report and stop.

### VALIDATE
Read-only exact candidate. Does not fix. Independent validation required only when risk/task demands it.

### REVIEW
Read-only assessment/recommendation. No simulated acceptance or correction.

### DELIVER
Handoff package, not stage or Git permission.

## 11. Stage Report

```yaml
task_id:
stage:
result:
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
Git_operations: {commit: NOT_RUN, push: NOT_RUN, merge: NOT_RUN, release: NOT_RUN}
next_required_action:
stop: true
```

## 12. Change control

One active task, one causal change, no unrelated cleanup, inventory before sensitive mutation, explicit scope expansion, changed-file allowlist, atomic commit after separate authorization, docs↔schema↔CLI↔code↔tests consistency, source read-only during extraction, no automatic `git add -A`.

## 13. Implementation rules

Implement observable behavior, one contract owner, separate analysis/mutation, preview binds apply, atomic/journaled writes, explicit idempotent retry, preserve user state, authority defaults false, same strict validator in runtime/tests, stable CLI failures, `--help` no writes, optional failure isolated, no hidden network/provider, no privilege escalation, no silent compatibility, portable links, adapter drift checks, AI-code rationale/ownership/tests/handoff.

## 14. Five verification gates

1. Structure.
2. Scope.
3. Acceptance.
4. Regression/smoke.
5. Security/release blockers.

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

## 15. Test strategy

Unit: schemas/status/path/state/digest/conflict/permission/idempotency. Contract: Task Brief, auth false, enums, CLI exits, generated decisions, ownership, output versions, SoT separation. Integration: intake→spec, discovery→map, preview→apply, task→executor, executor→validation, memory→resume, install→reconcile, review→decision, freeze→validation. E2E: first start, idea→review, interruption, protected block, NOT_RUN, update preservation, Git boundaries, incident→lesson.

## 16. Mandatory negative cases

Empty mapping, bogus status, free-form Risk Profile, bool-as-int, mismatched session, malformed idle bypass, CLI exit 0 on failure, runtime schema bypass, scope not enforced, stale baseline, write-after-freeze, self-reference, read-only writes, remote secret leak, unrelated staging, environment false blocker, NOT_RUN→PASS, Evidence as auth, default authorized true, partial mutation no journal, update overwrites state, external instruction, UI approval, stale index, absolute links, conflicting entrypoints, adapter drift.

## 17. Validation protocol

Freeze subject; verify environment/import provenance; run targeted checks; wider suite only if relevant; record commands/results; preserve required/optional; classify limitations; inspect diff; verify no validation mutation; stop with one next action.

## 18. Human review

One document: purpose, before/after, exact paths, Evidence, acceptance, negative cases, findings, NOT_RUN, deviations, decision options и next action.

## 19. Recovery and handoff

Execution failure → stop, preserve state/logs, classify partial writes, recovery facts, no auto-retry, correction task. Validation finding → report/stop, separate correction. Handoff records repo identity, task/candidate, result, changes, checks, blockers, decisions, permissions и next action. Mutable facts rechecked on resume.

## 20. Git delivery

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Before each action reverify repo/branch/HEAD/candidate/worktree/remote/auth. Later mutation invalidates old binding.

## 21. Manual dogfood and automation admission

Measure comprehension, clarification loops, scope drift, authority confusion, time to Evidence/review, handoff quality и Governance overhead. Automate only proven repetition with stable contracts, known failures, fallback/removal and no authority expansion.

## 22. Readiness chain

```text
Detailed Feature Passport ≠ accepted feature
Accepted feature ≠ accepted architecture
Accepted architecture ≠ Task Brief
Task Brief ≠ Execution Authorization
Successful implementation ≠ human acceptance
Human acceptance ≠ Git delivery
```
