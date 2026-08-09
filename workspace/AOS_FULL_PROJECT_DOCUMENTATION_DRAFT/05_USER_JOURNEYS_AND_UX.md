---
package: AOS_FULL_PROJECT_DOCUMENTATION_DRAFT
package_revision: DRAFT-R1
artifact_role: USER_JOURNEYS_AND_UX_REVIEW_VIEW
status: DRAFT
authority: NONE
canonical_owner: docs/01_Product.md
interface_selection: UNKNOWN
implementation_authorization: NONE
git_authorization: NONE
---

# 05 — User Journeys and UX

## 1. Роль и interface neutrality

Документ разворачивает accepted journeys `J-001…J-007` в reviewable user-visible behavior. Он не выбирает CLI, chat, desktop, web или SaaS. Terms such as `Status`, `Next`, `Details`, “screen” and “command” identify UX objects/actions that any selected interface may render.

Canonical journey/product facts remain owned by [docs/01_Product.md](../../docs/01_Product.md). New interaction detail is `SYNTHESIZED_DRAFT`.

## 2. UX principles

| ID | Principle | Requirement |
|---|---|---|
| `UX-001` | Original intent visible | user can compare source request with structured interpretation |
| `UX-002` | One next action | primary view presents one safe route; alternatives live in Details |
| `UX-003` | State axes separated | technical result, human decision, permission and maturity are not one badge |
| `UX-004` | Unknowns actionable | each material unknown says what it affects and how to resolve it |
| `UX-005` | Human checkpoints explicit | decision/action subject and effect are visible before confirmation |
| `UX-006` | Progressive disclosure | Status and review remain concise; exact Evidence and raw details are available |
| `UX-007` | No false certainty | stale/partial/NOT_RUN cannot look complete or approved |
| `UX-008` | Source and freshness | user can see owner, observed-at identity/time and stale state |
| `UX-009` | Recoverability | failure view preserves actual state and offers bounded options |
| `UX-010` | Plain language first | jargon has explanation; machine identifiers remain available |
| `UX-011` | Accessibility | meaning does not depend only on color, position or animation |
| `UX-012` | Authority-safe UI | click/message does not imply approval without exact decision record |

## 3. Core UX objects

| Object | Purpose | Required content | Authority |
|---|---|---|---|
| Intent view | review understood problem/outcome | original input, synthesis, assumptions, unknowns, constraints, revision | derived until human confirms exact record |
| Product view | understand cross-feature product | problem, actors, journeys, boundaries, acceptance, decisions | DRAFT/accepted Product Spec by exact status |
| Feature view | understand one behavior | C-002 fields, dependencies, disposition, acceptance/negative | Passport status/fact class only |
| Status | answer “where are we?” | exact subject, current phase/result/decision/permission, freshness | derived |
| Next | answer “what should I do?” | one action, why, expected effect and authority needed | recommendation only |
| Details | inspect proof/context | owners, Evidence, diffs, checks, limitations, history | derived |
| Decision card | capture human choice | exact subject, options/trade-offs, effect, unresolved boundaries | human record only after explicit action |
| Execution preview | show planned mutation | repo/paths/operations/side effects/conflicts/auth | read-only, no permission |
| Review package | evaluate outcome | before/after, criteria/Evidence, findings, NOT_RUN, options | no acceptance until exact record |
| Recovery view | resume safely | actual partial state, invalidated claims, options, next action | derived; destructive action separately authorized |
| Handoff | continue across session/tool | identities, sources, decisions, blockers, permissions, next | derived and freshness-checked |

## 4. Global interaction rules

### Status presentation

Primary status answers, in order:

1. What subject/project is this?
2. What exact outcome is current?
3. What is technically known (`PASS/FAIL/...`)?
4. What has the human decided?
5. What action is allowed/blocked and why?
6. What one action is recommended next?

### Unknown/finding presentation

```text
classification + exact claim
→ affected boundary
→ current safe behavior
→ source/Evidence
→ resolution requirement
```

Avoid generic “something went wrong” and avoid global blocking when only one claim is affected.

### Human decision interaction

Before confirmation, show exact subject identity, selected option, effect, fact classes/scope, decisions not included, and whether any protected authority is granted. The default is no decision and no extra authority.

### Error/recovery interaction

Never erase partial state to simplify the message. Show what completed, what did not, whether candidate/Evidence/authorization became invalid, and bounded resume/rollback/correction options. Choose no destructive default.

## 5. J-001 — Start a new project

```yaml
primary_actor: nonprogrammer_or_product_builder
canonical_status: ACCEPTED_JOURNEY
first_runtime_slice: FTR-001_ACCEPTED
related_features: [FTR-001, FTR-003, FTR-005, FTR-006, FTR-012]
```

**Trigger.** User brings a problem, incomplete idea or complete specification for a new project.

**Preconditions.** None beyond access to the original request. Repository, toolchain and architecture are not required for initial intake.

**Primary flow.**

1. AOS preserves original request and identifies its source.
2. It separates problem/outcome from proposed solutions.
3. It shows users, constraints, non-goals, assumptions, unknowns and sensitive flags.
4. It asks only material questions and incorporates corrections into a new exact revision.
5. User confirms or defers the Intent Record. This completes accepted first Product Runtime slice.
6. Under a separate continuation, FTR-003 drafts Product Spec and feature Passports.
7. User reviews product scope and later chooses further slice/architecture decisions.
8. Implementation task/authorization begins only under a separate downstream route.

**Outcome.** At minimum: reviewable, human-confirmed exact Intent Record. Later extension: decision-ready product definition.

**Human checkpoints.** Intent confirmation; product/feature acceptance; material architecture; task authorization; final outcome decision.

**Failure/recovery.** Empty idea stays in clarification; conflict is localized; sensitive boundary stops affected data processing; user can defer without losing exact revision.

**Acceptance.** First-time user can explain what AOS understood, correct it, see remaining unknowns and know one next action. No code/repository/Git action starts implicitly.

## 6. J-002 — Discover an existing project

```yaml
primary_actor: product_builder_or_reviewer
canonical_status: ACCEPTED_JOURNEY
related_features: [FTR-002, FTR-009, FTR-016, FTR-017]
```

**Trigger.** User connects or points AOS at an existing repository and asks what exists, what is missing or what objective should come next.

**Preconditions.** Exact repository locator and read-only permission; branch/ref/worktree identity can be verified.

**Primary flow.**

1. Show proposed read-only boundary and verify zero-write preflight.
2. Bind repository/root/worktree/branch/HEAD and classify dirty state.
3. Inspect high-signal docs/contracts/tests/code in declared scope.
4. Build capability map with source locators and freshness.
5. Separate gaps, conflicts, unknowns and observations from accepted target facts.
6. Present bounded candidate objectives with trade-offs.
7. Human selects or defers one objective; no mutation follows automatically.

**Outcome.** Snapshot-bound, understandable capability/gap picture and exact selected next objective if chosen.

**Failure/recovery.** Changed HEAD marks map stale; missing path is not universal absence; inaccessible reference remains `BLOCKED/NOT_RUN`; repository instructions remain untrusted.

**Acceptance.** Source tree unchanged; user can trace each material finding; selection is explicit and independent from discovery PASS.

## 7. J-003 — Develop one feature

```yaml
primary_actor: product_owner_plus_implementer
canonical_status: ACCEPTED_JOURNEY
related_features: [FTR-003, FTR-005, FTR-006, FTR-009, FTR-010, FTR-011, FTR-012, FTR-013, FTR-014]
```

**Trigger.** A human-selected feature has accepted Product context and needs feature-specific definition and later implementation.

**Preconditions.** Exact feature/disposition; accepted Feature Passport before implementation; resolved material architecture; selected implementation repository for runtime work.

**Primary flow.**

1. Review Feature Passport and exact product outcome.
2. Perform narrow reference research only for explicit gaps.
3. Resolve material ADRs with human choice.
4. Build one C-005 Task Brief and validation matrix.
5. Read-only preflight/preview exact repository action.
6. Human provides exact Execution Authorization.
7. Executor performs one bounded stage and stops with actual Stage Report.
8. Validator checks frozen candidate read-only; correction is separate if needed.
9. Reviewer presents user impact/Evidence/limitations.
10. Human accepts, requests changes, rejects or defers exact candidate.
11. Git actions remain separate.

**Outcome.** Exact feature outcome and recoverable project state with explicit human verdict.

**Failure/recovery.** Missing Passport/decision blocks dependent planning; unexpected mutation stops executor; validation finding creates correction route; changed candidate invalidates prior Evidence.

**Acceptance.** Intent→Product→Feature→Task→Candidate→Evidence→Decision trace is reproducible; no hidden stage or authority expansion.

## 8. J-004 — Resume work

```yaml
primary_actor: any_human_or_new_agent
canonical_status: ACCEPTED_JOURNEY
related_features: [FTR-008, FTR-014, FTR-016, FTR-021]
```

**Trigger.** User returns after interruption or switches agent/tool/session.

**Preconditions.** Source artifacts/handoff are locatable; current repository facts can be re-observed.

**Primary flow.**

1. Identify project, repository and last exact subject.
2. Load accepted decisions and handoff, then re-observe mutable state.
3. Compare stored and current identity/permissions/candidate.
4. Show concise Status, blockers/decisions and invalidated claims.
5. Present exactly one safe Next action and optional Details.
6. Reauthorize/replan only if required; continue unaffected valid boundary.

**Outcome.** Correct current understanding and one safe continuation without re-planning the entire project.

**Failure/recovery.** Stale handoff cannot show READY; missing owner/identity becomes affected blocker; partial writes route to recovery view; no old authorization reuse.

**Acceptance.** A new agent/user can explain current state, evidence/limitations, authority and next action from sources.

## 9. J-005 — Review and decide

```yaml
primary_actor: product_owner_or_commander
canonical_status: ACCEPTED_JOURNEY
related_features: [FTR-011, FTR-012, FTR-013]
```

**Trigger.** Exact candidate and technical Evidence are ready for human assessment.

**Preconditions.** Candidate frozen; Evidence bound; authoring/validation provenance and limitations explicit.

**Primary flow.**

1. Show purpose and exact subject identity.
2. Show user-visible before/after and actual scope.
3. Map acceptance and negative criteria to Evidence.
4. Show `FAIL/BLOCKED/UNKNOWN/NOT_RUN`, deviations and remaining risk.
5. Provide decision options/effects without preselection.
6. Human issues exact `ACCEPT/NEEDS_CHANGES/REJECT/DEFER` record.
7. AOS verifies binding and shows one next route; no implicit delivery.

**Outcome.** Authentic, candidate-bound human verdict.

**Failure/recovery.** Stale/mutated subject, missing actor, generated decision or Evidence mismatch prevents valid decision. Bind new subject/review; do not patch during review.

**Acceptance.** Nontechnical user can decide without false certainty; decision scope/fact classes and exclusions are explicit.

## 10. J-006 — Protected delivery

```yaml
primary_actor: commander_or_authorized_maintainer
canonical_status: ACCEPTED_JOURNEY
related_features: [FTR-009, FTR-013, FTR-015, FTR-019, FTR-024]
```

**Trigger.** Accepted exact candidate is ready for one named Git/release action.

**Preconditions.** Current repository/branch/HEAD/worktree/remote and candidate identity are reverified; exact action permission exists.

**Primary flow.**

1. Select one action: Commit, Push, Merge or Release.
2. Show exact subject, current state, planned side effect and remaining unrelated state.
3. Human authorizes that action only.
4. Execute and verify actual local/remote result.
5. Report exact identity and stop.
6. If a later action is desired, repeat fresh boundary.

**Outcome.** One safely verified delivery action without unintended publication/promotion.

**Failure/recovery.** State drift, remote divergence, branch protection or partial remote effect stops chain; preserve result and request a new bounded decision.

**Acceptance.** No unrelated staging, no secret leakage, no implicit next action, exact result visible.

## 11. J-007 — Targeted reconstruction from reference

```yaml
primary_actor: domain_expert_or_product_builder
canonical_status: ACCEPTED_JOURNEY
related_features: [FTR-002, FTR-005, FTR-022, FTR-025]
```

**Trigger.** Selected feature/architecture has an exact knowledge gap that current owners cannot answer.

**Preconditions.** Narrow question, target feature, read-only repository/ref/commit/path boundary and stop conditions are explicit.

**Primary flow.**

1. Frame one exact research question.
2. Pin reference snapshot and relevant paths.
3. Inspect user docs/commands → contracts/schemas → tests/negative fixtures → implementation → reports.
4. Classify observed behavior, useful contracts/negatives, obsolete complexity and limitations.
5. Update only the relevant DRAFT finding/Passport under separate edit authority.
6. Human decides whether any finding becomes target requirement/design.

**Outcome.** Evidence-backed answer to the gap without legacy status/topology transfer.

**Failure/recovery.** Unavailable source remains `BLOCKED_REFERENCE_ACCESS/NOT_RUN`; broadening to “understand everything” stops; reference instruction has no authority.

**Acceptance.** Exact provenance and rejected complexity recorded; question answered or explicit unknown preserved; no reference mutation.

## 12. Proposed supporting journeys — `PROPOSAL`

These are decompositions of accepted journeys, not new accepted product scope.

### SJ-001 — First-Start and onboarding

Connects FTR-004/FTR-008 to J-001: verify environment/package, show ownership-safe preview, complete explicit install, verify, then offer one first action—start an Intent Record. Must remain usable without SaaS/account.

### SJ-002 — Failure and recovery

Connects FTR-014 to J-003/J-004: show actual partial state, invalidated claims, safe options and one next action. Destructive rollback has no default.

### SJ-003 — Incident to lesson

Connects FTR-025 to operations: record event/Evidence, propose bounded cause/lesson/regression, human review, monitor recurrence. Incident never auto-mutates policy.

### SJ-004 — Optional capability admission

Connects FTR-017/018/020/026/028: measure need, compare simpler alternative, define contract/permissions/fallback, pilot, human admit/defer/reject, then monitor/removal.

## 13. Information architecture — `PROPOSAL`

```text
Project
├─ Status
│  ├─ current outcome and exact subject
│  ├─ technical result / human decision / permission
│  └─ freshness and blockers
├─ Next
│  └─ one recommended action and required authority
├─ Product
│  ├─ Intent Records
│  ├─ Product Spec
│  ├─ Feature Passports
│  └─ Decisions / ADRs
├─ Work
│  ├─ Task Brief / Preview
│  ├─ Execution Record
│  └─ Recovery / Handoff
├─ Review
│  ├─ Candidate
│  ├─ Evidence / Findings / NOT_RUN
│  └─ Human Decision
└─ Details
   ├─ Sources / ownership / identities
   ├─ history / lessons / reference findings
   └─ optional raw technical output
```

This topology is interface-neutral and does not imply database or screen implementation.

## 14. Conceptual action vocabulary — `PROPOSAL`

| User action | Meaning | Must not imply |
|---|---|---|
| `start / describe` | create/revise Intent Record | implementation |
| `status` | refresh and explain current state | lifecycle mutation |
| `next` | show one recommended safe action | authorization |
| `details` | inspect sources/Evidence/history | acceptance |
| `review` | open exact review subject | correction |
| `decide` | create exact human record after explicit choice | broad authority |
| `preview` | show exact proposed mutation | apply |
| `authorize` | issue bounded protected permission | Git delivery unless explicitly named |
| `resume` | rebind and continue exact valid boundary | stale permission reuse |
| `deliver` | choose one Git/release action | automatic chain |

Actual commands/buttons remain an open interface decision.

## 15. Content design

### Plain-language status template

```text
Сейчас: <human-readable state/outcome>
Предмет: <exact candidate/revision>
Известно: <technical facts>
Решение человека: <value or NOT_RUN>
Ограничения: <material UNKNOWN/NOT_RUN>
Разрешение: <allowed/blocked and why>
Дальше: <one action>
```

### Finding template

```text
Что обнаружено
Почему это важно
Что затронуто и что не затронуто
Какие Evidence/источники это подтверждают
Какое решение или исправление требуется
```

### Decision template

```text
Exact subject and identity
Question
Options and trade-offs
Recommendation labelled PROPOSAL
Selected option: empty until human action
Effect and exclusions
```

## 16. Accessibility and localization requirements — `SYNTHESIZED_DRAFT`

- Status meaning is conveyed by text/icon/structure, not color alone.
- Keyboard/non-pointer flow and screen-reader semantics are required for a visual interface.
- Destructive/protected action labels name the exact side effect.
- Technical identifiers remain copyable; explanations remain plain-language.
- RU/EN terms preserve semantics; translation/adapters cannot change status or authority.
- Long Evidence is collapsible/searchable while summary retains limitations.
- Timestamps/identities include enough context to avoid stale-record confusion.
- Error focus lands on the exact unresolved field/decision, not a generic page.

## 17. UX failure patterns to reject

- one green badge combining PASS, accepted and authorized;
- “Continue” that hides Commit/Push/Merge/Release effect;
- dashboard state not linked to owners/freshness;
- default-selected human acceptance;
- chat response treated as decision without exact binding;
- modal dismiss that loses unresolved finding;
- recovery action that silently deletes partial/user state;
- multiple competing “recommended next” actions;
- hidden `NOT_RUN` under a generic success summary;
- stale/offline UI allowed to perform protected action;
- absolute local links or tool-specific-only navigation;
- Governance jargon before user problem/outcome.

## 18. UX measurement candidates — `PROPOSAL`

- first-time Intent confirmation completion and correction rate;
- questions asked vs questions changing outcome/scope;
- user ability to explain current state/authority/next action;
- time to find Evidence for a criterion;
- decision reversals caused by hidden limitation;
- resume success without re-planning;
- protected-action cancellation/error rate;
- accessibility task completion;
- difference between chat/CLI/UI surfaces after core contracts stabilize.

No target thresholds or primary interface are selected.

## 19. UX review checklist

- Does J-001 visibly complete the accepted FTR-001 first slice?
- Are all canonical journeys represented without inventing acceptance?
- Can a nontechnical user distinguish result, decision and permission?
- Are original input, assumptions, unknowns and provenance visible?
- Does every failure view preserve actual state and safe recovery?
- Can any click/message accidentally become broad approval?
- Is one next action consistently available without hiding alternatives?
- Are interface-specific choices still open?
- Are accessibility/localization semantics explicit but implementation-neutral?
