---
document_id: 02_Architecture
title: "Architecture"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Architecture

## Architectural position

The target architecture is not the historical AgentOS architecture. Historical code and documents are evidence/reference only. Target adoption requires an explicit human design decision.

Current direction:

- product-first;
- Markdown-readable contracts;
- Minimal Safety Floor;
- one authority owner per concern;
- task-scoped context;
- modular monorepo first;
- enhanced Governance and runtime enforcement optional/deferred;
- thin deterministic validation where it prevents observed failure;
- no derived artifact or UI creates authority.

Status: direction `DECIDED`; exact component topology `UNKNOWN`.

## Historical observed architecture

At `NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)`, AgentOS contains:

- one bootstrap (`llms.txt`);
- five canonical modules: Core Rules, State, Workflow, Quality, Security;
- active-task, verification and approval-related contracts;
- Product Interview/Product Spec and task-candidate layers;
- schemas, validators, fixtures, scripts and reports;
- context-index and repository-health mechanisms;
- lessons, retry and false-PASS mechanisms;
- templates and tool-specific prompt packs.

Status: `OBSERVED`. Commands/tests/build: `NOT_RUN`. Authority for target: `NONE`.

## Candidate target layers

This is a synthesis model, not an accepted implementation design:

1. **Core** — identity, source hierarchy, status semantics, human authority.
2. **Product** — Problem Interview, Product Spec, Feature Passport/Registry.
3. **Task** — Task Brief, active Task Contract, scope/risk.
4. **Execution** — one agent action inside bounded permissions.
5. **Verification** — actual changes and evidence mapped to acceptance.
6. **State** — status, blockers, next action, recovery and handoff.
7. **Learning** — incident and lesson proposal.
8. **Reference** — on-demand historical/external research.
9. **Optional modules** — context index, enhanced Governance, UI, orchestration, cloud.

## Authority model

```text
system/owner instruction
  > explicit human decision
  > accepted current contract
  > implementation evidence
  > supporting report/document
  > generated index/cache/retrieval
  > legacy/reference proposal
```

Architectural invariants:

- derived indexes are never source of truth;
- agent profiles/adapters do not expand permissions;
- UI displays decisions but does not create them;
- report/validator output cannot mutate lifecycle;
- no automatic cascade from validation to commit/push/merge/release;
- read-only tools do not silently write;
- target architecture should be smaller than the historical system unless measured evidence justifies complexity.

## Product Runtime and Governance

### Product Runtime

Owns user intent, Feature Passport/Product Spec, task creation, execution handoff, visible evidence and human acceptance.

### Minimal Safety Floor

Always-on invariants for scope, uncertainty, protected/destructive operations and human authority.

### Enhanced Governance

Optional stricter contracts, registries, protected artifact policies, isolated evaluator or organizational controls. It should be introduced only after a real need is demonstrated.

Exact package/API boundaries remain `UNKNOWN`.

## State and lifecycle

Historical state models separate project, session and task lifecycles. The target should preserve semantic distinctions but use a smaller state vocabulary unless richer states prove necessary.

Minimum target state shape:

```yaml
project_state:
session_state:
task_state:
active_task:
blockers:
next_allowed_actions:
last_verified_step:
human_confirmation_required:
```

## Context architecture

Desired route:

```text
minimal bootstrap
  → identify project/task/state
  → locate relevant authoritative files
  → use index/repo-map only for navigation
  → create explained task-local context
  → verify freshness and handoff
```

Observed problems:

- repository map is stale;
- context index contains one old entry;
- metadata coverage is incomplete;
- bootstrap/architecture documents contain absolute local links.

A Light RAG/SQLite layer was historically proposed as derived-only state, later deferred. It must not re-enter without a measured context problem and a smaller experiment.

## Registries

Separate concepts:

- **Product Feature Registry** — desired, not found in inspected dev; indexes Feature Passports and maturity.
- **Execution/verification registry** — legacy observed mechanism for controlled runtime evidence.
- **Protected/canonical artifact registry** — possible Governance mechanism.

A registry never owns product truth independently of its human-reviewed source artifacts.

## Agent adapters

One common authority/rule source should feed thin adapters for Cursor, Claude Code, Codex and ChatGPT. Prompt packs exist, but a proven single-source renderer was not established. External Ruler/MDC patterns remain references, not dependencies.

## Repository topology

Current direction: modular monorepo first.

Historical cross-repo design is retained as reference for later organizations with separate teams/releases/compliance boundaries. Automatic merge/sync may not bypass human authority.

## Deferred architecture candidates

- specialized agents and model routing;
- multi-agent debate;
- Git-backed memory/replay;
- structural self-heal;
- control UI/SaaS/cloud;
- full RAG/vector infrastructure.

All require problem evidence, metrics, bounded experiment and rollback.

## Architecture feature map

| ID | Feature / component | Decision | Repository | Current note |
|---|---|---|---|---|
| `F-17` | State, Status, Next Action, and Recovery | DECIDED. | OBSERVED in state module and handoff. | Historical lifecycle is richer than necessary; current README/HANDOFF status is inconsistent. |
| `F-18` | Human Approval and Authorization Boundaries | DECIDED. | OBSERVED throughout canonical modules and false-PASS mechanisms. | A concise target decision-record format is not selected. |
| `F-20` | Honest PASS / False-PASS Resistance | DECIDED at principle level. | OBSERVED — contract, checker, fixtures, and repository completion report exist. | Repository-reported tests were NOT_RUN by this audit. |
| `F-21` | Controlled Runner and Dry-Run Protocol | DECIDED as a safety pattern. | OBSERVED in README capability claims and generator behavior; full runner not deeply inspected. | Target runner scope may be smaller than historical implementation. |
| `F-22` | Bounded Retry and Escalation | UNKNOWN | OBSERVED as a policy; the policy states automation was not implemented by that task. | Need evidence that a simpler retry rule is insufficient before importing the full mechanism. |
| `F-23` | Session Handoff / “На чём остановились” | DECIDED. | OBSERVED in `HANDOFF.md` and state rules. | Must remain compact and freshness-bound. |
| `F-25` | Context Engine and Minimal Context Pack | DECIDED direction: minimal task-scoped context. | OBSERVED but incomplete; context index has one stale entry. | Source metadata coverage, freshness, and target complexity are unresolved; full RAG/vector DB is not accepted. |
| `F-26` | Repository Map and Derived Index | UNKNOWN | OBSERVED, but `repo-map.md` and context index are stale/incomplete. | Current map reports 64 files while later inventory reports 5,183. |
| `F-27` | Single Source of Agent Rules and Adapters | DECIDED at principle level: one authority per rule area. | OBSERVED prompt packs/adapters; automated single-source generation is REPORTED. | Current adapters and absolute links need drift/portability review. |
| `F-28` | Cross-Repo Work and Reference-on-Demand | DECIDED for extraction/reference-on-demand; reusable product feature UNKNOWN. | REPORTED in project note, not established as a current canonical feature. | Sync, permissions, installation, and multi-repo governance topology need design. |
| `F-29` | Repository Hygiene and Documentation Drift | DECIDED that old complexity must not be repeated. | OBSERVED — scanner and M68 reports exist. | Historical report recorded 794 duplication signals, 371 same-stem ambiguities, 1,169 authority-wording candidates, and 197 bootstrap-adjacent files; remediation was not approved by that report. |
| `F-31` | Changed-File Guard | UNKNOWN | REPORTED in project note; related scope checkers exist but this exact pattern was not fully traced. | Need one canonical implementation and path policy. |
| `F-34` | Stack and Environment Capture in Specification | UNKNOWN | REPORTED; project documents contain stack sections. | Need to avoid duplicating environment facts across files. |
| `F-35` | Model Routing and Adaptive Accuracy | UNKNOWN | REPORTED research only. | Provider-specific, cost-dependent, and requires measurements; no early target dependency accepted. |
| `F-36` | Specialized Agents / Multi-Agent Debate | UNKNOWN | REPORTED; current README explicitly says multi-agent orchestration is not a current feature. | Contradicts minimal single-agent-first direction unless local evidence proves benefit. |
| `F-37` | Git-Backed Memory and Replay | UNKNOWN | REPORTED research; handoff and Git history provide a simpler partial substitute. | Replay infrastructure and background memory agents add major complexity. |
| `F-38` | Structural Self-Heal and Biological Evolution Rules | UNKNOWN | REPORTED; current README says self-heal is not a current feature. | Self-labelled canonical note conflicts with actual target authority; automation risk is high. |
| `F-39` | Admin/Control UI, Human Decision Cards, Chat, and Preview | UNKNOWN | REPORTED historical roadmap; current README says AgentOS is not a web UI/dashboard. | Product interface and authority model are not chosen. |
| `F-40` | SaaS, Cloud, Auth, GitHub Platform, and Marketplace | UNKNOWN | REPORTED historical roadmap; current README lists backend/cloud/dashboard/marketplace as non-goals. | Direct conflict with current minimal target and no product validation. |
| `F-41` | Feature Catalog and Acceptance Filter | DECIDED that a feature catalog is required; exact filter is REPORTED. | NOT_FOUND as one concise target catalog. | Human owner must approve the final scoring/selection rule. |
| `F-42` | Minimal Product-First Vertical Slice | DECIDED. | Not a single isolated target slice; historical mechanisms exist separately. | Final MVP feature subset and target repository remain UNKNOWN. |

Full details: [06_Features.md](06_Features.md).

## Known architectural blockers

- target name and repository;
- final MVP and first vertical slice;
- Product Runtime/Governance contract;
- target metadata and context minimum;
- human acceptance record;
- exact retained legacy mechanisms;
- official validation/entry route;
- portability repair.

Conflicts and lessons: [04_Lessons.md](04_Lessons.md).

**HUMAN REVIEW REQUIRED**
