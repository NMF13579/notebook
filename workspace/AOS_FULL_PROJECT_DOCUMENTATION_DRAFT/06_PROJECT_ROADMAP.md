---
package: AOS_FULL_PROJECT_DOCUMENTATION_DRAFT
package_revision: DRAFT-R1
artifact_role: PROJECT_ROADMAP_PROPOSAL
status: DRAFT
authority: NONE
roadmap_status: PROPOSAL
feature_disposition_effect: NONE
implementation_authorization: NONE
git_authorization: NONE
---

# 06 — Project Roadmap

## 1. Роль и authority boundary

Это decision-ready предложение о последовательности будущего AOS. Оно следует accepted strategy “Product definition → first Product Runtime slice → manual real-task cycles → stable core → justified automation → progressive Governance → optional scale”.

Roadmap placement:

- не меняет `human_disposition`;
- не принимает feature/architecture;
- не выбирает implementation repository/toolchain;
- не является estimate, schedule, Task Brief или Execution Authorization;
- не запускает Git/release.

The only exact accepted runtime sequencing decision is: **first Product Runtime vertical slice = FTR-001 request → reviewable, human-confirmed Intent Record**.

## 2. Planning principles

1. Vertical user outcome before platform components.
2. Product Runtime value before broad Development Factory automation.
3. Manual repeatable cycle before runtime enforcement/routing/RAG/UI.
4. Every phase has entry/exit Evidence and human gate.
5. Deferred features remain optional until admitted by exact decision.
6. Architecture decisions are made only when a dependent phase needs them.
7. No dates or velocity claims before implementation repository/team/toolchain decisions.
8. A failed/blocked phase does not authorize adjacent scope.
9. Documentation acceptance and implementation authorization are separate.
10. Git delivery is separately authorized for each exact action.

## 3. Roadmap overview

| Phase | Outcome | Feature placement | Status |
|---|---|---|---|
| `D0` | Full project documentation reviewed and decisions isolated | all FTRs as design subject | current DRAFT authoring outcome |
| `R0` | Implementation foundation chosen and first task made executable | no product feature admission | proposal; blocked on human decisions |
| `R1` | Human request becomes confirmed Intent Record | FTR-001 + minimum supporting semantics | first slice accepted; implementation NOT_RUN |
| `R2` | Confirmed intent becomes coherent Product Spec/Passport | FTR-003, support FTR-005 | proposal after R1 learning |
| `R3` | Existing/current project can be understood and resumed | FTR-002, FTR-008, FTR-016 | proposal |
| `R4` | One bounded repository change can be safely executed/recovered | FTR-006, 009, 010, 014, 019 | proposal |
| `R5` | Candidate can be frozen, validated, reviewed and decided | FTR-011, 012, 013 | proposal/supporting controls |
| `R6` | Install/update and Git closure are explicit/recoverable | FTR-004, 015 | proposal |
| `R7` | Repeat work generates patterns, incidents and measured quality automation | FTR-022, 025; conditional 021, 023, 030 | proposal |
| `R8` | Larger work and release lifecycle become manageable | FTR-007, 024 | deferred proposal |
| `R9` | Optional search/routing/governance/extensions/UI/domain scale | FTR-017, 018, 020, 026–029 | deferred proposal |

## 4. D0 — Documentation review and decision foundation

**Goal.** Make the full future project reviewable before implementation planning.

**Inputs.** Canonical seven-doc baseline, frozen AOS three-file foundation, accepted X1 package/decisions, all 30 feature dossiers and current human instruction.

**Outputs.** This exact full DRAFT package, decision register, traceability, candidate manifest and review findings.

**Entry.** Documentation-only scope authorized; current owners/source identities bound.

**Exit criteria.**

- all package artifacts exist and cross-link;
- every feature has full design-level coverage;
- accepted decisions are preserved without widening;
- roadmap/proposals/unknowns are visibly classified;
- construction checks pass;
- exact candidate is ready for human review.

**Human gate.** `ACCEPT | NEEDS_CHANGES | REJECT | DEFER` exact DRAFT; select only decisions required for next phase. Package acceptance does not authorize R0/R1.

## 5. R0 — Implementation foundation decisions

**Goal.** Establish a safe future implementation subject without implementing product behavior yet.

**Required human decisions.**

- implementation repository and repository role;
- compatibility relationship (greenfield default vs specific legacy target);
- initial interaction surface;
- language/toolchain/dependency policy;
- persistence/authenticity boundary required by R1;
- provider/privacy/data boundary;
- acceptance and Git/release conventions for implementation repo.

**Possible outputs after separate planning/authorization.** Repository scaffold, minimal contract/test/logging foundation and implementation roadmap—but none is authorized by this document.

**Exit Evidence.** Exact accepted ADRs/Product/Feature contracts; bound repository; focused build/test/dev loop; no product-success claim.

**Stop conditions.** Repository remains `UNASSIGNED`; material decisions conflict; task would mutate this knowledge repository role; implementation authority absent.

## 6. R1 — First Product Runtime slice: Intent

```yaml
primary_feature: FTR-001
human_selection: ACCEPTED_X1_DR_002_A
supporting_semantics:
  - C-001 Intent Record
  - authority/status separation
  - exact revision and human confirmation
  - minimal sensitive-content boundary
```

**User outcome.** A person submits a request, sees preserved original input and structured problem/outcome/assumptions/unknowns, corrects it and confirms an exact Intent Record.

**Not required.** Product Registry, FTR-003 runtime, full Factory, RAG, routing, SaaS, Git delivery or autonomous execution.

**Candidate increment.** One surface, one Intent revision mechanism, one exact human-confirmation record and focused negative cases.

**Entry.** Accepted FTR-001 behavior; exact R0 decisions/repository; Task Brief and authorization for implementation.

**Exit criteria.**

- original and synthesis distinguishable;
- material questions/unknowns visible;
- states `RECEIVED/CLARIFYING/REVIEWABLE/CONFIRMED/DEFERRED` behave as accepted;
- prompt injection, empty input, solution conflation and sensitive-boundary negatives pass;
- user completes manual first-contact journey;
- exact human confirmation cannot be simulated;
- Evidence and human acceptance obtained separately.

**Learning questions.** Does the user understand problem/outcome and authority? What is a material question? Which interface/persistence/authenticity choices create friction?

## 7. R2 — Product definition and Feature Passport

```yaml
primary_feature: FTR-003
supporting_control: FTR-005
ownership_rule: X1-DR-001_A_ACCEPTED
```

**User outcome.** A confirmed Intent becomes a coherent Product Spec and complete feature-specific Passport; distinct future slices can be compared without automatic selection.

**Entry.** R1 accepted manual outcome and learning; accepted Product/Feature contracts for the chosen increment; any material ADR resolved.

**Exit criteria.**

- Product Spec owns cross-feature facts and Passport links without drift;
- selected feature has full C-002 fields;
- dependencies/unknowns and slice trade-offs visible;
- exact revision and human product decision recorded;
- no recommendation becomes disposition/priority automatically.

**Learning questions.** How much structure helps vs burdens users? Is a Product Feature Registry needed yet? Which acceptance presentation works?

## 8. R3 — Discovery, status and continuity

```yaml
candidate_features: [FTR-002, FTR-008, FTR-016]
optional_only_after_measurement: FTR-017
```

**User outcomes.** Existing project can be mapped read-only; returning user sees trustworthy Status and one Next; new agent receives minimal source-linked context.

**Entry.** At least one real repository/use case and R1/R2 continuity friction measured. Human admits exact feature subset; dispositions updated separately if chosen.

**Exit criteria.**

- repository snapshot/map reproducible and zero-write;
- status projection detects staleness and does not own truth;
- handoff/resume works after session/tool switch;
- user explains blocker/permission/next action;
- direct search baseline measured before any RAG decision.

**Deferral rule.** FTR-017 stays deferred unless search/context benchmark shows material benefit.

## 9. R4 — Bounded execution and recovery

```yaml
candidate_features: [FTR-006, FTR-009, FTR-010, FTR-014, FTR-019]
recommendation: smallest_manual_safe_cycle
```

**User outcome.** One accepted feature task can change only exact authorized scope, stop truthfully and recover from interruption.

**Entry.** Selected implementation repository and feature contract; exact Risk Profile/human authority model; recovery requirements.

**Exit criteria.**

- Task Brief/auth/preview/actual diff agree;
- scope/path/trust classifier blocks forbidden cases;
- authorization is exact, closed-by-default and consumed once;
- executor performs one stage and reports actual changes;
- unexpected/partial mutation stops and produces safe recovery;
- no validation/commit/push follows implicitly.

**Simplification.** Implement minimum runner semantics; no full Control Plane, distributed jobs or autonomous self-heal.

## 10. R5 — Validation, Evidence, review and human decision

```yaml
candidate_features: [FTR-011, FTR-012, FTR-013]
current_X1_disposition: SUPPORTING_CONTROL_ONLY
```

**User outcome.** Exact candidate can be independently checked and understood, and the human can issue an authentic verdict.

**Entry.** R4 produces exact candidates and acceptance/negative criteria; validator independence need defined.

**Exit criteria.**

- deterministic candidate freeze detects every included byte change;
- one official result contract preserves `NOT_RUN` and limitations;
- validation is read-only and correction separate;
- review maps Evidence to user-visible criteria;
- generated/stale human decision is rejected;
- changed candidate invalidates old result/decision.

**Learning questions.** Which checks are truly required? How much Evidence is understandable? What authenticity mechanism is sufficient?

## 11. R6 — Installation and delivery closure

```yaml
candidate_features: [FTR-004, FTR-015]
later_release_helper: FTR-024
```

**User outcomes.** AOS can be installed/updated without losing state; accepted candidate can be committed/pushed/merged only through independent choices.

**Entry.** Actual packaging/distribution and Git hosting model selected; ownership/recovery policies accepted.

**Exit criteria.**

- dry-run zero-write and apply bound to preview;
- update/uninstall preserve ownership and recover from interruption;
- First-Start leads to R1 journey;
- Commit/Push/Merge permissions independent and state-reverified;
- no automatic release.

FTR-024 remains later until an actual distribution/release target exists.

## 12. R7 — Learning and measured quality automation

```yaml
core_candidates: [FTR-022, FTR-025]
conditional_candidates: [FTR-021, FTR-023, FTR-030]
```

**User outcome.** Repeated work/incident knowledge becomes reusable, and proven checks catch drift/regressions without creating authority.

**Entry.** Multiple manual cycles and incidents provide real Evidence; stable contracts/representations exist.

**Exit criteria.**

- incident→lesson proposal→human acceptance→regression trace works;
- pattern fit/anti-fit retains provenance/trade-offs;
- drift/CI/strict tooling admitted only for observed defects;
- CI PASS remains technical Evidence only;
- old parser/tool removed only after migration Evidence.

## 13. R8 — Larger work and release lifecycle

```yaml
candidate_features: [FTR-007, FTR-024]
default: DEFER
```

**Admission signals.** Repeated multi-task outcomes need hierarchy/queue; real merged artifacts and distribution target need version/release/rollback process.

**Exit criteria.** Lazy decomposition avoids speculative backlog; human selects one active task; release package exact and separately authorized; rollback/post-release check proven.

No general portfolio system, auto-scheduler or deployment platform by default.

## 14. R9 — Optional scale and ecosystem

| Capability | Feature | Admission Evidence | Default |
|---|---|---|---|
| RAG-light retrieval | FTR-017 | direct-search benchmark insufficient | DEFER |
| Model/provider routing | FTR-018 | task benchmarks + privacy/cost policy | DEFER |
| Runtime enforcement | FTR-020 | stable rules + repeated incidents + false-positive budget | DEFER |
| Plugin/extensions | FTR-026 | repeated stable extension points | DEFER |
| Domain modules | FTR-027 | exact domain job + specialist/data/compliance decision | DEFER |
| Workbench/SaaS | FTR-028 | measured interface/collaboration friction | DEFER |
| Export/localization | FTR-029 | concrete multi-tool/repo/locale consumers | DEFER |

Each is separately selectable, removable and isolated. None may become a prerequisite for core R1–R6 unless a new human decision changes the roadmap.

## 15. Cross-phase gates

### Product gate

Exact human-accepted Product/Feature behavior for the increment; user-visible outcome and non-goals clear.

### Architecture gate

Material non-reversible ownership/security/dependency choices resolved; reversible HOW left to implementation.

### Implementation gate

Repository bound; Task Brief/authorization exact; acceptance/negative/recovery plan sufficient.

### Validation gate

Exact candidate, required checks, Evidence and independence limitation known; no mutation in validate.

### Human gate

Exact review subject and explicit `ACCEPT/NEEDS_CHANGES/REJECT/DEFER`; scope/fact classes/effect recorded.

### Delivery gate

One named Commit/Push/Merge/Release action, fresh repo/remote facts and separate permission.

## 16. Feature coverage by proposed phase

| Feature | Proposed earliest phase | Rationale | Disposition remains |
|---|---:|---|---|
| FTR-001 | R1 | accepted first user-visible slice | SELECT_FOR_X1 |
| FTR-002 | R3 | discovery after exact repository/use case | UNDECIDED |
| FTR-003 | R2 | product definition after intent learning | SELECT_FOR_X1 |
| FTR-004 | R6 | packaging/ownership decisions required | UNDECIDED |
| FTR-005 | R2 support | ADR only for material choice | SUPPORTING_CONTROL_ONLY |
| FTR-006 | R4 | runtime boundary, not first product value | SUPPORTING_CONTROL_ONLY |
| FTR-007 | R8 | defer speculative backlog | UNDECIDED |
| FTR-008 | R3 | status/resume after real states exist | UNDECIDED |
| FTR-009 | R4 | required before protected repository mutation | UNDECIDED |
| FTR-010 | R4 | minimum scoped executor only | UNDECIDED |
| FTR-011 | R5 | exact candidate/check profiles needed | SUPPORTING_CONTROL_ONLY |
| FTR-012 | R5 | Evidence/review after candidate exists | SUPPORTING_CONTROL_ONLY |
| FTR-013 | R5 | freeze before independent validation | SUPPORTING_CONTROL_ONLY |
| FTR-014 | R4 | recovery designed with first writes | UNDECIDED |
| FTR-015 | R6 | delivery after accepted real candidate | UNDECIDED |
| FTR-016 | R3 | continuity after multiple sessions | UNDECIDED |
| FTR-017 | R9 | only after search measurement | UNDECIDED |
| FTR-018 | R9 | only after provider benchmarks/policy | UNDECIDED |
| FTR-019 | R4 | minimal action boundary with writes | UNDECIDED |
| FTR-020 | R9 | only after stable repeated incidents | UNDECIDED |
| FTR-021 | R7 conditional | representations/drift must first exist | UNDECIDED |
| FTR-022 | R7 | patterns after repeated cases | UNDECIDED |
| FTR-023 | R7 conditional | CI after runtime/toolchain/contracts | UNDECIDED |
| FTR-024 | R8 | actual release target required | UNDECIDED |
| FTR-025 | R7 | incidents/lessons after real cycles | UNDECIDED |
| FTR-026 | R9 | stable extension points required | UNDECIDED |
| FTR-027 | R9 | separate domain/specialist decisions | UNDECIDED |
| FTR-028 | R9 | UI after measured core UX friction | UNDECIDED |
| FTR-029 | R9 | concrete portability consumers required | UNDECIDED |
| FTR-030 | R7 conditional | strict tools after real representations | UNDECIDED |

## 17. Decision and research timing

Resolve decisions just before the first dependent phase, not all upfront:

| Before | Required decision/research class |
|---|---|
| R0/R1 | implementation repo, interface, toolchain, Intent persistence/authenticity, provider/privacy |
| R2 | product review format, Registry need, any material Product/Passport compatibility rule |
| R3 | existing-project discovery boundary, memory retention/privacy, search benchmark |
| R4 | Risk Profile vocabulary, permission/action taxonomy, recovery and sandbox boundary |
| R5 | validator independence, Evidence retention and decision authenticity |
| R6 | install ownership/distribution and Git hosting/branch model |
| R7 | incident retention, CI/drift/tooling admission based on Evidence |
| R8 | backlog scale and release/version/rollback model |
| R9 | each optional capability’s specific product/architecture/data decision |

Targeted reference research is commissioned only for exact gaps after current owners cannot answer them.

## 18. Roadmap success and stop rules

A phase is complete only when its user outcome, accepted contracts, technical Evidence, human verdict and recoverable handoff are all explicit. It is not complete because files/code/tests exist.

Stop the affected phase for:

- missing human-only product/architecture/repository decision;
- scope/disposition expansion;
- authoritative conflict;
- candidate/authorization identity mismatch;
- unavailable required validation;
- unsafe data/provider/destructive boundary;
- attempt to implement in the knowledge repository without role change;
- implied Git/release action.

Continue safe independent read-only/documentation work when no material dependency exists.

## 19. Roadmap review decisions

Human review should decide, in order:

1. Whether the phase sequence is directionally acceptable as a proposal.
2. Whether any non-X1 feature should receive an item-level disposition now.
3. Which exact decisions are required before R0/R1 planning.
4. Whether any optional capability is wrongly early/late or missing a dependency.
5. Whether implementation planning should be authorized as a separate next task.

No selection is recorded by this roadmap itself. Exact prompts are in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).
