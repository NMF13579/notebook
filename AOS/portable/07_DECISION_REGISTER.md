---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
artifact_role: DECISION_REGISTER_OWNER
status: DRAFT
authority: NONE
selected_open_options: NONE
implementation_authorization: NONE
git_authorization: NONE
package_readiness: READY_FOR_INDEPENDENT_AUDIT
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
| `ADR-AOS-010` | Exact DRAFT-R2 package was accepted after guided review and independent completeness re-audit | decision `DR-FULL-001: ACCEPT`; source identity in `README.md` | accepts only listed R2 fact classes; no implementation or Git authority |

The exact accepted X1 decision record is bound in [README.md](README.md), SHA-256 `3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197`.

## 3. Current safe states, not permanent choices

| State | Current value | Meaning |
|---|---|---|
| Implementation repository | `UNASSIGNED` | no target for runtime planning/execution |
| Implementation authorization | `NONE` | no code/scaffold/test/runtime mutation |
| Git authorization | `NONE` | no Commit/Push/Merge/Release in this run |
| Non-X1 feature dispositions | exactly 23 features are `UNDECIDED` | roadmap proposals do not change them; each uses one `DR-FTR-*` route |
| Exact interface/toolchain/persistence | `UNKNOWN` | not silently selected by architecture prose |
| Portable package publication/acceptance | `NOT_RUN` | source R2 facts remain accepted in scope; this new manifest-bound package remains DRAFT |

`UNASSIGNED` is deliberately absent from the accepted decision ledger. It is the current fail-closed state until a human selects `DR-ARCH-001`; repository presence or package acceptance cannot promote it into a decision.

## 4. Uniform decision-ready contract

Every material open `DR-*` below uses the same contract. A record is decision-ready only when all fields are present:

```yaml
decision_id: EXACT_ID
human_owner: HUMAN_ONLY_ROLE
exact_subject_and_question: REQUIRED
option_set_with_tradeoffs: REQUIRED
recommendation: PROPOSAL_OR_DEFER
required_by_or_trigger: REQUIRED
selected_option: null
current_safe_state: REQUIRED
effect_and_exclusions: REQUIRED
exact_response: "DECIDE <decision_id>: <option>"
```

`selected_option` remains `null` for every open record. Recommendations are proposals; they do not mutate feature disposition, roadmap admission, architecture, implementation authority or Git authority.

| Decision | Human owner | Exact question/subject | Options | Proposal | Required by / trigger | Current safe state | Effect / exclusions |
|---|---|---|---|---|---|---|---|
| `DR-FULL-002` | Product owner | retain proposed roadmap sequence | `A/B/C/DEFER` | `A` | before roadmap is used for planning | accepted FTR-001 only; later sequence unselected | sequence only; no feature admission or authorization |
| `DR-PROD-001` | Product owner | first concrete user/job for R1 dogfood | `A/B/C/DEFER` | `A` | R0 exit / before R1 dogfood | general accepted actors only | selects test context, not commercial segment or feature scope |
| `DR-PROD-002` | Product owner | when/how to admit Feature Registry | `A/B/C/DEFER` | `A` | multiple accepted Passports need navigation | direct owner links | derived navigation only; never owns behavior |
| `DR-PROD-003` | Product owner | when scenario/access modeling is mandatory | `A/B/C/DEFER` | `A` | first access-sensitive or multi-actor feature | proportional feature contract | process depth only; no interface selection |
| `DR-PROD-004` | Product owner | initial R1 success-measure set | `A/B/C/DEFER` | `A` | R0 exit / before R1 dogfood | no numeric target; qualitative observations allowed | measurement scope only; no product acceptance |
| `DR-PROD-005` | Product owner | route the 23 non-X1 feature dispositions | item routes `DR-FTR-*` or `DEFER` | use item routes | before each dependent phase | all 23 remain `UNDECIDED` | item scope only; no behavior acceptance or implementation |
| `DR-ARCH-001` | Repository owner | exact implementation repository/role | `A/B/C/DEFER` | `A` | R0 exit / implementation planning | `UNASSIGNED` | binds target only; no mutation/Git authority |
| `DR-ARCH-002` | Architecture owner | compatibility relation to legacy | `A/B/C/DEFER` | `A` | R0 exit / implementation architecture | no compatibility claim | target compatibility only; no legacy authority |
| `DR-ARCH-003` | Product + architecture owner | initial interaction surface | `A/B/C/D/DEFER` | `A` | R0 exit / R1 implementation | interface-neutral contracts | surface only; no hosting/provider decision |
| `DR-ARCH-004` | Architecture owner | Intent/Memory persistence outcome | `A/B/C/DEFER` | `A` | R0 exit / stateful R1 | no runtime persistence claim | state ownership/consistency outcome; implementation HOW open |
| `DR-ARCH-005` | Architecture owner | initial language/toolchain/dependency policy | `A/B/C/DEFER` | `DEFER` until repo/platform bound | R0 exit / Task Brief | no stack selected | stack boundary only; no repository mutation |
| `DR-ARCH-006` | Architecture owner | Runtime/Factory semantic boundary | `A/B/C/DEFER` | `A` | before R4 | accepted semantic layers; deployment topology open | responsibility boundary only; no process topology |
| `DR-POL-001` | Human authority owner | decision-authenticity mechanism for R1 | `A/B/C/DEFER` | `A` | R0 exit / confirmed runtime state | documentation decisions remain exact records; runtime unclaimed | authenticity only; no broad identity platform |
| `DR-POL-002` | Data owner | provider/privacy/data boundary | `A/B/C/DEFER` | `A` | R0 exit or before sensitive/external input | no implied external transfer | data/provider scope only; no provider admission beyond selection |
| `DR-POL-003` | Human authority owner | Risk Profile vocabulary | `A/B/C/DEFER` | `A` | before R4 protected execution | agent cannot assign profile | classification aid only; exact controls prevail |
| `DR-POL-004` | Validation/data owner | independence and Evidence retention | `A/B/C/DEFER` | `A` | before R5 | no independent-validation claim; minimal necessary retention | validation/retention policy only; no candidate decision |
| `DR-POL-005` | Governance owner | packaging/admission of stronger enforcement | `A/B/C/DEFER` | `A` | before FTR-020 admission | Minimal Safety only; stronger enforcement absent | optional control scope; no self-activation |
| `DR-LIFE-001` | Product + repository owner | install ownership/distribution model | `A/B/C/DEFER` | `A` after target exists | before FTR-004 | no installer/distribution claim | packaging/ownership only; no install authorization |
| `DR-LIFE-002` | Release owner | version/release/deployment model | `A/B/C/DEFER` | `DEFER` | before FTR-024 | no release/deployment target | release model only; Merge does not imply Release |
| `DR-LIFE-003` | Extension/security owner | extension version/trust model | `A/B/C/DEFER` | `DEFER` | before FTR-026 | extensions absent | extension admission only; no install/network authority |
| `DR-LIFE-004` | Product + domain specialist | select Medical, Design or neither | `MEDICAL/DESIGN/NO_DOMAIN/DEFER` | `DEFER` | before FTR-027 research/implementation | `selected_domain_profile: null` | one profile only; no feature admission, specialist authority or data transfer |

## 5. Decision ordering

### Next gate sequence

1. Separate independent read-only audit of the exact portable manifest — technical gate, not a human decision.
2. Exact package-level decision on the portable candidate and its audit result; this does not reopen resolved `DR-FULL-001`.
3. During later product review, optionally `DR-FULL-002` and any exact item-level decisions.

### Exact R0 decision set

R0 uses exactly this set, identically reproduced in the Roadmap:

```text
DR-PROD-001
DR-PROD-004
DR-ARCH-001
DR-ARCH-002
DR-ARCH-003
DR-ARCH-004
DR-ARCH-005
DR-POL-001
DR-POL-002
```

R0 completion also requires a separate instruction authorizing implementation planning. `DR-ARCH-006`, `DR-POL-003`, `DR-POL-004` and lifecycle/release choices retain their later R4/R5/R6 timing and are not R0 gates.

### Defer until evidence/dependent phase

Registry, broad metrics, Governance enforcement, RAG, routing, plugins, SaaS, domains and release choices.

## 6. Resolved source-package decision and remaining documentation decision

## DR-FULL-001 — Exact full DRAFT disposition

```yaml
classification: DOCUMENTATION_PACKAGE_DECISION
status: RESOLVED
selected_option: ACCEPT
required_now: false
subject_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
audit_identity: sha256:b6cd639302fb719ab7ef47e894075c791d683c3e46b35291c11a2c591f989cfe
decision_record_identity: sha256:0353347d106d1985e7b296f721ade4b9e51a1a26a304468b97dc39b00c7598df
```

**Recorded effect.** The exact R2 candidate is human-accepted only in the fact classes declared by its decision record. Source classifications, canonical precedence and all unselected options remain unchanged. Canonical publication, implementation planning, implementation authorization and Git authorization were not granted. The portable candidate has different bytes and requires its own later package decision.

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

## 7. Product decisions

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

## 8. Architecture and implementation-boundary decisions

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

**Recommendation:** `PROPOSAL: A` for R1, provided user/project ownership, interrupted-write observability, revision-consistency outcome and sensitive-data policy are explicit. Promote only on measured need.

## DR-ARCH-005 — Language/toolchain/dependency policy

```yaml
classification: IMPLEMENTATION_ARCHITECTURE_DECISION
selected_option: null
required_before: R0_EXIT_AND_IMPLEMENTATION_TASK_BRIEF
```

**Question.** Which initial implementation ecosystem and dependency policy should be bound after repository, platform and interface constraints are known?

| Option | Benefit | Risk / required evidence |
|---|---|---|
| `A` — TypeScript on a pinned supported Node.js LTS, strict schemas and minimal runtime dependencies | one language across conversational/local UI and tooling; mature packaging | verify target platform, type/runtime validation boundary and distribution constraints |
| `B` — Python on a pinned supported CPython release, strict validated records and minimal runtime dependencies | strong agent/tooling ecosystem and rapid local workflows | verify packaging, cross-platform delivery and type/runtime boundary |
| `C` — another exact stack named by the human | can fit team/platform constraints | must provide portability, validation, testing, packaging, maintenance and dependency evidence |
| `DEFER` | avoids premature HOW selection | blocks R0 exit and implementation Task Brief |

**Recommendation:** `PROPOSAL: DEFER` until `DR-ARCH-001` and `DR-ARCH-003` bind repository/platform/interface constraints, then compare A/B/custom through the stated matrix. One primary ecosystem and minimal dependencies are preferred for R1; legacy presence supplies no selection authority.

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

## 9. Authority, safety and policy decisions

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

## 10. Lifecycle, install and release decisions

## DR-LIFE-001 — Install ownership and distribution

```yaml
classification: PRODUCT_ARCHITECTURE_DECISION
selected_option: null
required_before: FTR_004_IMPLEMENTATION
```

**Recommended ownership classes — proposal:** `AOS_MANAGED`, `PROJECT_OWNED`, `USER_OWNED`, `GENERATED_DISPOSABLE`, `UNKNOWN_CONFLICT`. Only AOS-managed/generated paths may be replaced under exact preview; user/project paths require preservation/conflict decision.

**Question.** Which first distribution route and ownership boundary should FTR-004 support?

| Option | Trade-off |
|---|---|
| `A` — smallest verifiable local bundle/source bootstrap | minimal platform scope and inspectable ownership | manual acquisition/update friction |
| `B` — selected platform package manager | familiar install/update lifecycle | platform-specific packaging and ownership rules |
| `C` — hosted/account-managed distribution | centralized updates/collaboration | auth, privacy, network and service scope |
| `DEFER` | no unsupported installer claim | blocks FTR-004 implementation |

**Recommendation:** `PROPOSAL: A` after an exact toolchain/target exists, with zero-write preview, explicit removal and observable recovery outcomes before any auto-update.

## DR-LIFE-002 — Versioning, release and deployment model

```yaml
classification: LATER_LIFECYCLE_DECISION
selected_option: null
required_before: FTR_024_IMPLEMENTATION
```

**Question.** What artifact and promotion model should FTR-024 govern?

| Option | Trade-off |
|---|---|
| `A` — versioned local/CLI package release | inspectable artifact and rollback | packaging/channel maintenance |
| `B` — hosted service deployment promotion | centralized rollout | infrastructure, tenancy, privacy and rollback scope |
| `C` — exact hybrid artifact/service model | supports mixed consumers | highest compatibility and operations burden |
| `DEFER` | avoids fictional release target | no FTR-024 implementation or Release claim |

**Recommendation:** `PROPOSAL: DEFER` until actual consumers, compatibility and deployment target exist. Any selected model requires exact changelog, recovery and independent Release authorization; Merge never implies Release.

## DR-LIFE-003 — Extension/plugin version and trust model

```yaml
classification: OPTIONAL_EXTENSION_DECISION
selected_option: null
required_before: FTR_026_IMPLEMENTATION
```

**Question.** What initial version and trust boundary should admitted extensions use?

| Option | Trade-off |
|---|---|
| `A` — allowlisted signed modules | stronger provenance | signing/key/revocation operations |
| `B` — source-pinned modules with exact manifest, compatibility and permissions | smaller initial mechanism | weaker portable authenticity; manual trust decision |
| `C` — marketplace/discovery trust service | broad ecosystem UX | platform moderation, identity, hosting and supply-chain scope |
| `DEFER` | no premature extension platform | extensions remain absent |

**Recommendation:** `PROPOSAL: DEFER` until at least two repeated stable extension points. If admitted locally first, prefer B with failure isolation and safe removal; no marketplace default.

## DR-LIFE-004 — Domain module scope

```yaml
classification: REGULATED_OR_SPECIALIST_DECISION
selected_option: null
required_before: FTR_027_RESEARCH_OR_IMPLEMENTATION
```

**Question.** Which single FTR-027 profile, if any, may proceed to bounded research after its feature disposition is separately decided?

| Option | Trade-off |
|---|---|
| `MEDICAL` | addresses one exact regulated medical job | requires jurisdiction, specialist, consent/data/provider and prohibited-action boundaries |
| `DESIGN` | addresses one exact design job | requires product/design ownership, asset rights and accessibility boundaries |
| `NO_DOMAIN` | keeps domain extensions outside target scope | no specialist profile value |
| `DEFER` | preserves both proposals without selection | no domain research/implementation |

**Recommendation:** `PROPOSAL: DEFER`. `selected_domain_profile` remains `null`. Medical and Design cannot be selected together by this decision; profile selection does not admit FTR-027, authorize research/implementation or grant specialist/data/provider authority.

## 11. Item-specific disposition routes for 23 `UNDECIDED` features

Each route is an independent Product-owner decision with `selected_option: null`, exact subject equal to the named feature, effect/exclusions defined below, and exact response defined after the table. Its option set is:

```text
REQUIRED | OPTIONAL | DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED
```

`UNDECIDED` preserves the current safe state. Any other option changes only the exact feature disposition after an authentic human record updates the canonical owner. It does not accept this DRAFT behavior, roadmap phase, architecture, implementation, protected action or Git action.

| Decision route | Item-specific question / evidence trigger | Proposal only | Required before | Current safe state |
|---|---|---|---|---|
| `DR-FTR-002` | Does a bound existing-project case require snapshot discovery as AOS product behavior? | `OPTIONAL` after one reproducible case; otherwise `UNDECIDED` | R3 admission | FTR-002 `UNDECIDED`; no discovery scope |
| `DR-FTR-004` | Does an exact distribution target require managed install/update/remove and First-Start? | `DEFERRED` until target/ownership evidence | FTR-004 planning / R6 | FTR-004 `UNDECIDED`; no installer claim |
| `DR-FTR-007` | Do repeated multi-task outcomes require hierarchy beyond one active bounded task? | `DEFERRED` until recurrence | R8 admission | FTR-007 `UNDECIDED`; no backlog system |
| `DR-FTR-008` | Does observed resume/status confusion require a dedicated Status/Next product feature? | `OPTIONAL` after measured friction | R3 admission | FTR-008 `UNDECIDED`; derived status only |
| `DR-FTR-009` | Will R4 perform protected repository mutation requiring exact preflight/preview? | `REQUIRED` only if R4 mutation is admitted; otherwise `DEFERRED` | R4 entry | FTR-009 `UNDECIDED`; no protected mutation |
| `DR-FTR-010` | Will R4 expose bounded mutation as product/factory behavior? | `REQUIRED` only if R4 mutation is admitted; otherwise `DEFERRED` | R4 entry | FTR-010 `UNDECIDED`; execution absent |
| `DR-FTR-014` | Will any admitted write-capable flow require recovery/resume behavior? | `REQUIRED` with first write-capable flow; otherwise `DEFERRED` | R4 entry | FTR-014 `UNDECIDED`; no write flow |
| `DR-FTR-015` | Should AOS product scope include guided Git closure after accepted candidates? | `DEFERRED` until a real delivery case | R6 admission | FTR-015 `UNDECIDED`; Git actions external/separate |
| `DR-FTR-016` | Do multiple sessions/agents require persistent Project Memory and Context Pack behavior? | `OPTIONAL` after continuity evidence | R3 admission | FTR-016 `UNDECIDED`; source-linked handoff only |
| `DR-FTR-017` | Does a direct-search benchmark show material retrieval failure? | `DEFERRED` unless benchmark proves need | R9 admission | FTR-017 `UNDECIDED`; direct search baseline |
| `DR-FTR-018` | Do task benchmarks plus provider/privacy policy justify advisory routing? | `DEFERRED` until both exist | R9 admission | FTR-018 `UNDECIDED`; no routing product claim |
| `DR-FTR-019` | Will an admitted protected action need a product-visible trust/permission classifier? | `REQUIRED` only with R4 protected action; otherwise `DEFERRED` | R4 entry | FTR-019 `UNDECIDED`; deny by absent authority |
| `DR-FTR-020` | Do repeated stable-rule incidents justify optional runtime enforcement? | `DEFERRED` until measured incidents and false-positive budget | R9 admission | FTR-020 `UNDECIDED`; Minimal Safety only |
| `DR-FTR-021` | Do multiple representations produce observable owner/decision drift requiring detection? | `DEFERRED` until drift exists | conditional R7 admission | FTR-021 `UNDECIDED`; owners inspected directly |
| `DR-FTR-022` | Do repeated reconstruction/decision cases justify a reusable pattern library? | `OPTIONAL` after repeated fit/anti-fit evidence | R7 admission | FTR-022 `UNDECIDED`; exact source records only |
| `DR-FTR-023` | Do stable runtime contracts and repeated checks justify advisory CI/smoke automation? | `DEFERRED` until stable manual checks | conditional R7 admission | FTR-023 `UNDECIDED`; manual validation only |
| `DR-FTR-024` | Does an actual artifact and promotion target require release packaging? | `DEFERRED` until target exists | R8 admission | FTR-024 `UNDECIDED`; no Release model/action |
| `DR-FTR-025` | Do real incidents/near misses require product-visible observability and lesson routing? | `OPTIONAL` after first material incident | R7 admission | FTR-025 `UNDECIDED`; bounded reports/lessons only |
| `DR-FTR-026` | Have at least two stable extension points repeated with isolation/removal needs? | `DEFERRED` until evidence | R9 admission | FTR-026 `UNDECIDED`; extensions absent |
| `DR-FTR-027` | What disposition should FTR-027 receive; if admitted, should a separate profile-selection decision become eligible? | `DEFERRED`; profile remains unselected | before `DR-LIFE-004` or R9 admission | FTR-027 `UNDECIDED`; `selected_domain_profile: null` |
| `DR-FTR-028` | Does measured chat/CLI/local UX friction justify a visual or hosted wrapper? | `DEFERRED` until measured friction and access/privacy model | R9 admission | FTR-028 `UNDECIDED`; interface-neutral core |
| `DR-FTR-029` | Do concrete tool/repository/locale consumers require derived packages/localization? | `DEFERRED` until named consumers | R9 admission | FTR-029 `UNDECIDED`; no cross-target sync |
| `DR-FTR-030` | Do stable runtime representations show strict parser/schema drift defects? | `DEFERRED` until measured drift | conditional R7 admission | FTR-030 `UNDECIDED`; no strict tooling platform |

Exact response for an item route:

```text
DECIDE DR-FTR-<NNN>: REQUIRED | OPTIONAL | DEFERRED |
  REFERENCE_ONLY | REJECTED | UNDECIDED
```

No batch response is valid as 23 decisions. Each route binds one exact feature and one exact disposition.

## 12. Exact human response patterns

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

## 13. Recommended human review sequence

1. Run an independent read-only audit of the exact portable candidate; no correction occurs in that stage.
2. Review the exact portable audit result with Core/Product/Architecture and any remaining finding.
3. Review FTR-001/FTR-003 against already accepted X1 behavior.
4. Review non-X1 features by roadmap phase; use one `DR-FTR-*` response per item if a disposition decision is intended.
5. Review journeys/UX and proposed phase order.
6. Make one package-level decision on the exact portable candidate/audit subject; optionally decide `DR-FULL-002` separately.
7. Defer implementation decisions until/unless a separate R0/R1 planning task is desired.

## 14. Decision-register review checklist

- Are accepted decisions reproduced exactly and not reopened accidentally?
- Are current safe states distinguished from permanent decisions?
- Does every open item have options, trade-offs, recommendation and timing?
- Are recommendations visibly non-authoritative?
- Are future item-level feature dispositions still human-owned?
- Do implementation/Git actions require separate exact authority?
- Is any decision unnecessarily forced before its dependent phase?
