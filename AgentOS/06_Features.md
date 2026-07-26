---
document_id: 06_Features
title: "Features"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Features

## Purpose

This is the single detailed feature/component catalog. Each entry separates human decision, repository evidence, gaps and analyst disposition. Source IDs resolve in [05_Reference.md](05_Reference.md).

## Human selection outcomes

For each feature the owner should choose one outcome:

- `KEEP` — required in the target.
- `SIMPLIFY` — retain the problem/behavior but redesign the mechanism.
- `DEFER` — potentially useful after MVP evidence.
- `REFERENCE_ONLY` — keep as prior art.
- `REJECT` — do not carry into the target.

The existing `Analyst disposition` is advisory only. It is neither a decision nor implementation authorization.

## Recommended first review set

- `F-02` Problem Interview
- `F-04` Product Spec
- `F-10` Spec Wizard / Task Brief
- `F-12` Executable Task Contract
- `F-14` Scope Guard
- `F-15` Risk and Security
- `F-18` Human Authority
- `F-19` Verification Gates
- `F-23` Handoff
- `F-24` Lessons
- `F-41` Feature Catalog/Filter
- `F-42` Minimal Product-First Vertical Slice

Review next because they contain high cost or conflict:

- `F-20` Honest PASS
- `F-25` Context Engine
- `F-26` Repo Map/Index
- `F-29` Repository Hygiene
- `F-30` Code Stewardship
- `F-36` Multi-Agent
- `F-38` Self-Heal
- `F-39` Control UI
- `F-40` SaaS/Cloud

## Reading rules

- `Decision status` records human acceptance only.
- `Repository status` records what was found at RP-00.
- `Analyst disposition` is a recommendation for synthesis, not a decision or implementation authorization.
- External claims embedded in notes were not independently revalidated.
- This catalog excludes low-level internal helper functions.

## Summary

| Class | Count |
|---|---:|
| Significant features/components catalogued | 42 |
| Entries containing a human-decided direction | 22 |
| Entries with repository-observed evidence | 25 |
| Entries containing reported/candidate evidence | 16 |
| Entries containing explicit missing/conflicting evidence | 3 |


## F-01. Project Discovery / `/init`

- **Problem:** An agent cannot safely plan before it understands the repository, users, constraints, and current state.
- **Observable behavior:** Collects project identity and Discovery data before specification or execution.
- **Decision status:** UNKNOWN
- **Repository status:** OBSERVED — `INIT.md` and discovery capability claims exist.
- **Known gaps/limits:** No target-system acceptance; current discovery implementation was not executed.
- **Analyst disposition:** `KEEP_CANDIDATE` — not human approval.
- **Sources:** RP-01.

## F-02. Problem Interview

- **Problem:** Non-technical users provide incomplete solutions or ideas rather than implementation-ready requirements.
- **Observable behavior:** Guided interview records problem, users, pain, workaround, desired outcome, success signals, constraints, risks, non-goals, unknowns, and follow-up questions.
- **Decision status:** UNKNOWN
- **Repository status:** OBSERVED — architecture, templates, schema-related artifacts, fixtures, and checker are present.
- **Known gaps/limits:** Historical implementation is detailed; target interaction depth and UX are unselected.
- **Analyst disposition:** `KEEP_AND_SIMPLIFY` — not human approval.
- **Sources:** RP-07, NT-09.

## F-03. Interview Completeness and Missing-Information Detection

- **Problem:** An agent may invent missing requirements or treat a partial interview as ready.
- **Observable behavior:** Checks required fields, explicit missing markers, unknowns without follow-up, allowed statuses, and non-approval wording.
- **Decision status:** DECIDED — uncertainty must remain explicit.
- **Repository status:** OBSERVED — deterministic checker exists.
- **Known gaps/limits:** No independent execution in this audit.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-07.

## F-04. Product Spec

- **Problem:** Product intent is otherwise mixed with implementation details and execution authority.
- **Observable behavior:** Defines problem, users, JTBD, goals, non-goals, constraints, risks, metrics, acceptance, dependencies, open questions, and product lifecycle.
- **Decision status:** DECIDED — product-first direction.
- **Repository status:** OBSERVED — comprehensive architecture document exists.
- **Known gaps/limits:** Target schema and minimal sections still require human selection.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-01, CH-09, RP-08.

## F-05. Progressive Specification Depth

- **Problem:** A single heavy specification format overburdens trivial work.
- **Observable behavior:** Scales required detail from small change to medium feature to high-risk system.
- **Decision status:** DECIDED — avoid overdocumentation and support a simple path.
- **Repository status:** OBSERVED in Product Spec architecture.
- **Known gaps/limits:** Exact thresholds and fast-path contract are not selected for the target.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-08.

## F-06. Contextual Feature/Spec Conflict Review

- **Problem:** A new feature can duplicate existing behavior or violate architecture, constraints, or non-goals.
- **Observable behavior:** Compares a proposed feature/spec against accepted product, architecture, existing specs, dependencies, and constraints; reports conflicts without deciding for the owner.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED/partial — policy fragments exist; a single target checker was not established.
- **Known gaps/limits:** Semantic review implementation and authority contract remain undefined.
- **Analyst disposition:** `KEEP_CANDIDATE` — not human approval.
- **Sources:** NT-06, RP-08.

## F-07. Research Intake

- **Problem:** External evidence and prior art are often mixed into requirements without provenance or applicability review.
- **Observable behavior:** Captures source, claim, relevance, limitations, and decision boundary for research used by a feature.
- **Decision status:** DECIDED for on-demand research; full intake mechanism UNKNOWN.
- **Repository status:** REPORTED in historical roadmap and documents.
- **Known gaps/limits:** No concise target contract chosen.
- **Analyst disposition:** `SIMPLIFY` — not human approval.
- **Sources:** CH-11, NT-18.

## F-08. Scenario, Access, and UX Structure Pipeline

- **Problem:** A product spec does not by itself define actors, access-sensitive scenarios, UX objects, grouping, or screen flow.
- **Observable behavior:** Problem Interview → Problem Map → Scenario Interview → approved scenarios → access model → UX object inventory → grouping → screen map → human approval.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED in project sources; complete end-to-end implementation not established.
- **Known gaps/limits:** Standard vs high-stakes profiles and artifact boundaries need synthesis.
- **Analyst disposition:** `KEEP_CANDIDATE_FOR_PRODUCT_DESIGN` — not human approval.
- **Sources:** NT-09.

## F-09. Neutral, Semantic, Replaceable UI Foundation

- **Problem:** Generated UI may become inconsistent, tightly coupled, or falsely authoritative.
- **Observable behavior:** Separates product UI from AgentOS control UI; uses semantic components, design tokens, replaceability rules, and UI validation; UI renders decisions but cannot create authority.
- **Decision status:** UNKNOWN
- **Repository status:** NOT_FOUND for the three named core policy artifacts at RP-00.
- **Known gaps/limits:** `UI-SEMANTIC-COMPONENT-CONTRACT.md`, `DESIGN-TOKENS-POLICY.md`, and `UI-REPLACEABILITY-POLICY.md` are explicitly missing.
- **Analyst disposition:** `DEFER_UNTIL_PRODUCT_UI_EXISTS` — not human approval.
- **Sources:** NT-10, RP-09, RP-18.

## F-10. Spec Wizard and Task Brief

- **Problem:** A free-form request should not directly become executable work.
- **Observable behavior:** Creates a non-executable Task Brief; a separate validated Task Contract is required for execution.
- **Decision status:** DECIDED in principle.
- **Repository status:** OBSERVED in `INIT.md` and README capability claims.
- **Known gaps/limits:** Wizard behavior and target brief schema were not executed or selected.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-01.

## F-11. Spec-to-Task Candidate Generator

- **Problem:** Manual conversion from approved spec to implementation contract is repetitive and error-prone.
- **Observable behavior:** Generates one candidate Task Contract from an approved spec; dry-run by default; write is explicit; no automatic queue placement or approval.
- **Decision status:** UNKNOWN
- **Repository status:** OBSERVED — documentation and Python implementation exist.
- **Known gaps/limits:** One task only; no full decomposition, UX source, Context Pack selection, or real queue write.
- **Analyst disposition:** `KEEP_AND_SIMPLIFY` — not human approval.
- **Sources:** RP-09.

## F-12. Executable Task Contract / Active Task

- **Problem:** Execution needs one explicit source for goal, scope, risk, rollback, acceptance, and verification.
- **Observable behavior:** Maintains a single active executable contract with bounded fields and separate owner approval.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED — schema, validator, and idle active-task file exist.
- **Known gaps/limits:** Validator idle bypass is too broad and can skip malformed documents.
- **Analyst disposition:** `KEEP_CORE_FIX_VALIDATOR` — not human approval.
- **Sources:** CH-03, RP-10.

## F-13. Task Decomposition, Dependencies, and Queue

- **Problem:** Large product work must be split and ordered without authorizing every candidate automatically.
- **Observable behavior:** Produces candidate tasks, dependencies, blockers, priority, and queue-placement review.
- **Decision status:** UNKNOWN
- **Repository status:** OBSERVED as extensive historical scaffolding; full multi-task generation is a known gap in the inspected generator.
- **Known gaps/limits:** Target need, minimal queue model, and actual materialization policy are unresolved.
- **Analyst disposition:** `DEFER_UNTIL_SINGLE_TASK_SLICE_WORKS` — not human approval.
- **Sources:** RP-01, RP-09.

## F-14. Scope Guard and One-Task Rule

- **Problem:** Agents add unrelated cleanup, refactors, or features and make review/rollback difficult.
- **Observable behavior:** Classifies each requested change as in-scope, scope expansion, or out-of-scope; allows one live task and stops on drift.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED in canonical workflow and lessons.
- **Known gaps/limits:** Runtime enforcement breadth is not selected for the target.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-05, RP-12.

## F-15. Risk and Security Classification

- **Problem:** Documentation edits and destructive/data-sensitive operations cannot use the same execution path.
- **Observable behavior:** Classifies LOW/MEDIUM/HIGH/CRITICAL; applies least privilege, read-only investigation, explicit owner confirmation, and rollback for critical work.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED in security rules and task schema.
- **Known gaps/limits:** Risk taxonomy may be simplified; regulated-domain profiles remain target-specific.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-06, RP-10.

## F-16. Role and Permission Model

- **Problem:** Planner, implementer, verifier, and researcher should not silently gain each other's permissions.
- **Observable behavior:** Binds role, mode, allowed/forbidden paths, write ability, approval ability, lifecycle mutation, and handoff ability.
- **Decision status:** UNKNOWN for multi-role orchestration.
- **Repository status:** OBSERVED in task schema and historical policies.
- **Known gaps/limits:** The next system may begin with one agent and explicit phases rather than multiple agents.
- **Analyst disposition:** `KEEP_PERMISSION_CONTRACT_DEFER_ORCHESTRATION` — not human approval.
- **Sources:** RP-10, CH-03.

## F-17. State, Status, Next Action, and Recovery

- **Problem:** Long-running work loses its exact state and agents infer continuation from narrative history.
- **Observable behavior:** Tracks project/session/task state, blockers, last verified step, next allowed action, transitions, and recovery.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED in state module and handoff.
- **Known gaps/limits:** Historical lifecycle is richer than necessary; current README/HANDOFF status is inconsistent.
- **Analyst disposition:** `KEEP_AND_SIMPLIFY` — not human approval.
- **Sources:** CH-04, RP-04.

## F-18. Human Approval and Authorization Boundaries

- **Problem:** Agents and validators can simulate approval or treat evidence as permission.
- **Observable behavior:** Separates product approval, execution authorization, acceptance, commit, push, merge, deployment, and release.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED throughout canonical modules and false-PASS mechanisms.
- **Known gaps/limits:** A concise target decision-record format is not selected.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-02–RP-06, RP-14.

## F-19. Five Verification Gates / Spec-to-Verification

- **Problem:** A generic test PASS does not prove scope, acceptance, regression, or security.
- **Observable behavior:** Checks structure, scope, every acceptance criterion, regression/smoke, and security/release blockers; binds proof to each criterion.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED in quality rules and verification schema.
- **Known gaps/limits:** The inspected verification report is a TODO demo, not current task proof.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-03, RP-06, RP-11.

## F-20. Honest PASS / False-PASS Resistance

- **Problem:** A system may claim completion without trace, artifact binding, human review, or sufficient evidence.
- **Observable behavior:** Blocks approval/completion/production claims without proof, trace, binding, and explicit human-review status; uses negative fixtures and strict mode.
- **Decision status:** DECIDED at principle level.
- **Repository status:** OBSERVED — contract, checker, fixtures, and repository completion report exist.
- **Known gaps/limits:** Repository-reported tests were NOT_RUN by this audit.
- **Analyst disposition:** `KEEP_CORE_SIMPLIFY_TOKENS` — not human approval.
- **Sources:** CH-03, RP-14, NT-15.

## F-21. Controlled Runner and Dry-Run Protocol

- **Problem:** A proposed action should be inspectable before it mutates files or lifecycle.
- **Observable behavior:** Defaults to preview/dry-run, checks preconditions, and requires explicit write/execute mode.
- **Decision status:** DECIDED as a safety pattern.
- **Repository status:** OBSERVED in README capability claims and generator behavior; full runner not deeply inspected.
- **Known gaps/limits:** Target runner scope may be smaller than historical implementation.
- **Analyst disposition:** `KEEP_PATTERN_NOT_FULL_LEGACY_RUNNER` — not human approval.
- **Sources:** CH-03, RP-01, RP-09.

## F-22. Bounded Retry and Escalation

- **Problem:** Unbounded retry hides repeated failure, expands scope, and can become autonomous self-heal.
- **Observable behavior:** Limits attempts, blocks retry after violations, records attempts, reduces permissions, and escalates to human review.
- **Decision status:** UNKNOWN
- **Repository status:** OBSERVED as a policy; the policy states automation was not implemented by that task.
- **Known gaps/limits:** Need evidence that a simpler retry rule is insufficient before importing the full mechanism.
- **Analyst disposition:** `SIMPLIFY_AND_DEFER_AUTOMATION` — not human approval.
- **Sources:** RP-15.

## F-23. Session Handoff / “На чём остановились”

- **Problem:** Context is lost between agents, tools, and sessions.
- **Observable behavior:** Records terminal snapshot, last verified state, blockers, next allowed action, and persistent context without overriding canonical state.
- **Decision status:** DECIDED.
- **Repository status:** OBSERVED in `HANDOFF.md` and state rules.
- **Known gaps/limits:** Must remain compact and freshness-bound.
- **Analyst disposition:** `KEEP_CORE` — not human approval.
- **Sources:** CH-04, RP-04.

## F-24. Incident-to-Lesson Loop

- **Problem:** The same errors recur because fixes are not converted into specific reusable rules.
- **Observable behavior:** Records trigger, root cause, rule, target rule/file, status, and source incident; repeated failures prompt a human-reviewed rule change.
- **Decision status:** DECIDED at principle level.
- **Repository status:** OBSERVED in workflow and lessons registry.
- **Known gaps/limits:** Workflow's instruction to commit separately conflicts with human-only commit authorization unless explicitly gated.
- **Analyst disposition:** `KEEP_CORE_FIX_AUTHORITY_WORDING` — not human approval.
- **Sources:** RP-05, RP-12, NT-08.

## F-25. Context Engine and Minimal Context Pack

- **Problem:** Agents either read too much or omit relevant rules and lessons.
- **Observable behavior:** Selects minimal explained context, records reasons and hashes, checks freshness, and verifies plan/result against it.
- **Decision status:** DECIDED direction: minimal task-scoped context.
- **Repository status:** OBSERVED but incomplete; context index has one stale entry.
- **Known gaps/limits:** Source metadata coverage, freshness, and target complexity are unresolved; full RAG/vector DB is not accepted.
- **Analyst disposition:** `KEEP_CONCEPT_REBUILD_MINIMALLY` — not human approval.
- **Sources:** CH-11, RP-13, NT-11.

## F-26. Repository Map and Derived Index

- **Problem:** Agents need navigation without treating generated maps as source of truth.
- **Observable behavior:** Generates file inventory/map/index with commit/hash metadata; detects stale derived artifacts.
- **Decision status:** UNKNOWN
- **Repository status:** OBSERVED, but `repo-map.md` and context index are stale/incomplete.
- **Known gaps/limits:** Current map reports 64 files while later inventory reports 5,183.
- **Analyst disposition:** `REBUILD_OR_REMOVE_STALE_MAPS` — not human approval.
- **Sources:** RP-13, RP-17.

## F-27. Single Source of Agent Rules and Adapters

- **Problem:** AGENTS/CLAUDE/GEMINI/Cursor rules drift when copied manually.
- **Observable behavior:** Keeps common policy in one canonical source and renders tool-specific adapters/prompt packs.
- **Decision status:** DECIDED at principle level: one authority per rule area.
- **Repository status:** OBSERVED prompt packs/adapters; automated single-source generation is REPORTED.
- **Known gaps/limits:** Current adapters and absolute links need drift/portability review.
- **Analyst disposition:** `KEEP_CORE_ADAPTERS_THIN` — not human approval.
- **Sources:** RP-03, RP-20, NT-04, NT-07.

## F-28. Cross-Repo Work and Reference-on-Demand

- **Problem:** The system must inspect one repository while writing safely to another and avoid importing all legacy content.
- **Observable behavior:** Pins source SHA, uses read-only source access, writes outside source, preserves provenance, and imports only human-selected artifacts.
- **Decision status:** DECIDED for extraction/reference-on-demand; reusable product feature UNKNOWN.
- **Repository status:** REPORTED in project note, not established as a current canonical feature.
- **Known gaps/limits:** Sync, permissions, installation, and multi-repo governance topology need design.
- **Analyst disposition:** `KEEP_AS_WORKFLOW_FIRST` — not human approval.
- **Sources:** CH-08, CH-11, NT-12.

## F-29. Repository Hygiene and Documentation Drift

- **Problem:** Thousands of generated docs, reports, duplicates, stale routes, and approval phrases make authority and maintenance unreliable.
- **Observable behavior:** Read-only scan inventories paths, duplicates, owners, protected artifacts, drift candidates, prompt metrics, and anomalies.
- **Decision status:** DECIDED that old complexity must not be repeated.
- **Repository status:** OBSERVED — scanner and M68 reports exist.
- **Known gaps/limits:** Historical report recorded 794 duplication signals, 371 same-stem ambiguities, 1,169 authority-wording candidates, and 197 bootstrap-adjacent files; remediation was not approved by that report.
- **Analyst disposition:** `KEEP_SMALL_READ_ONLY_HEALTH_CHECK` — not human approval.
- **Sources:** CH-10, RP-16, NT-19.

## F-30. AI Code Stewardship and Maintainability

- **Problem:** AI-written code can lack ownership, rationale, traceability, handoff quality, and docs-code consistency.
- **Observable behavior:** Defines ownership/rationale, decision ledger, maintainability checks, doc drift, handoff, negative fixtures, and weekly review.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED in source notes; dedicated maintainability and doc-drift scripts were NOT_FOUND at RP-00.
- **Known gaps/limits:** General repo drift scanning is not equivalent to the full proposed feature.
- **Analyst disposition:** `KEEP_PROBLEM_DEFER_FULL_SYSTEM` — not human approval.
- **Sources:** NT-13, NT-14, RP-19.

## F-31. Changed-File Guard

- **Problem:** Protected task, queue, or canonical files can change outside the declared scope.
- **Observable behavior:** Compares `git status`/diff against allowed paths and fails closed on unexpected changes.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED in project note; related scope checkers exist but this exact pattern was not fully traced.
- **Known gaps/limits:** Need one canonical implementation and path policy.
- **Analyst disposition:** `KEEP_CANDIDATE` — not human approval.
- **Sources:** NT-16, RP-05.

## F-32. Code Quality Micro-Improvement and Final Quality Gate

- **Problem:** A feature may meet its local criterion while leaving obvious maintainability or correctness debt.
- **Observable behavior:** Permits only task-relevant small improvements, then runs a bounded final quality check before review.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED in source note.
- **Known gaps/limits:** Must not become scope creep or unbounded cleanup.
- **Analyst disposition:** `DEFER_UNTIL_SCOPE_RULES_STABLE` — not human approval.
- **Sources:** NT-17.

## F-33. Installation, Template, and Simple Mode

- **Problem:** A non-programmer needs a safe entry path for a new or existing repository.
- **Observable behavior:** Offers clean template or dry-run installation, conflict review, explicit apply, and Simple Mode by default.
- **Decision status:** DECIDED direction: low-friction entry.
- **Repository status:** OBSERVED in README and historical handoff.
- **Known gaps/limits:** Installer and template behavior were not run; target packaging is unselected.
- **Analyst disposition:** `KEEP_AFTER_CORE_VERTICAL_SLICE` — not human approval.
- **Sources:** CH-01, RP-01.

## F-34. Stack and Environment Capture in Specification

- **Problem:** Tasks can be designed against an unknown or incompatible stack.
- **Observable behavior:** Records language, framework, runtime, package manager, services, environments, constraints, and dependency policy in project/spec context.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED; project documents contain stack sections.
- **Known gaps/limits:** Need to avoid duplicating environment facts across files.
- **Analyst disposition:** `KEEP_SMALL` — not human approval.
- **Sources:** NT-22, RP-01.

## F-35. Model Routing and Adaptive Accuracy

- **Problem:** Using the same model and compute budget for every task wastes cost or lowers accuracy.
- **Observable behavior:** Routes by complexity/risk; may use schema retry, few-shot examples, second opinion, adaptive attempts, or stronger-model escalation.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED research only.
- **Known gaps/limits:** Provider-specific, cost-dependent, and requires measurements; no early target dependency accepted.
- **Analyst disposition:** `DEFER` — not human approval.
- **Sources:** NT-04, NT-05.

## F-36. Specialized Agents / Multi-Agent Debate

- **Problem:** Planning, navigation, implementation, and verification may interfere when one agent performs all roles.
- **Observable behavior:** Separates roles or uses independent model debate for selected high-risk decisions.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED; current README explicitly says multi-agent orchestration is not a current feature.
- **Known gaps/limits:** Contradicts minimal single-agent-first direction unless local evidence proves benefit.
- **Analyst disposition:** `REFERENCE_ONLY_UNTIL_NEEDED` — not human approval.
- **Sources:** NT-04, NT-21, RP-01.

## F-37. Git-Backed Memory and Replay

- **Problem:** Session context and incidents are hard to inspect, version, and reproduce.
- **Observable behavior:** Versions context/memory changes and records reproducible agent actions or sessions.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED research; handoff and Git history provide a simpler partial substitute.
- **Known gaps/limits:** Replay infrastructure and background memory agents add major complexity.
- **Analyst disposition:** `DEFER_REFERENCE_ONLY` — not human approval.
- **Sources:** NT-07.

## F-38. Structural Self-Heal and Biological Evolution Rules

- **Problem:** Missing files, broken metadata, or stale indexes can degrade the workspace.
- **Observable behavior:** Repairs only structural artifacts, logs every repair, preserves canonical decisions, and measures context/health degradation.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED; current README says self-heal is not a current feature.
- **Known gaps/limits:** Self-labelled canonical note conflicts with actual target authority; automation risk is high.
- **Analyst disposition:** `DO_NOT_IMPORT_WHOLESALE` — not human approval.
- **Sources:** NT-08, RP-01.

## F-39. Admin/Control UI, Human Decision Cards, Chat, and Preview

- **Problem:** A non-programmer may need a visible control surface rather than raw Markdown and CLI.
- **Observable behavior:** Shows task state, risk, evidence, decisions, next action, chat, and preview without creating authority.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED historical roadmap; current README says AgentOS is not a web UI/dashboard.
- **Known gaps/limits:** Product interface and authority model are not chosen.
- **Analyst disposition:** `DEFER_UNTIL_CHAT_FIRST_MVP_PROVES_NEED` — not human approval.
- **Sources:** NT-09, NT-10, NT-18, NT-24, RP-01.

## F-40. SaaS, Cloud, Auth, GitHub Platform, and Marketplace

- **Problem:** Teams may eventually need hosted collaboration and managed integrations.
- **Observable behavior:** Cloud account, authentication, repository integration, hosted control plane, usage/pricing, and public pilot.
- **Decision status:** UNKNOWN
- **Repository status:** REPORTED historical roadmap; current README lists backend/cloud/dashboard/marketplace as non-goals.
- **Known gaps/limits:** Direct conflict with current minimal target and no product validation.
- **Analyst disposition:** `DO_NOT_IMPORT_IN_MVP` — not human approval.
- **Sources:** NT-18, NT-24, RP-01.

## F-41. Feature Catalog and Acceptance Filter

- **Problem:** Ideas accumulate without a consistent test for user value, risk reduction, portability, or verifiability.
- **Observable behavior:** Records each feature's problem, user, behavior, dependencies, maturity, evidence, constraints, and human decision; rejects ideas that add complexity without measurable value.
- **Decision status:** DECIDED that a feature catalog is required; exact filter is REPORTED.
- **Repository status:** NOT_FOUND as one concise target catalog.
- **Known gaps/limits:** Human owner must approve the final scoring/selection rule.
- **Analyst disposition:** `KEEP_CORE_FOR_SYNTHESIS` — not human approval.
- **Sources:** CH-11–CH-13, NT-02.

## F-42. Minimal Product-First Vertical Slice

- **Problem:** Historical development built extensive governance before proving the basic user value.
- **Observable behavior:** Implements one path: idea → product intent → bounded task → one change → verification → human acceptance → handoff/lesson.
- **Decision status:** DECIDED.
- **Repository status:** Not a single isolated target slice; historical mechanisms exist separately.
- **Known gaps/limits:** Final MVP feature subset and target repository remain UNKNOWN.
- **Analyst disposition:** `NEXT_DESIGN_ANCHOR` — not human approval.
- **Sources:** CH-01, CH-03, CH-09, CH-11.

## Catalog status

The catalog is a reviewable feature source, not an approved roadmap. No feature is implemented in the target merely because a related legacy artifact exists.

**PARTIAL EXTRACTION READY FOR REVIEW**

**HUMAN REVIEW REQUIRED**
