---
document_type: AOS_CORE_SCHEMA_CORRECTION
contract_family: AOS_CORE_CONTRACT
schema_id: aos.core.project_memory
schema_version: 2.0.0
record_kind: PROJECT_MEMORY
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: DRAFT_CONTRACT_CANDIDATE
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope: C-012_PROJECT_MEMORY_SCHEMA_VERSION_2_0_0
task_id: DOC-007-CORRECTION-CORE-C012-V2
technical_result: PASS
readiness: READY_FOR_FINAL_PACKAGE_REVIEW
human_acceptance: NOT_RUN
supersedes_for_future_consumers: aos.core.project_memory@1.0.0
accepted_v1_subject: AOS_CORE_CONTRACT_R1.md
accepted_v1_sha256: 24f1af001bc0249d9c8e40a9608c2c5b67ea047bf2307cbda251f184b223d5db
accepted_v1_modified: false
runtime_implementation: NOT_RUN
runtime_migration: NOT_RUN
implementation_repository_creation: NOT_RUN
execution_authorization: NOT_RUN
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 — C-012 Project Memory schema v2.0.0

## 1. Решение и граница коррекции

Этот candidate устраняет один конфликт между принятым `C-012 v1` и принятым first-cycle outcome `H1-003`:

- Project Memory должен существовать после сохранения `Intent Record` и до появления `Product Spec`/`Task Brief`;
- `C-012 v1` безусловно требует `current_stage` и `active_task_ref`;
- следовательно, `v1` не может честно представить допустимое состояние без active Task Brief.

Текущая explicit human decision задаёт единственное schema-level изменение:

```text
active_task_status: NONE | ACTIVE
NONE   → current_stage absent AND active_task_ref absent
ACTIVE → current_stage present AND active_task_ref present
```

Принятый subject [`AOS_CORE_CONTRACT_R1.md`](AOS_CORE_CONTRACT_R1.md) не изменяется. Этот файл является отдельной major-version correction и до exact final human acceptance имеет `authority: NONE_UNTIL_HUMAN_ACCEPTANCE`.

```text
Accepted C-012 v1 remains immutable
→ C-012 v2 is the current provisional schema owner
→ future consumers bind exact version 2.0.0
→ runtime migration remains NOT_RUN
```

## 2. Version identity и compatibility boundary

| Field | Value |
|---|---|
| `schema_id` | `aos.core.project_memory` |
| `record_kind` | `PROJECT_MEMORY` |
| accepted prior version | `1.0.0` |
| corrected candidate version | `2.0.0` |
| version reason | requiredness change + new closed enum |
| silent upgrade/downgrade | forbidden |
| accepted v1 bytes | unchanged |
| existing runtime records | `NOT_RUN` — implementation отсутствует |

Версия `2.0.0` использует primitives, `CoreRecord` envelope, canonical serialization, strict loader и общие authority/permission rules из принятого `AOS_CORE_CONTRACT_R1.md`. При конфликте v2 может изменять только payload schema `C-012`; все остальные `C1–C2` правила остаются неизменными.

## 3. Closed enum

```text
ActiveTaskStatus = NONE | ACTIVE
```

Unknown member, wrong case, `null`, пустая строка или пропущенное поле дают `CONTRACT_VIOLATION`. Значение не выводится по наличию других полей: producer обязан записать его явно, validator затем проверяет cross-field invariants.

## 4. Exact payload schema `aos.core.project_memory@2.0.0`

```text
required:
  memory_id: Identifier
  mode: enum<MemoryMode>
  repository_identity: RepositoryIdentity
  active_task_status: enum<ActiveTaskStatus>
  baseline_ref: SubjectRef
  candidate_refs: list<SubjectRef>
  accepted_decision_refs: list<RecordRef>
  findings: list<NonEmptyText>
  blockers: list<NonEmptyText>
  check_refs: list<RecordRef>
  authorization_status: enum<AuthorizationStatus>
  one_next_action: NonEmptyText
  freshness_checked_at: UtcTimestamp
optional:
  current_stage: enum<TaskStage>
  active_task_ref: RecordRef
  authorization_ref: RecordRef
```

Как и в `C1`, `additionalProperties: false`, `null` запрещён, optional означает только отсутствие поля.

### 4.1. Active-task invariants

1. `active_task_status: NONE` запрещает одновременно `current_stage` и `active_task_ref`.
2. `active_task_status: ACTIVE` требует одновременно `current_stage` и `active_task_ref`.
3. Наличие только одного conditional field всегда `CONTRACT_VIOLATION` при любом status.
4. При `ACTIVE` `active_task_ref.schema_id` должен быть `aos.core.task_brief`, его `record_kind` после resolution — `TASK_BRIEF`, а digest/subject должны соответствовать exact active task.
5. При `NONE` `authorization_status` должен быть `NONE`, а `authorization_ref` должен отсутствовать: authorization не может существовать без exact task binding.
6. `NONE` не означает terminal project state. `one_next_action` остаётся обязательным и описывает один bounded read-only/human action либо literal `NONE`.

### 4.2. Unchanged v1 invariants retained in v2

- `authorization_status: NONE` требует отсутствующий `authorization_ref`; любой другой authorization status требует exact ref;
- только `authorization_status: ACTIVE` может участвовать в разрешении protected action, после fresh C2 recheck;
- `candidate_refs` не содержат duplicate subject identity и имеют canonical order;
- every `accepted_decision_ref` resolves to an authentic exact human decision;
- `freshness_checked_at` — observation timestamp, не вечное утверждение freshness;
- summaries in `findings`/`blockers` не являются authority и должны иметь exact supporting refs;
- Project Memory остаётся единственным current lifecycle owner; handoff/index/dashboard — derived.

## 5. Valid state matrix

| `active_task_status` | `current_stage` | `active_task_ref` | `authorization_status` | Result |
|---|---:|---:|---|---|
| `NONE` | absent | absent | `NONE` | valid |
| `NONE` | present | absent | any | `CONTRACT_VIOLATION` |
| `NONE` | absent | present | any | `CONTRACT_VIOLATION` |
| `NONE` | present | present | any | `CONTRACT_VIOLATION` |
| `NONE` | absent | absent | not `NONE` | `CONTRACT_VIOLATION` |
| `ACTIVE` | present | present | any valid status | valid subject to ref/auth invariants |
| `ACTIVE` | absent | absent | any | `CONTRACT_VIOLATION` |
| `ACTIVE` | present | absent | any | `CONTRACT_VIOLATION` |
| `ACTIVE` | absent | present | any | `CONTRACT_VIOLATION` |

## 6. First-cycle examples

### 6.1. Valid `NONE` payload fragment

После сохранения `Intent Record` и до создания Task Brief:

```json
{
  "active_task_status": "NONE",
  "authorization_status": "NONE",
  "one_next_action": "Review the saved Intent Record and decide whether to start Product Spec preparation"
}
```

`current_stage`, `active_task_ref` и `authorization_ref` отсутствуют. Остальные required fields из section 4 остаются обязательными; fragment не является standalone record.

### 6.2. Valid `ACTIVE` payload fragment

```json
{
  "active_task_status": "ACTIVE",
  "current_stage": "PLAN",
  "active_task_ref": {
    "schema_id": "aos.core.task_brief",
    "record_id": "TASK-001",
    "schema_version": "1.0.0",
    "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "authorization_status": "NONE",
  "one_next_action": "Review the exact Task Brief and permission requirements"
}
```

## 7. Compatibility and migration

### 7.1. Consumer rules

1. Consumer declares exact supported version; same-major compatibility is not inferred.
2. A future first-cycle runtime MUST emit `2.0.0`, provided this exact candidate is human-accepted before implementation.
3. A `1.0.0` payload is never silently treated as `2.0.0`.
4. A `2.0.0/NONE` payload has no lossless v1 representation; downgrade is `BLOCKED_POLICY`.
5. A `2.0.0/ACTIVE` payload may be representable in v1 only through a separately implemented/tested explicit migration; direct relabeling is forbidden.

### 7.2. Deterministic future v1 → v2 mapping

Because valid v1 always contains `current_stage` and `active_task_ref`, a future explicit migration may:

```text
strict-load v1
→ preserve all v1 fields
→ add active_task_status: ACTIVE
→ set schema_version: 2.0.0
→ canonicalize
→ create new record identity and migration Evidence
→ preserve source bytes/digest
```

No migration code or data mutation is performed in this documentation repository.

```yaml
runtime_implementation: NOT_RUN
runtime_records_inspected: NOT_RUN
runtime_migration: NOT_RUN
migration_reason: IMPLEMENTATION_DOES_NOT_EXIST
source_record_mutation: NOT_RUN
```

## 8. Acceptance and negative fixtures

| ID | Fixture | Expected result |
|---|---|---|
| `C012-V2-ACC-001-none-before-task` | `NONE`, both conditional fields absent, auth `NONE` | `PASS` |
| `C012-V2-ACC-002-active-plan` | `ACTIVE`, both fields present, exact Task Brief ref | `PASS` |
| `C012-V2-ACC-003-none-handoff` | handoff snapshot with no active task | `PASS` |
| `C012-V2-ACC-004-v1-preserved` | accepted v1 subject digest unchanged | `PASS` |
| `C012-V2-ACC-005-runtime-not-run` | no runtime implementation/migration claimed | `PASS` |
| `C012-V2-NEG-001-none-with-stage` | `NONE` + `current_stage` | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-002-none-with-task-ref` | `NONE` + `active_task_ref` | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-003-none-with-both` | `NONE` + both conditional fields | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-004-active-no-stage` | `ACTIVE` + task ref only | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-005-active-no-task-ref` | `ACTIVE` + stage only | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-006-active-neither` | `ACTIVE` + neither conditional field | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-007-unknown-status` | unregistered status | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-008-none-with-auth` | `NONE` + non-`NONE` authorization | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-009-fake-task-ref` | `ACTIVE` + non-Task Brief ref | `CONTRACT_VIOLATION` |
| `C012-V2-NEG-010-silent-relabel` | v1 bytes relabeled v2 without migration | `CONTRACT_VIOLATION` |

## 9. Recovery matrix

| Finding | Preserved authority | Bounded recovery | Validation oracle |
|---|---|---|---|
| v1 record observed in future runtime | original v1 bytes/digest | explicit v1→v2 migration task | both records strict-load; new identity/Evidence |
| invalid conditional pair | previous valid Project Memory | reject write; regenerate complete v2 record | strict loader + invariant matrix |
| `NONE` with authorization ref | previous valid Project Memory + auth record | reject state write; resolve task/auth lifecycle separately | C2 recheck + v2 strict load |
| attempted downgrade of `NONE` | v2 source record | stop with `BLOCKED_POLICY`; do not fabricate task | source digest unchanged |
| partial future migration | v1 source and previous current owner | no owner swap; recovery-required Evidence | atomic C3 protocol and ref integrity |

Recovery is never automatic self-heal and never creates a Task Brief to satisfy a schema.

## 10. Traceability

| Requirement | Source | Contract effect | Tests |
|---|---|---|---|
| save/resume before Task Brief | accepted `H1-003`, `FTR-001/FTR-016` first-cycle boundary | `active_task_status: NONE` | `ACC-001`, `NEG-001…003` |
| one current state owner | `docs/02_Architecture.md`, C3 | v2 changes schema only, not owner path | C3 owner/recovery checks |
| no invented lifecycle state | `docs/00_Core.md`; `LES-023…025` | conditional absence is explicit, not inferred | `NEG-004…009` |
| compatibility honesty | accepted C1 version rules | major version; no silent migration | `ACC-004/005`, `NEG-010` |
| PASS/authorization separation | accepted C2 | `NONE` cannot carry authorization | `NEG-008` |

## 11. Candidate status

```yaml
correction_id: CORE-C012-V2-CORRECTION
schema_id: aos.core.project_memory
schema_version: 2.0.0
technical_result: PASS
readiness: READY_FOR_FINAL_PACKAGE_REVIEW
human_acceptance: NOT_RUN
accepted_C012_v1_modified: false
runtime_implementation: NOT_RUN
runtime_migration: NOT_RUN
implementation_authorization: NOT_RUN
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: CONTINUE_DOC-012_UNDER_CURRENT_AUTONOMOUS_MANDATE
stop: false
```
