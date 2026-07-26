---
document_id: 00_Core
title: "Core"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Core

## Purpose

Core fixes project identity, product purpose, authority, non-negotiable invariants, boundaries, status semantics and criteria for adopting future mechanisms. It does not contain detailed feature specifications or implementation plans.

## Project identity

- Historical implementation: `AgentOS`, repository `NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)`.
- Historical role: technical and failure-reference only.
- Authority over the next system: `NONE` until a human explicitly adopts a mechanism.
- Target working names: `AOS`, `AgentOS`, “next-generation AOS”.
- Final target name, implementation repository, architecture and MVP: `UNKNOWN` or `CONFLICT`.

Sources: `CH-01`, `CH-09`, `CH-11`, `RP-00`.

## Human-decided purpose

The target system should help a nonprogrammer, domain expert or product owner direct AI-assisted software development without managing every implementation detail. It must make intent, scope, risk, evidence, uncertainty, current state and human decisions visible while reducing operational burden.

The project succeeds only when this works on real tasks. Governance artifacts, validator counts and green reports are not the product goal.

Status: `DECIDED`. Sources: `CH-01`, `CH-03`, `CH-11`, `NT-01`, `NT-03`.

## Primary users

| User | Core need | Status |
|---|---|---|
| Nontechnical product owner / domain expert | Turn intent into controlled and understandable development | `DECIDED` |
| Vibe-coder | Use coding agents without losing scope, state or authority boundaries | `DECIDED` |
| AI coding agent | Receive minimal context, explicit contracts, limits and proof requirements | `DECIDED` |
| Developer/reviewer | Understand implementation, evidence, remaining risk and handoff | `REPORTED` |
| Operator/maintainer | Diagnose drift, repeated failures and repository health | `REPORTED` |

## Status model

- `DECIDED` — explicit human decision or direction.
- `OBSERVED` — found in the pinned repository snapshot.
- `REPORTED` — described in a note, report or assistant output but not independently adopted/proven.
- `CONFLICT` — sources or decisions disagree.
- `NOT_FOUND` — named mechanism/path was not found in the inspected area.
- `UNKNOWN` — evidence is insufficient.
- `NOT_RUN` — command/test/build was not executed in this audit.

`DECIDED ≠ OBSERVED`. `NOT_RUN ≠ PASS`. `PASS ≠ approval`.

## Non-negotiable invariants

1. Human final authority.
2. Validation, evidence, CI and readiness cannot simulate approval.
3. `UNKNOWN`, `NOT_RUN`, `BLOCKED` and warnings remain visible.
4. Analysis, plan, execution, commit, push, merge and release are separate permissions/states.
5. Scope expansion requires an explicit decision.
6. One active task and the smallest bounded change where practical.
7. High-risk uncertainty fails closed.
8. Read-only checks do not silently write.
9. Derived indexes/cache/retrieval are navigation, not source of truth.
10. Legacy repositories and self-labelled canonical notes do not govern the target.
11. Product Runtime and a Minimal Safety Floor precede enhanced Governance/runtime enforcement.
12. Real-task dogfood precedes scaling automation.

Sources: `CH-01`, `CH-03`, `CH-04`, `CH-09`, `RP-02`–`RP-06`.

## Current strategic direction

- Use compact, feature-oriented reconstruction instead of exhaustive legacy extraction.
- Keep purpose, schemes, significant features/components, errors, lessons, gaps and references.
- Consult historical/external references on demand for a concrete feature.
- Use a modular monorepo first; split only after a real team/release/compliance boundary appears.
- Keep enhanced Governance optional/deferred while retaining the invariant safety floor.
- Do not import milestone numbering, duplicate authority, stale reports/maps or heavy runtime chains wholesale.

Status: `DECIDED` at principle level; target topology and first slice remain unapproved.

## Product boundary

### In design scope

- problem and idea elicitation;
- Product Spec / Feature Passport;
- bounded Task Brief and Task Contract;
- scope, risk and human authority;
- evidence-based verification and acceptance;
- state, handoff, recovery and learning;
- minimal context selection;
- portability across common coding agents;
- source-on-demand reference use.

### Not automatically in scope

- autonomous coding without checkpoints;
- mandatory multi-agent orchestration;
- full RAG/vector backend;
- autonomous policy/self-heal decisions;
- SaaS/cloud/dashboard/marketplace;
- automatic commit, push, merge, deploy or release;
- wholesale import of historical governance.

## Feature admission questions

Before accepting a new mechanism, answer:

1. Which observed user problem does it solve?
2. Is the problem present in the target system?
3. Can a simpler process solve it?
4. Does it preserve human authority and readable contracts?
5. What metric shows improvement?
6. What is the smallest experiment?
7. What are failure and rollback conditions?
8. What context, maintenance and operational cost does it add?

The exact scoring policy is still `UNKNOWN`; this is a review checklist, not an automatic gate.

## Core unresolved decisions

- final product name;
- target implementation repository;
- first commercial/user segment;
- first vNext vertical slice;
- exact Minimal/Strict governance contract;
- human acceptance identity/record;
- target metadata policy.

## Navigation

- Product: [01_Product.md](01_Product.md)
- Architecture: [02_Architecture.md](02_Architecture.md)
- Development: [03_Development.md](03_Development.md)
- Lessons and conflicts: [04_Lessons.md](04_Lessons.md)
- Sources and repository snapshot: [05_Reference.md](05_Reference.md)
- Detailed feature registry: [06_Features.md](06_Features.md)

**PARTIAL EXTRACTION READY FOR REVIEW**

**HUMAN REVIEW REQUIRED**
