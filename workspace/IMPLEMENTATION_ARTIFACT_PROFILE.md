# Implementation Artifact Profile

```yaml
document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
revision: R4
freeze_identity: EXTERNAL_FREEZE_MANIFEST
status: DRAFT
authority_state: PROPOSAL
intended_fact_class: implementation_artifact_semantics
intended_owner_status: CANDIDATE
profile_activation: NOT_RUN
technical_result: NOT_RUN
readiness:
  target: HUMAN_PROFILE_PIPELINE_REVIEW
  state: NOT_READY
human_acceptance:
  state: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## 1. Ownership & Authority

После Human Acceptance exact revision этот Profile становится owner `implementation_artifact_semantics`.
До acceptance запрещено утверждать active normative ownership. До Human Acceptance Profile является только candidate.

**Invariant:**
`Pipeline defines FLOW. Artifact Profile defines ARTIFACT SEMANTICS.`

Profile не определяет: stages, flow, gates, lifecycle, execution.

### Dependency ≠ Authority (Package Internal Authority)
```yaml
authoritative_inputs:
  - source:
    authority_scope:
upstream_sources:
  - artifact_type:
    artifact_identity:
    required_role: PACKAGE_INTERNAL_UPSTREAM_SOURCE
    required_state: FROZEN_OR_VALIDATED_CANDIDATE
authority_inheritance: NONE
```
**Rule:** `Package component dependency ≠ authority inheritance`
Product Contract, Engineering Design, Portable Task и Validation Plan до принятия exact Package являются package-internal sources, а не автоматически HUMAN_ACCEPTED_FACT.

### Materiality Rule
**Burden of proof:**
`UNKNOWN → MATERIAL_ENGINEERING_DECISION` допустим только если доказано:
1. exact affected upstream requirement/invariant;
2. material impact на observable guarantee;
3. Capability Boundary недостаточен;
4. выбор нельзя отложить без изменения design.
Если это не доказано — не создавать false Human blocker.

---

## 2. Product Contract

```yaml
artifact_type: PRODUCT_CONTRACT
purpose: Define observable semantic boundaries and behaviors without implementation mechanics.
```

### Allowed Claim Classes
* observable behaviour
* semantic inputs
* semantic outputs
* observable states
* observable failures
* authority boundaries
* acceptance criteria

### Forbidden Claim Classes
* JSON/YAML/Markdown
* filesystem/storage mechanics
* repository facts (paths, branches)
* concrete commands (shell, git)
* implementation APIs
* transport mechanics
* target technology

### Required Sections & Section Semantics
1. **Contract Identity & Purpose:** Идентификация документа.
2. **Scope & Non-Goals:** Границы.
3. **Actors & Users:** Описание участников взаимодействия.
4. **User Outcome:** Какая ценность достигается.
5. **Trigger & Preconditions:** Условие запуска.
6. **Semantic Inputs:** Данные на входе.
7. **Semantic Outputs:** Ожидаемый результат.
8. **Observable Information Requirements:** Требуемая информация.
9. **Semantic Identifiers / Versioning:** Where material.
10. **Observable States & Transitions:** Изменение состояний среды.
11. **Observable State Effects:** Эффекты от состояний.
12. **Semantic Boundary Violations:** Недопустимые действия.
13. **Recovery / Retry / Cancellation Semantics:** Поведение при сбоях.
14. **Capability Dependencies:** Зависимости.
15. **Authority Boundaries:** Решения, принимаемые в контракте.
16. **Acceptance Criteria:** Условия завершенности (ID: AC-*).
17. **Observable Negative Scenarios:** Поведение при отказе (ID: NEG-*).
18. **Unresolved Product Decisions:** Нерешенные вопросы.
19. **Human Decision Block:** Требования к решению человека.

### Operational Pre-Freeze Checks
Каждый material check должен иметь запись `check_id`, `result`, `evidence`. PASS без evidence для material boundary check не использовать.
* `check_id: PROD-1`, `result: NOT_RUN` — no HOW leakage
* `check_id: PROD-2`, `result: NOT_RUN` — no representation leakage
* `check_id: PROD-3`, `result: NOT_RUN` — no repository facts

---

## 3. Engineering Design

```yaml
artifact_type: ENGINEERING_DESIGN
purpose: Define portable engineering choices and realization mechanisms for the Product Contract.
```

### Allowed Claim Classes
* portable engineering (must not require target repository knowledge, must have upstream justification, must not be a guessed mutable fact)
* schemas and data formats
* serialization
* persistence mechanisms
* execution mechanics
* implementation technologies

### Forbidden Claim Classes
* new Product behaviour
* new acceptance semantics
* guessed repository facts (exact target branch, existing topology)
* guessed target language/version/framework/test runner (without authority/target evidence)
* material dependency admission without Human Decision
* authority expansion

### Required Sections & Section Semantics
1. **Design Identity & Scope**
2. **Architecture Context & Contract Mapping**
3. **Design Non-Goals**
4. **Interfaces & Module Boundaries**
5. **Data / Serialization / Persistence Mechanics**
6. **Internal State Representation**
7. **Execution Mechanics**
8. **Authority Enforcement**
9. **Failure / Recovery / Cancellation Realization**
10. **Dependency Proposals & Materiality**
11. **Verification Mechanics**
12. **Observability & Evidence Generation**
13. **Alternatives / Trade-Offs**
14. **Unknowns & Conflicts**
15. **Product-to-Engineering Traceability Matrix**

**Invariant:** `Portable Engineering Choice ≠ Guessed Target Technology`

### Operational Pre-Freeze Checks
* `check_id: ENG-1`, `result: NOT_RUN` — no new Product behavior
* `check_id: ENG-2`, `result: NOT_RUN` — no guessed target technology
* `check_id: ENG-3`, `result: NOT_RUN` — all material HOW traceable upstream

---

## 4. Portable Task

```yaml
artifact_type: PORTABLE_TASK
purpose: Provide abstract implementation instructions ready for binding.
```

### Allowed Claim Classes
* implementation obligations
* engineering traceability

### Forbidden Claim Classes
* target paths
* branch / HEAD
* repository topology
* concrete shell/Git commands
* exact validation commands
* actual toolchain assumptions
* new Product/Engineering decisions
* execution authorization
* Git authorization

### Required Sections & Section Semantics
1. **Task Identity**
2. **Upstream Artifact Identities**
3. **Objective & User Outcome**
4. **Allowed Scope**
5. **Forbidden Scope & Non-Goals**
6. **Portable Inputs**
7. **Implementation Obligations**
8. **Expected Implementation Outcomes**
9. **Acceptance Criteria Mapping**
10. **Negative Scenario Mapping**
11. **Dependencies / Capabilities**
12. **Assumptions & Unknowns**
13. **Portable Validation Obligations**
14. **Stop Conditions**
15. **Completion Boundary**
16. **Authority State**

### Operational Pre-Freeze Checks
* `check_id: TASK-1`, `result: NOT_RUN` — no repository binding
* `check_id: TASK-2`, `result: NOT_RUN` — no concrete execution commands
* `check_id: TASK-3`, `result: NOT_RUN` — no new Engineering decisions

---

## 5. Validation Plan

```yaml
artifact_type: VALIDATION_PLAN
purpose: Define verification semantics to ensure Product Contract invariants are met.
```

### Allowed Claim Classes
* validation semantics
* observable outcomes
* coverage matrices

### Forbidden Claim Classes
* repository test commands
* concrete runner
* target paths
* shell invocation
* toolchain-specific commands

### Required Sections & Section Semantics
1. **Validation Identity & Subject**
2. **Verification Semantics**
3. **Acceptance Coverage Matrix**
4. **Negative Scenario Coverage Matrix**
5. **Positive Validation**
6. **Negative & Failure Validation**
7. **Result Aggregation**
8. **Evidence Requirements**
9. **No-Self-Heal / Mutation Boundary** (where applicable)
10. **Limitations / UNKNOWN / NOT_RUN**
11. **Deviations**
12. **Authority State**

**Result Semantics:** `PASS | FAIL | BLOCKED | UNKNOWN | NOT_RUN`
**Invariant:** `UNKNOWN ≠ PASS`, `NOT_RUN ≠ PASS`
Каждый AC-* и NEG-* должен иметь validation coverage и Evidence Requirement.

### Operational Pre-Freeze Checks
* `check_id: VAL-1`, `result: NOT_RUN` — semantic oracle only
* `check_id: VAL-2`, `result: NOT_RUN` — no target validation mechanics

---

## 6. Implementation Package

```yaml
artifact_type: IMPLEMENTATION_PACKAGE
purpose: Group portable artifacts and determine readiness for Phase B.
```

### Allowed Claim Classes
* composition
* traceability
* readiness
* package authority

### Forbidden Claim Classes
* target binding (Repository Binding)
* repository facts
* execution authorization
* Git authorization
* automatic Human Acceptance
* automatic Phase B activation
* authority elevation внутренних компонентов

### Required Sections & Section Semantics
1. **Package Identity & Slice Subject**
2. **Exact Composition Manifest** (exact revisions/digests)
3. **Product Boundary Traceability**
4. **Engineering Decisions Traceability**
5. **Portable Task Coverage**
6. **Validation Coverage Matrix**
7. **Evidence Requirements**
8. **End-to-End Traceability**
9. **Handoff Readiness Report**
10. **Conflict / Unknown / Materiality Review**
11. **Authority & Human Acceptance State**
12. **Package Invalidation Rules**
13. **Next Route Proposal**

**Package Acceptance:** Относится только к exact composition.
Material изменение компонента: `→ new Package revision → new validation → new Human Decision`
**Invariant:** `Phase A Human Acceptance ≠ Phase B activation`

### Operational Pre-Freeze Checks
* `check_id: PKG-1`, `result: NOT_RUN` — no authority elevation
* `check_id: PKG-2`, `result: NOT_RUN` — no execution authorization
* `check_id: PKG-3`, `result: NOT_RUN` — no target binding

---

## 7. Required Regression Inventory (Cross-Artifact)

Каждый material check должен иметь формат:
```yaml
check_id: <ID>
result: PASS | FAIL | BLOCKED | UNKNOWN | NOT_RUN
evidence: ""
affected_section: ""
finding_id: ""
```

* `REG-ABS-001` Product Contract: no HOW/representation/repository leakage
* `REG-ABS-002` Engineering Design: no new Product behavior
* `REG-TGT-001` Engineering Design: no guessed target technology
* `REG-TGT-002` Portable Task: no target paths/commands/toolchain
* `REG-VAL-001` Validation Plan: no target validation mechanics
* `REG-AUTH-001` Package components are not Human Accepted automatically
* `REG-AUTH-002` Package has no execution/Git authorization
* `REG-MAT-001` UNKNOWN is not escalated to material without evidence
* `REG-PHASE-001` Phase A completion does not activate Phase B
* `REG-TRACE-001` Every downstream material claim has upstream source
* `REG-COMP-001` Every AC/NEG has validation + evidence coverage
