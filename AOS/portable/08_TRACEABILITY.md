---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
artifact_role: LIVE_TRACEABILITY_DERIVED_VIEW
status: DRAFT
authority: NONE
navigation_role: DERIVED_ONLY
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
implementation_authorization: NONE
git_authorization: NONE
---

# 08 — Traceability

This derived view connects package-local owners without taking ownership of Product, Architecture, Workflow, Feature or human-decision facts. It contains live coverage and review routes only; source construction history and prior audit chronology are intentionally excluded.

## 1. Package artifact/owner map

| Artifact | Review claim | Upstream owner | Internal authority |
|---|---|---|---|
| AGENTS | package-local routing and authority boundaries | all owners | derived only |
| README | package navigation/status/source bindings | all owners | derived only |
| Project Core | integrated identity/principles/authority view | `docs/00_Core.md` | none |
| Product Model | integrated product requirements/capabilities | `docs/01_Product.md` + accepted X1 | none |
| Architecture Contracts | integrated layers/C-001…014/invariants | `docs/02_Architecture.md` + accepted foundation/X1 | none |
| Engineering Workflow | integrated documentation/runtime semantics | `docs/03_Development.md` | none |
| Feature Specifications | C-002-depth design for all 30 features | `docs/06_Features.md` + accepted X1 | none |
| Journeys/UX | accepted journey expansion and UX proposals | `docs/01_Product.md` | none |
| Roadmap | proposed sequencing/admission gates | human decisions required | none |
| Decision Register | accepted ledger and decision-ready proposals | exact human/accepted records | none |
| this traceability view | coverage and human review routing | all sources | derived only |

## 2. Problem → journey → feature traceability

| Problem | Primary journey(s) | Feature response | Contract/Evidence boundary |
|---|---|---|---|
| P-001 distributed state | J-004 | FTR-016, FTR-008 | C-012 freshness-checked handoff/status |
| P-002 unclear stop point | J-004/J-005 | FTR-008, FTR-014 | terminal report + one next action |
| P-003 request→assumption | J-001 | FTR-001, FTR-003 | C-001 then C-003/C-002 with human checkpoints |
| P-004 hidden scope drift | J-003/J-006 | FTR-006, 009, 010, 013, 019 | C-005/006/007/008 and exact candidate |
| P-005 PASS→approval | J-005 | FTR-011, 012 | C-009/C-010 separate from C-011 decision |
| P-006 implementation+validation mixed | J-003/J-005 | FTR-011, 013 | frozen read-only validation; separate correction |
| P-007 Git collapsed | J-006 | FTR-015, 024 | separate C-014 records |
| P-008 legacy complexity | J-007 | FTR-002, 005, 022 | exact reference record; authority none |
| P-009 exhaustive extraction | J-007 | FTR-002, 022 | narrow question/stop conditions |
| P-010 duplicate owners | all | FTR-003, 016, 021 | Product Spec/Passport option A; derived views |
| P-011 shallow features | J-003 | FTR-003 + all Passports | full C-002 fields and exact acceptance |
| P-012 install ownership | J-001 supporting/J-006 | FTR-004, 014 | C-013 preview/recovery |
| P-013 routing unmeasured | optional SJ-004 | FTR-018 | advisory measured routing; no authority |
| P-014 automation too early | all later phases | FTR-020, 023, 030 | manual proof and admission gates |
| P-015 unclear blocker/next | J-004/J-005 | FTR-008, 012, 014 | plain-language Status/Next/Review/Recovery |

### 2.1 Complete feature-edge trace graph

Each row is a traversable edge chain. `Acceptance/negative` locators refer to the exact named subsection inside the feature section in [04_FEATURE_SPECIFICATIONS.md](04_FEATURE_SPECIFICATIONS.md). Roadmap placement is a proposal unless an accepted decision is named. `DR-FTR-*` records have `selected_option: null`.

| Problem | User / JTBD | Product requirement | Journey | Feature | Contract | Acceptance / negative locator | Roadmap | Human decision route |
|---|---|---|---|---|---|---|---|---|
| `P-003`, `P-015` | `U-001` turn domain knowledge into outcome; `U-002` retain intent/control | `PR-001`, `PR-002`, `PR-003`, `PR-004`, `PR-005` | `J-001` | `FTR-001` | `C-001` | FTR-001 `Acceptance` + `Negative cases` | `R1` | `ADR-AOS-005`, `ADR-AOS-008` accepted |
| `P-001`, `P-008`, `P-009`, `P-015` | `U-002` understand existing project; `U-004` trace observations | `PR-018`, `PR-019`, `PR-023` | `J-002`, `J-007` | `FTR-002` | snapshot-bound discovery record using `C-007` identity semantics | FTR-002 `Acceptance/negative` | `R3` | `DR-FTR-002` |
| `P-003`, `P-010`, `P-011` | `U-001` define outcome; `U-002` preserve product intent; `U-003` receive sufficient contract | `PR-003`, `PR-005`, `PR-006` | `J-001`, `J-003` | `FTR-003` | `C-003`, `C-002` | FTR-003 `Acceptance/negative` | `R2` | `ADR-AOS-005`, `ADR-AOS-007` accepted |
| `P-012`, `P-015` | `U-002` install without state loss; `U-005` preserve ownership/recovery | `PR-019`, `PR-020`, `PR-021`, `PR-024` | `SJ-001`, `J-006` | `FTR-004` | `C-013` | FTR-004 `Acceptance/negative` | `R6` | `DR-FTR-004`, then `DR-LIFE-001` if admitted |
| `P-008`, `P-010`, `P-011` | `U-002` choose material architecture; `U-003` receive one exact decision | `PR-003`, `PR-006`, `PR-023` | `J-003`, `J-007` | `FTR-005` | `C-004` | FTR-005 `Acceptance/negative` | `R2 support` | `ADR-AOS-006` accepted supporting role; exact ADR remains human-only |
| `P-004`, `P-005` | `U-002` retain scope/control; `U-003` execute one bounded outcome | `PR-007`, `PR-008`, `PR-009`, `PR-012` | `J-003` | `FTR-006` | `C-005`, `C-006`, `C-008` | FTR-006 `Acceptance/negative` | `R4` | `ADR-AOS-006` accepted supporting role |
| `P-002`, `P-004`, `P-014` | `U-002` manage larger outcome; `U-003` receive one active task | `PR-007`, `PR-012`, `PR-018`, `PR-019`, `PR-026` | `J-003` | `FTR-007` | `C-005` reference hierarchy | FTR-007 `Acceptance/negative` | `R8` | `DR-FTR-007` |
| `P-001`, `P-002`, `P-015` | `U-001/U-002` understand state; `U-005` continue safely | `PR-018`, `PR-019` | `J-004` | `FTR-008` | `C-012` derived status view | FTR-008 `Acceptance/negative` | `R3` | `DR-FTR-008` |
| `P-004`, `P-007`, `P-012` | `U-002` preview exact effect; `U-003/U-005` protect repository state | `PR-009`, `PR-010`, `PR-021`, `PR-025` | `J-002`, `J-003`, `J-006` | `FTR-009` | `C-007` | FTR-009 `Acceptance/negative` | `R4` | `DR-FTR-009` |
| `P-004`, `P-006`, `P-014` | `U-002` receive bounded change; `U-003` report actual effects | `PR-011`, `PR-012`, `PR-020`, `PR-021`, `PR-026` | `J-003` | `FTR-010` | `C-006`, `C-008` | FTR-010 `Acceptance/negative` | `R4` | `DR-FTR-010` |
| `P-005`, `P-006` | `U-004` validate without correcting/approving | `PR-013`, `PR-014`, `PR-015` | `J-003`, `J-005` | `FTR-011` | `C-009` | FTR-011 `Acceptance/negative` | `R5` | `ADR-AOS-006` accepted supporting role |
| `P-005`, `P-010`, `P-015` | `U-001/U-002` understand result; `U-004` present evidence | `PR-013`, `PR-014`, `PR-016`, `PR-017` | `J-001`, `J-003`, `J-005` | `FTR-012` | `C-010`, `C-011` | FTR-012 `Acceptance/negative` | `R5` | `ADR-AOS-006` accepted supporting role; verdict remains exact human record |
| `P-004`, `P-005`, `P-006` | `U-003` freeze actual subject; `U-004` audit exact bytes | `PR-013`, `PR-015` | `J-003`, `J-005`, `J-006` | `FTR-013` | candidate identity + `C-009` | FTR-013 `Acceptance/negative` | `R5` | `ADR-AOS-006` accepted supporting role |
| `P-002`, `P-004`, `P-012`, `P-015` | `U-002/U-003` recover bounded work; `U-005` preserve continuity | `PR-011`, `PR-018`, `PR-019`, `PR-020`, `PR-021` | `J-003`, `J-004`, `SJ-002` | `FTR-014` | `C-012` recovery/handoff | FTR-014 `Acceptance/negative` | `R4` | `DR-FTR-014` |
| `P-007` | `U-002` retain Git control; `U-005` verify delivery state | `PR-009`, `PR-010`, `PR-020`, `PR-025` | `J-006` | `FTR-015` | `C-014` | FTR-015 `Acceptance/negative` | `R6` | `DR-FTR-015` |
| `P-001`, `P-002`, `P-010`, `P-015` | `U-002/U-003/U-005` resume across agents/sessions | `PR-018`, `PR-019`, `PR-020`, `PR-022` | `J-002`, `J-004` | `FTR-016` | `C-012` | FTR-016 `Acceptance/negative` | `R3` | `DR-FTR-016` |
| `P-001`, `P-009`, `P-014` | `U-002/U-003` retrieve only relevant context | `PR-018`, `PR-019`, `PR-022`, `PR-026` | `J-002`, `SJ-004` | `FTR-017` | rebuildable derived-index contract | FTR-017 `Acceptance/negative` | `R9` | `DR-FTR-017` |
| `P-013`, `P-014` | `U-002` control cost/privacy; `U-003` receive advisory route | `PR-022`, `PR-023`, `PR-026` | `SJ-004` | `FTR-018` | advisory routing record | FTR-018 `Acceptance/negative` | `R9` | `DR-FTR-018` |
| `P-004`, `P-005`, `P-007` | `U-002` retain authority; `U-003/U-005` classify protected action | `PR-008`, `PR-009`, `PR-010`, `PR-021`, `PR-025` | `J-003`, `J-006` | `FTR-019` | permission classification over `C-006/C-007` | FTR-019 `Acceptance/negative` | `R4` | `DR-FTR-019` |
| `P-014` | `U-002` avoid premature controls; `U-005` admit measured enforcement | `PR-021`, `PR-023`, `PR-026`, `PR-027` | `SJ-004` | `FTR-020` | optional policy/mode record | FTR-020 `Acceptance/negative` | `R9` | `DR-FTR-020`, `DR-POL-005` |
| `P-001`, `P-005`, `P-010`, `P-014` | `U-004/U-005` detect drift without new owner | `PR-005`, `PR-006`, `PR-013`, `PR-018`, `PR-026`, `PR-027` | `J-004` | `FTR-021` | owner graph + drift finding | FTR-021 `Acceptance/negative` | `R7 conditional` | `DR-FTR-021` |
| `P-008`, `P-009`, `P-014` | `U-002/U-003/U-005` reuse evidence-backed patterns | `PR-023`, `PR-026`, `PR-027` | `J-007` | `FTR-022` | reference/pattern record | FTR-022 `Acceptance/negative` | `R7` | `DR-FTR-022` |
| `P-005`, `P-006`, `P-014` | `U-003/U-004/U-005` automate proven checks without approval | `PR-013`, `PR-014`, `PR-015`, `PR-026`, `PR-027` | `J-005` | `FTR-023` | `C-009`, `C-010` | FTR-023 `Acceptance/negative` | `R7 conditional` | `DR-FTR-023` |
| `P-007`, `P-012` | `U-002/U-005` package and promote exact artifact safely | `PR-020`, `PR-021`, `PR-025`, `PR-027` | `J-006` | `FTR-024` | `C-014` + release package | FTR-024 `Acceptance/negative` | `R8` | `DR-FTR-024`, then `DR-LIFE-002` if admitted |
| `P-002`, `P-014`, `P-015` | `U-004/U-005` diagnose recurrence and preserve next route | `PR-013`, `PR-014`, `PR-018`, `PR-019`, `PR-020`, `PR-027` | `J-007`, `SJ-003` | `FTR-025` | incident + lesson proposal record | FTR-025 `Acceptance/negative` | `R7` | `DR-FTR-025` |
| `P-010`, `P-012`, `P-014` | `U-002/U-003/U-005` add removable capability safely | `PR-020`, `PR-021`, `PR-022`, `PR-023`, `PR-026` | `SJ-004` | `FTR-026` | module manifest/compatibility contract | FTR-026 `Acceptance/negative` | `R9` | `DR-FTR-026`, then `DR-LIFE-003` if admitted |
| `P-011`, `P-013`, `P-014` | `U-001` express domain outcome; `U-002` retain product authority; domain specialist validates | `PR-003`, `PR-005`, `PR-017`, `PR-022`, `PR-023`, `PR-026` | `SJ-004` | `FTR-027` | distinct Medical and Design profile contracts | both FTR-027 profile `Acceptance/negative` blocks | `R9` | `DR-FTR-027`; then `DR-LIFE-004`; selection currently `null` |
| `P-001`, `P-015` | `U-001/U-002` understand product state; `U-004` present accessible review | `PR-016`, `PR-017`, `PR-018`, `PR-019`, `PR-022` | `J-001`, `J-004`, `J-005`, `SJ-004` | `FTR-028` | source-linked views + `C-011` | FTR-028 `Acceptance/negative` | `R9` | `DR-FTR-028` |
| `P-001`, `P-010`, `P-015` | `U-001/U-002/U-003/U-005` carry semantics across targets | `PR-018`, `PR-019`, `PR-022`, `PR-023`, `PR-026` | `J-004`, `SJ-004` | `FTR-029` | derived package/manifest contract | FTR-029 `Acceptance/negative` | `R9` | `DR-FTR-029` |
| `P-005`, `P-006`, `P-010`, `P-014` | `U-003/U-004/U-005` reject invalid representations and drift | `PR-006`, `PR-013`, `PR-014`, `PR-015`, `PR-026`, `PR-027` | `J-005` | `FTR-030` | `C-009` + owner-schema conformance contract | FTR-030 `Acceptance/negative` | `R7 conditional` | `DR-FTR-030` |

Graph union invariants:

- problems: exactly `P-001…P-015` are reachable;
- users/JTBD: exactly `U-001…U-005` are represented;
- product requirements: exactly `PR-001…PR-027` are reachable;
- canonical journeys: `J-001…J-007` are represented; `SJ-*` rows remain proposals;
- features: exactly one row for each `FTR-001…FTR-030`;
- canonical contracts: `C-001…C-014` are represented, with feature-local contracts named where no canonical C-class exists;
- every feature row terminates in its acceptance/negative locator, proposed roadmap placement and exact accepted or open human decision route.

## 3. Feature coverage and traceability

| Feature | Journey/value relation | Primary contract(s) | Proposed earliest phase | Disposition |
|---|---|---|---:|---|
| FTR-001 | J-001 intent confirmation | C-001 | R1 | SELECT_FOR_X1 |
| FTR-002 | J-002/J-007 discovery | C-007-like snapshot evidence | R3 | UNDECIDED |
| FTR-003 | J-001/J-003 product definition | C-002/C-003 | R2 | SELECT_FOR_X1 |
| FTR-004 | onboarding/install | C-013 | R6 | UNDECIDED |
| FTR-005 | J-003/J-007 architecture choice | C-004 | R2 support | SUPPORTING_CONTROL_ONLY |
| FTR-006 | J-003 bounded task | C-005/C-006/C-008 | R4 | SUPPORTING_CONTROL_ONLY |
| FTR-007 | large-work decomposition | C-005 references | R8 | UNDECIDED |
| FTR-008 | J-004 status/next | C-012 derived view | R3 | UNDECIDED |
| FTR-009 | J-002/J-003/J-006 preflight | C-007 | R4 | UNDECIDED |
| FTR-010 | J-003 scoped execution | C-006/C-008 | R4 | UNDECIDED |
| FTR-011 | J-005 validation | C-009 | R5 | SUPPORTING_CONTROL_ONLY |
| FTR-012 | J-005 review/decision | C-010/C-011 | R5 | SUPPORTING_CONTROL_ONLY |
| FTR-013 | J-003/J-005 freeze | candidate identity + C-009 | R5 | SUPPORTING_CONTROL_ONLY |
| FTR-014 | J-003/J-004 recovery | C-012 | R4 | UNDECIDED |
| FTR-015 | J-006 Git closure | C-014 | R6 | UNDECIDED |
| FTR-016 | J-004 continuity/context | C-012 | R3 | UNDECIDED |
| FTR-017 | optional retrieval | derived index | R9 | UNDECIDED |
| FTR-018 | optional model/provider route | advisory routing record | R9 | UNDECIDED |
| FTR-019 | all protected actions | permission classification | R4 | UNDECIDED |
| FTR-020 | optional enforcement | policy/mode record | R9 | UNDECIDED |
| FTR-021 | drift/authenticity | owner graph/findings | R7 conditional | UNDECIDED |
| FTR-022 | J-007/pattern reuse | reference/pattern record | R7 | UNDECIDED |
| FTR-023 | automated technical Evidence | C-009/C-010 | R7 conditional | UNDECIDED |
| FTR-024 | J-006 release | C-014/release package | R8 | UNDECIDED |
| FTR-025 | operations/learning | incident/lesson record | R7 | UNDECIDED |
| FTR-026 | optional extension | module manifest/contract | R9 | UNDECIDED |
| FTR-027 | optional Medical or Design profile; selection null | distinct profile contracts/specialist decision | R9 | UNDECIDED |
| FTR-028 | optional visual UX | source-linked views/C-011 | R9 | UNDECIDED |
| FTR-029 | portability/localization | derived package/manifest | R9 | UNDECIDED |
| FTR-030 | strict internal contracts | C-009 + owner schemas | R7 conditional | UNDECIDED |

Every feature’s complete fields are in [04_FEATURE_SPECIFICATIONS.md](04_FEATURE_SPECIFICATIONS.md). Roadmap placement is non-authoritative.

## 4. Contract traceability

| Contract | Product semantics | Feature producers/consumers | Review focus |
|---|---|---|---|
| C-001 Intent | original request/problem/outcome | FTR-001 → FTR-003 | source/synthesis separation and exact confirmation |
| C-002 Passport | feature-specific behavior | FTR-003; one per selected feature | completeness, disposition, acceptance/negative |
| C-003 Product Spec | cross-feature Product facts | FTR-003; referenced by Passports | owner option A and no execution authority |
| C-004 ADR | human architecture decision | FTR-005 | distinct options, empty selection until human |
| C-005 Task Brief | bounded intended work | FTR-006 | scope/acceptance completeness, no permission |
| C-006 Authorization | protected permission | human→FTR-010 | exact actor/subject/stage/paths/consumption |
| C-007 Preflight | current identity/action preview | FTR-009 | read-only, freshness and conflict |
| C-008 Execution | actual mutation/report | FTR-010/FTR-006 | intended-vs-actual and stop |
| C-009 Validation | technical result | FTR-011/013/023 | exact candidate, NOT_RUN, no correction |
| C-010 Evidence | criterion-bound proof | FTR-011/012/023 | method/subject/limitations |
| C-011 Review/Decision | human verdict | FTR-012 | authenticity, exact fact classes, no simulation |
| C-012 Memory/Handoff | continuity | FTR-008/014/016 | derived/freshness/one next action |
| C-013 Install Manifest | ownership-safe apply | FTR-004 | dry-run/preview/recovery/user state |
| C-014 Git Delivery | independent delivery actions | FTR-015/024 | no action implication chain |

## 5. Accepted facts vs package proposals

### Accepted and carried forward

- AOS identity/direction, authority/status/safety semantics and product boundary.
- Canonical product problems, actors/JTBD and journeys.
- Architecture layers, ownership classes and C-001…C-014 semantic categories.
- Documentation/runtime/validation/Git separation.
- Feature identities, recommendations and current dispositions.
- Exact accepted X1 FTR-001/FTR-003 behavior fact classes.
- Product Spec↔Passport option A and FTR-001 first-slice option A.
- Frozen global package identity and its explicit unknown boundary.

### New review proposals

- integrated PR/UX/architecture requirement identifiers;
- detailed non-X1 feature-visible states/flows;
- full roadmap phasing after FTR-001;
- concrete recommended options for still-open product/architecture/policy decisions;
- supporting journey/information architecture/content templates;
- feature admission batching and measurement sequence.

No proposal is selected by package presence or construction checks.

## 6. Preserved unknowns and decision routing

| Unknown/decision | Affected boundary | Safe current behavior | Register |
|---|---|---|---|
| first concrete segment/job | R1 dogfood/product validation | retain general accepted actors; no segment claim | DR-PROD-001 |
| implementation repository | all runtime planning | `UNASSIGNED`, no implementation | DR-ARCH-001 |
| compatibility | implementation architecture | greenfield recommendation only | DR-ARCH-002 |
| interface | R1 UX/implementation | interface-neutral contracts | DR-ARCH-003 |
| persistence | R1 exact revision/state | no runtime claim; local-record proposal | DR-ARCH-004 |
| language/toolchain | implementation HOW | evaluate later; no named winner | DR-ARCH-005 |
| decision authenticity | runtime confirmation/acceptance | exact raw records in current documentation only | DR-POL-001 |
| provider/privacy | sensitive/external processing | no implied external transfer | DR-POL-002 |
| Risk Profile | first protected execution | agent does not assign | DR-POL-003 |
| Registry | multiple Passports | direct owner links | DR-PROD-002 |
| install/distribution | FTR-004 | no installer behavior claim | DR-LIFE-001 |
| release/version/deploy | FTR-024 | no Release action/target | DR-LIFE-002 |
| 23 `UNDECIDED` feature dispositions | R3–R9 item admission | preserve each current disposition | `DR-FTR-002`, `004`, `007…010`, `014…030` (23 exact routes) |
| optional enforcement/extensions | R7–R9 | deferred until admission Evidence | DR-POL-005/DR-LIFE-003 |
| FTR-027 domain profile | R9 | both proposals retained; `selected_domain_profile: null` | DR-FTR-027 then DR-LIFE-004 |

## 7. Authority and mutation audit questions

- Does any package statement imply canonical ownership? Expected: no.
- Does any recommendation appear as human selection? Expected: no.
- Does roadmap placement change `human_disposition`? Expected: no.
- Does accepted X1 package imply implementation/Git authority? Expected: no.
- Does PASS/Evidence/readiness imply acceptance? Expected: no.
- Can UI/registry/memory/index own product/decision/repository truth? Expected: no.
- Is implementation HOW selected without decision? Expected: no.
- Are canonical docs, frozen AOS and accepted X1 paths unchanged? Expected: yes.

## 8. Human review by document

### Project Core

Confirm identity, mission, source precedence, boundaries, principles and glossary. Flag any foundational claim that does not describe the intended future AOS.

### Product Model

Confirm problem, users/JTBD, product promise, requirements, first slice and acceptance model. Decide whether primary segment/metrics need selection now.

### Architecture Contracts

Confirm layer/responsibility boundaries, C-001…C-014 relationships, owners, trust/failure/recovery and deferred HOW. Identify any material ADR not listed.

### Engineering Workflow

Confirm documentation/runtime split, stage boundaries, validation independence, Evidence/review/recovery and Git separation.

### Feature Specifications

Review FTR-001/FTR-003 against accepted X1; then non-X1 features by proposed phase. Record exact content findings separately from disposition decisions.

### Journeys/UX

Walk through J-001 first, then resume/review/protected delivery. Confirm plain-language status and no authority-bearing UI assumption.

### Roadmap

Review phase dependencies, not estimates. Decide direction only; feature admission remains item-scoped.

### Decision Register

Verify accepted ledger and select/defer only what is needed. Package acceptance alone selects none of the open options.

## 9. Package-wide acceptance criteria

- `PKG-AC-01`: exact source/decision context is reproducible.
- `PKG-AC-02`: all eleven Markdown content files plus one non-self-referential manifest have distinct roles and valid links.
- `PKG-AC-03`: canonical owner boundaries are preserved.
- `PKG-AC-04`: the full trace graph covers all 15 problems, five users/JTBD, 27 PRs, seven canonical journeys, 30 features, contract/acceptance-negative/roadmap nodes and exact decision routes.
- `PKG-AC-05`: all C-001…C-014 contract classes are represented.
- `PKG-AC-06`: exactly 30 unique feature sections retain source recommendation/disposition.
- `PKG-AC-07`: each feature covers required C-002 behavior fields.
- `PKG-AC-08`: accepted X1 behavior/decisions are preserved without widening.
- `PKG-AC-09`: proposals/unknowns/NOT_RUN are visibly classified.
- `PKG-AC-10`: roadmap covers every feature without admitting it.
- `PKG-AC-11`: every material open DR uses the uniform decision contract; 23 `UNDECIDED` features have distinct `DR-FTR-*` routes; all selected options remain null/unselected.
- `PKG-AC-12`: observable recovery/consistency outcomes are specified without prescribing reversible implementation mechanisms; no implementation HOW, runtime authorization or Git grant is introduced.
- `PKG-AC-13`: Markdown structure/fences/relative links/whitespace pass focused construction checks.
- `PKG-AC-14`: exact candidate manifest byte-binds every included artifact and excludes itself.
- `PKG-AC-15`: source/protected paths remain unchanged and Git actions remain `NOT_RUN`.

## 10. Mandatory negative review cases

- `PKG-NEG-01`: accepting README/navigation cannot accept underlying product facts implicitly.
- `PKG-NEG-02`: roadmap phase cannot mutate a feature disposition.
- `PKG-NEG-03`: FTR-001 confirmation cannot authorize FTR-003 or implementation.
- `PKG-NEG-04`: X1 acceptance cannot publish canonical/global package silently.
- `PKG-NEG-05`: required construction/audit `NOT_RUN` cannot become PASS.
- `PKG-NEG-06`: an implementation repository cannot be inferred from current checkout.
- `PKG-NEG-07`: reference/legacy presence cannot become target requirement.
- `PKG-NEG-08`: technical audit cannot select any option in Decision Register.
- `PKG-NEG-09`: candidate byte change invalidates prior audit/review binding.
- `PKG-NEG-10`: package review cannot authorize Commit/Push/Merge/Release unless exact action is separately named.
