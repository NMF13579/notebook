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
document_role: PRODUCT_BASELINE
proposed_post_acceptance_role: CANONICAL_PRODUCT_BASELINE
proposed_authority_scope:
  - target_users
  - user_problems
  - product_boundaries
  - accepted_product_directions
  - product_non_goals
source_files_bound_by_blob_sha: true
---

# 01 — Продукт

## 1. Граница статуса

Документ является APPROVED product baseline. Подтверждённая цель и product-first direction отделены от proposed MVP, metrics, interface и feature selection. Ни один раздел не разрешает implementation.

## 2. Проблема продукта

Непрограммист может описать желаемый результат, но не способен надёжно контролировать каждую repository operation, permission, test и implementation detail. AI-агенты могут потерять product intent, расширить scope, завысить completion или создать maintenance debt.

| ID | Проблема | Последствие |
|---|---|---|
| `P-001` | State распределён между chats, worktrees, reports и decisions | Потеря context и повторный planning |
| `P-002` | Неясно, где остановились | Unsafe assumptions on resume |
| `P-003` | Free-form request превращается в implementation assumptions | Wrong feature/problem fit |
| `P-004` | Scope расширяется скрыто | Contamination и difficult rollback |
| `P-005` | PASS/Evidence/readiness смешиваются с approval | False completion |
| `P-006` | Implementation и validation смешиваются | Self-validation и hidden fixes |
| `P-007` | Git operations считаются одним действием | Unauthorized publication |
| `P-008` | Legacy содержит ценность и obsolete complexity | Wrong target architecture |
| `P-009` | Exhaustive extraction имеет low ROI | Product work delayed |
| `P-010` | Documentation дублирует fact owners | Drift и unclear SoT |
| `P-011` | Feature descriptions shallow | Agent invents behavior/tests |
| `P-012` | Install/update ownership unclear | User data loss |
| `P-013` | Model/agent routing lacks measurements | Cost/quality unpredictability |
| `P-014` | Automation precedes manual flow | Bad process automated |
| `P-015` | Blockers/next action не понятны | Dependence on specialists |

## 3. Product promise

```text
пользователь формулирует проблему или идею
→ AOS делает понимание и uncertainty видимыми
→ создаёт bounded, reviewable development cycle
→ показывает Evidence и remaining risk
→ человек принимает решение
→ работа безопасно возобновляется
```

## 4. Пользователи и JTBD

### Непрограммист / domain expert

- объяснить problem обычным языком;
- увидеть understood/missing/assumed;
- утвердить product intent и high-risk actions;
- оценить user-visible result без чтения всего кода;
- resume after interruption.

### Vibe-coder / product builder

- получить safe default workflow;
- предотвращать scope drift и false completion;
- менять coding agents без переписывания rules;
- сохранять maintainable project knowledge.

### Agent / implementer / reviewer

- получить bounded context и one task;
- знать allowed/forbidden changes;
- связать acceptance criteria с Evidence;
- сообщить uncertainty/remaining risk;
- оставить recoverable handoff.

### Maintainer / operator

- inspect current state/drift;
- понимать ownership/rationale;
- reproduce checks;
- отличать historical report от current result.

## 5. Adaptive intake

### Existing complete specification

AOS сохраняет original input, проверяет missing fields и contradictions, показывает added assumptions, задаёт только material questions, создаёт APPROVED Product Spec/Feature Passport и останавливается до architecture/execution authority.

### Incomplete idea

Problem Interview определяет user/pain/current workaround, отделяет outcome от solution, фиксирует success signals, constraints, non-goals, unknowns, follow-up questions и sensitive/provider concerns.

### Progressive depth

| Profile | Minimum depth |
|---|---|
| Small reversible | Goal, scope, observable result, focused check |
| Medium feature | Users, flow, acceptance, dependencies, regression |
| High/protected | Full constraints, rollback, authority checkpoints |
| Sensitive/regulated | Data/provider boundary, specialist review |

Точные thresholds остаются `UNDECIDED`.

## 6. Product artifacts

### Intent Record

Original request, actor, problem, desired outcome, constraints, non-goals, assumptions, unknowns, source и sensitive flags.

### Product Spec

Problem, users/JTBD, goals/non-goals, journeys, product boundaries, constraints, risks, metrics, dependencies, acceptance и open decisions. Product Spec не разрешает execution.

### Feature Passport

Identity/owner, problem/user, observable behavior, trigger/preconditions, inputs/outputs, flow/states, failures/recovery, dependencies, constraints, authority boundaries, acceptance/negative scenarios, maturity, evidence status и human disposition.

### Product Feature Registry — architecture candidate

Registry индексирует Feature Passports, но не заменяет их и не смешивается с execution/verification/protected registries.

## 7. Scenario, access and UX pipeline — optional

```text
Problem Interview
→ Problem Map
→ Scenario Interview
→ approved scenarios
→ access model
→ UX object inventory
→ grouping
→ screen map
→ human review
```

Запускается только когда Product Spec недостаточно описывает actors, access-sensitive behavior и UX flow.

## 8. Product boundaries

### Product Runtime

Intent/Problem Intake, Discovery, Product Spec/Feature Passport, Status/Next/Details, Review Package, Project Memory/Handoff, First-Start/Tutor и optional Architecture Support/Guided Bootstrap.

### Development Factory

Task Brief compiler, preflight/preview, execution adapters, validators/test harness, Context Packs, backlog/decomposition, CI/release helpers, strict loaders/drift checks.

### Governance

Minimal Safety Floor всегда; stronger controls только после observed need. Governance не является product value сама по себе.

### Knowledge / Reference

Accepted documents, APPROVED Feature Passports, lessons/patterns, targeted findings и rebuildable indexes.

## 9. Core user journeys

### J-001 — Start a project

```text
intent → clarification → problem/outcome → Product Spec → slice choice
→ architecture decision if needed → Task Brief → authorization
→ implementation → validation → review → human decision
```

### J-002 — Understand existing project

```text
repository → read-only identity/preflight → capability map
→ gaps/conflicts/unknowns → candidate objectives → human selection
```

### J-003 — Implement one feature

```text
Feature Passport → targeted research → Product Contract → architecture
→ Task Brief → EXECUTE → Stage Report → VALIDATE → REVIEW → decision
```

### J-004 — Resume

```text
/status → repository-derived state → exact identity → blockers/decisions
→ /next → optional /details
```

### J-005 — Review

```text
before/after → scope → Evidence → NOT_RUN/limitations → findings
→ ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

### J-006 — Protected delivery

```text
protected scope → plan → human Risk Profile → authorized EXECUTE
→ independent VALIDATE → REVIEW → separate Commit/Push/Merge/Release
```

### J-007 — Reference-driven reconstruction

```text
feature gap → narrow question → pinned snapshot → inspect evidence
→ classify → reject legacy complexity → update dossier → human decision
```

## 10. Candidate MVP — PROPOSAL

Safe entry/discovery, adaptive intake, Product Spec/Feature Passport, one Task Brief, separate Execution Authorization, scope/risk/human authority, one change, Evidence mapped to acceptance, human acceptance, compact handoff и lesson proposal.

## 11. First vertical slice criteria

Slice решает identified user problem, даёт observable result, имеет described I/O/states/failures/recovery, executable acceptance/negative cases, работает без full Control Plane, имеет minimal dependencies, создаёт learning и не включает implicit Git delivery.

## 12. Product acceptance model

Feature documentation-ready, когда определены users, trigger, I/O, observable result, states, failures/recovery, non-goals, acceptance, negative cases, human decisions и research gaps.

Product acceptance требует explicit human decision по exact revision.

## 13. Candidate success indicators — PROPOSAL

Time intent→Task Brief, clarification loops, scope drift, resume time, review time, false-green incidents, tasks without re-planning, lesson reuse, user understanding, Governance overhead и maintainability.

## 14. Required product decisions

First segment/job/slice, Product Spec↔Feature Passport, Feature Registry, scenario/access/UX timing, interface, acceptance identity, install ownership, feature dispositions и metrics.
