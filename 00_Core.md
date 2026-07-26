# 00 — AOS Core


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Назначение документа

Этот документ задаёт общий контекст reconstruction package: identity проекта, authority, source precedence, claim/status semantics, минимальные safety boundaries и открытые границы. Он не утверждает product scope, architecture, dependencies или implementation repository.

## 2. Цель AOS

`FACT — human-confirmed direction.` Новый AOS должен стать понятной человеку системой для управления AI-assisted разработкой: от идеи и project context до bounded change, technical Evidence, human review и отдельно разрешённой Git delivery.

Основная ценность:

```text
не максимальная автономность
→ а снижение стоимости постановки, координации, проверки и продолжения работы
```

AOS должен помогать:

1. превратить свободное намерение в проверяемую задачу;
2. сохранить контекст между sessions и agent environments;
3. показать current state и один следующий безопасный action;
4. выполнить только bounded authorized change;
5. отделить technical result от human acceptance;
6. использовать legacy ситуативно, не наследуя его complexity;
7. накопить reusable patterns, failures и tests.

## 3. Active project identity

```yaml
project_name: AOS
current_work_mode: DOCUMENTATION_RECONSTRUCTION
knowledge_repository: NMF13579/notebook
knowledge_subtree: /AOS
expected_branch: dev
expected_branch_verified: false
knowledge_repository_role: ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY
implementation_repository: UNASSIGNED
execution_authorized: false
human_review_required: true
```

`expected_branch` — expectation, а не current Git fact. Перед repository claims или writes требуется проверять repository, worktree, branch, HEAD, baseline, working tree status и diff.

## 4. Source precedence

Применяется domain-scoped precedence:

1. explicit human decision — только в указанной decision boundary;
2. human-accepted canonical repository document — только в его fact class;
3. current Project Instructions — для agent behavior и safety;
4. `DRAFT` documents — proposals;
5. research — analytical support;
6. legacy repositories, chats, reports и generated artifacts — `READ_ONLY_REFERENCE`, `authority: NONE`.

```text
Repository presence ≠ authority
DRAFT ≠ accepted decision
Research ≠ architecture
Reference ≠ requirement
Evidence ≠ approval
Historical PASS ≠ current PASS
```

Canonical artifact требует одновременно:

- explicit fact class;
- `canonical` status;
- human acceptance exact artifact/revision;
- отсутствия unresolved higher-priority conflict.

## 5. Legacy boundary

Reference-only sources:

- `NMF13579/AOS-FARM`;
- historical `NMF13579/AOS-02`;
- `AgentOS`, `AOS-1`, `AgentOS Next`;
- старые chats, plans, reports, recovery packages и extracted corpora.

Из них допустимо извлекать:

- product intent и user problems;
- observable behavior;
- feature candidates;
- interfaces и contracts;
- tests и negative cases;
- failures, anti-patterns и lessons;
- implementation observations.

Нельзя автоматически переносить:

- target architecture и repository topology;
- dependencies, database, registry или Control Plane;
- lifecycle/status model;
- approval или execution authority;
- current readiness;
- legacy code как normative implementation.

Default reuse policy:

```text
legacy observation
→ targeted verification
→ lesson / requirement candidate
→ DRAFT proposal
→ human decision
→ greenfield implementation
```

## 6. Claim classes

| Class | Значение | Правило |
|---|---|---|
| `FACT` | Прямо подтверждено identified source или current inspection | Указывать source и temporal scope |
| `INFERENCE` | Вывод из facts | Не выдавать за fact |
| `PROPOSAL` | Product/architecture/process candidate | Scope effect только после human decision |
| `UNKNOWN` | Evidence недостаточно | Сохранить вопрос и resolution mode |
| `NOT_FOUND` | Не найдено в declared search boundary | Не считать глобальным отсутствием |
| `NOT_RUN` | Check не выполнялся | Никогда не повышать до `PASS` |
| `BLOCKED` | Нет required source/decision/permission | Остановить affected operation |

Для исторических capability observations дополнительно:

```text
VERIFIED_WORKING
PARTIALLY_WORKING
DESIGN_ONLY
BROKEN
OBSOLETE
RECOVERY_SPECIFIC
UNKNOWN
```

Эти statuses относятся к reference mechanism, а не к новому AOS.

## 7. Technical results и human decisions

Technical results:

- `PASS` — declared check выполнен;
- `FAIL` — declared check не выполнен;
- `UNKNOWN` — данных недостаточно;
- `NOT_RUN` — check не выполнялся;
- `BLOCKED` — operation остановлена boundary;
- `HUMAN_REVIEW_REQUIRED` — Evidence готова для решения человека.

Human decisions:

- `ACCEPT`;
- `NEEDS_CHANGES`;
- `REJECT`;
- `DEFER`.

Инварианты:

```text
PASS ≠ approval
Evidence ≠ approval
CI PASS ≠ approval
Readiness ≠ approval
UNKNOWN/BLOCKED ≠ OK
NOT_RUN ≠ PASS
Agent output ≠ human decision
```

## 8. Minimal Safety Floor

Minimal Safety Floor действует всегда, но не должен превращаться в full Governance platform.

1. Scope известен до mutation.
2. Material unknown не скрывается.
3. Protected/destructive action требует human decision.
4. Risk Profile назначает человек.
5. `PLAN`, `EXECUTE`, `VALIDATE`, `REVIEW` разделены.
6. Один run — один stage; после completion/finding/failure — report и stop.
7. Validation не исправляет artifact.
8. `Edit`, `Commit`, `Push`, `Merge`, `Release` — отдельные authorizations.
9. Temporary outputs не являются durable Evidence или human decisions.
10. Generated views, indexes и dashboards не заменяют Source of Truth.

## 9. Стратегическое sequencing

```text
Product definition
→ Product contracts
→ Product Runtime vertical slice
→ manual cycles and validation
→ stable product core
→ justified Development Factory
→ progressive Governance
→ later Runtime Enforcement / RAG / routing / SaaS / domain modules
```

Подтверждённые направления:

- Product Runtime раньше Development Factory;
- manual workflow раньше automation;
- contract-first и observable behavior;
- shortest safe path;
- targeted feature research вместо exhaustive extraction;
- new implementation по умолчанию `REIMPLEMENT_FROM_CONTRACT`.

## 10. Protected human decisions

Только человек принимает:

- product scope и feature priority;
- architecture и dependencies;
- Source of Truth и canonical artifacts;
- implementation repository;
- Risk Profile;
- material scope expansion;
- protected/destructive changes;
- execution;
- commit, push, merge и release.

## 11. Current confirmed directions

| ID | Direction | Classification |
|---|---|---|
| `DIR-001` | Использовать имя `AOS` до отдельного rename | `FACT` |
| `DIR-002` | Knowledge package состоит ровно из `00_Core.md`…`06_Features.md` | `FACT` для текущего artifact |
| `DIR-003` | Legacy repositories — read-only references | `FACT` |
| `DIR-004` | Exhaustive extraction прекращена как low-ROI | `FACT` |
| `DIR-005` | При реализации feature использовать targeted repository research | `FACT` |
| `DIR-006` | Feature descriptions должны быть понятны человеку и agent | `FACT` |
| `DIR-007` | Implementation repository остаётся `UNASSIGNED` | `FACT` current safe state |

## 12. Open boundaries

- first Product Runtime domain и first vertical slice — `UNKNOWN`;
- exact interface (`CLI`, local app, service, mixed) — `UNKNOWN`;
- persistence model Project Memory — `UNKNOWN`;
- implementation language/toolchain/dependencies — `UNASSIGNED`;
- legacy compatibility target — `UNKNOWN`;
- Governance packaging — `PROPOSAL`;
- human decision authenticity mechanism — `UNKNOWN`;
- runtime enforcement admission point — `DEFERRED`.

## 13. Agent reading contract

Для одной feature agent должен читать:

```text
00_Core.md
→ relevant Product context из 01_Product.md
→ feature dossier из 06_Features.md
→ shared contracts из 02_Architecture.md
→ workflow/tests из 03_Development.md
→ related failures из 04_Lessons.md
→ source/research map из 05_Reference.md
```

Загрузка всего legacy repository или всей chat history по умолчанию запрещена как неэффективная и рискованная.
