---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-07-26'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: c60c39b4bee652cde2fd2e38f81dc12b498aa817
active_path: docs/03_Development.md
document_language: ru
technical_identifiers_language: en
document_role: CANONICAL_DEVELOPMENT_WORKFLOW
authority_scope:
- task_workflow
- stage_boundaries
- validation_rules
- reporting_rules
- git_action_boundaries
---

# 03 — Разработка

## 1. Граница статуса

Документ задаёт принятый normative workflow для подготовки и проверки работы. Он не является Task Brief, Execution Authorization или разрешением на конкретную mutation либо Git-operation.

## 2. Сквозная модель проектирования и реализации

Процесс строго разделен на проектирование документации и runtime-реализацию.

### Проектирование документации (Workspace → AOS)

```text
Knowledge Baseline
↓
Workspace (Drafts)
↓
Pass 1 (System Design)
↓
Structural Review
↓
Pass 2 (Pipeline + Contracts)
↓
Integration Review
↓
Global Design Freeze
↓
Publish to AOS (Deliverable)
```

### Runtime Implementation (Реализация)

После публикации Deliverable в AOS:

```text
Implementation Roadmap
↓
Slice
↓
Task
↓
bounded Task Brief
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

## 3. Семантические различия

Analysis ≠ execution; Plan ≠ implementation; file presence ≠ behavior; readiness ≠ authorization; execution ≠ verification; test PASS ≠ acceptance; CI PASS ≠ approval; verification ≠ commit permission; Commit ≠ Push ≠ Merge ≠ Release; UNKNOWN ≠ OK; NOT_RUN ≠ PASS.

## 4. Условия входа

Feature должна иметь purpose/value, actors, trigger/preconditions, I/O, happy path, states, failures/recovery, dependencies, authority boundaries, acceptance, negative scenarios, unknowns и targeted reference questions.

## 5. Процесс, масштабируемый по риску

### Низкий / trivial

Scope → one reversible change → focused check → concise report. No redundant architecture chain.

### Средний

Explicit acceptance, short plan, relevant regression и handoff.

### Высокий / protected

Pinned baseline, inventory, protected paths, explicit authorization, rollback, Evidence package и human review.

### Критический / destructive / sensitive

Stop-before-action, least privilege, data/provider boundary, recovery plan и explicit human decision.

## 6. Reconstruction через feature

1. Выбрать feature из `06_Features.md`.
2. Подтвердить user/problem/outcome/disposition.
3. Сформулировать exact gaps.
4. Bind legacy repository/ref/SHA/paths read-only.
5. Inspect docs/commands → contracts/schemas → tests/negative fixtures → implementation → reports/plans.
6. Classify findings.
7. Обновить Feature Passport.
8. Не копировать legacy topology.
9. Stop when question answered or scope expands.

## 7. Ленивая декомпозиция

```text
Epic → Stage → Sub-stage only when material → executable Task
```

Child создаётся только по authority boundary, independent validation, material risk, protected operation, distinct acceptance или dependency. Closed children не доказывают parent completion.

## 8. Task Brief и Execution Authorization

Task Brief описывает goal/scope/constraints/validation. Authorization создаётся отдельно человеком, bind к exact task/subject, ограничен stage/operations/paths, имеет expiry/consumption и не разрешает Git actions.

## 9. Preflight репозитория

Проверить root, worktree, branch, HEAD, baseline, staged/unstaged/untracked, diff, nested repos, symlinks, paths, interpreter/dependencies, sandbox/network/remote, temp boundary, stop conditions, candidate identity, source/destination и credentials/data boundary.

```text
IN_SCOPE_EXISTING | OUT_OF_SCOPE_USER_STATE | ENVIRONMENT_NOISE | GENERATED_DISPOSABLE | UNKNOWN_MATERIAL
```

## 10. Модель стадий Runtime-реализации

Эти стадии применяются исключительно к написанию кода и защищенным операциям. Создание и редактирование документации в `workspace/` не требует прохождения через PLAN, EXECUTE, VALIDATE и REVIEW.

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

## 11. Жизненный цикл документации (Workspace → AOS)

Документационный цикл избавлен от тяжеловесных инженерных проверок.

1. **Workspace**: Вся черновая работа (drafts, research, notes) ведется в `workspace/`.
2. **Pass 1 (System Design)**: Проработка концепции, целей, границ продукта и Feature Dossiers (уровень WHAT).
3. **Structural Review**: Сверка границ WHAT / HOW. Убедиться, что в архитектуру не просочились детали реализации. Переход к Pass 2 только после успешного Structural Review.
4. **Pass 2 (Pipeline + Contracts)**: Формирование архитектурных контрактов, I/O и data flows.
5. **Integration Review**: Финальная проверка согласованности всех документов пакета. Переход к Freeze только после устранения всех конфликтов.
6. **Global Design Freeze**: Заморозка изменений. Критерий завершения документационного цикла — готовность пакета к передаче coding agent'у без неразрешенных архитектурных вопросов.
7. **Publish to AOS**: Перенос утвержденного пакета из `workspace/` в папку `AOS/` (чистовик-deliverable).

**Локальные корректировки (Local Corrections)**: 
Исправление опечаток, ссылок и форматирования в `workspace/` выполняется без полного ревью-цикла по маршруту: `Short Markdown Task → edit → check → report → stop`.

**Правила публикации deliverable (Handoff)**:
Пакет в `AOS/` передается coding agent'у как read-only Source of Truth. Coding agent не имеет права изменять документы в `AOS/` самостоятельно.

## 12. Отчёт стадии

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

## 13. Контроль изменений (только для Runtime)

*Данные правила относятся исключительно к Runtime Implementation. Они не распространяются на документационные изменения в `workspace/` (создание и редактирование Markdown-документов регулируется документационным workflow и не требует Runtime Execution Authorization).*

One active task, one causal change, no unrelated cleanup, inventory before sensitive mutation, explicit scope expansion, changed-file allowlist, atomic commit after separate authorization, docs↔schema↔CLI↔code↔tests consistency, source read-only during extraction, no automatic `git add -A`.

## 14. Правила реализации (только для Runtime)

*Данные правила относятся исключительно к Runtime Implementation.*

Implement observable behavior, one contract owner, separate analysis/mutation, preview binds apply, atomic/journaled writes, explicit idempotent retry, preserve user state, authority defaults false, same strict validator in runtime/tests, stable CLI failures, `--help` no writes, optional failure isolated, no hidden network/provider, no privilege escalation, no silent compatibility, portable links, adapter drift checks, AI-code rationale/ownership/tests/handoff.

## 15. Пять verification gates (для Runtime)

1. Structure.
2. Scope.
3. Acceptance.
4. Regression/smoke.
5. Security/release blockers.

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

## 16. Стратегия тестирования

Unit: schemas/status/path/state/digest/conflict/permission/idempotency. Contract: Task Brief, auth false, enums, CLI exits, generated decisions, ownership, output versions, SoT separation. Integration: intake→spec, discovery→map, preview→apply, task→executor, executor→validation, memory→resume, install→reconcile, review→decision, freeze→validation. E2E: first start, idea→review, interruption, protected block, NOT_RUN, update preservation, Git boundaries, incident→lesson.

## 17. Обязательные негативные сценарии

Empty mapping, bogus status, free-form Risk Profile, bool-as-int, mismatched session, malformed idle bypass, CLI exit 0 on failure, runtime schema bypass, scope not enforced, stale baseline, write-after-freeze, self-reference, read-only writes, remote secret leak, unrelated staging, environment false blocker, NOT_RUN→PASS, Evidence as auth, default authorized true, partial mutation no journal, update overwrites state, external instruction, UI approval, stale index, absolute links, conflicting entrypoints, adapter drift.

## 18. Протокол validation

Freeze subject; verify environment/import provenance; run targeted checks; wider suite only if relevant; record commands/results; preserve required/optional; classify limitations; inspect diff; verify no validation mutation; stop with one next action.

## 19. Human review

One document: purpose, before/after, exact paths, Evidence, acceptance, negative cases, findings, NOT_RUN, deviations, decision options и next action.

## 20. Recovery и handoff

Execution failure → stop, preserve state/logs, classify partial writes, recovery facts, no auto-retry, correction task. Validation finding → report/stop, separate correction. Handoff records repo identity, task/candidate, result, changes, checks, blockers, decisions, permissions и next action. Mutable facts rechecked on resume.

## 21. Git delivery

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Before each action reverify repo/branch/HEAD/candidate/worktree/remote/auth. Later mutation invalidates old binding.

## 22. Manual dogfood и допуск automation

Measure comprehension, clarification loops, scope drift, authority confusion, time to Evidence/review, handoff quality и Governance overhead. Automate only proven repetition with stable contracts, known failures, fallback/removal and no authority expansion.

## 23. Цепочка готовности

```text
Detailed Feature Passport ≠ accepted feature
Accepted feature ≠ accepted architecture
Accepted architecture ≠ Task Brief
Task Brief ≠ Execution Authorization
Successful implementation ≠ human acceptance
Human acceptance ≠ Git delivery
```
