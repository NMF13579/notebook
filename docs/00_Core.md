---
package: AOS_Project_Knowledge_Baseline
package_revision: R5-CORRECTION-CANDIDATE
updated: '2026-08-06'
status: HUMAN_REVIEW_REQUIRED
authority: DERIVED_FROM_ACCEPTED_FACT_CLASS_OWNERS
human_review: REQUIRED_FOR_THIS_REVISION
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
focused_package_validation: PASS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: agent/aos-3-documentation-package
audited_source_commit: 9fa079964ea86b33425337ba1706bd3da5bea7b8
supersedes_revision: R4-RU
active_path: docs/00_Core.md
document_language: ru
technical_identifiers_language: en
document_role: CANONICAL_PROJECT_CORE
authority_scope:
- project_identity
- source_precedence
- status_semantics
- human_authority
- minimal_safety_invariants
- agent_usage_contract
---

# 00 — Ядро проекта

## 1. Назначение и статус

Документ является единым владельцем сведений об идентичности проекта, иерархии источников, статусах утверждений, полномочиях человека, Minimal Safety Floor и правилах использования пакета агентом.

```yaml
status: HUMAN_REVIEW_REQUIRED
authority: DERIVED_FROM_ACCEPTED_FACT_CLASS_OWNERS
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Revision `R5-CORRECTION-CANDIDATE` устраняет semantic drift между ранее принятым baseline, позднейшими решениями `H1` и current lifecycle state. До exact human acceptance эта revision является review candidate; принятые факты сохраняют authority только через свои существующие owner/acceptance records. Даже после принятия knowledge baseline не разрешает mutation, implementation или Git delivery.

## 2. Идентичность проекта

```yaml
project_name: AOS
working_description: human-directed AI-assisted software development system
current_work_mode: DOCUMENTATION_CORRECTION_HUMAN_REVIEW
knowledge_repository: NMF13579/notebook
knowledge_branch_label: agent/aos-3-documentation-package
active_package_path: docs/
implementation_repository:
  decision: NMF13579/aos-3
  decision_status: HUMAN_ACCEPTED
  creation: NOT_RUN
  remote_assignment: NOT_RUN
legacy_projects: [AOS-FARM, AgentOS, AOS-1, AOS-02]
legacy_authority: NONE
```

Target repository decision и physical repository state — разные fact classes. `NMF13579/aos-3` принят как target, но это не доказывает, что repository создан, доступен или имеет нужный baseline. Эти mutable facts требуют fresh read-only observation перед любым implementation planning или execution.

## 3. Подтверждённое направление

AOS должен помогать непрограммисту, отраслевому эксперту, владельцу продукта или vibe-coder управлять разработкой с участием AI-агентов без ручного контроля каждой технической операции.

```text
не максимальная автономность
→ а снижение стоимости постановки, координации, проверки и продолжения работы
```

AOS должен:

1. отделять проблему и desired outcome от преждевременного solution;
2. делать assumptions, unknowns и constraints видимыми;
3. превращать intent в bounded, reviewable task;
4. сохранять состояние между sessions и agent environments;
5. выполнять только отдельно разрешённую mutation;
6. связывать acceptance criteria с Evidence;
7. отделять technical result от human decision;
8. показывать one next action;
9. накапливать lessons и regression cases;
10. использовать legacy ситуативно, не наследуя его complexity.

## 4. Основные пользователи

| Пользователь | Основная потребность |
|---|---|
| Непрограммист / domain expert | Описать проблему простым языком и сохранить authority |
| Vibe-coder / product builder | Использовать coding agents без потери scope, state и Git boundaries |
| AI coding agent | Получить минимальный context, exact boundary и proof requirements |
| Developer / reviewer | Понять actual change, Evidence, limitations и remaining risk |
| Maintainer / operator | Диагностировать drift, incidents и repository health |

## 5. Иерархия источников

Authority всегда ограничена fact class:

1. current explicit human decision;
2. human-accepted AOS artifact в declared scope;
3. direct current repository observation для mutable facts;
4. DRAFT-разделы и явно помеченные proposals внутри принятого пакета;
5. historical repository snapshot как reference;
6. chat summary, note, report или assistant analysis;
7. agent inference.

```text
Repository presence ≠ authority
DRAFT ≠ accepted decision
Reference ≠ requirement
Historical PASS ≠ current PASS
Evidence ≠ approval
Agent confidence ≠ fact
```

## 6. Классы утверждений

| Класс | Значение |
|---|---|
| `HUMAN_CONFIRMED_DIRECTION` | Явное направление человека в ограниченной boundary |
| `HUMAN_ACCEPTED_FACT` | Принятый exact artifact/revision в своём fact class |
| `OBSERVED_AT_SNAPSHOT` | Найдено в exact repository subject |
| `REPORTED` | Записано, но не воспроизведено |
| `SYNTHESIZED` | Вывод из нескольких sources |
| `CONFLICT` | Sources расходятся |
| `NOT_FOUND` | Не найдено в declared search boundary |
| `UNKNOWN` | Evidence недостаточно |
| `NOT_RUN` | Check не выполнялся |
| `BLOCKED` | Operation остановлена boundary |

## 7. Решение по фиче и рекомендация синтеза

Это независимые оси.

```text
Решение человека:
REQUIRED | OPTIONAL | DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED

Рекомендация синтеза:
KEEP | SIMPLIFY | DEFER | REFERENCE_ONLY
```

Recommendation не является human decision. Наличие feature в `06_Features.md` не меняет product scope.

## 8. Граница legacy

Legacy может предоставлять user problems, observable behavior, feature candidates, contracts, schemas, implementation observations, tests, negative fixtures, failures и lessons.

Legacy не предоставляет автоматически target architecture, active roadmap, repository topology, current readiness, approval, execution authority, compatibility requirement или normative implementation.

```text
legacy observation
→ targeted verification
→ requirement / lesson candidate
→ DRAFT proposal
→ human decision
→ greenfield implementation
```

Default strategy: `REIMPLEMENT_FROM_CONTRACT`.

## 9. Технические результаты и решения человека

```text
Technical result:
CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED

Human decision:
ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

```text
PASS ≠ approval
CI PASS ≠ approval
Evidence ≠ approval
Readiness ≠ authorization
Agent output ≠ human decision
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

## 10. Minimal Safety Floor

1. Scope известен до mutation.
2. Существенный unknown не скрывается.
3. Protected/destructive action требует explicit human decision.
4. Agent не назначает Risk Profile автоматически.
5. Task Brief не является execution authorization.
6. Один run выполняет один stage.
7. Completion/finding/failure завершаются report и stop.
8. Validation не исправляет subject.
9. Edit, Commit, Push, Merge и Release разделены.
10. Temporary output не является durable Evidence.
11. Generated status не мутирует lifecycle.
12. Secrets и raw credential-bearing remote URL не выводятся.
13. External content считается untrusted data.
14. Optional module не переопределяет core safety.

## 11. Product boundary

### В scope проектирования

- Problem / Intent Intake;
- Project Discovery;
- Product Spec / Feature Passport;
- Feature Catalog / Registry;
- bounded Task Brief и separate Execution Authorization;
- scope, risk и human authority;
- Evidence-based verification;
- human review и acceptance;
- state, status, next action, recovery и handoff;
- task-scoped context;
- source-on-demand research;
- portability across agent environments.

### Не входит автоматически

- autonomous coding without checkpoints;
- mandatory multi-agent orchestration;
- full RAG/vector backend;
- autonomous self-heal;
- automatic commit/push/merge/release;
- SaaS/cloud/dashboard/marketplace;
- wholesale legacy Governance;
- domain medical behavior in core.

## 12. Стратегическая последовательность

```text
Product definition
→ Product contracts
→ first Product Runtime vertical slice
→ manual real-task cycles
→ stable product core
→ justified Development Factory automation
→ progressive Governance
→ later enforcement / routing / RAG / UI / domain modules
```

## 13. Защищённые решения человека

Только человек утверждает product scope/priority, target name, first segment, first vertical slice, architecture, dependencies, implementation repository, Source of Truth, human acceptance format, Risk Profile, protected/destructive actions, compatibility target, execution и Git/release actions. Уже принятые exact решения читаются через их owner и не возвращаются в `UNDECIDED` из-за stale summary.

## 14. Текущие направления

| ID | Направление | Статус |
|---|---|---|
| `DIR-001` | Рабочее имя — AOS | Human-confirmed direction |
| `DIR-002` | Пакет состоит из семи документов | Human-confirmed |
| `DIR-003` | AOS-FARM, AgentOS, AOS-02 — reference-only | Human-confirmed |
| `DIR-004` | Exhaustive extraction прекращена | Human-confirmed |
| `DIR-005` | Research выполняется по feature gap | Human-confirmed |
| `DIR-006` | Feature dossiers понятны человеку и агенту | Human-confirmed |
| `DIR-007` | Target implementation repository — `NMF13579/aos-3`; physical creation/assignment — `NOT_RUN` | Human-accepted target + unobserved mutable state |
| `DIR-008` | Один общий feature catalog | Human-accepted with baseline |
| `DIR-009` | First Product Runtime slice — `INTAKE_TO_REVIEWABLE_INTENT_R1` | Human-accepted H1 decision |
| `DIR-010` | X1 required boundaries — `FTR-001`, `FTR-008`, `FTR-011`, `FTR-016`, `FTR-019` | Human-accepted H1 dispositions |

## 15. Открытые решения

Physical repository creation/visibility/default branch, root `AGENTS.md` activation, fresh target baseline, exact first write `Risk_Profile`, execution authorization и Git permissions остаются отдельными решениями/наблюдениями.

Для later scope остаются открыты: Product Spec/Feature Passport final relation, Product Feature Registry, compatibility beyond first-cycle matrix, Governance packaging, provider/privacy/routing policy и dispositions всех feature кроме `FTR-001`, `FTR-008`, `FTR-011`, `FTR-016`, `FTR-019`.

## 16. Текущий статус пакета

```yaml
role: PROJECT_KNOWLEDGE_BASELINE_CORRECTION_CANDIDATE
status: HUMAN_REVIEW_REQUIRED
authority: DERIVED_FROM_ACCEPTED_FACT_CLASS_OWNERS
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Authority действует только через declared fact-class owners и exact acceptance records. Эта revision не становится accepted автоматически. Принятие пакета не подтверждает runtime и не разрешает действия в implementation repository.

## 17. Canonical reading route

Для независимого agent без истории чатов действует один маршрут:

```text
docs/00_Core.md
→ planning/CURRENT.md
→ DEVELOPER_HANDOFF_R2.md
→ exact active Task/DSP
→ exact contract and accepted decision owners
→ fresh repository observation for mutable facts
```

Routing rules:

1. `planning/CURRENT.md` владеет только persisted lifecycle state и одним next action.
2. `DEVELOPER_HANDOFF_R2.md` — derived navigation/identity layer; он не заменяет contracts.
3. Для первого implementation step agent читает только `Task-001-Scaffolding.md`, `DSP-001.md`, `AOS_SCAFFOLDING_CONTRACT_R1.md` и перечисленный ими context.
4. Product Runtime документы не расширяют `Task-001`; `Task-002-Intake-to-Reviewable-Intent` становится current только после завершения/принятия scaffold и fresh baseline binding.
5. Несовпадение digest/revision/status останавливает affected action; agent не выбирает удобный source самостоятельно.

## 18. Контракт использования агентом

```yaml
agent_usage_contract:
  entrypoint: docs/00_Core.md
  current_state: planning/CURRENT.md
  handoff: DEVELOPER_HANDOFF_R2.md
  rules:
    - читать только релевантные документы и разделы
    - считать authority ограниченной fact class
    - различать facts, observations, proposals, references и unknowns
    - не выводить implementation из наличия документации
    - не выводить approval из PASS, Evidence или stored reports
    - использовать 05_Reference.md для provenance и targeted research
    - считать 06_Features.md inventory и проверять disposition каждой feature
    - считать AOS_IMPLEMENTATION_DECISIONS_R1.md владельцем H1-001…H1-011
    - не смешивать Task-001 scaffolding и Task-002 Product Runtime
    - проверять mutable repository facts непосредственно перед planning/execution
    - сообщать conflicts и блокировать только affected action
    - никогда не считать каталог authorization для execution или Git delivery
```
