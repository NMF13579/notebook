# 01 — AOS Product


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Product intent

AOS — product layer для управления AI-assisted software development человеком, которому нужны ясность, контроль и скорость без постоянного ручного связывания chats, repositories, IDE agents, reports и Git operations.

Product promise candidate:

```text
пользователь формулирует цель
→ получает ясный bounded путь
→ видит observable result и Evidence
→ принимает решение сам
→ может безопасно продолжить работу позже
```

## 2. Target users

### U-01 — Non-programmer product owner / vibe coder

Нуждается в plain-language interaction, понятном current state, reviewable results, explicit decisions и low-friction continuation. Не должен разбираться в каждом Git/CI/internal contract detail.

### U-02 — Developer или coding agent

Нуждается в accepted behavior, exact scope, architecture constraints, allowed/forbidden paths, known failure modes, deterministic validation и clear handoff.

### U-03 — Reviewer / validator

Нуждается в immutable candidate identity, acceptance criteria, negative scenarios, exact checks и separation Evidence/approval.

### U-04 — Maintainer / team lead

Нуждается в compact project map, decisions, feature dependencies, known debt, risks, lifecycle and release boundaries.

## 3. Primary user problems

| ID | Problem | Consequence |
|---|---|---|
| `P-001` | Project state распределён между chats, worktrees, plans, reports и human decisions | Потеря context и повторная работа |
| `P-002` | Неясно, «на чём остановились» | Повторный planning и risky assumptions |
| `P-003` | Свободный request превращается в implementation assumptions | Feature не решает user problem |
| `P-004` | Scope скрыто расширяется | Contamination, rollback, distrust |
| `P-005` | PASS/Evidence/readiness путаются с approval | False completion |
| `P-006` | Validation и implementation смешиваются | Self-validation и скрытые fixes |
| `P-007` | Git operations воспринимаются как один шаг | Unauthorized publication |
| `P-008` | Legacy содержит полезные mechanisms, но много obsolete complexity | Неверная target architecture |
| `P-009` | Exhaustive extraction даёт low signal при высокой стоимости | Задержка product work |
| `P-010` | Documentation разрастается и дублируется | Неясный owner facts и stale content |
| `P-011` | Feature ideas описаны поверхностно | Человек не понимает value, agent не может спроектировать behavior/tests |
| `P-012` | Installer/update могут повредить user-owned state | Data loss и сложный recovery |
| `P-013` | Agents и models выбираются без измерений | Cost/quality unpredictability |
| `P-014` | Automation появляется до stable manual flow | Автоматизация плохого процесса |
| `P-015` | Non-programmer не понимает blockers и next action | Постоянная зависимость от специалиста |

## 4. Jobs to Be Done

1. **Clarify intent.** Превратить идею в user/problem/outcome/constraints/unknowns.
2. **Understand a project.** Получить read-only capability and gap map.
3. **Select a bounded objective.** Выбрать smallest user-visible slice.
4. **Prepare executable work.** Сформировать Task Brief без избыточного planning.
5. **Execute safely.** Ограничить mutation и проверить actual diff.
6. **Validate honestly.** Показать PASS/FAIL/UNKNOWN/NOT_RUN без approval simulation.
7. **Review efficiently.** Получить one-document review package.
8. **Resume.** Продолжить в новом session/agent без replay всей истории.
9. **Deliver deliberately.** Отдельно разрешать commit/push/merge/release.
10. **Learn.** Превратить failure в preventive rule и regression test.

## 5. Product boundaries

### Product Runtime

User-facing capabilities, создающие observable value:

- Intent Intake;
- Project Discovery;
- Project Brief / Specification;
- Status / Next / Details;
- First-Start / onboarding;
- Review Package;
- Project Memory / Handoff;
- Guided Bootstrap, если он доказан как user job;
- Architecture Decision Support, если человек действительно использует его для выбора.

### Development Factory

Internal capabilities для разработки и поддержки AOS:

- Task Brief compiler;
- scoped execution adapters;
- validators and test harness;
- context packs;
- backlog/decomposition;
- CI/release helpers;
- internal loaders, registries и integrity checks.

### Governance / Control

Always-on minimum boundaries плюс deferred stronger controls. Governance сама по себе не считается Product Runtime value.

### Reference / Knowledge

Durable docs, lessons, targeted findings, pattern library и derived indexes.

## 6. Product non-goals первого этапа

- full autonomous software factory;
- self-hosting Control Plane;
- mandatory registry/database/vector store;
- runtime enforcement до stable contracts;
- SaaS platform до proof of local product value;
- automatic architecture/Risk Profile/approval;
- exact clone AOS-FARM;
- backward compatibility без explicit decision;
- domain-specific medical capability в core.

## 7. Core user journeys

### J-001 — Start a new project

```text
intent
→ clarification
→ user/problem/outcome
→ Project Brief candidate
→ feature/slice choice
→ architecture decision where needed
→ Task Brief
→ human execution authorization
→ bounded implementation
→ validation
→ review
→ human decision
```

### J-002 — Understand an existing project

```text
select repository
→ read-only identity/preflight
→ capability map
→ gaps/conflicts/unknowns
→ candidate improvements
→ human selects one objective
```

### J-003 — Implement one feature

```text
selected feature dossier
→ targeted legacy questions
→ Product Contract
→ architecture candidate
→ Task Brief
→ EXECUTE
→ Stage Report
→ VALIDATE
→ REVIEW
→ human decision
```

### J-004 — Resume after interruption

```text
/status
→ repository-derived state
→ candidate/stage identity
→ decisions/findings/blockers
→ /next one bounded action
→ optional /details
```

### J-005 — Review and accept/reject

```text
compact change summary
→ user impact
→ exact Evidence and NOT_RUN
→ findings/limitations
→ decision options
→ human ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

### J-006 — Protected change / Git delivery

```text
protected scope detected
→ PLAN/decision package
→ human Risk Profile
→ bounded EXECUTE
→ independent VALIDATE
→ REVIEW
→ separate Commit
→ separate Push
→ separate Merge
→ separate Release
```

### J-007 — Reconstruct a feature from references

```text
select feature and gaps
→ narrow research questions
→ bind read-only snapshot
→ inspect docs/contracts/tests/code
→ classify findings
→ reject legacy complexity
→ update DRAFT dossier
→ human product/architecture decision
```

## 8. Product capability map

Detailed dossiers are in `06_Features.md`.

### Near-term candidate domains

- intent/specification;
- discovery/status/resume;
- Task Brief and review;
- bounded execution and validation;
- first-start/onboarding/doctor;
- safe install/update;
- project memory/handoff.

### Later candidate domains

- routing and RAG-light;
- progressive Governance;
- runtime enforcement;
- release/observability;
- plugin/domain modules;
- SaaS UI.

No item is `REQUIRED` until explicit human product decision.

## 9. First vertical slice criteria

A first slice is admissible only if:

1. it solves one identified user problem;
2. result is observable without reading internal governance artifacts;
3. inputs, outputs, states, failures and recovery are described;
4. acceptance and negative cases are executable;
5. it works without full Control Plane;
6. dependencies are minimal and replaceable;
7. it creates learning for next manual cycle;
8. it does not require implicit Git delivery.

Scaffolding/bootstrap is acceptable only when direct measurable user value is explicit; otherwise it belongs to Development Factory.

## 10. Product acceptance model

A feature is documentation-ready when a human and agent can answer:

- who uses it and why;
- what triggers it;
- what data enters and leaves;
- what the user observes;
- what states and transitions exist;
- how it fails and recovers;
- what it must never do;
- how it is accepted and negatively tested;
- what decisions remain human;
- what targeted research is still needed.

A feature is product-accepted only after explicit human decision over exact dossier/revision.

## 11. Candidate success indicators

`PROPOSAL`, not accepted metrics:

- time from intent to reviewable Task Brief;
- number of clarification loops;
- frequency of scope drift;
- time to resume after interruption;
- human review time;
- false-green/overclaim incidents;
- percentage of tasks completed without re-planning;
- reuse of lessons/patterns;
- user understanding of blocker and next action.

## 12. Product decisions still required

- priority user/job;
- first Product Runtime domain;
- first vertical slice;
- exact interface;
- required vs optional features;
- compatibility target;
- acceptable autonomy level;
- onboarding/install ownership model;
- success metrics.
