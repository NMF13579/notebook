---
document_id: 03_Development
title: "Development"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Development

## Working model

```text
pin repository / branch / baseline
  → restore state
  → load relevant context
  → define expected result, in/out scope, risk, acceptance and verification
  → plan only when required
  → obtain applicable execution authorization
  → make the smallest bounded change
  → verify actual structure/scope/acceptance/regression/security
  → report run/not-run evidence and remaining risk
  → human acceptance
  → separately authorize commit/push/merge/release
  → handoff and lesson proposal
```

Status: `DECIDED` at principle level.

## Required semantic distinctions

- analysis is not execution;
- plan is not implementation;
- file presence is not behavior;
- task candidate is not active task;
- readiness is not authorization;
- execution is not verification;
- test PASS is not product acceptance;
- CI PASS is not human approval;
- verification is not commit permission;
- commit is not push;
- push is not merge;
- merge is not release;
- `UNKNOWN` is not `OK`;
- `NOT_RUN` is not `PASS`.

## Task Brief and executable contract

A material task should define:

```yaml
task:
  goal:
  expected_result:
  in_scope:
  out_of_scope:
  files_or_areas:
  allowed_changes:
  forbidden_changes:
  risk_level:
  requires_owner_approval:
  acceptance_criteria:
  verification_plan:
  rollback_or_recovery:
  stopping_conditions:
```

A Task Brief is descriptive and non-executable. Promotion/activation is a separate human checkpoint.

## Risk-scaled flow

### Trivial / low risk

Confirm scope → one change → focused check → concise report. No redundant architecture chain.

### Medium

Explicit acceptance, plan, relevant regression and handoff.

### High / protected

Pinned baseline, inventory, protected paths, explicit authorization, rollback, evidence package and human review.

### Critical / destructive / sensitive

Stop-before-action, least privilege, recovery plan and explicit human decision. No inferred authorization.

## Preflight

For protected work verify:

- repository identity and branch;
- baseline and working-tree state;
- source/destination separation;
- active task and authority;
- allowed and forbidden paths/commands;
- credentials/data boundary;
- rollback/recovery;
- required context and evidence freshness.

Clean tree is a useful default for bootstrap/protected operations, not a universal substitute for scoped isolation.

## Change control

- one active task;
- one causal change where practical;
- no unrelated cleanup or policy changes;
- inventory before sensitive modification;
- explicit scope expansion decision;
- changed-file allowlist/diff guard;
- atomic commits after separate authorization;
- code ↔ docs ↔ schema ↔ CLI ↔ tests consistency;
- source repository read-only during audit/extraction.

## Verification

Recommended gates:

1. **Structure** — required files/routes/contracts exist and parse.
2. **Scope** — actual changed paths match declared and allowed scope.
3. **Acceptance** — every criterion has relevant evidence or explicit missing status.
4. **Regression / smoke** — relevant behavior was checked or a reason for `NOT_RUN` is recorded.
5. **Security / release blockers** — required for data, auth, API, database, deployment or CI changes.

Fail-closed priority:

```text
CONTRACT_VIOLATION > FAIL > UNKNOWN > NOT_RUN > PASS
```

The target should keep a smaller status vocabulary than the historical repository unless extra states provide measured value.

## Evidence rules

A trustworthy report states:

- what changed;
- actual changed files;
- commands/checks that were run;
- exit/results;
- checks not run and why;
- evidence freshness and relevance;
- known limitations and remaining risk;
- human acceptance status.

Agent text is a claim. Runner/test/manual observation may be evidence. Evidence still is not approval.

## Recovery and bounded retry

```text
detect failure/drift
  → stop and preserve state/evidence
  → classify root cause
  → retry smaller approach, rollback or re-plan
  → verify restored state
  → continue only after confirmation
```

Retry must be bounded. Repeated failure escalates to the owner rather than creating endless correction loops.

## Incident and lesson

After a material incident record:

- event and trigger;
- root cause;
- impact;
- corrective action;
- verification;
- distilled lesson;
- repeat risk;
- proposed rule/template change.

A lesson proposal does not mutate policy or authorize a commit.

## AI-written code maintainability

For material code, future work should preserve:

- intent and architectural rationale;
- ownership/affected components;
- invariants and safe-change boundaries;
- tests and validation commands;
- known debt and deferred work;
- docs-code consistency;
- handoff for the next human/agent.

Dedicated maintainability tooling was not found at the inspected snapshot. The feature is a review candidate, not current implementation.

## Manual dogfood before automation

Run a real bounded task and measure:

- owner comprehension;
- number of clarification loops;
- scope drift;
- false status/authority confusion;
- time to evidence and acceptance;
- handoff quality;
- governance overhead.

Only automate repeated proven friction.

## Cross-repository/reference work

Pin exact source SHA, keep source read-only, write outside source, preserve provenance and import only human-selected output. External claims are revalidated only when material to a selected feature.

## Development sequence

1. Human-select first vertical slice.
2. Execute manual real-task cycles.
3. Add schema/scope/evidence automation for observed repetition.
4. Add context routing only when measured context problems exist.
5. Add enhanced Governance/runtime only for demonstrated risks.
6. Defer orchestration/UI/cloud until product evidence requires them.

## Development feature map

| ID | Feature / component | Decision | Repository | Current note |
|---|---|---|---|---|
| `F-03` | Interview Completeness and Missing-Information Detection | DECIDED — uncertainty must remain explicit. | OBSERVED — deterministic checker exists. | No independent execution in this audit. |
| `F-05` | Progressive Specification Depth | DECIDED — avoid overdocumentation and support a simple path. | OBSERVED in Product Spec architecture. | Exact thresholds and fast-path contract are not selected for the target. |
| `F-10` | Spec Wizard and Task Brief | DECIDED in principle. | OBSERVED in `INIT.md` and README capability claims. | Wizard behavior and target brief schema were not executed or selected. |
| `F-11` | Spec-to-Task Candidate Generator | UNKNOWN | OBSERVED — documentation and Python implementation exist. | One task only; no full decomposition, UX source, Context Pack selection, or real queue write. |
| `F-12` | Executable Task Contract / Active Task | DECIDED. | OBSERVED — schema, validator, and idle active-task file exist. | Validator idle bypass is too broad and can skip malformed documents. |
| `F-13` | Task Decomposition, Dependencies, and Queue | UNKNOWN | OBSERVED as extensive historical scaffolding; full multi-task generation is a known gap in the inspected generator. | Target need, minimal queue model, and actual materialization policy are unresolved. |
| `F-14` | Scope Guard and One-Task Rule | DECIDED. | OBSERVED in canonical workflow and lessons. | Runtime enforcement breadth is not selected for the target. |
| `F-15` | Risk and Security Classification | DECIDED. | OBSERVED in security rules and task schema. | Risk taxonomy may be simplified; regulated-domain profiles remain target-specific. |
| `F-16` | Role and Permission Model | UNKNOWN for multi-role orchestration. | OBSERVED in task schema and historical policies. | The next system may begin with one agent and explicit phases rather than multiple agents. |
| `F-17` | State, Status, Next Action, and Recovery | DECIDED. | OBSERVED in state module and handoff. | Historical lifecycle is richer than necessary; current README/HANDOFF status is inconsistent. |
| `F-18` | Human Approval and Authorization Boundaries | DECIDED. | OBSERVED throughout canonical modules and false-PASS mechanisms. | A concise target decision-record format is not selected. |
| `F-19` | Five Verification Gates / Spec-to-Verification | DECIDED. | OBSERVED in quality rules and verification schema. | The inspected verification report is a TODO demo, not current task proof. |
| `F-20` | Honest PASS / False-PASS Resistance | DECIDED at principle level. | OBSERVED — contract, checker, fixtures, and repository completion report exist. | Repository-reported tests were NOT_RUN by this audit. |
| `F-21` | Controlled Runner and Dry-Run Protocol | DECIDED as a safety pattern. | OBSERVED in README capability claims and generator behavior; full runner not deeply inspected. | Target runner scope may be smaller than historical implementation. |
| `F-22` | Bounded Retry and Escalation | UNKNOWN | OBSERVED as a policy; the policy states automation was not implemented by that task. | Need evidence that a simpler retry rule is insufficient before importing the full mechanism. |
| `F-23` | Session Handoff / “На чём остановились” | DECIDED. | OBSERVED in `HANDOFF.md` and state rules. | Must remain compact and freshness-bound. |
| `F-24` | Incident-to-Lesson Loop | DECIDED at principle level. | OBSERVED in workflow and lessons registry. | Workflow's instruction to commit separately conflicts with human-only commit authorization unless explicitly gated. |
| `F-28` | Cross-Repo Work and Reference-on-Demand | DECIDED for extraction/reference-on-demand; reusable product feature UNKNOWN. | REPORTED in project note, not established as a current canonical feature. | Sync, permissions, installation, and multi-repo governance topology need design. |
| `F-29` | Repository Hygiene and Documentation Drift | DECIDED that old complexity must not be repeated. | OBSERVED — scanner and M68 reports exist. | Historical report recorded 794 duplication signals, 371 same-stem ambiguities, 1,169 authority-wording candidates, and 197 bootstrap-adjacent files; remediation was not approved by that report. |
| `F-30` | AI Code Stewardship and Maintainability | UNKNOWN | REPORTED in source notes; dedicated maintainability and doc-drift scripts were NOT_FOUND at RP-00. | General repo drift scanning is not equivalent to the full proposed feature. |
| `F-31` | Changed-File Guard | UNKNOWN | REPORTED in project note; related scope checkers exist but this exact pattern was not fully traced. | Need one canonical implementation and path policy. |
| `F-32` | Code Quality Micro-Improvement and Final Quality Gate | UNKNOWN | REPORTED in source note. | Must not become scope creep or unbounded cleanup. |
| `F-33` | Installation, Template, and Simple Mode | DECIDED direction: low-friction entry. | OBSERVED in README and historical handoff. | Installer and template behavior were not run; target packaging is unselected. |
| `F-34` | Stack and Environment Capture in Specification | UNKNOWN | REPORTED; project documents contain stack sections. | Need to avoid duplicating environment facts across files. |
| `F-42` | Minimal Product-First Vertical Slice | DECIDED. | Not a single isolated target slice; historical mechanisms exist separately. | Final MVP feature subset and target repository remain UNKNOWN. |

Full details: [06_Features.md](06_Features.md).

## Audit caveat

No historical command, test, build, validator, CI job or release check was run while creating this catalog. Stored repository reports do not become current PASS.

**HUMAN REVIEW REQUIRED**
