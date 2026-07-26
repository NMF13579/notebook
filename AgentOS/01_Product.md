---
document_id: 01_Product
title: "Product"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Product

## Product problem

Nontechnical owners can describe a desired outcome but cannot reliably supervise every repository operation, permission, test and implementation detail. AI agents can produce code quickly while losing product intent, expanding scope, overstating completion or creating maintenance debt.

Status: `DECIDED`. Sources: `CH-01`, `CH-03`, `CH-11`, `NT-01`.

## Product promise

Turn a human idea into a bounded, understandable and evidence-backed development cycle while preserving explicit human decisions and minimizing unnecessary governance work.

## Primary product flow

```text
Idea / pain / ready specification
  → choose intake depth
  → Problem Interview or clarification when needed
  → Product Spec / Feature Passport
  → contextual conflict and dependency review
  → non-executable Task Brief
  → executable Task Contract after a human checkpoint
  → one bounded implementation change
  → evidence-based verification
  → human ACCEPT / NEEDS_CHANGES / REJECT
  → handoff and lesson proposal
```

Status: high-level direction `DECIDED`; exact target artifacts and first implemented slice `UNKNOWN`.

## Users and jobs-to-be-done

### Nontechnical owner / domain expert

- explain the real problem in ordinary language;
- see what is understood, missing and assumed;
- approve product intent and high-risk actions;
- evaluate the user-visible result without reading all code;
- continue work after a session break.

### Vibe-coder / product builder

- receive a safe default workflow;
- prevent scope drift and false completion;
- use different coding agents without rewriting all rules;
- maintain code and project knowledge after AI changes.

### Agent / implementer / reviewer

- receive bounded context and one active task;
- know allowed and forbidden changes;
- map acceptance criteria to evidence;
- report uncertainty and remaining risk;
- hand off a recoverable state.

## Intake and Product Spec

The desired intake is adaptive:

- a complete existing specification is checked rather than re-interviewed;
- an incomplete idea enters a Problem Interview;
- missing material information becomes explicit questions;
- high-risk domains require greater specification depth;
- the Product Spec contains problem, users, JTBD, goals, non-goals, constraints, risks, metrics, acceptance criteria, dependencies and open questions;
- Product Spec approval does not authorize execution.

Historical repository support is `OBSERVED`; target schema and interaction design require new human approval.

## Feature knowledge layer

The desired product knowledge model is:

```text
Feature Passport
  → Product Feature Registry
  → dependencies / maturity / implementation evidence
  → accepted roadmap selection
```

A Feature Passport should record problem, target user, observable behavior, scope, dependencies, constraints, acceptance, implementation links, tests, limitations, maturity and human decision. A product Feature Registry was not found in the inspected repository; its execution-verification registry is a different mechanism.

Status: direction `DECIDED`; target implementation `NOT_FOUND`.

## Task and acceptance boundary

- Spec Wizard creates a Task Brief, not an executable task.
- Only an explicit active Task Contract may authorize bounded execution.
- Generated candidates and queue items do not become active automatically.
- Verification signals do not accept the product result.
- Human acceptance should record `ACCEPT`, `NEEDS_CHANGES` or `REJECT`, the reviewed subject, actor/date and evidence references.

The final vNext acceptance-record format remains `UNKNOWN`.

## UX and control surface

Historically desired product surfaces include:

- guided workflow and status dashboard;
- risk/evidence/human-decision cards;
- chat as a reasoning and clarification layer;
- Product Spec and task views;
- HTML/application preview;
- later SaaS/auth/project collaboration.

They are not current implementation commitments. The inspected legacy README explicitly excludes backend/web UI/cloud/marketplace from that stage. Current disposition: `DEFERRED` until the core product cycle is proven.

## Product MVP decision boundary

A candidate minimum is:

1. safe project entry/discovery;
2. adaptive problem/spec intake;
3. Product Spec or Feature Passport;
4. one bounded Task Brief and active Task Contract;
5. scope/risk/human authorization;
6. one implementation change;
7. verification mapped to acceptance;
8. human acceptance;
9. handoff and lesson proposal.

This is a synthesis candidate. The final MVP subset and implementation repository are `UNKNOWN`.

## User-facing success indicators

- owner can explain what changes and what does not;
- missing data becomes a visible question, not an invented requirement;
- high-risk action stops before execution;
- every acceptance criterion has evidence or an explicit `NOT_RUN/UNKNOWN`;
- “done” requires human acceptance;
- another session can continue from a compact state;
- repeated failures produce specific lessons;
- governance overhead does not exceed product value.

Numeric baselines and thresholds still require human definition.

## Product feature map

| ID | Feature / component | Decision | Repository | Current note |
|---|---|---|---|---|
| `F-01` | Project Discovery / `/init` | UNKNOWN | OBSERVED — `INIT.md` and discovery capability claims exist. | No target-system acceptance; current discovery implementation was not executed. |
| `F-02` | Problem Interview | UNKNOWN | OBSERVED — architecture, templates, schema-related artifacts, fixtures, and checker are present. | Historical implementation is detailed; target interaction depth and UX are unselected. |
| `F-03` | Interview Completeness and Missing-Information Detection | DECIDED — uncertainty must remain explicit. | OBSERVED — deterministic checker exists. | No independent execution in this audit. |
| `F-04` | Product Spec | DECIDED — product-first direction. | OBSERVED — comprehensive architecture document exists. | Target schema and minimal sections still require human selection. |
| `F-05` | Progressive Specification Depth | DECIDED — avoid overdocumentation and support a simple path. | OBSERVED in Product Spec architecture. | Exact thresholds and fast-path contract are not selected for the target. |
| `F-06` | Contextual Feature/Spec Conflict Review | UNKNOWN | REPORTED/partial — policy fragments exist; a single target checker was not established. | Semantic review implementation and authority contract remain undefined. |
| `F-07` | Research Intake | DECIDED for on-demand research; full intake mechanism UNKNOWN. | REPORTED in historical roadmap and documents. | No concise target contract chosen. |
| `F-08` | Scenario, Access, and UX Structure Pipeline | UNKNOWN | REPORTED in project sources; complete end-to-end implementation not established. | Standard vs high-stakes profiles and artifact boundaries need synthesis. |
| `F-09` | Neutral, Semantic, Replaceable UI Foundation | UNKNOWN | NOT_FOUND for the three named core policy artifacts at RP-00. | `UI-SEMANTIC-COMPONENT-CONTRACT.md`, `DESIGN-TOKENS-POLICY.md`, and `UI-REPLACEABILITY-POLICY.md` are explicitly missing. |
| `F-10` | Spec Wizard and Task Brief | DECIDED in principle. | OBSERVED in `INIT.md` and README capability claims. | Wizard behavior and target brief schema were not executed or selected. |
| `F-11` | Spec-to-Task Candidate Generator | UNKNOWN | OBSERVED — documentation and Python implementation exist. | One task only; no full decomposition, UX source, Context Pack selection, or real queue write. |
| `F-12` | Executable Task Contract / Active Task | DECIDED. | OBSERVED — schema, validator, and idle active-task file exist. | Validator idle bypass is too broad and can skip malformed documents. |
| `F-13` | Task Decomposition, Dependencies, and Queue | UNKNOWN | OBSERVED as extensive historical scaffolding; full multi-task generation is a known gap in the inspected generator. | Target need, minimal queue model, and actual materialization policy are unresolved. |
| `F-17` | State, Status, Next Action, and Recovery | DECIDED. | OBSERVED in state module and handoff. | Historical lifecycle is richer than necessary; current README/HANDOFF status is inconsistent. |
| `F-18` | Human Approval and Authorization Boundaries | DECIDED. | OBSERVED throughout canonical modules and false-PASS mechanisms. | A concise target decision-record format is not selected. |
| `F-23` | Session Handoff / “На чём остановились” | DECIDED. | OBSERVED in `HANDOFF.md` and state rules. | Must remain compact and freshness-bound. |
| `F-24` | Incident-to-Lesson Loop | DECIDED at principle level. | OBSERVED in workflow and lessons registry. | Workflow's instruction to commit separately conflicts with human-only commit authorization unless explicitly gated. |
| `F-33` | Installation, Template, and Simple Mode | DECIDED direction: low-friction entry. | OBSERVED in README and historical handoff. | Installer and template behavior were not run; target packaging is unselected. |
| `F-39` | Admin/Control UI, Human Decision Cards, Chat, and Preview | UNKNOWN | REPORTED historical roadmap; current README says AgentOS is not a web UI/dashboard. | Product interface and authority model are not chosen. |
| `F-40` | SaaS, Cloud, Auth, GitHub Platform, and Marketplace | UNKNOWN | REPORTED historical roadmap; current README lists backend/cloud/dashboard/marketplace as non-goals. | Direct conflict with current minimal target and no product validation. |
| `F-41` | Feature Catalog and Acceptance Filter | DECIDED that a feature catalog is required; exact filter is REPORTED. | NOT_FOUND as one concise target catalog. | Human owner must approve the final scoring/selection rule. |
| `F-42` | Minimal Product-First Vertical Slice | DECIDED. | Not a single isolated target slice; historical mechanisms exist separately. | Final MVP feature subset and target repository remain UNKNOWN. |

Full feature passports: [06_Features.md](06_Features.md).

## Product decisions still required

- final target name and first primary segment;
- first vertical slice;
- Product Spec versus Feature Passport relationship;
- exact Feature Registry contract;
- Problem/Scenario/RBAC/UX phase timing;
- acceptance record and human identity;
- when UI/chat/preview/SaaS re-enter the roadmap.

Sources and historical decisions: [05_Reference.md](05_Reference.md).

**HUMAN REVIEW REQUIRED**
