---
package: AOS_FULL_PROJECT_DOCUMENTATION_DRAFT
package_revision: DRAFT-R1
artifact_role: DECISION_REGISTER_AND_REQUESTS
status: DRAFT
authority: NONE
selected_open_options: NONE
implementation_authorization: NONE
git_authorization: NONE
---

# 07 — Decision Register

## 1. Роль и decision semantics

Документ разделяет уже принятые решения, current safe states и открытые human-only decisions. Он предлагает варианты и recommendations, но не выбирает их.

```text
recommendation = PROPOSAL
empty selected_option = no decision
package ACCEPT ≠ acceptance of every proposed option
documentation acceptance ≠ implementation/Git authority
```

Any valid decision must bind exact subject/revision, selected option, actor/source, effect/fact classes and exclusions. Human may also choose `DEFER`.

## 2. Accepted decision ledger

| ID | Decision | Exact source/status | Effect |
|---|---|---|---|
| `ADR-AOS-001` | Working project name is AOS | current human-confirmed direction in `docs/00_Core.md` | project identity label |
| `ADR-AOS-002` | `docs/00…06` are active canonical owner set | human-accepted baseline | owner routing; no parallel canonical catalogs |
| `ADR-AOS-003` | AOS-FARM, AgentOS, AOS-02 and other legacy are reference-only | human-accepted baseline | target authority `NONE`; targeted research only |
| `ADR-AOS-004` | Global three-file design foundation is frozen exact subject | `AOS/GLOBAL_DESIGN_FREEZE.md`, manifest `b9ef…aebf` | no unreviewed mutation/publication |
| `ADR-AOS-005` | FTR-001 and FTR-003 are `SELECT_FOR_X1` | `docs/06_Features.md` + accepted X1 record | dispositions preserved |
| `ADR-AOS-006` | FTR-005/006/011/012/013 are `SUPPORTING_CONTROL_ONLY` for X1 | accepted feature inventory/X1 | not independent X1 product subjects |
| `ADR-AOS-007` | Product Spec owns cross-feature product facts; Passports own feature behavior and link to Product Spec | accepted `X1-DR-001: A` | C-003↔C-002 ownership relation |
| `ADR-AOS-008` | First Product Runtime slice is FTR-001 request→reviewable human-confirmed Intent Record | accepted `X1-DR-002: A` | first slice behavior selected |
| `ADR-AOS-009` | Implementation repository remains `UNASSIGNED` | current safe canonical state | blocks implementation planning/execution against a target repo |
| `ADR-AOS-010` | Current task produces a full documentation DRAFT followed by human review/changes/decisions | current explicit human instruction | authoring scope only; no product acceptance |

The exact X1 decision record is [workspace/AOS_DOCUMENTATION_X1/HUMAN_DECISION_RECORD.yaml](../AOS_DOCUMENTATION_X1/HUMAN_DECISION_RECORD.yaml), SHA-256 `3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197`.

## 3. Current safe states, not permanent choices

| State | Current value | Meaning |
|---|---|---|
| Implementation repository | `UNASSIGNED` | no target for runtime planning/execution |
| Implementation authorization | `NONE` | no code/scaffold/test/runtime mutation |
| Git authorization | `NONE` | no Commit/Push/Merge/Release in this run |
| Non-X1 feature dispositions | mostly `UNDECIDED` | roadmap proposals do not change them |
| Exact interface/toolchain/persistence | `UNKNOWN` | not silently selected by architecture prose |
| Canonical publication of X1/full DRAFT | `NOT_RUN` | accepted X1 facts remain scoped; this package remains DRAFT |

## 4. Decision ordering

### Review now

1. `DR-FULL-001` — disposition of exact full documentation candidate.
2. `DR-FULL-002` — directional roadmap acceptance as a proposal.
3. Any exact content corrections or feature behavior objections.

### Required before R0/R1 implementation planning

`DR-PROD-001`, `DR-ARCH-001…006`, `DR-POL-001` and a separate instruction authorizing implementation planning.

### Defer until evidence/dependent phase

Registry, broad metrics, Governance enforcement, RAG, routing, plugins, SaaS, domains and release choices.

## 5. Immediate documentation decisions

## DR-FULL-001 — Exact full DRAFT disposition

```yaml
classification: DOCUMENTATION_PACKAGE_DECISION
selected_option: null
required_now: true
subject_binding: EXTERNAL_CANDIDATE_MANIFEST_PATH
subject_manifest_path: workspace/AOS_FULL_PROJECT_DOCUMENTATION_DRAFT/CANDIDATE_MANIFEST.txt
```

**Question.** Is the exact full documentation package acceptable as the basis for bounded revisions and later canonical/audit decisions?

| Option | Effect |
|---|---|
| `ACCEPT` | accepts only explicitly declared package fact classes; does not publish or authorize implementation |
| `NEEDS_CHANGES` | creates bounded correction scope from exact findings/decisions; new candidate/audit required |
| `REJECT` | rejects exact candidate without changing canonical owners |
| `DEFER` | preserves candidate for later review |

**Recommendation:** review by document order, decide content/roadmap/open choices explicitly, then request separate read-only audit of the corrected/final exact candidate.

## DR-FULL-002 — Roadmap direction

```yaml
classification: PRODUCT_SEQUENCE_PROPOSAL
selected_option: null
required_now: false
```

**Question.** Should `D0 → R0 → R1 Intent → R2 Product Definition → R3 Continuity → R4 Execution → R5 Review → R6 Delivery → later learning/extensions` be retained as the planning baseline?

| Option | Trade-off |
|---|---|
| `A` — retain sequence | product-first, smallest accepted slice, automation later; slower arrival of broad platform features |
| `B` — combine R1+R2 | richer definition flow earlier; larger first implementation boundary and more decisions |
| `C` — custom order | can match concrete project need; requires exact dependency/risk rationale |
| `DEFER` | no implementation sequence beyond accepted FTR-001 is selected |

**Recommendation:** `PROPOSAL: A`. It matches accepted strategic sequencing and X1 first slice.

## 6. Product decisions

## DR-PROD-001 — First concrete user segment/job

```yaml
classification: MATERIAL_PRODUCT_DECISION
selected_option: null
required_before: R1_IMPLEMENTATION_PRODUCT_ACCEPTANCE
```

**Question.** Which concrete user/job supplies the first manual dogfood context for FTR-001?

| Option | Benefit | Risk |
|---|---|---|
| `A` — domain expert/product owner starting a small software project | closest to core promise; tests plain-language intake | may need an available real user/problem |
| `B` — vibe-coder starting own project | easy internal dogfood; rich repository context | may under-test nontechnical comprehension |
| `C` — existing-project maintainer | immediate real context | mixes FTR-001 with discovery/resume dependencies |

**Recommendation:** `PROPOSAL: A`, with one real bounded problem and a secondary vibe-coder usability check. Exact user/research ethics/data boundary remain required.

## DR-PROD-002 — Product Feature Registry timing

```yaml
classification: PRODUCT_ARCHITECTURE_DECISION
selected_option: null
required_before: MULTIPLE_ACCEPTED_PASSPORTS_NEED_INDEX
```

| Option | Trade-off |
|---|---|
| `A` — defer; use direct Passport links | minimum complexity; manual navigation |
| `B` — derived file index after R2 | easier navigation; drift check required |
| `C` — runtime registry | richer query/state; premature authority/drift risk |

**Recommendation:** `PROPOSAL: A`, then B only after multiple accepted Passports. Registry remains derived and never owns behavior.

## DR-PROD-003 — Scenario/access/UX modeling timing

```yaml
classification: PRODUCT_PROCESS_DECISION
selected_option: null
required_before: MULTI_ACTOR_OR_ACCESS_SENSITIVE_FEATURE
```

| Option | Trade-off |
|---|---|
| `A` — conditional only for access-sensitive/multi-actor journeys | proportional and aligned with progressive depth | needs a clear trigger review |
| `B` — mandatory for every feature | consistency | heavy ceremony and delay |
| `C` — defer entirely | smallest documentation | may miss material access/UX contracts |

**Recommendation:** `PROPOSAL: A`.

## DR-PROD-004 — Success metrics and targets

```yaml
classification: PRODUCT_MEASUREMENT_DECISION
selected_option: null
required_before: R1_DOGFOOD
```

**Options.**

- `A`: minimal R1 set—completion/correction count, material-question count, user comprehension, time to confirmed intent, authority-confusion incidents.
- `B`: broad full-program dashboard from the start.
- `C`: qualitative notes only.

**Recommendation:** `PROPOSAL: A`; add scope drift/resume/review metrics when corresponding phases exist. Numeric targets follow baseline measurement.

## DR-PROD-005 — Non-X1 feature admission/dispositions

```yaml
classification: ITEM_SCOPED_HUMAN_DECISIONS
selected_option: null
required_before: EACH_DEPENDENT_PHASE
```

**Question.** Which features beyond accepted X1 are admitted, and with what disposition?

**Recommended batching — proposal only:**

| Batch | Candidate features | Recommended timing |
|---|---|---|
| `B1` | FTR-001 | already selected first slice |
| `B2` | FTR-003 | after R1 evidence; already selected for X1 documentation |
| `B3` | FTR-002/008/016 | select individually when discovery/resume need is observed |
| `B4` | FTR-006/009/010/014/019 | select exact minimum for first protected repository mutation |
| `B5` | FTR-011/012/013 | preserve supporting-control role until runtime product admission is explicitly needed |
| `B6` | FTR-004/015 | after packaging/delivery targets exist |
| `B7` | FTR-022/025; conditional 021/023/030 | after real cycles/incidents/representations |
| `B8` | FTR-007/024 | defer until scale/release evidence |
| `B9` | FTR-017/018/020/026–029 | defer; admit separately by measured trigger |

Each feature receives its own exact human disposition; accepting the batch table as roadmap guidance does not mutate inventory.

## 7. Architecture and implementation-boundary decisions

## DR-ARCH-001 — Implementation repository

```yaml
classification: PROTECTED_REPOSITORY_ROLE_DECISION
selected_option: null
required_before: IMPLEMENTATION_PLANNING
```

| Option | Trade-off |
|---|---|
| `A` — new dedicated greenfield repository | preserves knowledge repo role; clean target; explicit history | requires creation/naming/access decision |
| `B` — selected existing repository | may reuse setup | compatibility/contamination/ownership must be proven |
| `C` — change this notebook repository role | co-location | conflicts with current accepted role and raises high migration risk |

**Recommendation:** `PROPOSAL: A`. Exact repository name/owner/visibility/default branch and Git authority require a separate instruction.

## DR-ARCH-002 — Compatibility relationship

```yaml
classification: MATERIAL_ARCHITECTURE_DECISION
selected_option: null
required_before: IMPLEMENTATION_ARCHITECTURE
```

| Option | Trade-off |
|---|---|
| `A` — greenfield semantics; no legacy runtime compatibility by default | smallest/cleanest target | migrations/adapters later if real consumers appear |
| `B` — compatibility with one pinned legacy contract | easier transition for known consumer | imports constraints and test burden |
| `C` — broad backward compatibility | maximum reuse claim | contradicts smaller greenfield direction without evidence |

**Recommendation:** `PROPOSAL: A`; targeted adapters only after exact need and decision.

## DR-ARCH-003 — Initial interaction surface

```yaml
classification: PRODUCT_ARCHITECTURE_DECISION
selected_option: null
required_before: R1_IMPLEMENTATION
```

| Option | Trade-off |
|---|---|
| `A` — conversational intake with a minimal local exact-record interface | closest to user language; small R1 value | requires clear record/identity boundary |
| `B` — CLI-first | deterministic and developer-friendly | weaker nontechnical first-contact UX |
| `C` — local visual UI first | accessible presentation | larger implementation/auth/state surface |
| `D` — SaaS first | collaboration potential | hosting/auth/privacy/platform scope too early |

**Recommendation:** `PROPOSAL: A`; exact carrier may be chat or local form, while repository/protected actions can use later explicit CLI/adapter. No SaaS prerequisite.

## DR-ARCH-004 — Intent/Project Memory persistence

```yaml
classification: MATERIAL_ARCHITECTURE_DECISION
selected_option: null
required_before: R1_STATEFUL_CONFIRMATION
```

| Option | Trade-off |
|---|---|
| `A` — local human-readable revisioned records with exact digests | inspectable/portable/simple | concurrency/query limits; ownership/location decision needed |
| `B` — local database/service | stronger transactions/query | more implementation complexity and opaque state |
| `C` — hosted service | cross-device/collaboration | auth/privacy/network/platform burden |

**Recommendation:** `PROPOSAL: A` for R1, provided user/project ownership, atomicity and sensitive-data policy are explicitly designed. Promote only on measured need.

## DR-ARCH-005 — Language/toolchain/dependency policy

```yaml
classification: IMPLEMENTATION_ARCHITECTURE_DECISION
selected_option: null
required_before: IMPLEMENTATION_TASK_BRIEF
```

**Options.** Select after repository/interface/platform constraints using a decision matrix for portability, strict data validation, testability, packaging, maintainability, ecosystem and team familiarity; avoid selecting from legacy presence.

**Recommendation:** `PROPOSAL: bounded evaluation in implementation planning`, one primary ecosystem and minimal dependencies for R1. This DRAFT intentionally does not name a winner without current constraints/research.

## DR-ARCH-006 — Exact runtime/factory boundary

```yaml
classification: MATERIAL_ARCHITECTURE_DECISION
selected_option: null
required_before: R4_IMPLEMENTATION
```

| Option | Trade-off |
|---|---|
| `A` — Product Runtime owns user artifacts/views; thin Factory owns protected repository work | clear value/control split | explicit adapters/contracts needed |
| `B` — single combined runtime initially | fewer components | boundary may blur and controls become product state |
| `C` — separate service/process boundary | strong isolation | premature deployment/ops complexity |

**Recommendation:** `PROPOSAL: A` semantically; implementation may remain one deployable until measured isolation need.

## 8. Authority, safety and policy decisions

## DR-POL-001 — Human decision authenticity

```yaml
classification: PROTECTED_AUTHORITY_DECISION
selected_option: null
required_before: R1_CONFIRMED_RUNTIME_STATE
```

| Option | Trade-off |
|---|---|
| `A` — exact raw decision record bound to subject plus trusted active-session actor/source | minimal local slice, reproducible | session identity/trust assumptions must be explicit |
| `B` — cryptographic user signature | stronger portable authenticity | key management and UX complexity |
| `C` — authenticated hosted account record | collaboration/audit | service/auth/privacy dependency |

**Recommendation:** `PROPOSAL: A` for local R1, designed for later stronger mechanism. Generated decisions, unverifiable actor and stale subject remain invalid.

## DR-POL-002 — Provider/privacy/data policy

```yaml
classification: SENSITIVE_DATA_DECISION
selected_option: null
required_before: EXTERNAL_PROVIDER_OR_SENSITIVE_INPUT
```

| Option | Trade-off |
|---|---|
| `A` — local/same-boundary processing by default; external transmission explicit opt-in per policy | safest default and clear trust | may limit model capability/convenience |
| `B` — approved provider allowlist by data class | scalable policy | requires classification/audit/maintenance |
| `C` — user-selected provider per task without baseline policy | flexible | inconsistent privacy and consent risk |

**Recommendation:** `PROPOSAL: A`, evolving to B after concrete providers/data classes are selected.

## DR-POL-003 — Risk Profile vocabulary

```yaml
classification: HUMAN_AUTHORITY_MODEL_DECISION
selected_option: null
required_before: FIRST_PROTECTED_EXECUTION
```

| Option | Trade-off |
|---|---|
| `A` — four levels `LOW/MEDIUM/HIGH/CRITICAL` with objective risk factors and human assignment | understandable/proportional | thresholds need dogfood calibration |
| `B` — action-specific profiles only | precise | harder global comprehension |
| `C` — no named levels; exact controls only | avoids label misuse | more verbose and inconsistent planning |

**Recommendation:** `PROPOSAL: A` as a review aid, never agent-assigned; exact controls/authority override label.

## DR-POL-004 — Validation independence and Evidence retention

```yaml
classification: VALIDATION_POLICY_DECISION
selected_option: null
required_before: R5
```

| Option | Trade-off |
|---|---|
| `A` — independence required for protected/material candidates; same-context limitation explicit otherwise | risk-scaled and practical | requires classification |
| `B` — always independent | strongest separation | high overhead for trivial work |
| `C` — never require independence | simplest | self-validation risk |

**Recommendation:** `PROPOSAL: A`; retain exact Evidence only as long as needed for reproducibility/privacy, with policy selected per data class.

## DR-POL-005 — Governance packaging and enforcement admission

```yaml
classification: ARCHITECTURE_GOVERNANCE_DECISION
selected_option: null
required_before: FTR_020_ADMISSION
```

| Option | Trade-off |
|---|---|
| `A` — Minimal Safety in core; optional isolated `DISABLED/OBSERVE/ENFORCED` controls | matches progressive Governance | needs admission/measurement discipline |
| `B` — broad always-on Control Plane | centralized enforcement | premature complexity/product blockage |
| `C` — documentation-only controls forever | smallest runtime | insufficient if repeated violations occur |

**Recommendation:** `PROPOSAL: A`.

## 9. Lifecycle, install and release decisions

## DR-LIFE-001 — Install ownership and distribution

```yaml
classification: PRODUCT_ARCHITECTURE_DECISION
selected_option: null
required_before: FTR_004_IMPLEMENTATION
```

**Recommended ownership classes — proposal:** `AOS_MANAGED`, `PROJECT_OWNED`, `USER_OWNED`, `GENERATED_DISPOSABLE`, `UNKNOWN_CONFLICT`. Only AOS-managed/generated paths may be replaced under exact preview; user/project paths require preservation/conflict decision.

Distribution options (package manager, downloadable bundle, source/bootstrap, hosted) remain dependent on toolchain/platform. Recommendation: smallest verifiable local package with zero-write dry-run and explicit uninstall before auto-update.

## DR-LIFE-002 — Versioning, release and deployment model

```yaml
classification: LATER_LIFECYCLE_DECISION
selected_option: null
required_before: FTR_024_IMPLEMENTATION
```

**Recommendation:** defer until actual artifact consumers/compatibility/deployment target exist. Then select versioning and channel with exact changelog, rollback and independent Release authorization. Merge must not imply release.

## DR-LIFE-003 — Extension/plugin version and trust model

```yaml
classification: OPTIONAL_EXTENSION_DECISION
selected_option: null
required_before: FTR_026_IMPLEMENTATION
```

**Recommendation:** defer until at least two repeated extension points. When admitted, require manifest version, core compatibility, explicit permissions, source/trust provenance, failure isolation and safe removal; no marketplace default.

## DR-LIFE-004 — Domain module scope

```yaml
classification: REGULATED_OR_SPECIALIST_DECISION
selected_option: null
required_before: FTR_027_RESEARCH_OR_IMPLEMENTATION
```

**Recommendation:** no shared Medical+Design module. Select one exact domain/job separately, bind specialist/data/provider/compliance authority, and keep core neutral/removable.

## 10. Exact human response patterns

After exact candidate manifest exists, decisions may use:

```text
PACKAGE <candidate_identity>: ACCEPT
PACKAGE <candidate_identity>: NEEDS_CHANGES <exact findings>
PACKAGE <candidate_identity>: REJECT
PACKAGE <candidate_identity>: DEFER

DECIDE <decision_id>: <option>
DECIDE <decision_id>: DEFER

FEATURE <feature_id>: REQUIRED | OPTIONAL | DEFERRED |
  REFERENCE_ONLY | REJECTED | UNDECIDED
```

If a decision grants implementation planning, repository mutation or Git action, it must be a separate explicit instruction naming exact subject/path/action. None is requested or inferred here.

## 11. Recommended human review sequence

1. Review Core/Product/Architecture for any wrong foundational claim.
2. Review FTR-001/FTR-003 against already accepted X1 behavior.
3. Review non-X1 features by roadmap phase, recording exact corrections or dispositions.
4. Review journeys/UX and proposed phase order.
5. Decide `DR-FULL-001` and optionally `DR-FULL-002`.
6. Defer implementation decisions until/unless a separate R0/R1 planning task is desired.
7. After corrections, request exact read-only audit before any acceptance/publication.

## 12. Decision-register review checklist

- Are accepted decisions reproduced exactly and not reopened accidentally?
- Are current safe states distinguished from permanent decisions?
- Does every open item have options, trade-offs, recommendation and timing?
- Are recommendations visibly non-authoritative?
- Are future item-level feature dispositions still human-owned?
- Do implementation/Git actions require separate exact authority?
- Is any decision unnecessarily forced before its dependent phase?
