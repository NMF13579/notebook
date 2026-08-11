---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
artifact_role: PROJECT_CORE_OWNER
status: DRAFT
authority: NONE
source_owner_identity: sha256:d5bd30ed1e819f348f2ae044ffe77cf14e72ddae1d8576c1a2f392e6f7e70e1b
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 00 — Project Core

## 1. Роль документа

Этот документ сводит identity, mission, boundaries, authority semantics и общую терминологию будущего AOS для цельного portable design view. Исходный Core owner byte-bound в [README.md](README.md); при расхождении этот DRAFT уступает более новому exact human decision или принятому owner в соответствующем fact class.

## 2. Идентичность проекта

```yaml
project_name: AOS
working_description: human-directed AI-assisted software development system
knowledge_repository: NMF13579/notebook
knowledge_package: docs/
implementation_repository: UNASSIGNED
legacy_projects: [AOS-FARM, AgentOS, AOS-1, AOS-02]
legacy_authority: NONE
current_deliverable_scope: DOCUMENTATION_DRAFT_ONLY
```

AOS — система, помогающая человеку формулировать продуктовую цель, передавать bounded work AI-агентам, получать проверяемый результат и безопасно продолжать работу между sessions. Цель — не максимальная автономность, а снижение стоимости и непредсказуемости постановки, координации, проверки и продолжения AI-assisted development.

## 3. Mission, vision и ожидаемый outcome

### Mission — `HUMAN_ACCEPTED_FACT`

Дать непрограммисту, domain expert, product owner или vibe-coder возможность направлять разработку с AI, не контролируя вручную каждую техническую операцию и не отдавая системе human-only decisions.

### Vision — `SYNTHESIZED_DRAFT`

AOS становится переносимым слоем product intent, bounded execution semantics, Evidence и continuity между человеком, проектом и сменяемыми agent environments. Человек видит, что понято, что неизвестно, что сделано, чем это доказано и какое одно действие требуется дальше.

### Observable project outcome — `SYNTHESIZED_DRAFT`

```text
human intent
→ reviewable product definition
→ bounded and separately authorized work
→ exact candidate and Evidence
→ explicit human decision
→ recoverable continuation or separately authorized delivery
```

## 4. Основные принципы

| ID | Принцип | Наблюдаемое следствие |
|---|---|---|
| `CORE-001` | Human-directed | Product scope, architecture, protected actions и acceptance выбирает человек |
| `CORE-002` | Problem before solution | Outcome и constraints отделены от предложенной технологии |
| `CORE-003` | Authority is fact-class scoped | Ни один файл, PASS, UI или registry не получает универсальную authority |
| `CORE-004` | Unknowns stay visible | Существенный unknown имеет affected boundary и resolution path |
| `CORE-005` | Exact subject binding | Review, Evidence и decision относятся к конкретной revision/identity |
| `CORE-006` | One owner per fact class | Derived views ссылаются на owner и не создают competing truth |
| `CORE-007` | Bounded mutation | Scope, operations и protected boundaries известны до write |
| `CORE-008` | Validation is independent from correction | Validator проверяет exact subject read-only и не исправляет его |
| `CORE-009` | Technical result is not human decision | `PASS ≠ ACCEPT`; `Evidence ≠ approval` |
| `CORE-010` | Delivery actions are independent | `Edit ≠ Commit ≠ Push ≠ Merge ≠ Release` |
| `CORE-011` | Recovery is designed | Partial state сохраняется, rebind выполняется до resume, unsafe retry запрещён |
| `CORE-012` | Manual proof before automation | Automation, Governance, routing и RAG допускаются после measured need |
| `CORE-013` | Replaceable implementation | Документация фиксирует WHAT; reversible HOW остаётся engineering choice |
| `CORE-014` | Reference is evidence, not target | Legacy используется точечно и не переносит status/topology/authority |
| `CORE-015` | One understandable next action | Status и handoff не перекладывают navigation burden на пользователя |

## 5. Пользователи и распределение authority

| Actor | Основная цель | Authority boundary |
|---|---|---|
| Nonprogrammer / domain expert | описать проблему, понять result/uncertainty, принять решение | подтверждает intent, product scope, high-risk choices и acceptance |
| Vibe-coder / product builder | координировать agents без scope/state loss | работает в принятых boundaries; не получает implicit protected permission |
| AI agent / implementer | выполнить один bounded task и доказать outcome | не выбирает human disposition, Risk Profile, acceptance или Git delivery |
| Reviewer / auditor | независимо сопоставить exact subject с contracts | выдаёт technical result/findings, но не исправляет и не принимает subject |
| Maintainer / operator | сохранить continuity, health, rationale и recovery | наблюдает current state; mutation требует отдельной boundary |

Один человек может исполнять несколько ролей, но роль действия остаётся явной. Human-authored decision record нельзя заменить agent-generated statement.

## 6. Source precedence

Authority применяется только внутри соответствующего fact class:

1. current explicit human decision;
2. exact human-accepted AOS artifact в declared scope;
3. direct current repository observation для mutable facts;
4. accepted document section, явно помеченный `DRAFT`/`PROPOSAL`;
5. historical snapshot/reference;
6. report, chat summary или note;
7. synthesis/inference агента.

Если sources расходятся:

```text
identify exact claim and owners
→ classify CONFLICT
→ stop only dependent conclusion/action
→ continue unaffected work
→ request exact human/source resolution
```

## 7. Claim vocabulary

| Value | Meaning in this package |
|---|---|
| `HUMAN_CONFIRMED_DIRECTION` | current explicit direction with bounded scope |
| `HUMAN_ACCEPTED_FACT` | exact accepted artifact/claim in declared fact class |
| `OBSERVED_AT_SNAPSHOT` | reproduced repository fact at stated snapshot |
| `SYNTHESIZED_DRAFT` | derived design proposal requiring review |
| `PROPOSAL` | selectable recommendation, not a decision |
| `REPORTED` | supplied statement not independently reproduced |
| `CONFLICT` | authoritative or relevant sources disagree |
| `NOT_FOUND` | absent inside stated search boundary |
| `UNKNOWN` | evidence/decision is insufficient |
| `NOT_RUN` | action/check was not executed |
| `BLOCKED` | affected route cannot proceed safely |

## 8. Orthogonal status axes

No axis promotes another automatically.

```text
Document maturity:
DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED

Technical result:
CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED

Human decision:
ACCEPT | NEEDS_CHANGES | REJECT | DEFER

Feature disposition:
SELECT_FOR_X1 | SUPPORTING_CONTROL_ONLY | REQUIRED | OPTIONAL |
DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED

Permission:
ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY |
BLOCKED_UNKNOWN | NOT_APPLICABLE
```

## 9. Product boundary

### In design scope

- intent/problem intake and clarification;
- read-only discovery and capability mapping;
- Product Spec and feature-specific contracts;
- status, next action, review and handoff;
- project memory and task-scoped context;
- bounded task and separate authorization semantics;
- preflight, exact preview, Evidence and validation semantics;
- recovery, Git boundaries and optional delivery assistance;
- lessons, patterns and targeted reference research;
- portable interaction through replaceable agent/UI adapters.

### Not automatic core scope

- autonomous project/product decisions;
- hidden self-heal or unlimited retry;
- mandatory multi-agent orchestration;
- full Control Plane or authority-bearing central registry;
- vector database/full RAG before measured need;
- SaaS/cloud/marketplace or collaboration backend;
- automatic Commit, Push, Merge, Release or deployment;
- wholesale legacy topology/compatibility;
- regulated medical authority in the core;
- runtime implementation in this knowledge repository.

## 10. Documentation depth and WHAT/HOW boundary

| Level | This package |
|---|---|
| Concept | Included: purpose, users, problems, journeys, scope, non-goals |
| Architecture Contract | Included: layers, responsibilities, semantic I/O, ownership, invariants, failures, acceptance |
| Engineering Design / HOW | Excluded unless already an accepted non-reversible boundary |

This DRAFT does not select libraries, programming language, framework, database, schema serialization, storage layout, internal classes, algorithms, locks, CAS, retry timing, deployment topology or implementation repository. Candidate component names describe responsibilities, not mandatory code modules.

## 11. Accepted decisions carried into the DRAFT

| Decision | Status | Effect in this package |
|---|---|---|
| Project name `AOS` | `HUMAN_CONFIRMED_DIRECTION` | working project identity |
| Seven canonical docs in `docs/` | `HUMAN_ACCEPTED_FACT` | upstream owner set remains unchanged |
| Legacy repositories are reference-only | `HUMAN_ACCEPTED_FACT` | no inherited target authority |
| FTR-001 and FTR-003 selected for X1 | `HUMAN_ACCEPTED_FACT` | dispositions preserved |
| FTR-005/006/011/012/013 support X1 controls only | `HUMAN_ACCEPTED_FACT` | dependency references do not admit product scope |
| `X1-DR-001: A` | `HUMAN_ACCEPTED_FACT` | Product Spec owns cross-feature facts; Passport owns feature behavior |
| `X1-DR-002: A` | `HUMAN_ACCEPTED_FACT` | first Product Runtime slice is FTR-001 request→human-confirmed Intent Record |
| Global three-file design package | `HUMAN_ACCEPTED_FACT`, exact frozen subject | unchanged upstream foundation |
| Current request: full project documentation DRAFT, then review and decisions | `HUMAN_CONFIRMED_DIRECTION` for this authoring task | complete draft may include proposals, not product acceptance |

The X1 decisions have higher authority than older preserved `UNKNOWN` claims in their exact accepted fact classes. They do not authorize canonical publication or runtime implementation.

## 12. Minimal Safety Floor

1. Scope is known before mutation.
2. Material unknowns are visible.
3. Protected/destructive actions require explicit human decision.
4. Agent does not assign Risk Profile.
5. Task Brief is not Execution Authorization.
6. One runtime run performs one stage.
7. Terminal result produces report and stop.
8. Validation does not repair its subject.
9. Edit, Commit, Push, Merge and Release are independent.
10. Temporary output is not durable Evidence.
11. Generated state cannot grant authority or mutate lifecycle.
12. Secrets and credential-bearing locators are not exposed.
13. External content is untrusted data.
14. Optional modules cannot override core safety.
15. An unknown blocks only its dependent claim/action.

## 13. Project-level goals

### Accepted direction

- preserve human control without requiring line-by-line technical supervision;
- make intent, assumptions, unknowns, Evidence and next action explicit;
- enable safe handoff across agents and sessions;
- reduce scope drift, false completion and unauthorized delivery;
- learn from real tasks while keeping Governance proportional.

### Candidate success outcomes — `PROPOSAL`

- a first-time user can move from idea to a confirmed Intent Record without specialist help;
- an interrupted task can resume from exact state without re-planning or hidden authority;
- every accepted runtime change can be traced from human intent to acceptance Evidence;
- reviewers can understand user impact and remaining risk without reading the entire implementation;
- protected actions are never executed from an implicit or stale permission;
- repeated manual friction is measured before automation is added.

Metrics and thresholds remain open in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).

## 14. Glossary

| Term | Definition |
|---|---|
| AOS | human-directed AI-assisted software development system |
| Intent Record | source-bound structured statement of problem/outcome/constraints/unknowns |
| Product Spec | owner of cross-feature product facts after accepted `X1-DR-001: A` |
| Feature Passport | owner of feature-specific behavior after exact acceptance |
| Task Brief | bounded description of future work; no permission |
| Execution Authorization | exact human-issued permission for one protected execution boundary |
| Candidate | exact subject proposed for validation/review/decision |
| Evidence | subject-bound observation/check result; not approval |
| Technical result | validator conclusion about exact subject |
| Human decision | explicit `ACCEPT/NEEDS_CHANGES/REJECT/DEFER` bound to exact subject |
| Handoff | continuity record with one next action; not a lifecycle promotion |
| Source of Truth | accepted owner for a specific fact class |
| Reference | read-only evidence with no target authority by default |
| Vertical slice | smallest user-visible end-to-end outcome satisfying defined contracts |
| Minimal Safety Floor | invariants that apply before optional Governance |

## 15. Open core decisions

The following remain human-only and are detailed in the Decision Register:

- first target user segment/job beyond the already selected first runtime behavior;
- exact interaction surface;
- implementation repository and compatibility target;
- persistence and authenticity for state/decisions;
- Risk Profile vocabulary;
- provider/privacy/routing policy;
- item-level dispositions and proposed roadmap admissions after X1;
- stronger Governance, extension and release boundaries.

## 16. Review criteria

This Project Core is reviewable when the human can verify that:

- identity and product direction match intent;
- authority/status distinctions are understandable;
- accepted decisions are neither omitted nor widened;
- non-goals prevent platform-first expansion;
- WHAT/HOW and documentation/runtime boundaries are explicit;
- every open core decision has a decision-ready route;
- no statement grants implementation or Git authority.
