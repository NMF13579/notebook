---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-07-26'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: c02141ea44840f88b10285e66d641d6508653989
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
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_acceptance: ACCEPTED
implementation_authorization: NONE
git_authorization: NONE
```

Пакет принят человеком как текущая база знаний для анализа, проектирования и targeted research. Принятие knowledge baseline не разрешает mutation, implementation или Git delivery.

## 2. Идентичность проекта

```yaml
project_name: AOS
working_description: human-directed AI-assisted software development system
current_work_mode: HUMAN_ACCEPTED_DOCUMENTATION_BASELINE
knowledge_repository: NMF13579/notebook
knowledge_branch_label: dev
active_package_path: docs/
implementation_repository: UNASSIGNED
legacy_projects: [AOS-FARM, AgentOS, AOS-1, AOS-02]
legacy_authority: NONE
```

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

Только человек утверждает product scope/priority, target name, first segment, first vertical slice, architecture, dependencies, implementation repository, Source of Truth, human acceptance format, Risk Profile, protected/destructive actions, compatibility target, execution и Git/release actions.

## 14. Текущие направления

| ID | Направление | Статус |
|---|---|---|
| `DIR-001` | Рабочее имя — AOS | Human-confirmed direction |
| `DIR-002` | Пакет состоит из семи документов | Human-confirmed |
| `DIR-003` | AOS-FARM, AgentOS, AOS-02 — reference-only | Human-confirmed |
| `DIR-004` | Exhaustive extraction прекращена | Human-confirmed |
| `DIR-005` | Research выполняется по feature gap | Human-confirmed |
| `DIR-006` | Feature dossiers понятны человеку и агенту | Human-confirmed |
| `DIR-007` | Implementation repository — `UNASSIGNED` | Current safe state |
| `DIR-008` | Один общий feature catalog | Human-accepted with baseline |

## 15. Открытые решения

First Product Runtime domain, first vertical slice, interface, Product Spec/Feature Passport relation, Product Feature Registry, Project Memory persistence, human decision authenticity, Risk Profile vocabulary, language/toolchain/dependencies, compatibility scope, Governance packaging и provider/privacy/routing policy.

## 16. Текущий статус пакета

```yaml
role: ACTIVE_PROJECT_KNOWLEDGE_BASELINE
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
implementation_authorization: NONE
git_authorization: NONE
```

Authority действует только в declared fact class. Принятие пакета не принимает каждую feature, не подтверждает runtime и не разрешает действия в implementation repository.

## 17. Контракт использования агентом

```yaml
agent_usage_contract:
  entrypoint: docs/00_Core.md
  rules:
    - читать только релевантные документы и разделы
    - считать authority ограниченной fact class
    - различать facts, observations, proposals, references и unknowns
    - не выводить implementation из наличия документации
    - не выводить approval из PASS, Evidence или stored reports
    - использовать 05_Reference.md для provenance и targeted research
    - считать 06_Features.md inventory и проверять disposition каждой feature
    - проверять mutable repository facts непосредственно перед planning/execution
    - сообщать conflicts и блокировать только affected action
    - никогда не считать каталог authorization для execution или Git delivery
```
