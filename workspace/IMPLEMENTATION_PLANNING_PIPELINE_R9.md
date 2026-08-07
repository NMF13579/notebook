# AOS — Implementation Planning Pipeline

```yaml
document_id: AOS-IMPLEMENTATION-PLANNING-PIPELINE
revision: R9
status: DRAFT
purpose: REPEATABLE_IMPLEMENTATION_DOCUMENTATION_PIPELINE
revision_reason: IDENTITY_AND_AUTHORITY_TERMINOLOGY_CORRECTION
freeze_identity: EXTERNAL_FREEZE_MANIFEST
implementation_authorization: NONE
git_authorization: NONE
automation_state: NOT_IMPLEMENTED
```

## Purpose

Этот документ определяет повторяемый процесс подготовки документационного пакета для Coding Agent.

Он отвечает на вопрос:

> Как из принятой архитектуры AOS получить проверенный, target-bound implementation package без скрытых Product, Architecture или material Engineering decisions внутри Coding Agent.

Документ не является automation platform, runtime orchestration system или permission на implementation.

```text
Planning Pipeline ≠ Automation Platform
Task Brief ≠ Execution Authorization
PASS ≠ Human Acceptance
READY ≠ Permission
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

---

## Scope

В scope:

- выбор exact vertical slice человеком;
- Phase A: Portable Implementation Package;
- Phase B: Repository Binding;
- read-only validations;
- bounded correction cycles;
- traceability;
- final handoff readiness review;
- human acceptance gates.

Вне scope:

- runtime code;
- repository mutation;
- Git actions;
- autonomous implementation;
- automatic Product/Architecture decisions;
- automatic dependency admission;
- automatic repository selection;
- release/deploy.

---

## Authority Model

Для всех generated artifacts применяется иерархия:

1. Current explicit human decision.
2. Human-accepted project artifact — только в его fact class.
3. Direct current repository observation — для mutable repository facts.
4. DRAFT/PROPOSAL.
5. Reference material.
6. Model inference.

Каждый material claim должен быть классифицирован как один из:

- `HUMAN_ACCEPTED_FACT`
- `HUMAN_CONFIRMED_DIRECTION`
- `OBSERVED_AT_SNAPSHOT`
- `PROPOSAL`
- `CONFLICT`
- `UNKNOWN`
- `NOT_FOUND`
- `NOT_RUN`
- `BLOCKED`

Agent не повышает authority автоматически.

---

## High-Level Flow

Pipeline разделен на две независимые фазы.

### Phase A: Portable Implementation Package

```text
Frozen Architecture + Accepted Roadmap
        ↓
HUMAN selects exact Slice
        ↓
Feature / Slice Product Contract (DRAFT)
        ↓
Engineering Design (DRAFT)
        ↓
Portable Task (DRAFT)
        ↓
Validation Plan & Evidence Requirements
        ↓
Traceability
        ↓
Handoff Readiness Report
        ↓
HUMAN ACCEPT exact Implementation Package
```

### Phase B: Repository Binding

```text
HUMAN selects implementation repository
        ↓
Fresh read-only repository preflight
        ↓
Target Repository Binding
        ↓
Target-Bound Task Brief
        ↓
Handoff Review
        ↓
HUMAN ACCEPT exact Task Brief
        ↓
Separate Execution Authorization
        ↓
Coding Agent
```

---

## Implementation Package

Pipeline производит **ровно один Implementation Package** для одного bounded Slice. 

Документы (Product Contract, Engineering Design, Portable Task и т.д.) являются внутренней структурой Package, а не самостоятельной целью Pipeline.

---

# PHASE A: PORTABLE IMPLEMENTATION PACKAGE

Все документы в Phase A должны быть полностью готовы.

## Candidate-pair binding

```yaml
artifact_profile_dependency:
  document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
  required_revision: R4
  identity_source:
    manifest_path: workspace/IMPLEMENTATION_PROFILE_PIPELINE_FREEZE_MANIFEST_R2.md
  activation_requirement:
    acceptance_record:
      required: true
      manifest_id: AOS-IMPLEMENTATION-PROFILE-PIPELINE-FREEZE
      manifest_revision: R2
      decision: ACCEPT

candidate_pair_state: PROPOSAL
candidate_pair_activation: NOT_RUN
```

До Human Acceptance exact pair:

```text
Pipeline candidate references Profile candidate.
DRAFT Profile is not an active normative dependency.
```

После Human Acceptance exact pair:

```text
Pipeline uses accepted Profile R4
for Phase A artifact authoring and validation.
```

## Ownership invariant

```text
Pipeline defines FLOW.
Artifact Profile defines ARTIFACT SEMANTICS.

Pipeline must not redefine Profile semantics.
Profile must not define Pipeline flow, stages, gates or permissions.
```

Pipeline owns:
- stage sequence;
- Phase A / Phase B;
- stage entry/exit;
- Human Gates;
- Package lifecycle;
- Repository Binding;
- readiness routing;
- Execution Authorization boundary;
- Git permission boundary.

Profile owns only:
- artifact-type purpose;
- allowed/forbidden claim classes;
- required sections;
- section semantics;
- pre-freeze artifact checks.

### Boundary (Portable Engineering Choices vs Repository-Specific Mechanics)

**Portable Engineering Choices (Phase A)**
Phase A может определять (если это обосновано в exact frozen/validated Engineering Design with role PACKAGE_INTERNAL_UPSTREAM_SOURCE):
* implementation pattern;
* serialization choice;
* interface style;
* CLI как interface choice;
* LLM integration;
* persistence model;
* validation approach;
* concrete technology choice;
* other engineering decisions.
*Эти решения допустимы, если они не требуют знания конкретного target repository.*

**Repository-Specific Mechanics (Phase B)**
Phase A не может определять repository-specific facts:
* repository path;
* branch;
* HEAD;
* exact target files/modules;
* observed repository topology;
* installed dependency versions;
* actual toolchain discovered in repository;
* exact executable repository commands;
* concrete rollback commands;
* repository-local constraints.

**Зафиксированный invariant:**
`Portable Engineering Choices ≠ Repository-Specific Mechanics`

**Repository Independence** означает: Implementation Package может быть оценён и принят без знания конкретного target repository snapshot. Engineering decisions допустимы, если они не являются guessed repository facts и technical choice must be traceable to either:

1. an authoritative external input
   within its fact-class authority;

or

2. an exact PACKAGE_INTERNAL_UPSTREAM_SOURCE
   with authority_inheritance: NONE.

## Stage 0 — Slice Selection

Человек выбирает один exact vertical slice. Agent не выбирает feature/slice самостоятельно.

## Stage 1 — Feature / Slice Product Contract

```yaml
authoring_contract:
  profile_document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
  profile_revision: R4
  artifact_type: PRODUCT_CONTRACT
```

Pipeline may state **which artifact** is required and **when**, but must not restate:
- allowed claims;
- forbidden claims;
- required sections;
- section semantics;
- Profile pre-freeze checks.

**Зафиксированный invariant:**
`Product Contract WHAT ≠ Engineering / Execution Mechanics`

## Stage 2 — Engineering Design

```yaml
authoring_contract:
  profile_document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
  profile_revision: R4
  artifact_type: ENGINEERING_DESIGN
```
В рамках Phase A он не может привязываться к целевому репозиторию (используются абстрактные топологии или отложенные решения).

## Stage 3 — Portable Task Candidate

```yaml
authoring_contract:
  profile_document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
  profile_revision: R4
  artifact_type: PORTABLE_TASK
```

## Stage 4 — Validation Plan, Evidence, Traceability, Handoff Readiness Report

В пакет добавляются Validation Plan, Evidence Requirements, Traceability, Handoff Readiness Report.

```yaml
authoring_contract:
  profile_document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
  profile_revision: R4
  artifact_type: VALIDATION_PLAN
```

```yaml
authoring_contract:
  profile_document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
  profile_revision: R4
  artifact_type: IMPLEMENTATION_PACKAGE
```

**Зафиксированный invariant:**
`Portable Validation Semantics ≠ Target Validation Mechanics`

## Package Authority & Acceptance Semantics

```text
Package components are PACKAGE_INTERNAL_UPSTREAM_SOURCE
until Human Acceptance of exact Package composition.

authority inheritance between components: NONE

Validated/Frozen Package Component
≠
Individually Human-Accepted Artifact

Dependency ≠ Authority Inheritance
```

Do not use `accepted upstream source` unless an exact separate Human Decision exists.

**Package Acceptance Semantics:**
Human Acceptance Package относится к exact composition/revisions, перечисленным в Package manifest.
Изменение любого material component после Package Acceptance:
* создаёт новую Package revision;
* делает предыдущий Package acceptance неприменимым к изменённому composition;
* требует повторного package-level review и Human Decision.

## Profile validation route

Before a Phase A artifact can be frozen:

```text
authoring against exact accepted Profile
→ Profile pre-freeze checks
→ artifact freeze
→ separate read-only artifact validation
```

Before Package Human Review:

```text
all component identities frozen
→ cross-artifact regression inventory
→ package-level validation
→ READY_FOR_IMPLEMENTATION_PACKAGE_REVIEW
→ STOP
```

Validation never edits the subject.

## Phase A Exit: Human Gate

```text
Phase A Human Acceptance
≠
Phase B activation
```

Phase B begins only после a separate explicit Human Decision selecting/activating Repository Binding.

---

# PHASE B: REPOSITORY BINDING

Только после Human Acceptance Implementation Package начинается эта отдельная фаза. 
Она только дополняет Package repository-specific информацией, не изменяя Product Contract и Engineering Design.

## Stage 5 — Repository Selection

Implementation repository выбирает человек.

## Stage 6 — Fresh Read-Only Repository Preflight

Агент читает repository state (topology, branch, toolchain, existing tests, etc.). Stored reports не заменяют fresh observation.

## Stage 7 — Target Repository Binding

Portable task компилируется в target-specific task (связывание абстракций с реальными путями и командами).

## Stage 8 — Target-Bound Task Brief

Создать exact task для Coding Agent с учетом реального репозитория.

После Repository Binding появляется новый статус:
`READY_FOR_CODING_REVIEW`

## Stage 9 — Handoff Review

Проверяется отсутствие Decision Leakage и соответствие репозиторию. Repository Binding не должен неявно менять Product Contract или Engineering Design.

Repository Independence `PASS` разрешён только если:
* all technical choices are traceable to:
  - an accepted exact Implementation Package composition;
  - its frozen package-internal sources;
  - or an authoritative external input within its fact class;
* отсутствуют guessed repository facts;
* отсутствуют target paths/commands/snapshot assumptions;
* Phase B может выполнить binding без изменения Product Contract;
* Phase B не обязана заново проектировать material Engineering HOW.

## Phase B Exit: Human Gate

Человек принимает exact Task Brief revision. Допустимые решения: `ACCEPT`, `NEEDS_CHANGES`, `REJECT`, `DEFER`.

---

# Risk + Execution Authorization

Выдаётся отдельная Execution Authorization, привязанная к exact Task Brief revision.
Git permissions остаются отдельными.

---

# Agent Autonomy Model

Цель UX: Agent готовит фазу, останавливается на Human Checkpoint.

## Human checkpoint 1
Select Slice.

## Human checkpoint 2
Accept exact Implementation Package целиком (Phase A).

## Human checkpoint 3
Select implementation repository.

## Human checkpoint 4
Accept exact Target-Bound Task Brief (Phase B).

## Human checkpoint 5
Authorize execution / Git actions separately.

---

# Conflict / Unknown Handling

Нельзя угадывать. Для material gap агент фиксирует `UNKNOWN` / `CONFLICT` и блокирует зависимый action.

---

# Exact-pair activation rule

The R9 candidate may become active only after
Human Acceptance of the exact Freeze Manifest R2 identity.

```yaml
accepted_pair:
  pipeline:
    document_id: AOS-IMPLEMENTATION-PLANNING-PIPELINE
    revision: R9
    identity_source:
      manifest_path: workspace/IMPLEMENTATION_PROFILE_PIPELINE_FREEZE_MANIFEST_R2.md
  profile:
    document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
    revision: R4
    identity_source:
      manifest_path: workspace/IMPLEMENTATION_PROFILE_PIPELINE_FREEZE_MANIFEST_R2.md
```

Acceptance of only one candidate does not activate the pair.

Any material change to either candidate requires:
- new revision;
- new integration review;
- new Human Decision.

Frozen Profile/Pipeline subjects remain immutable.
Human Acceptance is stored in a separate Acceptance Record
bound to the exact Freeze Manifest revision and SHA-256.

# Required integration reviews

Before Human Review exact pair, run read-only:

1. Identity Review
2. Ownership / No-Duplication Review
3. Profile Coverage Review
4. Pipeline Stage Reference Review
5. Package-Internal Authority Review
6. Validation / No-Mutation Review
7. Phase Activation Review
8. Backward Compatibility Review
9. Slice 4 Dogfood Readiness Review

# Backward compatibility

```yaml
slice_1_3:
  mandatory_migration: []
  optional_migration: []
  no_change_required:
    - accepted exact package revisions remain valid in their fact classes

slice_4:
  state: NOT_RUN
  activation_condition:
    - exact Pipeline R9 accepted
    - exact Profile R4 accepted
```

# Candidate result

```yaml
technical_result: NOT_RUN
readiness:
  target: HUMAN_PROFILE_PIPELINE_REVIEW
  state: NOT_READY
human_acceptance:
  state: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```
