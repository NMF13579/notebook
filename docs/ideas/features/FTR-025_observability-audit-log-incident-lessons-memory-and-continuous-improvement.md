---
document_id: AOS-FEATURE-FTR-025
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-025
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
human_acceptance: NOT_REQUESTED
product_scope_effect: NONE
implementation_authorization: NONE
execution_authorized: false
git_authorization: NONE
implementation_repository: UNASSIGNED
repository_verification: NOT_RUN
layer: "Product Runtime support / Later operations"
disposition: CANDIDATE_SUPPORT
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-063
  - IDEA-064
human_review_required: true
---

# FTR-025 — Observability, Audit Log, Incident/Lessons Memory and Continuous Improvement

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-025` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича фиксирует material events, incidents и lessons с provenance и превращает только human-reviewed lessons в test, pattern или backlog candidate.

**Source-derived desired outcome:** Minimal redacted event/incident/lesson loop that separates facts/inferences and converts reviewed lessons into preventive rules, tests or backlog candidates.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, maintainer, support agent, reviewer and future feature designer.

Основные jobs-to-be-done:

- Не потерять повторяющийся failure/near miss.
- Разделить observed facts и root-cause hypothesis.
- Собрать user friction и recovery data.
- Связать accepted lesson с preventive action.
- Не превратить metrics в readiness/approval.

## 4. Проблема и ожидаемая ценность

### Проблема

Failures, denied actions, user friction and workarounds are buried in chats/logs. Metrics can become vanity readiness signals, and lessons do not become tests.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Redacted audit events.
- Incident records and severity.
- Lesson candidates and human review.
- Preventive test/pattern/backlog links.
- Trend views with limitations.

### Out of scope / non-goals

- Log every event indefinitely.
- Automatic policy/priority changes.
- Full production APM platform.
- Root-cause assertion without evidence.
- Metrics as Source of Truth or approval.

## 6. Trigger и preconditions

### Triggers

- Material failure, denied action or near miss.
- Repeated user confusion/workaround.
- Release/runtime event.
- Dogfood cycle reveals friction.
- Dependency/security finding.

### Preconditions

- Event subject/time/impact identifiable.
- Privacy/redaction/retention policy.
- Fact vs inference classification.
- Human review path for lessons.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `stage_validation_review_results`
- `denied_action_and_recovery_records`
- `user_feedback`
- `runtime_or_release_metrics`
- `dependency_security_findings`
- `related_tests_patterns_tasks`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Audit event
- Incident record
- Lesson candidate
- Preventive test/rule proposal
- Trend view

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Capture material event.
2. Classify severity and evidence.
3. Analyze impact/root-cause candidate.
4. Propose lesson/preventive test.
5. Human reviews.
6. Link accepted lesson to test/backlog/pattern.
7. Measure recurrence.

### Иллюстративный сценарий

1. Возникает trigger: Material failure, denied action or near miss.
2. Система принимает входы `stage_validation_review_results, denied_action_and_recovery_records, user_feedback` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Audit event, Incident record, Lesson candidate.
5. При failure `Every log line becomes incident.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
EVENT_CAPTURED → TRIAGED → INCIDENT_OPEN | FYI → ANALYZED → LESSON_CANDIDATE → HUMAN_REVIEW → ACCEPTED_LESSON | REJECTED | UNKNOWN_CAUSE → PREVENTIVE_LINKED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Incident view shows impact, facts, hypotheses and unknowns separately.
- Sensitive data is redacted by default.
- Lesson card states proposed preventive test/rule and owner.
- Trend view declares sample/coverage limitations.
- Recurrence is linked to prior incident/lesson.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Only material events captured durably.
- `FR-002` — Root cause remains INFERENCE until supported/accepted.
- `FR-003` — Lesson cannot change policy/priority automatically.
- `FR-004` — Accepted lesson links to test/pattern/task and owner.
- `FR-005` — Metrics expose denominator/missing data.
- `FR-006` — Records support correction/supersession/redaction.
- `FR-007` — Retention and privacy boundaries enforced.

## 13. Capabilities из source synthesis

- Capture material event with subject/time/impact.
- Incident record with fact vs root-cause candidate.
- Redaction/privacy policy.
- Lesson candidate and human confirmation.
- Link preventive rule to test, feature or pattern.
- Track recurrence and user-friction trends.
- Optional dependency/security audit findings.
- Derived metrics with limitations, not Source of Truth.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `AuditEvent`: event_id, subject, time, type, impact, evidence, redaction, source.
- `CTR-002` — `IncidentRecord`: facts, hypotheses, severity, affected_users, response, unknowns, status.
- `CTR-003` — `LessonCandidate`: lesson, rationale, preventive_action, owner, evidence, human_disposition.
- `CTR-004` — `TrendMetric`: definition, source_coverage, window, value, limitations.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-014`, `FTR-022`, `FTR-023`, `FTR-016`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Lessons and metrics do not authorize or become Source of Truth without human acceptance in the correct fact class.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Every log line becomes incident.
- Root cause asserted without evidence.
- Sensitive data stored.
- Lesson automatically changes policy/priority.
- Metrics treated as approval.
- No owner/test, lesson forgotten.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Correct/supersede records transparently, redact/remove sensitive content per policy and retain unknown cause as inference.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Event/source timestamps and subject identity.
- Incident/recovery records.
- Human lesson disposition.
- Linked preventive test/pattern/task and recurrence data.

Минимальный Evidence package связывает:

```text
source / human decision
→ user problem
→ expected outcome
→ feature requirement
→ candidate / output
→ check result
→ finding / limitation
→ human decision
```

## 20. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-001` — Facts and hypotheses are distinguishable.
- `AC-002` — Sensitive data is not exposed.
- `AC-003` — Lesson requires human review.
- `AC-004` — Accepted lesson has an owner/preventive link.
- `AC-005` — Metrics do not imply approval.
- `AC-006` — Record can be corrected without history loss.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Every debug log becomes incident.
- `NEG-002` — Agent asserts root cause.
- `NEG-003` — Secret/token stored.
- `NEG-004` — Lesson automatically changes governance.
- `NEG-005` — Metric with incomplete coverage shown as absolute.
- `NEG-006` — Incident closed without unresolved unknowns visible.

## 22. Minimal implementation model — `PROPOSAL`

Repository-native incident/lesson records and small aggregator. Runtime telemetry/APM remains outside baseline. Focus on high-value failures and dogfood evidence.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: manual incident/lesson template.
- M1: denied-action/recovery integration.
- M2: preventive test/pattern/backlog linkage.
- M3: minimal trend view after sufficient data.

**Disposition rule:** Supporting capability; допускается только после связи с конкретным user-visible workflow и измеримой пользой.

## 24. Related micro-features

- `IDEA-063` — Observability and Audit Log
- `IDEA-064` — Continuous Improvement, Lessons Feedback and Dependency/Security Audit

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which events are material enough to persist?
- What privacy/retention policy applies?
- Who accepts lessons?
- Which metrics support Product Runtime learning?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-025`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `03 — AOS Future and Legacy Reference.txt`
- `05 - AOS-FARM — справочные идеи из harness engineering.txt`

Limitations:

- Full raw export всех historical chats не доказан.
- Current repository/worktree/branch/HEAD/baseline и runtime implementation не проверялись: `NOT_RUN`.
- Legacy AOS-FARM/AOS-02/AgentOS materials имеют `READ_ONLY_REFERENCE`, `authority: NONE`.
- Requirements/contracts/tests в этом файле являются clean-room `PROPOSAL`.
- Family boundary может быть пересмотрена после Product Contract и human review.

## 27. Promotion path

```text
DRAFT feature description
→ human product-fit decision
→ Product Contract and refined acceptance scenarios
→ DRAFT architecture options
→ human architecture/dependency decision
→ bounded Task Brief
→ explicit execution authorization
→ EXECUTE
→ separate VALIDATE
→ separate REVIEW
→ human decision
→ separately authorized Git/release operations
```

## 28. Отдельные документы атомарных функций

Каждая функция ниже имеет собственный standalone document; ссылки не означают product acceptance.

- [`IDEA-063` — Observability and Audit Log](../functions/IDEA-063_observability-and-audit-log.md)
- [`IDEA-064` — Continuous Improvement, Lessons Feedback and Dependency/Security Audit](../functions/IDEA-064_continuous-improvement-lessons-feedback-and-dependency-security-audit.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_025`
