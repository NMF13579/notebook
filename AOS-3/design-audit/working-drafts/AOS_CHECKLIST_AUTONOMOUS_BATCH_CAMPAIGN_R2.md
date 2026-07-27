---
document_id: AOS_CHECKLIST_AUTONOMOUS_BATCH_CAMPAIGN_R2
document_type: AUTONOMOUS_BOUNDED_EXECUTION_PACKAGE
revision: R2
status: GENERATED_DRAFT
authority: PROPOSAL
campaign_id: CTD-R2-91c09008c67fc81bd7948383
supersedes: AOS_CHECKLIST_AUTONOMOUS_BATCH_CAMPAIGN_R1
current_validated_state:
  pilot: PASS_REPORTED
  B001: PASS_REPORTED
  B002: PASS_REPORTED
  B003: PASS_REPORTED
indexed_items: 346
processed_items_reported: 27
remaining_items_reported: 319
automatic_conflict_resolution: BOUNDED
human_decision_authority_preserved: true
implementation_authorization: NONE
git_authorization: NONE
reference_write_authorization: NONE
network_authorization: NONE
---

# Autonomous Checklist Batch Campaign R2

## 1. Вывод

Этот пакет автоматизирует оставшуюся checklist extraction campaign без ручной пересылки каждого batch и добавляет bounded automatic conflict resolution.

```text
human authorizes campaign once
→ controller selects batch
→ executor performs research
→ conflict resolver classifies and resolves permitted conflicts
→ validator checks batch
→ PASS: continue automatically
→ unresolved material conflict / FAIL / BLOCKED: stop
→ all items terminal: compile
→ final campaign validation
→ HUMAN_REVIEW_REQUIRED
```

Автоматическое разрешение конфликтов не означает автоматическое принятие Product, Architecture или authority decisions.

---

# 2. Conflict classes

Каждый conflict получает один exact class:

```yaml
conflict_classes:
  - DUPLICATE_EVIDENCE
  - DUPLICATE_QUESTION
  - PATH_ALIAS
  - FORMAT_VARIATION
  - SNAPSHOT_STALENESS
  - TARGET_SOURCE_PRECEDENCE
  - TARGET_INTERNAL_CONFLICT
  - REFERENCE_INTERNAL_CONFLICT
  - CROSS_REFERENCE_CONFLICT
  - TARGET_REFERENCE_CONFLICT
  - CLAIM_SCOPE_CONFLICT
  - COVERAGE_DERIVATION_CONFLICT
  - PRODUCT_DECISION_CONFLICT
  - ARCHITECTURE_DECISION_CONFLICT
  - AUTHORITY_CONFLICT
  - SAFETY_BOUNDARY_CONFLICT
  - UNKNOWN_CONFLICT
```

Conflict record:

```yaml
conflict_id:
question_id:
batch_id:
class:
claims:
sources:
fact_classes:
authority_ranking:
resolution_mode: AUTO|DEFER|HUMAN_REQUIRED
resolution_rule:
selected_claim:
rejected_or_retained_claims:
confidence: HIGH|MEDIUM|LOW
evidence_ids:
impact:
status: RESOLVED|UNRESOLVED
```

---

# 3. Automatically resolvable conflicts

Automatic resolution разрешена только при deterministic rule и достаточном evidence.

## 3.1 Duplicate evidence

Если два evidence records имеют одинаковые:

```text
repository + commit + path + line range + excerpt_sha256
```

оставить один canonical record, остальные отметить:

```yaml
resolution: DEDUPLICATED
authority_change: NONE
```

## 3.2 Duplicate questions

Автоматически объединять только exact normalized duplicates при совпадении:

- normalized text;
- section path;
- document owner;
- material dimensions.

Один ID становится primary, второй получает `alias_of`.

Не объединять одинаковый текст из разных contexts автоматически.

## 3.3 Path aliases

Если realpath и Git object identity доказывают, что два пути указывают на один объект, использовать canonical repository-relative path.

Symlink escape не разрешать — `BLOCKED`.

## 3.4 Format variations

Различия whitespace, heading punctuation, YAML key ordering или Markdown formatting разрешать через canonical normalization, если semantic content неизменён.

## 3.5 Snapshot staleness

При конфликте mutable observation:

```text
older current observation
vs
newer current observation
```

выбирать snapshot, pinned для текущей campaign.

Не использовать newest worktree автоматически. Campaign snapshot имеет приоритет в рамках campaign reproducibility.

## 3.6 Target source precedence

Применять project authority hierarchy:

```text
1. Current explicit human decision
2. Human-accepted project artifact — только в его fact class
3. Direct current repository observation — mutable repository facts
4. DRAFT/PROPOSAL
5. Historical/reference reports
6. Model inference
```

Автоматически выбирать higher-authority claim только когда:

- claims относятся к одному fact class;
- scope совпадает;
- higher authority однозначна;
- нет current human decision conflict;
- selected claim не расширяется за пределы evidence.

## 3.7 Reference conflicts

AOS-FARM и AgentOS имеют authority над target `NONE`.

При различии reference approaches:

- не выбирать один как target truth;
- сохранить оба как alternative reference patterns;
- классифицировать differences;
- создать `SYNTHESIZED` comparison;
- recommendation: `DESIGN_NEW` или `HUMAN_DECISION_REQUIRED`.

Conflict считается operationally resolved для продолжения extraction, но не design-resolved.

## 3.8 Target vs reference

Target accepted artifact всегда имеет приоритет в своём fact class.

Reference finding:

- не заменяет target fact;
- может выявить gap;
- может добавить alternative;
- получает `authority_over_target: NONE`.

## 3.9 Claim scope conflict

Если broad claim не полностью поддержан evidence, автоматически сузить claim до доказанного scope.

Пример:

```text
"Система всегда блокирует mutation"
→
"Guard X блокирует mutation для перечисленных protected paths в tested scenario Y"
```

Нельзя повышать claim ceiling.

## 3.10 Coverage derivation conflict

Применять deterministic ordering:

```text
CONFLICT
> UNKNOWN
> NOT_RUN
> NOT_FOUND
> PARTIAL
> COVERED
```

Но `CONFLICT` используется только при несовместимых target claims одного fact class.

Reference disagreement само по себе не делает target coverage `CONFLICT`.

---

# 4. Conflicts requiring human decision

Автоматически не разрешать:

## 4.1 Product decisions

- actors;
- user priority;
- product boundary;
- feature disposition;
- acceptance semantics;
- UX choice;
- MVP scope.

```yaml
resolution_mode: HUMAN_REQUIRED
stop_campaign: false_if_question_can_be_marked_terminal
question_status: HUMAN_DECISION_REQUIRED
```

Campaign может продолжить другие вопросы.

## 4.2 Architecture decisions

- topology;
- module ownership;
- state model selection;
- API/schema choice;
- lifecycle semantics;
- dependency choice;
- platform/control-plane foundation.

Такие conflicts записываются в unresolved decision register.

## 4.3 Authority conflicts

Если current human decision расходится с accepted artifact:

```yaml
selected_for_current_action: CURRENT_EXPLICIT_HUMAN_DECISION
artifact_status: CONFLICT
canonical_artifact_mutation: NOT_AUTHORIZED
human_followup_required: true
```

Campaign продолжает только если затронутый вопрос можно завершить как `HUMAN_DECISION_REQUIRED`.

## 4.4 Safety boundary conflicts

Любая неоднозначность в destructive action, protected path, mutation permission, Git action или reference write:

```yaml
resolution_mode: HUMAN_REQUIRED
technical_result: BLOCKED
stop_campaign: true
```

## 4.5 Unknown conflict

Если conflict нельзя надёжно классифицировать:

```yaml
class: UNKNOWN_CONFLICT
technical_result: BLOCKED
stop_campaign: true
```

---

# 5. Continue-vs-stop policy

Не каждый human-required design conflict останавливает всю campaign.

## Continue automatically

Продолжать, если:

- conflict локален одному question;
- mutation не требуется;
- вопрос можно завершить terminal state:
  - `CONFLICT`;
  - `UNKNOWN`;
  - `HUMAN_DECISION_REQUIRED`;
- остальные questions независимы;
- safety/identity/fingerprint не затронуты.

## Stop immediately

Остановиться, если conflict затрагивает:

- campaign identity;
- parser index;
- accepted baseline identity;
- evidence integrity;
- output fingerprint;
- candidate immutability;
- protected paths;
- Git/reference mutation;
- controller state;
- более 20% оставшихся вопросов;
- shared assumption, от которого зависят следующие batches.

---

# 6. Conflict resolver pipeline

```text
DETECT
→ NORMALIZE CLAIMS
→ CLASSIFY
→ APPLY AUTHORITY AND FACT-CLASS RULES
→ TEST AUTO-RESOLUTION ELIGIBILITY
→ RESOLVE OR DEFER
→ VALIDATE RESOLUTION
→ WRITE CONFLICT RECORD
→ CONTINUE OR STOP
```

`resolve_conflict.py` не редактирует source evidence.

Он может создавать только:

```text
02_batches/<BATCH_ID>/records/conflicts/**
03_compiled/unresolved-decisions.md
00_control/CONFLICT_LEDGER.jsonl
```

---

# 7. Automatic correction boundary

Разрешена только data-level correction внутри незамороженного staging:

- remove exact duplicate record;
- normalize path;
- recalculate derived status;
- narrow unsupported claim;
- restore missing deterministic metadata;
- rerun deterministic extraction for same bounded query.

Запрещено автоматически:

- менять parser index;
- менять selected question text;
- менять accepted baseline;
- редактировать published batch;
- менять production guards;
- расширять research scope без budget;
- выбирать Product/Architecture option;
- изменять canonical documents.

После publication любая correction создаёт новый batch attempt и требует отдельного conflict/correction record.

---

# 8. Retry policy

```yaml
max_auto_resolution_attempts_per_conflict: 2
max_auto_research_retry_per_question: 1
max_batch_rebuilds: 0
```

Если conflict не разрешён после двух bounded attempts:

```yaml
status: UNRESOLVED
question_status: HUMAN_DECISION_REQUIRED|UNKNOWN|CONFLICT
```

Не зацикливаться.

---

# 9. Autonomous state machine

```yaml
states:
  - READY
  - SELECTING_BATCH
  - EXECUTING_BATCH
  - RESOLVING_CONFLICTS
  - VALIDATING_BATCH
  - BATCH_VALIDATED
  - COMPILING
  - VALIDATING_CAMPAIGN
  - COMPLETE
  - FAILED
  - BLOCKED
  - HUMAN_REVIEW_REQUIRED
```

Transitions:

```text
EXECUTING_BATCH → RESOLVING_CONFLICTS
RESOLVING_CONFLICTS → VALIDATING_BATCH
RESOLVING_CONFLICTS → BLOCKED
VALIDATING_BATCH → BATCH_VALIDATED
BATCH_VALIDATED → SELECTING_BATCH
BATCH_VALIDATED → COMPILING
VALIDATING_CAMPAIGN → HUMAN_REVIEW_REQUIRED
```

---

# 10. Conflict metrics

После каждого batch записывать:

```yaml
conflicts_detected:
conflicts_auto_resolved:
conflicts_deferred:
conflicts_human_required:
conflicts_blocking:
resolution_attempts:
authority_overrides:
claim_scope_narrowings:
reference_alternatives_retained:
```

Campaign completion допускает:

```yaml
blocking_conflicts: 0
unresolved_safety_conflicts: 0
unresolved_identity_conflicts: 0
human_decision_required_questions: any_nonnegative_integer
```

То есть design questions могут остаться на human review, но extraction campaign завершится.

---

# 11. Exact authorization prompt

```text
AOS EXECUTE OK CHECKLIST-EXTRACTION-AUTONOMOUS-CAMPAIGN-R2;
CAMPAIGN_ID=CTD-R2-91c09008c67fc81bd7948383;
START_AFTER_BATCH=B003;
PROCESS_SCOPE=ALL_REMAINING_PARSER_ELIGIBLE_ITEMS;
BATCH_SIZE_DEFAULT=8;
BATCH_SIZE_MAX=12;
MAX_NEW_BATCHES=45;
AUTO_CONTINUE_ON=VALIDATION_PASS,AUTO_RESOLVED_CONFLICT,NON_BLOCKING_HUMAN_DECISION_REQUIRED;
AUTO_RESOLVE_CONFLICT_CLASSES=DUPLICATE_EVIDENCE,DUPLICATE_QUESTION_SAME_CONTEXT,PATH_ALIAS,FORMAT_VARIATION,SNAPSHOT_STALENESS,TARGET_SOURCE_PRECEDENCE,REFERENCE_INTERNAL_CONFLICT,CROSS_REFERENCE_CONFLICT,TARGET_REFERENCE_CONFLICT,CLAIM_SCOPE_CONFLICT,COVERAGE_DERIVATION_CONFLICT;
DEFER_CONFLICT_CLASSES=PRODUCT_DECISION_CONFLICT,ARCHITECTURE_DECISION_CONFLICT,AUTHORITY_CONFLICT;
STOP_ON=SAFETY_BOUNDARY_CONFLICT,UNKNOWN_CONFLICT,CONTRACT_VIOLATION,FAIL,BLOCKED,BUDGET_EXHAUSTED,FINGERPRINT_MISMATCH,CANDIDATE_MUTATION,REFERENCE_MUTATION,CAMPAIGN_IDENTITY_CHANGE,PARSER_INDEX_CHANGE,ACCEPTED_BASELINE_CHANGE;
MAX_AUTO_RESOLUTION_ATTEMPTS_PER_CONFLICT=2;
ALLOW_STAGING_DATA_CORRECTION=true;
ALLOW_PUBLISHED_BATCH_CORRECTION=false;
ALLOW_AUTOMATIC_DESIGN_DECISIONS=false;
ALLOW_AUTOMATIC_AUTHORITY_CHANGE=false;
PROGRESS_REPORT_EVERY_BATCHES=5;
PROGRESS_REPORT_STOPS_EXECUTION=false;
COMPILE_ONLY_WHEN_UNPROCESSED_IN_SCOPE_ZERO=true;
ALLOW_HUMAN_DECISION_REQUIRED_AS_TERMINAL=true;
RUN_FINAL_CAMPAIGN_VALIDATION=true;
CREATE_WORKING_DRAFTS=false;
CANONICAL_DOC_WRITES=NONE;
CHECKLIST_WRITES=NONE;
REFERENCE_WRITES=NONE;
GIT_ACTIONS=NONE;
NETWORK=NONE
```

---

# 12. Terminal report

Добавить:

```yaml
conflict_summary:
  detected:
  auto_resolved:
  deferred:
  human_required:
  blocking:
automatic_resolution_log:
unresolved_decision_register:
questions_completed_as_human_decision_required:
```

Final result:

```yaml
PASS:
  meaning: extraction and validation completed
  acceptance: NOT_GRANTED
  next_required_action: HUMAN_REVIEW_GENERATED_DRAFTS_AND_UNRESOLVED_DECISIONS
```

---

# 13. Итоговое решение

Автоматизировать разрешение можно, но только по заранее заданным deterministic rules.

Оптимальная граница:

```text
technical/evidence/reference conflict
→ auto-resolve where deterministic

Product/Architecture choice
→ record and continue

authority/safety/identity conflict
→ stop
```

Так campaign сможет завершиться без постоянной пересылки сообщений и без симуляции human authority.
