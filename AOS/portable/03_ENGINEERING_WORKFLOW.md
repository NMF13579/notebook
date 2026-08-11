---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
artifact_role: ENGINEERING_WORKFLOW_OWNER
status: DRAFT
authority: NONE
source_owner_identity: sha256:3f880c14b9e00e9428032bc07b29cc18d46b7eed6ceac1084f6ef7745f684fab
accepted_foundation_identity: sha256:b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf
implementation_authorization: NONE
git_authorization: NONE
---

# 03 — Engineering Workflow

## 1. Роль и граница

Документ описывает product-design-level semantics подготовки, выполнения, проверки, review, recovery и delivery будущего AOS. Исходный Workflow owner и frozen Global Design foundation byte-bound в [README.md](README.md).

Он не запускает runtime implementation и не является Task Brief, Execution Authorization, validation result или Git permission.

## 2. Два разных lifecycle

### Documentation design

```text
accepted knowledge sources
→ workspace source synthesis
→ full DRAFT
→ structural refinement
→ package harmonization
→ exact candidate binding
→ separate read-only audit when requested
→ human review and decisions
→ optional publication/freeze under separate authority
```

Documentation editing in this package is not runtime execution. Authoring may correct its own bounded draft during refinement/harmonization; an independent audit or re-audit may not repair the exact subject.

### Future runtime implementation

```text
accepted Product/Feature/Architecture contracts
→ implementation roadmap
→ one vertical slice
→ one bounded task
→ Task Brief
→ repository preflight
→ explicit Execution Authorization
→ EXECUTE one stage
→ Stage Report and stop
→ separate VALIDATE when required
→ REVIEW
→ explicit human decision
→ separate Commit / Push / Merge / Release decisions
→ handoff and lesson proposal
```

No transition from the first lifecycle to the second occurs automatically.

## 3. Roles

| Role | Owns | Must not do |
|---|---|---|
| Product owner / Commander | product scope, exact decisions, protected authorization and acceptance | delegate implicit authority to status/PASS |
| Documentation author | source-bound DRAFT and bounded internal corrections | publish as canonical or invent decisions |
| Planner / analyst | decision-ready Task Brief/proposal | execute protected mutation from plan presence |
| Executor | exact authorized mutation and truthful terminal report | expand scope, validate as independent reviewer, deliver Git implicitly |
| Validator | read-only exact candidate checks and findings | fix subject or simulate acceptance |
| Reviewer | assess user impact, Evidence and remaining risk | mutate candidate or author human verdict |
| Maintainer/operator | current observations, recovery and continuity | treat stale stored state as current truth |

Roles may be performed by the same person/tool in low-risk contexts only when independence is not claimed and stage boundaries remain explicit.

## 4. Documentation authoring workflow

### 4.1 Scope bind

Before editing:

- identify exact goal and output paths;
- bind canonical owners and accepted decisions;
- observe repository/branch/HEAD/worktree;
- declare protected/read-only boundaries;
- classify missing facts and human-only decisions;
- define candidate inventory and review criteria.

### 4.2 Skeleton

Create the entire package topology before deep refinement. Each artifact records role, owner routing, status, provenance, required sections, links, expected review and visible gaps.

### 4.3 Saturation

Fill in authority order:

```text
current human decision
→ accepted exact artifacts
→ canonical owners
→ current observations
→ targeted reference Evidence
→ explicit synthesis/proposal
```

Never fill a human-only decision or missing product fact with plausible text.

### 4.4 Refinement

Deepen each document in dependency order: Core → Product → Architecture → Workflow → Features → Journeys → Roadmap → Decisions → Traceability. Update downstream links and terms after each material refinement.

### 4.5 Harmonization

Review the package as one subject for vocabulary, owner boundaries, status/authority, accepted-decision closure, feature dispositions, traceability, link consistency, remaining unknowns and absence of implementation HOW.

Bounded authoring corrections are allowed for defects supported by already bound sources. New product scope, architecture choice, material conflict or protected mutation becomes a finding/decision request.

### 4.6 Exact binding and handoff

Compute raw-byte SHA-256 for every included artifact, create a deterministic non-self-referential manifest, run construction checks and stop at the declared next gate. For a correction responding to an independent audit `FAIL`, the next gate is independent read-only re-audit; human review remains later and separate.

## 5. Risk-scaled task preparation

| Risk/complexity | Minimum workflow |
|---|---|
| Low/reversible documentation | scope → edit → focused checks → concise report → stop |
| Medium change | explicit acceptance criteria → short plan → relevant regression → handoff |
| High/protected | pinned identity → exact allowlist → authorization → rollback/Evidence → independent validation/review |
| Critical/destructive/sensitive | stop-before-action → least privilege → data/provider boundary → recovery plan → human decision |

Risk Profile itself remains human-owned. An agent may identify risk factors and propose a profile, but cannot assign one.

## 6. Feature-to-implementation entry gate

Before future implementation planning, the selected feature requires:

- explicit `feature_id` and current human disposition;
- human-accepted Product Spec context;
- human-accepted feature-specific Passport;
- observable outcome, users, trigger and preconditions;
- semantic I/O, flow, states and transitions;
- failures, recovery and negative scenarios;
- dependencies and authority boundaries;
- acceptance criteria and required Evidence;
- resolved material product/architecture decisions;
- exact implementation repository decision;
- open implementation choices classified, not silently selected.

Feature dossier or this full DRAFT alone is insufficient.

## 7. Lazy decomposition

```text
Outcome / Epic
→ vertical slice
→ stage
→ sub-stage only for material boundary
→ executable task
```

Create a child only for distinct authority, independent validation, material risk, protected operation, different acceptance, dependency or recovery boundary. Avoid full speculative backlog. One active task at a time unless human selects explicit parallel work.

## 8. Task Brief contract

A future C-005 Task Brief minimally binds:

- task/feature identity and user outcome;
- requested runtime stage;
- repository/worktree/branch/HEAD/baseline;
- allowed and forbidden paths/operations;
- assumptions, unknowns and dependencies;
- proposed risk factors and human-assigned Risk Profile;
- acceptance/validation matrix;
- stop conditions, side-effect and recovery boundaries.

Completeness makes the task reviewable, not executable.

## 9. Preflight and preview

Preflight is read-only and performed immediately before a dependent mutation. It verifies:

- repository root/identity, registered worktree, branch and HEAD;
- baseline/candidate, staged/unstaged/untracked state and nested repos;
- allowed paths, forbidden paths, traversal/symlink risks;
- interpreter/dependency provenance and relevant environment;
- network/remote/data/provider boundary;
- credentials redaction;
- temp-root/output absence or recoverable reuse rule;
- exact planned operations and conflicts;
- current authorization and stop conditions.

Dirty state classification:

```text
IN_SCOPE_EXISTING
OUT_OF_SCOPE_USER_STATE
ENVIRONMENT_NOISE
GENERATED_DISPOSABLE
UNKNOWN_MATERIAL
```

Preview is invalid if any relevant subject, scope, permission or environmental premise changes.

## 10. Runtime stages

### PLAN

Read-only. Produces a decision-ready Task Brief, risk analysis, validation design and stop conditions. It does not authorize EXECUTE.

### EXECUTE

Entry requires exact current authorization. Performs one smallest bounded causal change, records observable actual effects, reconciles intended/actual state, runs authorized focused checks, writes terminal Stage Report and stops. No unrelated cleanup, hidden correction cycle, validation claim or Git delivery.

### VALIDATE

Read-only exact candidate. Verifies source/import/environment provenance, required checks, acceptance, negatives, regression and relevant security gates. Does not fix. A finding leads to a separate correction task/candidate.

Independence is claimed only when reviewer context/tooling is genuinely independent; otherwise the limitation is explicit.

### REVIEW

Read-only assessment of purpose, user impact, before/after, scope, Evidence, findings, `NOT_RUN`, limitations and decision options. The agent/reviewer does not write the human decision.

### DELIVER / Handoff

Not a runtime stage and not Git permission. Records exact state, results, blockers, decisions, permissions and one next action for continuation.

## 11. Terminal results and aggregation

```text
CONTRACT_VIOLATION
> FAIL
> BLOCKED
> UNKNOWN
> NOT_RUN
> PASS
```

Aggregation is fail-closed within declared required checks. `HUMAN_REVIEW_REQUIRED` indicates an authority/decision boundary, not technical success.

Every terminal result includes:

- exact subject and starting/ending identities;
- performed and not-performed checks;
- changed paths/side effects;
- findings, limitations and unknowns;
- authorization state/consumption;
- one next required action;
- explicit stop.

## 12. Validation strategy

### Gate 1 — Structure

Required files, schemas/format, enumerations, links, syntax, path portability and identity rules.

### Gate 2 — Scope

Task Brief/authorization/preview/actual diff agreement; unrelated dirty state excluded; no forbidden side effects.

### Gate 3 — Acceptance

Each user-observable criterion mapped to current subject-bound Evidence; required unknown/NOT_RUN visible.

### Gate 4 — Regression and smoke

Relevant positive path, negative fixtures, prior accepted regressions and no accidental breakage of adjacent contracts.

### Gate 5 — Security/release blockers

Authority, permission, secret/data/provider, path/traversal, external content, remote/delivery and rollback boundaries.

Wider suites run only when risk/change scope warrants them. A passing irrelevant suite is not acceptance Evidence.

## 13. Evidence rules

Good Evidence is:

- tied to exact candidate and criterion;
- reproducible or sufficiently inspectable;
- current for mutable facts;
- explicit about method/tool/environment;
- clear about temporal and search boundary;
- redacted without hiding material claim;
- immutable after review binding or re-identified after change.

Historical reports, screenshots without subject identity, temporary output, model confidence and file presence are not sufficient current Evidence by themselves.

## 14. Human review and decision

The review package should answer:

1. What outcome was intended?
2. What exact subject changed?
3. What is the user-visible before/after?
4. What Evidence supports each criterion?
5. What failed, was not run or remains unknown?
6. What decisions/options are now available?
7. What authority is still absent?

Valid human outcomes:

```text
ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

The record binds exact subject, actor/source, decision scope/fact classes and any selected options. Acceptance cannot grant implementation/Git authority unless the human decision explicitly and separately does so.

## 15. Correction semantics

### Documentation authoring correction

Allowed inside the same authoring interval only for bounded defects already resolvable from bound sources: terminology, missing source-grounded section, links, formatting, internal traceability and duplication.

### Runtime/candidate correction

Separate authorized change after validation finding. Any byte change creates a new candidate identity and invalidates old Evidence/audit/human decision for the prior subject.

### Prohibited hidden correction

Validator/reviewer must not silently repair subject, loosen checks, alter expected output or reinterpret a required `NOT_RUN` as PASS.

## 16. Failure, recovery and resume

### On execution failure

1. Stop further mutation.
2. Preserve logs, exact partial state and the exact effect record needed to reconstruct what happened.
3. Compare intended/actual changes.
4. Classify safe state, data risk and invalidated evidence.
5. Present bounded resume/rollback/correction options.
6. Request human decision when scope/authority/data risk changed.

### On validation finding

Report and stop. Create a separate exact correction task if authorized; re-freeze and revalidate the new subject.

### On session resume

Read current owners/handoff, re-observe repository facts, verify candidate/decision/authorization identity, reject stale projections and continue only the exact still-valid action.

## 17. Git and release delivery

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Each action requires an exact current subject, repository/branch/HEAD/remote observation and separate explicit authority. After any action, verify actual result and stop unless the next action is separately authorized. Force push, branch deletion, tag/release or deployment are never inferred.

## 18. Testing and regression design for future runtime

### Unit/contract targets

- strict status/enums and bool/int edge cases;
- subject digests and mismatch handling;
- authority defaults false and authorization freshness;
- path normalization/traversal/symlink boundaries;
- state-axis independence;
- `NOT_RUN` aggregation;
- ownership and registry derivation.

### Integration targets

- intent→specification;
- discovery→capability map;
- preview→authorized apply;
- execution→candidate→validation;
- Evidence→review→human record;
- memory→resume;
- install/update→reconcile;
- candidate freeze→identity validation.

### End-to-end targets

- first contact and FTR-001 slice;
- idea→reviewable product definition;
- interruption/recovery;
- protected action blocked without authority;
- required check `NOT_RUN` remains visible;
- update preserves user state;
- Git actions stay independent;
- incident produces lesson proposal, not automatic rule.

The accepted regression catalog byte-bound in [README.md](README.md) remains the source for `AUTH-*`, `STATUS-*`, `SCOPE-*`, `CLI-*`, `ENV-*`, `FREEZE-*`, `INSTALL-*`, `UPDATE-*`, `RECOVERY-*`, `REVIEW-*`, `GIT-*`, `ROUTING-*`, `CONTENT-*`, `DRIFT-*`, `ADAPTER-*`, `DOGFOOD-*`, `LESSON-*`, `IDLE-*` and `PORTABLE-*` prompts.

## 19. Manual dogfood before automation

For each candidate flow, record comprehension, clarification loops, scope drift, authority confusion, time to Evidence/review, recovery success, handoff quality and control overhead. Automate only repeated stable work with known failures, measurable benefit, fallback/removal and no authority expansion.

## 20. Roadmap and readiness chain

```text
full DRAFT documentation
≠ human-accepted documentation
≠ accepted feature dispositions
≠ accepted architecture decisions
≠ implementation roadmap
≠ Task Brief
≠ Execution Authorization
≠ successful implementation
≠ human acceptance
≠ Git delivery
```

The proposed sequence is in [06_PROJECT_ROADMAP.md](06_PROJECT_ROADMAP.md); open selections are in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).

## 21. Workflow review checklist

- Are documentation and runtime lifecycles unambiguously separated?
- Can a plan, PASS, review or accepted document accidentally authorize execution?
- Does each protected stage have exact entry, exit and stop semantics?
- Is validation read-only and candidate-bound?
- Are Evidence, limitations and `NOT_RUN` preserved?
- Is correction always a new exact subject when validation has begun?
- Are failure/recovery/resume paths safe and understandable?
- Are Git actions independently authorized and verified?
- Is ceremony proportional, with manual proof before automation?
- Does this document avoid choosing implementation HOW?
