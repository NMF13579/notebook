---
document_type: AOS_CORE_CONTRACT
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: SYNTHESIZED_PROPOSAL
authority: NONE_UNTIL_EXACT_HUMAN_ACCEPTANCE
authority_scope: C1_DATA_CONTRACTS_AND_C2_AUTHORITY_PERMISSIONS
task_id: DOC-006
technical_result: PASS
readiness: READY_FOR_HUMAN_REVIEW
human_acceptance: NOT_RUN
implementation_task_created: false
nearest_unimplemented_task: Task-001-Scaffolding.md
implementation_repository_creation: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 — Core Contract R1: C1–C2

## 1. Назначение и нормативная граница

Этот candidate определяет exact machine boundary постоянного ядра AOS для двух первых core slices:

- `C1` — versioned records, closed enums, strict validation, canonical serialization и compatibility;
- `C2` — authority precedence, Action Trust Boundary, permission classification, authorization lifecycle и protected-action enforcement.

Документ детализирует contract classes `C-001…C-014` из `docs/02_Architecture.md`, но не заменяет владельцев product facts, architecture baseline, workflow или human decisions. До exact human acceptance он остаётся `SYNTHESIZED_PROPOSAL`.

```text
Schema-valid ≠ true
Evidence ≠ authority
Task Brief ≠ Execution Authorization
Permission classification ≠ execution
PASS ≠ human acceptance
Human acceptance ≠ Git authorization
```

В `DOC-006` новый implementation Task Brief не создаётся: принятый `Task-001-Scaffolding.md` остаётся ближайшей нереализованной задачей.

## 2. Contract catalog и version identity

### 2.1. Exact schema IDs

| Architecture contract | `schema_id` | `record_kind` |
|---|---|---|
| `C-001` Intent Record | `aos.core.intent_record` | `INTENT_RECORD` |
| `C-003` Product Spec | `aos.core.product_spec` | `PRODUCT_SPEC` |
| `C-002` Feature Contract | `aos.core.feature_contract` | `FEATURE_CONTRACT` |
| `C-004` ADR | `aos.core.adr` | `ADR` |
| `C-005` Task Brief | `aos.core.task_brief` | `TASK_BRIEF` |
| `C-006` Execution Authorization | `aos.core.execution_authorization` | `EXECUTION_AUTHORIZATION` |
| `C-007` Preflight / Preview | `aos.core.preflight_preview` | `PREFLIGHT_PREVIEW` |
| `C-008` Execution / Stage Record | `aos.core.stage_record` | `STAGE_RECORD` |
| `C-009` ValidationEnvelope | `aos.core.validation_envelope` | `VALIDATION_ENVELOPE` |
| `C-010` Evidence Record | `aos.core.evidence_record` | `EVIDENCE_RECORD` |
| `C-011` Human Decision Record | `aos.core.human_decision` | `HUMAN_DECISION` |
| `C-012` Project Memory / Handoff | `aos.core.project_memory` | `PROJECT_MEMORY` |
| `C-013` Install / Update Manifest | `aos.core.install_manifest` | `INSTALL_MANIFEST` |
| `C-014` Git Delivery Record | `aos.core.git_delivery` | `GIT_DELIVERY_RECORD` |
| C2 support record | `aos.core.denied_action` | `DENIED_ACTION_RECORD` |

Initial version каждого schema ID: `1.0.0`. Один `schema_id` имеет одного schema owner; aliases запрещены.

### 2.2. Version rules

`schema_version` использует `MAJOR.MINOR.PATCH` без prefix.

- `MAJOR`: удаление/переименование поля, изменение типа/requiredness/meaning, добавление или удаление closed-enum member, изменение canonicalization или authority semantics.
- `MINOR`: только новое optional поле, которое отсутствует по умолчанию и не меняет результат старого payload.
- `PATCH`: clarification, fixture или validator defect fix без изменения accepted payload set.

Любая migration является отдельной deterministic function `source schema/version → target schema/version`, сохраняет исходные bytes/digest и создаёт новый record identity. Silent migration запрещена.

## 3. Exact data model

### 3.1. Schema notation

В этом документе:

- `T!` — required и не `null`;
- `T?` — optional; отсутствие допустимо, `null` недопустим;
- `list<T>` — JSON array, порядок значим, duplicate scalar items запрещены;
- `set<T>` — JSON array, canonical order ascending, duplicates запрещены;
- `enum<X>` — только members closed enum `X`;
- каждый object имеет `additionalProperties: false`;
- пустая строка недопустима; пустой list допустим только когда это прямо указано;
- JSON boolean не принимается как integer.

### 3.2. Primitive types

| Type | Exact constraint |
|---|---|
| `Identifier` | string, `^[A-Za-z][A-Za-z0-9._:-]{0,127}$` |
| `SchemaId` | one value из catalog section 2.1 |
| `SemVer` | `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$` |
| `Sha256` | lowercase string, `^[0-9a-f]{64}$` |
| `UtcTimestamp` | RFC 3339 UTC seconds, `YYYY-MM-DDTHH:MM:SSZ`; fractional seconds и offsets запрещены |
| `NonEmptyText` | Unicode string after NFC, length `1..65536`, no NUL |
| `ShortText` | Unicode string after NFC, length `1..1024`, no NUL |
| `RelativePath` | POSIX repository-relative path; no leading `/`, `..`, `.`, empty segment, NUL, backslash or percent-decoded escape |
| `CommandArg` | one argv element; no shell interpretation implied |
| `ExitCode` | integer `0..255`; boolean invalid |
| `PositiveInt` | integer `>=1`; boolean invalid |

### 3.3. Reusable exact objects

```text
ActorRef = {
  actor_class: enum<ActorClass>!,
  actor_id: Identifier!,
  display_name: ShortText?
}

RecordRef = {
  schema_id: SchemaId!,
  record_id: Identifier!,
  schema_version: SemVer!,
  sha256: Sha256!
}

SubjectRef = {
  subject_kind: enum<SubjectKind>!,
  subject_id: Identifier!,
  revision: Identifier!,
  sha256: Sha256!,
  repository: ShortText?,
  baseline_head: Sha256?
}

RepositoryIdentity = {
  repository: ShortText!,
  root_fingerprint: Sha256!,
  branch: ShortText!,
  head: Sha256!,
  worktree_fingerprint: Sha256!
}

Criterion = {
  criterion_id: Identifier!,
  statement: NonEmptyText!,
  oracle: NonEmptyText!
}

UnknownItem = {
  unknown_id: Identifier!,
  statement: NonEmptyText!,
  materiality: enum<Materiality>!,
  affected_action: ShortText?,
  resolution_step: NonEmptyText!
}

CheckResult = {
  check_id: Identifier!,
  required: boolean!,
  result: enum<CheckResultStatus>!,
  command: list<CommandArg>?,
  evidence_refs: list<RecordRef>!,
  limitations: list<NonEmptyText>!
}

PathScope = {
  allowed_paths: set<RelativePath>!,
  forbidden_paths: set<RelativePath>!,
  allowed_operations: set<enum<ActionClass>>!,
  forbidden_operations: set<enum<ActionClass>>!
}
```

`allowed_paths` и `forbidden_paths` не могут пересекаться после lexical normalization. Пустой `allowed_paths` означает отсутствие write permission, а не wildcard.

### 3.4. Common record envelope

Каждый persisted core record — один JSON object:

```text
CoreRecord = {
  schema_id: SchemaId!,
  schema_version: SemVer!,
  record_kind: enum<RecordKind>!,
  record_id: Identifier!,
  created_at: UtcTimestamp!,
  producer: ActorRef!,
  subject: SubjectRef!,
  claim_class: enum<ClaimClass>!,
  payload: PayloadBySchemaId!
}
```

Cross-field invariants:

1. `schema_id ↔ record_kind ↔ payload` должны совпадать с catalog.
2. `record_id` immutable; изменение payload создаёт новый record и digest.
3. `producer.actor_class: AGENT|SYSTEM_TOOL` не допускается для human authority.
4. `claim_class` описывает происхождение claim, но не открывает permission.
5. Self-reference на digest текущего record запрещена.

## 4. Closed enums

| Enum | Closed members |
|---|---|
| `RecordKind` | `INTENT_RECORD`, `PRODUCT_SPEC`, `FEATURE_CONTRACT`, `ADR`, `TASK_BRIEF`, `EXECUTION_AUTHORIZATION`, `PREFLIGHT_PREVIEW`, `STAGE_RECORD`, `VALIDATION_ENVELOPE`, `EVIDENCE_RECORD`, `HUMAN_DECISION`, `PROJECT_MEMORY`, `INSTALL_MANIFEST`, `GIT_DELIVERY_RECORD`, `DENIED_ACTION_RECORD` |
| `ActorClass` | `HUMAN`, `AGENT`, `SYSTEM_TOOL` |
| `ClaimClass` | `HUMAN_CONFIRMED_DIRECTION`, `HUMAN_ACCEPTED_FACT`, `OBSERVED_AT_SNAPSHOT`, `REPORTED`, `SYNTHESIZED`, `CONFLICT`, `NOT_FOUND`, `UNKNOWN`, `NOT_RUN`, `BLOCKED` |
| `SubjectKind` | `DOCUMENT`, `TASK`, `CANDIDATE`, `REPOSITORY_SNAPSHOT`, `EXECUTION_RUN`, `VALIDATION_RUN`, `DELIVERY_ACTION` |
| `DocumentMaturity` | `DRAFT`, `HUMAN_REVIEW_REQUIRED`, `HUMAN_ACCEPTED`, `SUPERSEDED` |
| `TaskStage` | `PLAN`, `EXECUTE`, `VALIDATE`, `REVIEW`, `DELIVER` |
| `TechnicalResult` | `CONTRACT_VIOLATION`, `FAIL`, `BLOCKED`, `UNKNOWN`, `NOT_RUN`, `PASS`, `HUMAN_REVIEW_REQUIRED` |
| `CheckResultStatus` | `CONTRACT_VIOLATION`, `FAIL`, `BLOCKED`, `UNKNOWN`, `NOT_RUN`, `PASS` |
| `HumanDecision` | `ACCEPT`, `NEEDS_CHANGES`, `REJECT`, `DEFER` |
| `DecisionIntent` | `ARTIFACT_DISPOSITION`, `ACTION_AUTHORIZATION`, `ACTION_DENIAL`, `AUTHORIZATION_REVOCATION` |
| `FeatureDisposition` | `SELECT_FOR_X1`, `SUPPORTING_CONTROL_ONLY`, `REQUIRED`, `OPTIONAL`, `DEFERRED`, `REFERENCE_ONLY`, `REJECTED`, `UNDECIDED` |
| `PermissionClass` | `ALLOWED`, `HUMAN_AUTHORIZATION_REQUIRED`, `BLOCKED_POLICY`, `BLOCKED_UNKNOWN`, `NOT_APPLICABLE` |
| `AuthorizationStatus` | `NONE`, `DRAFT_UNSIGNED`, `ACTIVE`, `CONSUMED`, `EXPIRED`, `REVOKED`, `INVALIDATED` |
| `AuthorizationScopeKind` | `TASK_EXECUTION`, `REPOSITORY_CREATION`, `GIT_COMMIT`, `GIT_PUSH`, `GIT_MERGE`, `GIT_RELEASE`, `DESTRUCTIVE_RECOVERY`, `SENSITIVE_OPERATION` |
| `RiskProfile` | `UNASSIGNED`, `ROUTINE`, `ELEVATED`, `PROTECTED`, `DESTRUCTIVE_SENSITIVE` |
| `ActionClass` | `READ_ONLY_LOCAL`, `DOCUMENTATION_EDIT`, `REPOSITORY_WRITE`, `RUNTIME_EXECUTION`, `NETWORK_READ`, `NETWORK_WRITE`, `CREDENTIAL_ACCESS`, `SENSITIVE_DATA_PROCESSING`, `EXTERNAL_DATA_EXPORT`, `REPOSITORY_CREATE`, `GIT_COMMIT`, `GIT_PUSH`, `GIT_MERGE`, `GIT_RELEASE`, `DESTRUCTIVE_FILE_OPERATION`, `AUTHORITY_STATE_MUTATION` |
| `Materiality` | `NON_MATERIAL`, `MATERIAL`, `CRITICAL` |
| `PreviewStatus` | `PREFLIGHT_ONLY`, `PREVIEW_READY`, `STALE`, `REJECTED` |
| `MemoryMode` | `CURRENT_STATE`, `HANDOFF_SNAPSHOT` |
| `DeliveryAction` | `COMMIT`, `PUSH`, `MERGE`, `RELEASE` |
| `AuthenticityMode` | `EXPLICIT_HUMAN_STATEMENT_EXACT_SUBJECT` |
| `HumanChannel` | `CHAT_SESSION`, `LOCAL_INTERACTIVE_CLI` |

Unknown enum member is `CONTRACT_VIOLATION`; it is never mapped to `UNKNOWN`, ignored or preserved as an extension.

## 5. Exact payload schemas

Все поля ниже являются exhaustive; unspecified fields запрещены.

### 5.1. `C-001` Intent Record

```text
required:
  actor: ActorRef
  original_request: NonEmptyText
  problem: NonEmptyText
  desired_outcome: NonEmptyText
  context: list<LabeledValue>
  constraints: list<NonEmptyText>
  non_goals: list<NonEmptyText>
  assumptions: list<NonEmptyText>
  unknowns: list<UnknownItem>
  sensitive_domain_flags: set<Identifier>
  source_refs: list<RecordRef>
optional: none

LabeledValue = {key: Identifier!, value: NonEmptyText!}
```

### 5.2. `C-003` Product Spec

```text
required:
  spec_id: Identifier
  title: ShortText
  problem: NonEmptyText
  users: list<ActorRef> (min 1)
  journeys: list<FlowStep> (min 1)
  scope: list<NonEmptyText>
  non_goals: list<NonEmptyText>
  constraints: list<NonEmptyText>
  metrics: list<Metric>
  dependencies: list<RecordRef>
  acceptance_criteria: list<Criterion> (min 1)
  open_decisions: list<UnknownItem>
optional: none

FlowStep = {step_id: Identifier!, actor: ActorRef!, trigger: NonEmptyText!, outcome: NonEmptyText!}
Metric = {metric_id: Identifier!, definition: NonEmptyText!, target: NonEmptyText!}
```

### 5.3. `C-002` Feature Contract

```text
required:
  feature_id: Identifier
  purpose: NonEmptyText
  users: list<ActorRef> (min 1)
  trigger: NonEmptyText
  preconditions: list<NonEmptyText>
  inputs: list<IOField>
  outputs: list<IOField>
  main_flow: list<FlowStep> (min 1)
  states: set<Identifier>
  transitions: list<Transition>
  failures: list<FailureCase>
  recovery: list<RecoveryRule>
  dependencies: list<RecordRef>
  constraints: list<NonEmptyText>
  authority_boundaries: list<NonEmptyText>
  acceptance_criteria: list<Criterion> (min 1)
  negative_scenarios: list<Criterion> (min 1)
  maturity: enum<DocumentMaturity>
  evidence_status: enum<TechnicalResult>
  human_disposition: enum<FeatureDisposition>
optional: none

IOField = {name: Identifier!, data_type: ShortText!, required: boolean!, constraints: list<NonEmptyText>!}
Transition = {transition_id: Identifier!, from: Identifier!, to: Identifier!, trigger: NonEmptyText!, guard: NonEmptyText!}
FailureCase = {failure_id: Identifier!, condition: NonEmptyText!, result: enum<TechnicalResult>!, observable: NonEmptyText!}
RecoveryRule = {failure_id: Identifier!, action: NonEmptyText!, validation: NonEmptyText!, automatic: boolean!}
```

`RecoveryRule.automatic: true` допустим только для idempotent, non-protected action, явно разрешённого feature contract.

### 5.4. `C-004` ADR

```text
required:
  adr_id: Identifier
  question: NonEmptyText
  context: NonEmptyText
  constraints: list<NonEmptyText>
  options: list<AdrOption> (min 2)
  consequences: list<NonEmptyText>
  reversal_conditions: list<NonEmptyText>
optional:
  selected_option: Identifier
  human_decision_ref: RecordRef

AdrOption = {option_id: Identifier!, description: NonEmptyText!, tradeoffs: list<NonEmptyText>!, evidence_refs: list<RecordRef>!}
```

`selected_option` и `human_decision_ref` либо оба присутствуют, либо оба отсутствуют. Присутствие без valid human decision — `CONTRACT_VIOLATION`.

### 5.5. `C-005` Task Brief

```text
required:
  task_id: Identifier
  goal: NonEmptyText
  user_outcome: NonEmptyText
  stage: enum<TaskStage>
  repository_requirement: RepositoryRequirement
  scope: PathScope
  assumptions: list<NonEmptyText>
  unknowns: list<UnknownItem>
  risk_profile: enum<RiskProfile>
  validation_matrix: list<Criterion> (min 1)
  stop_conditions: list<NonEmptyText> (min 1)
  correction_boundary: NonEmptyText
optional:
  feature_ref: RecordRef
  contract_refs: list<RecordRef>

RepositoryRequirement = {
  repository: ShortText!,
  baseline_requirement: enum<BaselineRequirement>!,
  observed_identity: RepositoryIdentity?
}
BaselineRequirement enum = FRESH_PREFLIGHT_REQUIRED | EXACT_OBSERVED_IDENTITY
```

Task Brief with write-capable operation and `risk_profile: UNASSIGNED` is valid as draft but not authorizable.

### 5.6. `C-006` Execution Authorization

```text
required:
  authorization_id: Identifier
  status: enum<AuthorizationStatus>
  scope_kind: enum<AuthorizationScopeKind>
  task_ref: RecordRef
  subject_ref: SubjectRef
  repository_identity: RepositoryIdentity
  allowed_stage: enum<TaskStage>
  path_scope: PathScope
  preview_ref: RecordRef
  risk_profile: enum<RiskProfile>
  single_use: boolean
  consumed_by: list<RecordRef>
  invalidation_reasons: list<NonEmptyText>
optional:
  issued_by_decision_ref: RecordRef
  issued_at: UtcTimestamp
  expires_at: UtcTimestamp
  revoked_by_decision_ref: RecordRef
```

`status: NONE` is forbidden in an Execution Authorization record and exists only for current-state projections where no authorization record exists.

- `DRAFT_UNSIGNED`: all issue/revocation fields absent; `consumed_by` and `invalidation_reasons` empty.
- `ACTIVE`: all issue fields present; revocation absent; `single_use: true`; `risk_profile != UNASSIGNED`; `consumed_by` and `invalidation_reasons` empty; `expires_at` future; exact human decision has `ACTION_AUTHORIZATION`; preview/repository/subject match; allowed operations non-empty.
- `CONSUMED`: all issue fields preserved; exactly one `consumed_by`; revocation absent.
- `EXPIRED`: all issue fields preserved; `consumed_by` empty; `invalidation_reasons` contains `EXPIRY_REACHED`; revocation absent.
- `REVOKED`: all issue fields preserved; `consumed_by` empty; `revoked_by_decision_ref` present and authentic; invalidation reasons include `HUMAN_REVOCATION`.
- `INVALIDATED`: all issue fields preserved; `consumed_by` empty; non-empty exact `invalidation_reasons`; revocation absent.

Execution Authorization never authorizes another authorization record.

### 5.7. `C-007` Preflight / Preview

```text
required:
  preview_id: Identifier
  status: enum<PreviewStatus>
  repository_identity: RepositoryIdentity
  task_ref: RecordRef
  subject_ref: SubjectRef
  planned_operations: list<PlannedOperation>
  intended_paths: set<RelativePath>
  conflicts: list<NonEmptyText>
  material_unknowns: list<UnknownItem>
  credentials_data_boundary: list<NonEmptyText>
  created_at: UtcTimestamp
  expires_at: UtcTimestamp
optional: none

PlannedOperation = {operation_id: Identifier!, action_class: enum<ActionClass>!, paths: set<RelativePath>!, description: NonEmptyText!}
```

`PREVIEW_READY` requires zero material unknowns/conflicts and exact normalized intended paths.

### 5.8. `C-008` Execution / Stage Record

```text
required:
  run_id: Identifier
  task_ref: RecordRef
  stage: enum<TaskStage>
  result: enum<TechnicalResult>
  starting_identity: RepositoryIdentity
  ending_identity: RepositoryIdentity
  actual_operations: list<ActualOperation>
  changed_paths: set<RelativePath>
  checks_run: list<CheckResult>
  checks_not_run: list<CheckResult>
  findings: list<NonEmptyText>
  limitations: list<NonEmptyText>
  unknowns: list<UnknownItem>
  out_of_scope_state: list<NonEmptyText>
  stop_reason: NonEmptyText
  next_required_action: NonEmptyText
  stop: boolean
optional:
  authorization_ref: RecordRef

ActualOperation = {operation_id: Identifier!, action_class: enum<ActionClass>!, paths: set<RelativePath>!, result: enum<CheckResultStatus>!}
```

`stop` MUST be `true`. A Stage Record containing any write/protected `actual_operations` requires `authorization_ref` to the consumed exact authorization. For a fully read-only run, `authorization_ref` MUST be absent; a fabricated sentinel is forbidden.

### 5.9. `C-009` ValidationEnvelope

```text
required:
  validation_id: Identifier
  subject_ref: SubjectRef
  validator_identity: ActorRef
  environment_identity: list<LabeledValue>
  required_checks: list<CheckResult>
  optional_checks: list<CheckResult>
  aggregate_result: enum<TechnicalResult>
  limitations: list<NonEmptyText>
  mutation_observed: boolean
  started_at: UtcTimestamp
  completed_at: UtcTimestamp
optional: none
```

Aggregation precedence for required checks:

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

`HUMAN_REVIEW_REQUIRED` may be emitted only as the terminal envelope result after all required checks aggregate to `PASS`; it is not a check result. Any required `NOT_RUN` prevents `PASS`.

### 5.10. `C-010` Evidence Record

```text
required:
  evidence_id: Identifier
  evidence_kind: enum<EvidenceKind>
  method: NonEmptyText
  command: list<CommandArg>
  subject_ref: SubjectRef
  observed_at: UtcTimestamp
  output_summary: NonEmptyText
  locator: NonEmptyText
  artifact_sha256: Sha256
  result: enum<CheckResultStatus>
  limitations: list<NonEmptyText>
  redaction: enum<RedactionStatus>
optional: none

EvidenceKind enum = COMMAND_OUTPUT | FILE_DIGEST | DIFF | TEST_RESULT | RUNTIME_OBSERVATION | HUMAN_OBSERVATION
RedactionStatus enum = NOT_REQUIRED | APPLIED | BLOCKED_SENSITIVE
```

Evidence records are immutable observations. They cannot contain permission or human decision fields.

### 5.11. `C-011` Human Decision Record

```text
required:
  decision_id: Identifier
  intent: enum<DecisionIntent>
  decision: enum<HumanDecision>
  candidate_id: Identifier
  subject_ref: SubjectRef
  human_statement: NonEmptyText
  actor: ActorRef
  decided_at: UtcTimestamp
  authenticity_mode: enum<AuthenticityMode>
  channel: enum<HumanChannel>
  evidence_refs: list<RecordRef>
  changes: list<NonEmptyText>
optional:
  supersedes: list<RecordRef>
```

`actor.actor_class` MUST equal `HUMAN`. `candidate_id`, exact `subject_ref.sha256` and semantic decision must all be present in `human_statement`; generated or inferred statements are invalid. `ACCEPT` with `changes` non-empty is invalid; corrected content requires a new subject.

### 5.12. `C-012` Project Memory / Handoff

```text
required:
  memory_id: Identifier
  mode: enum<MemoryMode>
  repository_identity: RepositoryIdentity
  current_stage: enum<TaskStage>
  active_task_ref: RecordRef
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
  authorization_ref: RecordRef
```

`authorization_status: NONE` requires absent `authorization_ref`; every other status requires an exact ref. Exact persistence path, atomic write и resume semantics принадлежат будущему `C3`; этот schema не разрешает second current-state owner.

### 5.13. `C-013` Install / Update Manifest

```text
required:
  manifest_id: Identifier
  package_ref: SubjectRef
  repository_identity: RepositoryIdentity
  ownership_entries: list<OwnershipEntry>
  operations: list<PlannedOperation>
  conflicts: list<NonEmptyText>
  preview_ref: RecordRef
  recovery_steps: list<NonEmptyText> (min 1)
  post_apply_checks: list<Criterion> (min 1)
optional: none

OwnershipEntry = {path: RelativePath!, owner_class: enum<OwnerClass>!, allowed_writers: set<Identifier>!}
OwnerClass enum = MANAGED | USER_OWNED | GENERATED | TEMPORARY | PROTECTED | FORBIDDEN
```

### 5.14. `C-014` Git Delivery Record

```text
required:
  delivery_id: Identifier
  action: enum<DeliveryAction>
  repository_identity_before: RepositoryIdentity
  repository_identity_after: RepositoryIdentity
  candidate_ref: SubjectRef
  human_decision_ref: RecordRef
  authorization_ref: RecordRef
  command: list<CommandArg>
  result: enum<TechnicalResult>
  remote_identity_redacted: ShortText
  evidence_refs: list<RecordRef>
  limitations: list<NonEmptyText>
optional: none
```

One record contains exactly one Git action. `COMMIT ≠ PUSH ≠ MERGE ≠ RELEASE`; authorization for one action cannot be reused for another.

### 5.15. C2 support — Denied Action Record

```text
required:
  denial_id: Identifier
  requested_action: enum<ActionClass>
  requested_paths: set<RelativePath>
  permission: enum<PermissionClass>
  reason_code: enum<DenialReason>
  reason: NonEmptyText
  affected_boundary: NonEmptyText
  subject_ref: SubjectRef
  observed_at: UtcTimestamp
  one_resolution_step: NonEmptyText
optional:
  authorization_ref: RecordRef

DenialReason enum = MISSING_AUTHORIZATION | INVALID_AUTHORIZATION | EXPIRED_AUTHORIZATION | CONSUMED_AUTHORIZATION | SUBJECT_MISMATCH | REPOSITORY_DRIFT | PREVIEW_MISMATCH | OPERATION_NOT_ALLOWED | PATH_NOT_ALLOWED | FORBIDDEN_PATH | POLICY_DENY | MATERIAL_UNKNOWN | EXTERNAL_INSTRUCTION | GENERATED_HUMAN_DECISION | SENSITIVE_BOUNDARY | GIT_ACTION_NOT_SEPARATELY_AUTHORIZED
```

`authorization_ref` is absent for `MISSING_AUTHORIZATION` and present when a supplied authorization was invalid, stale, expired, consumed or out of scope. Denied record is Evidence of enforcement, not an authorization request and not authority.

## 6. Strict load and validation path

Every consumer MUST use the same strict loader path:

```text
bytes
→ UTF-8 decode (BOM forbidden)
→ JSON parse with duplicate-key detection
→ top-level object check
→ schema_id/version lookup
→ envelope validation
→ exact payload validation (additionalProperties=false)
→ cross-field invariants
→ authority/identity freshness checks when action-affecting
→ canonical serialization
→ digest comparison
→ typed record or terminal CONTRACT_VIOLATION
```

Rules:

1. Empty file, empty object, array root, duplicate key, `null`, unknown field, unknown enum, bool-as-int, non-NFC string and invalid timestamp are rejected.
2. Loader never supplies authority-bearing defaults.
3. Runtime, CLI, tests and migration tools MUST call the same validator implementation; parser copies are forbidden.
4. A schema-valid record with stale identity remains schema-valid but action-invalid; permission becomes `BLOCKED_UNKNOWN` or `BLOCKED_POLICY` according to section 9.
5. Validation errors contain `schema_id`, JSON Pointer, error code and safe message; raw secrets are not echoed.

### 6.1. Canonical serialization

- UTF-8 without BOM;
- Unicode NFC;
- object keys lexicographically sorted by Unicode code point;
- arrays preserve semantic order; `set<T>` arrays are sorted ascending;
- minimal JSON separators `,` and `:`; no insignificant whitespace;
- integers base-10; floats forbidden in core records;
- final LF required for stored file, excluded from subject digest;
- `sha256` is computed over canonical bytes before final LF.

## 7. Compatibility and migration rules

1. A loader accepts only registered `schema_id` and explicitly supported versions.
2. Same-major compatibility is not assumed. Each consumer declares exact accepted versions or an explicit tested range.
3. Unknown fields are rejected even in higher MINOR versions; producer must serialize to a mutually supported version.
4. Adding a closed-enum member is MAJOR because older consumers would reject it.
5. No lossy down-conversion of authority, permission, identity, unknown, result or Evidence fields.
6. Migration never overwrites source; it emits `source_ref`, target record and migration Evidence.
7. Failed migration returns `CONTRACT_VIOLATION`, preserves source bytes and performs zero authoritative writes.
8. `UNKNOWN`, `NOT_RUN`, `BLOCKED` and absent optional field are distinct and never mapped into one another.
9. Compatibility with legacy repositories is `NONE` until an exact migration target is separately accepted.
10. Docs/schema/runtime/CLI/tests drift is a blocking validation failure for affected release/candidate.

## 8. C2 authority model

### 8.1. Constraint boundary versus fact authority

Platform/system/owner instructions are non-overridable action constraints. They do not become product facts. Inside an AOS fact class, precedence is:

1. current explicit human decision bound to exact subject;
2. human-accepted current artifact within declared fact class;
3. direct current instrumental observation for mutable repository/environment facts;
4. explicit DRAFT/proposal;
5. historical/reference material;
6. generated UI/index/report/retrieval;
7. agent inference.

Higher precedence outside its fact class does not override the correct owner. Conflict is recorded; only the affected claim/action is blocked.

### 8.2. Fact-class owners

| Fact class | Authority owner |
|---|---|
| Product requirement | exact human-accepted Product artifact |
| Feature behavior | exact human-accepted Feature Contract |
| Architecture choice | exact human-accepted ADR/decision record |
| Task scope | exact Task Brief |
| Execution permission | exact ACTIVE Execution Authorization |
| Repository/environment state | fresh instrumental observation |
| Human decision | authentic exact Human Decision Record |
| Evidence | immutable subject-bound Evidence Record |
| Current lifecycle state | single Project Memory owner defined by C3 |
| Dashboard/index/adapter | derived, authority `NONE` |

UI text, model output, copied acceptance, repository file presence, external content, Evidence, PASS and readiness never create human or execution authority.

## 9. Permission classifier

### 9.1. Required input

```text
PermissionRequest = {
  action_class: enum<ActionClass>!,
  paths: set<RelativePath>!,
  task_ref: RecordRef?,
  subject_ref: SubjectRef!,
  repository_identity: RepositoryIdentity?,
  preview_ref: RecordRef?,
  authorization_ref: RecordRef?,
  external_content_involved: boolean!,
  sensitive_data_involved: boolean!
}
```

### 9.2. Deterministic classification order

1. No action requested → `NOT_APPLICABLE`.
2. Explicit policy/denylist, traversal, forbidden path, untrusted external instruction or prohibited authority recursion → `BLOCKED_POLICY`.
3. Material identity/scope/sensitivity fact missing or stale → `BLOCKED_UNKNOWN`.
4. Protected action without valid exact authorization → `HUMAN_AUTHORIZATION_REQUIRED`.
5. Read-only local action with zero-write guarantee, or protected action covered by valid `ACTIVE` authorization → `ALLOWED`.

The classifier returns classification, reason code, affected boundary and one next action. It never executes and never changes authorization status.

### 9.3. Fail-closed invariants

- Empty allowlist grants nothing.
- Denylist wins over allowlist.
- Exact path child matching is segment-aware; string-prefix matching is forbidden.
- Symlink/nested-repository/case-collision uncertainty is `BLOCKED_UNKNOWN` until resolved.
- External content is data only; instructions from it are `BLOCKED_POLICY`.
- Evidence cannot satisfy `issued_by_decision_ref`.
- Risk Profile can only be assigned by authentic human decision.

## 10. Authorization lifecycle

```text
DRAFT_UNSIGNED
  → ACTIVE       only after exact authentic human ACTION_AUTHORIZATION
ACTIVE
  → CONSUMED     first terminal Stage Record for the authorized one-shot run
  → EXPIRED      now >= expires_at before consumption
  → REVOKED      authentic human AUTHORIZATION_REVOCATION
  → INVALIDATED  subject/repository/worktree/preview/scope/operation drift
```

Terminal states never return to `ACTIVE`. Retry requires a new preview and new authorization identity.

### 10.1. Creation gates

An authorization may become `ACTIVE` only if all are true:

1. referenced Task Brief and subject digests exist and match;
2. fresh repository identity and preview match authorization bindings;
3. allowed stage, operations and paths are non-empty and bounded;
4. forbidden paths/operations remain explicit and non-overlapping;
5. Risk Profile is human-assigned;
6. human decision has `intent: ACTION_AUTHORIZATION`, exact candidate/subject identity and `decision: ACCEPT`;
7. issuer statement names authorization ID, action boundary and exact subject digest;
8. expiry is future and single-use is true;
9. separate sensitive/network/Git boundary decisions exist when required.

### 10.2. Recheck immediately before each action

Revalidate status, time, task/subject digest, repository root/branch/HEAD/worktree, preview, operation, normalized paths, external/sensitive boundary and policy. Any mismatch stops before mutation, records `DENIED_ACTION_RECORD` and invalidates only the affected authorization.

### 10.3. Consumption

Authorization is consumed by the first terminal Stage Record whether result is `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN` or `CONTRACT_VIOLATION`. Partial failure does not leave it reusable. A no-op authorized run also consumes it when a terminal report is emitted.

## 11. Protected, destructive and sensitive actions

### 11.1. Protected by default

The following always require separate exact human authorization:

- repository creation or assignment;
- any Product Runtime or repository write outside a directly authorized documentation edit;
- runtime execution with side effects;
- network mutation;
- credential access, sensitive-data processing or external data export;
- authority/current-state mutation;
- destructive file operation or destructive recovery;
- `Commit`, `Push`, `Merge` and `Release`, each independently.

### 11.2. Never implied

- accepted Task Brief does not authorize execution;
- accepted implementation result does not authorize Git;
- Git `Commit` authorization does not authorize `Push`;
- `Push` does not authorize `Merge`; `Merge` does not authorize `Release`;
- permission for one repository, branch, subject, operation or path does not transfer;
- human acceptance of documentation does not authorize repository creation or scaffold generation.

### 11.3. Destructive stop rules

Before a destructive action, exact targets must be resolved by read-only observation; broad roots, unresolved variables/globs, unknown symlinks, unrelated user state and missing recovery are `BLOCKED_POLICY` or `BLOCKED_UNKNOWN`. Recovery must be scoped, previewed and separately authorized when destructive.

## 12. Valid examples

### 12.1. Minimal valid Human Decision payload

```json
{
  "actor":{"actor_class":"HUMAN","actor_id":"human:muhammed"},
  "authenticity_mode":"EXPLICIT_HUMAN_STATEMENT_EXACT_SUBJECT",
  "candidate_id":"AOS_3_CORE_C1_C2_DRAFT_R1_2026_08_05",
  "changes":[],
  "channel":"CHAT_SESSION",
  "decided_at":"2026-08-05T12:00:00Z",
  "decision":"ACCEPT",
  "decision_id":"decision:core-c1-c2-r1",
  "evidence_refs":[],
  "human_statement":"ACCEPT AOS_3_CORE_C1_C2_DRAFT_R1_2026_08_05 0000000000000000000000000000000000000000000000000000000000000000",
  "intent":"ARTIFACT_DISPOSITION",
  "subject_ref":{"revision":"DRAFT-R1","sha256":"0000000000000000000000000000000000000000000000000000000000000000","subject_id":"AOS_3_CORE_C1_C2_DRAFT_R1_2026_08_05","subject_kind":"DOCUMENT"}
}
```

The zero digest is illustrative only and MUST be replaced by the exact reviewed digest in a real record.

### 12.2. Valid permission classification without mutation

```json
{
  "classification":"HUMAN_AUTHORIZATION_REQUIRED",
  "reason_code":"MISSING_AUTHORIZATION",
  "affected_boundary":"REPOSITORY_CREATE",
  "one_next_action":"Request exact human authorization bound to repository identity and preview"
}
```

## 13. Acceptance matrix

| ID | Contract | Case | Expected observable result |
|---|---|---|---|
| `CORE-001` | C1 | valid record for every catalog schema | strict loader returns typed record; canonical round-trip stable |
| `CORE-002` | C1 | required/optional semantics | absent optional accepted; absent required and explicit `null` rejected |
| `CORE-003` | C1 | canonical bytes | same semantic record has one digest and byte representation |
| `CORE-004` | C1 | result aggregation | required worst status selected; required `NOT_RUN` prevents `PASS` |
| `CORE-005` | C1 | exact schema/runtime path | runtime and tests call same strict validator |
| `CORE-006` | C1 | exact version support | supported version accepted; unsupported version rejected without migration |
| `CORE-007` | C1 | explicit migration | source preserved; target and migration Evidence emitted |
| `CORE-008` | C1 | closed enums | every documented member accepted; no undocumented member accepted |
| `CORE-009` | C1 | subject binding | digest/revision mismatch detected before action-affecting use |
| `CORE-010` | C1 | evidence isolation | Evidence validates as observation but cannot populate authority fields |
| `CORE-011` | C2 | read-only local request | zero-write action classified `ALLOWED` without execution authorization |
| `CORE-012` | C2 | protected action without auth | `HUMAN_AUTHORIZATION_REQUIRED`, zero mutation, explicit reason |
| `CORE-013` | C2 | exact active auth | matching operation/path/subject/repository/preview classified `ALLOWED` |
| `CORE-014` | C2 | one-shot consumption | first terminal Stage Record changes status to `CONSUMED` |
| `CORE-015` | C2 | human revocation | active auth becomes `REVOKED`; subsequent request denied |
| `CORE-016` | C2 | expiry | expired auth cannot authorize any operation |
| `CORE-017` | C2 | Git independence | four actions require four separately bound authorizations/records |
| `CORE-018` | C2 | external content | content retained as data; embedded instruction ignored and denied |
| `CORE-019` | C2 | affected-only blocking | material unknown blocks only dependent action, not safe read-only analysis |
| `CORE-020` | C2 | denial reporting | denied request emits safe reason and one resolution step, no raw secret |

## 14. Negative fixtures

| Fixture | Input defect/attack | Expected result |
|---|---|---|
| `C1-NEG-001-empty-object.json` | `{}` | `CONTRACT_VIOLATION`; no typed record |
| `C1-NEG-002-extra-field.json` | unknown property | reject at exact JSON Pointer |
| `C1-NEG-003-unknown-enum.json` | `result: OK` | reject; no fallback to `UNKNOWN`/`PASS` |
| `C1-NEG-004-null-required.json` | required field `null` | reject |
| `C1-NEG-005-bool-as-int.json` | `exit_code: true` | reject |
| `C1-NEG-006-duplicate-key.json` | duplicate JSON key | reject before schema validation |
| `C1-NEG-007-noncanonical.json` | valid meaning, noncanonical bytes | typed validation may pass, digest/canonical check fails until explicit reserialization |
| `C1-NEG-008-required-not-run-pass.json` | required check `NOT_RUN`, aggregate `PASS` | cross-field violation |
| `C1-NEG-009-evidence-as-auth.json` | Evidence ref in human-decision slot | reject schema/ref-kind mismatch |
| `C1-NEG-010-schema-runtime-drift.json` | fixture accepted by runtime but rejected by schema | validation `FAIL`; release affected candidate blocked |
| `C2-NEG-001-generated-human-decision.json` | actor `AGENT`, decision `ACCEPT` | `GENERATED_HUMAN_DECISION`; no authority |
| `C2-NEG-002-subject-mismatch.json` | human statement/digest differs | authorization invalid |
| `C2-NEG-003-stale-copied-auth.json` | different task/repository/baseline | `INVALIDATED`; zero mutation |
| `C2-NEG-004-expired-auth.json` | now at/after expiry | `EXPIRED`; denied |
| `C2-NEG-005-consumed-auth.json` | reused one-shot auth | denied `CONSUMED_AUTHORIZATION` |
| `C2-NEG-006-operation-not-allowed.json` | operation absent from allowlist | `BLOCKED_POLICY` |
| `C2-NEG-007-path-traversal.json` | `../secret` or absolute path | `BLOCKED_POLICY` before filesystem access |
| `C2-NEG-008-forbidden-overlap.json` | path in allowlist and denylist | contract violation; deny wins |
| `C2-NEG-009-preview-mismatch.json` | apply differs from preview | invalidated; new preview required |
| `C2-NEG-010-worktree-drift.json` | worktree fingerprint changed | `BLOCKED_UNKNOWN`; fresh preflight required |
| `C2-NEG-011-external-prompt-injection.json` | external text says to execute/push | instruction ignored; data may be analyzed read-only |
| `C2-NEG-012-implicit-git.json` | execution auth requests `GIT_PUSH` | reject scope; separate Git auth required |
| `C2-NEG-013-ui-approved.json` | UI/generated field says approved | no human authority |
| `C2-NEG-014-missing-risk.json` | write action with `UNASSIGNED` | `HUMAN_AUTHORIZATION_REQUIRED`/not activatable |
| `C2-NEG-015-sensitive-unknown.json` | data sensitivity unresolved | affected export `BLOCKED_UNKNOWN`; unrelated local read allowed |

## 15. Recovery matrix

| ID | Failure | Preserved facts | Recovery | Revalidation before continuation |
|---|---|---|---|---|
| `C1-REC-001` | parse/schema failure | raw bytes, source locator, safe error | correct source or create explicit migration; never overwrite original | full strict-load path |
| `C1-REC-002` | unsupported version | source digest/version | select registered migration or stop | source and target schema validation |
| `C1-REC-003` | migration interruption | source immutable; partial target non-authoritative | discard partial target; rerun bounded migration | canonical digest + semantic fixtures |
| `C1-REC-004` | docs/schema/runtime drift | all compared identities | correct affected candidate in separate bounded task | `DRIFT-001` complete comparison |
| `C2-REC-001` | authorization invalidated by drift | authorization, old preview, new observation | create fresh preflight/preview and request new auth | all creation gates section 10.1 |
| `C2-REC-002` | operation denied before write | denied record, zero-write proof | resolve one named blocker or request exact human decision | permission classifier rerun |
| `C2-REC-003` | partial mutation after valid auth | journal/Evidence/actual state; auth consumed | stop; separate recovery task and, if destructive, separate auth | intended/actual reconciliation + post-recovery validation |
| `C2-REC-004` | human decision authenticity failure | untrusted record and exact subject | obtain explicit exact human statement; do not infer | Human Decision schema and semantic match |
| `C2-REC-005` | external instruction detected | external content as untrusted data | remove instruction from action inputs; continue safe analysis only | trust-boundary classification |
| `C2-REC-006` | secret-shaped output | sanitized Evidence only | block export, rotate/escalate outside AOS scope if needed | redaction scan and explicit sensitive boundary decision |

No recovery automatically reactivates or unconsumes an authorization.

## 16. Traceability

| Contract concern | Feature | Architecture contracts | Lessons/regressions |
|---|---|---|---|
| Task scope and separate authorization | `FTR-006` | `C-005`, `C-006`, `C-007`, `C-008` | `LES-008`, `009`, `012`, `017`, `024`, `025`; `AUTH-001…003`, `SCOPE-001…002`, `FREEZE-001` |
| Unified Result Contract | `FTR-011` | `C-008`, `C-009`, `C-010` | `LES-010`, `011`, `013…016`, `031`; `STATUS-001…003`, `CLI-001` |
| Action Trust Boundary | `FTR-019` | `C-006`, `C-007`, `C-010`, `C-011` | `LES-012`, `017`, `020`, `021`, `039`; `AUTH-002…003`, `CONTENT-001`, `GIT-001` |
| Strict loaders and drift | `FTR-030` | `C-001…C-014` | `LES-013…015`, `027`, `029`, `031`; `DRIFT-001`, `ADAPTER-001`, `IDLE-001` |
| Human authenticity | `FTR-019`, `FTR-021` reference dependency | `C-011` | `LES-008`, `009`, `039`; `AUTH-001`, `STATUS-003` |
| Git independence | `FTR-006`, `FTR-015` reference dependency | `C-006`, `C-014` | `LES-008`, `012`, `036`; `GIT-001` |

Feature dispositions remain those owned by `AOS_IMPLEMENTATION_DECISIONS_R1.md` and `docs/06_Features.md`; traceability does not select or implement a feature.

`LES-*` citations use the accepted lessons/regression inventory as design input. They do not promote any item from `LESSON_PROPOSAL` to `HUMAN_ACCEPTED_RULE`; normative effect in this file comes only from the exact C1–C2 candidate if separately accepted.

## 17. Proposed future implementation outline — non-executable

After `Task-001-Scaffolding` is actually completed and accepted, a future human-selected task may implement the smallest C1–C2 consumer gate:

```text
strict envelope + Intent Record + ValidationEnvelope
→ permission classifier in read-only mode
→ Human Decision / Execution Authorization validation
→ negative fixtures
```

This outline has no task ID, allowlist, authorization form or execution readiness. It is not a backlog activation or Task Brief.

## 18. Candidate status and stop

```yaml
DOC-006:
  technical_result: PASS
  readiness: READY_FOR_HUMAN_REVIEW
  human_acceptance: NOT_RUN
contract_scope:
  C1: DOCUMENTED_AS_CANDIDATE
  C2: DOCUMENTED_AS_CANDIDATE
nearest_unimplemented_task: Task-001-Scaffolding.md
new_implementation_Task_Brief: NOT_CREATED
DOC-007: NOT_RUN
implementation_repository_creation: NOT_RUN
scaffold_generation: NOT_RUN
runtime_implementation: NOT_RUN
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: HUMAN_REVIEW_EXACT_DOC-006_PACKAGE
stop: true
```
