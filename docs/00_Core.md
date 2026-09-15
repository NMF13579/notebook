---
package: AOS_Project_Knowledge_Baseline
package_revision: R7-RU
updated: '2026-09-15'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: FIRST_CORE_HUMAN_DECISIONS_HD_01_28
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_status: HUMAN_ACCEPTED_FACT
current_change_scope: FIRST_CORE_HD_01_28_ONLY
current_change_agent_review: PASS
current_change_agent_review_scope: DOCUMENTATION_AUTHOR_SELF_CHECK
current_change_human_review: ACCEPTED
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
implementation_repository: NMF13579/AOS-3
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

Default strategy: `REIMPLEMENT_FROM_CONTRACT`; для первого ядра действуют
HD-04/27 у [Architecture](02_Architecture.md#first-core-build-boundary).

## 9. Технические результаты и решения человека

Технический vocabulary принадлежит [Result Contract C-009](02_Architecture.md#technical-result-contract).
R5 устраняет прежнее включение HUMAN_REVIEW_REQUIRED в technical result:
это значение зрелости документа, а ожидание runtime-решения выражает WAIT_HUMAN.
Ни то ни другое не является technical PASS или human decision. Уточнение R5
принято для первого ядра по [HD-01](#scaffold-core-decisions); старые records
не получают новое значение автоматической конвертацией.

```text
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
6. Один effectful worker выполняет один `EXECUTE` или `CORRECT` по fresh exact
   Stage Envelope и после factual result останавливается; controller открывает
   следующий worker только по canonical state-machine transition и в пределах
   действующей Parent Task Authorization.
7. Stage completion/finding/failure завершаются report и stop этого worker. Task остаётся активной до доказанного completion predicate, явной паузы, Human Gate, отмены или доказанной невозможности.
8. Validation не исправляет subject. Finding может быть возвращён controller в diagnostic/correction loop, но mutation выполняет отдельный corrector по fresh envelope и создаёт новый candidate.
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

- unbounded autonomous coding without parent task authority, stage envelopes и
  controller checkpoints;
- mandatory multi-agent orchestration;
- full RAG/vector backend;
- broad autonomous self-heal вне заранее bounded diagnostic/correction loop;
- automatic commit/push/merge/release без применимой отдельной политики; узкое
  правило первого ядра HD-26 — [Development](03_Development.md#first-core-local-commit);
- SaaS/cloud/dashboard/marketplace;
- wholesale legacy Governance;
- domain medical behavior in core.

## 12. Уровни проектирования документации

AOS использует строгую иерархию уровней детализации (Documentation Levels). Документация определяет WHAT, а coding agent определяет reversible HOW:

1. **Concept**: Идея, целевые пользователи, границы.
2. **Architecture Contract**: Структура, слои, контракты I/O.
3. **Engineering Design (Implementation)**: Детали реализации, выбор библиотек, псевдокод (HOW). К этому уровню относятся: алгоритмы реализации, внутренние структуры данных, внутреннее представление состояния, runtime state layout, helper APIs, implementation classes, lock protocols, CAS, retry strategies, persistence mechanisms, journals, thread synchronization и другие обратимые инженерные решения. Подобные решения не являются частью архитектурной документации уровня Concept или Architecture Contract и принимаются coding agent во время реализации.

**WHAT / HOW boundary**: Пакет AOS останавливается до стадии Engineering Design. Документация не должна содержать детали реализации, псевдокод или иные элементы Engineering Design (HOW). Coding agent отвечает за обратимую техническую реализацию.

В модульном проектировании обязательность данных, семантика версии, единственный владелец состояния, защита от повторного эффекта и наблюдаемое восстановление являются гарантиями WHAT. Требование гарантии не предписывает CAS, locks, journal format, storage engine или wire serialization. Инженерные схемы предназначены для будущего runtime и не являются формой обязательной документационной процедуры. Новые уточнения состава и совместимости отмечаются DRAFT до соответствующего решения.

## 13. Жизненный цикл проектирования и мутации

- **Documentation Edit ≠ Runtime Mutation**: Редактирование текстового черновика (Documentation Edit) не является выполнением кода (Runtime Mutation) и не требует применения тяжелых инженерных проверок (Execution Authorization, Task Brief) до этапа реализации.
- **Global Design Freeze**: Состояние, при котором мутация пакета документации останавливается, и он признаётся Deliverable для стадии реализации. Любые изменения после фриза запрещены без явного Reopen.
- **Условия Reopen**: Если реализация заходит в тупик или обнаруживает критический изъян в архитектуре, процесс возвращается в стадию проектирования через явную процедуру Reopen.

## 14. Стратегическая последовательность

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

Для первого ядра принято scoped уточнение [порядка S0–K4 и dogfood](01_Product.md#scaffold-core-outcome)
по HD-01. Оно имеет приоритет в этой области; прежние последовательности и
acceptance вне неё сохраняют свои исходные subjects.

## 15. Защищённые решения человека

Только человек утверждает material Product/Architecture scope, priority, first
segment/slice, implementation repository, Source of Truth, human acceptance,
Risk Profile, protected/destructive actions и расширение authority. Обычный
обратимый HOW и малые зависимости первого ядра регулируются HD-12/13/25 ниже;
их выбор не требует отдельного Human Gate. Git-действия имеют собственную
политику; для первого ядра действует узкое правило HD-26 у Development.

## 16. Текущие направления

| ID | Направление | Статус |
|---|---|---|
| `DIR-001` | Рабочее имя — AOS | Human-confirmed direction |
| `DIR-002` | Пакет состоит из семи документов | Human-confirmed |
| `DIR-003` | AOS-FARM, AgentOS, AOS-02 — reference-only | Human-confirmed |
| `DIR-004` | Exhaustive extraction прекращена | Human-confirmed |
| `DIR-005` | Research выполняется по feature gap | Human-confirmed |
| `DIR-006` | Feature dossiers понятны человеку и агенту | Human-confirmed |
| `DIR-007` | Implementation repository первого ядра — `NMF13579/AOS-3` | Human decision HD-02; launch отдельно |
| `DIR-008` | Один общий feature catalog | Human-accepted with baseline |

## 17. Открытые решения

Для полного проекта остаются вопросы segment/domain, interface, Feature Registry, persistence, human decision authenticity, Risk Profile, toolchain/dependencies, compatibility, Governance и provider/privacy/routing. Product Spec/Feature Passport relation и first slice имеют отдельные зафиксированные решения для X1; их нельзя снова считать полностью неизвестными или распространять на новый scope без проверки применимости. Точное состояние для scaffold/core приведено [ниже](#scaffold-core-decisions).

## 18. Текущий статус пакета

```yaml
role: ACTIVE_PROJECT_KNOWLEDGE_BASELINE
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
implementation_authorization: NONE
git_authorization: NONE
```

Authority действует только в declared fact class. Принятие пакета не принимает каждую feature, не подтверждает runtime и не разрешает действия в implementation repository.

## 19. Контракт использования агентом

```yaml
agent_usage_contract:
  entrypoint: docs/00_Core.md
  rules:
    - читать только релевантные документы и разделы
    - перед созданием или изменением фичи/модуля проверять соответствие Development §25.4; подключение и удаление проверять по §25.5
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

<a id="scaffold-core-decisions"></a>

## 20. Scaffold/core: принятые решения и граница запуска

Источник — текущее явное сообщение пользователя «Integrate Human Decisions for
AOS First-Core Implementation into notebook», HD-01…28, 2026-09-15.
Это `HUMAN_ACCEPTED_FACT` в пределах выбранного первого ядра, а не результат
аудита, принятие всех модулей или разрешение запуска. [Привязка исходного
R7 candidate](05_Reference.md#first-core-human-source) учитывает working bytes,
а не только HEAD. Семантика решений записана у owners ниже; HD-IDs служат
трассировке этого сообщения, не новым каталогом задач или decision service.

HD-01 принимает текущий first-core scope у [Product](01_Product.md#first-core-selected-scope),
R7 handoff и C-015/C-016 вместе с V3 loop; противоречащие этому scoped принятию
прежние фразы «ожидает SC-DEC-01» больше не действуют для этого предмета.
Сохранённые метки SCAFFOLD_CORE_DRAFT/R5/R7 обозначают происхождение редакции,
а не отменяют HD-01. Принятие не распространяется на остальные MODULAR_DRAFT,
поздние сценарии семейств, иные proposals или будущие изменения contracts.

### Репозиторий и нормативная граница — HD-02, HD-05, HD-15

Implementation/build repository первого ядра — `NMF13579/AOS-3` (HD-02).
Notebook остаётся knowledge repository: runtime здесь запрещён, текущая задача
разрешает только документацию. Назначение target не разрешает его изменение.

Для новой сборки нормативны current accepted Product, Architecture Contracts,
Development rules и authority boundaries notebook (HD-05). Старые AOS-3
Feature-development/artifact-process/lifecycle/governance документы —
`REFERENCE_ONLY`. Малый локальный router/handoff и repository-specific run/test
инструкции могут направлять к notebook и конкретизировать HOW, но не становятся
конкурирующими owners. Копировать весь notebook как вторую canonical базу не нужно.

При конфликте с legacy выигрывает применимый принятый notebook contract (HD-15).
DRAFT/PROPOSAL/UNKNOWN/CONFLICT вне принятого HD-01 scope не повышаются автоматически:
показать exact gap и блокировать только зависимое действие. Исторические frozen,
portable, X1 records и их Evidence не переписываются; их прежний UNASSIGNED и
исходная acceptance относятся к старым subjects. Текущий target выбран этим
сообщением, не извлечён из старого PASS или blueprint.

<a id="first-core-data-policy"></a>

### Доступ, зависимости и существенные решения — HD-11…13, HD-25

**HD-11 — LOCAL_FIRST.** По умолчанию доступны только разрешённый local repository,
локальные файлы, tests/tools и task-scoped state/evidence. Новый network/API/provider,
account/credential/secret, внешняя DB/service или recipient требуют отдельной
явной Human authorization. Наличие token/account не даёт доступа. До запроса
объяснить необходимость, provider/service, читаемые/передаваемые данные, эффект
и наличие локальной альтернативы. Выбор Codex не разрешает любые его connections
или data routes; фактический существующий допуск и путь данных проверяются при
preflight. Для нового внешнего доступа действует это правило.

**HD-12 — bounded dependencies.** Агент самостоятельно выбирает малую обратимую
локальную библиотеку, если она не требует external service, не меняет существенно
security boundary/runtime architecture, не ухудшает существенно переносимость,
не несёт material licensing/maintenance risk и reasonably replaceable.
Материальная dependency требует решения человека. Выбор библиотеки не разрешает
новый network download: доступ проверяется отдельно по HD-11. Отдельного gate на
каждую обычную техническую библиотеку нет.

**HD-13 — новый материальный механизм.** Перед новым service, queue family,
registry, daemon, database, persistent subsystem, control layer, agent role или
широким enforcement показать наблюдаемый сбой либо дорогой/необратимый риск,
недостаточность существующих механизмов, минимальную альтернативу, стоимость и
последствия. Такой механизм требует Human decision. Малую обратимую техническую
проблему исследовать ограниченным экспериментом в действующей authority.
Реализация уже принятой локальной очереди/регистрации и durable state остаётся
HOW в их гарантиях: правило не требует нового разрешения на каждый lock/file
или внутреннее представление, но не разрешает новую постоянную подсистему.

**HD-25 — Human-only Product/Architecture.** Material выбор возвращается одним
decision-ready вопросом: issue/gap, почему действующего contract недостаточно,
bounded варианты, trade-offs/последствия и рекомендация. Обычные обратимые HOW
выбирает агент; классификация не превращает предпочтение реализации в новый gate.

<a id="first-core-human-capture"></a>

### Решение человека и хранение основания — HD-23, HD-24

**HD-23.** Решение действительно только при явной выдаче человеком через
допустимый текущий канал по конкретному subject/version/action. Сохраняются
само решение, exact identity/revision, достаточный по принятой host-модели
source/channel identity, необходимые time/ordering и allowed next route.
PASS, Evidence, generated text, old reports, commit messages, agent-written
`approved: true` и принятие другого subject не заменяют этот источник.
Это требование к существующему C-011/trusted capture, не новый authority record.
Фактическая пригодность capture Codex — UNKNOWN, проверка NOT_RUN.

**HD-24.** Долговременно хранится decision-relevant минимум: accepted result
identity, Human decisions, достаточное verification Evidence, material limitations,
unresolved unknowns, recovery/rollback данные, значимые findings и созданные
lessons/regression cases. Временная подробная история/логи могут очищаться, когда
не нужны для этих целей и допустимого resume/dedup. Не требуется сохранять каждый
trace навсегда. Очистка использует отдельно покрытые exact paths/операцию и
retention boundary; это сообщение не выполняет deletion и не разрешает потерять
единственное основание решения, проверки либо неизвестного эффекта.

### SC-DEC: решение отдельно от фактической пригодности

| ID | Принятое решение / owner | Статус и точный остаток |
|---|---|---|
| SC-DEC-01 | HD-01: полный предложенный first-core package S0–K4, 13 core-срезов, R7/C-015/C-016/V3 | ACCEPTED. Scope/contracts выбраны; не все 33 FTR и не runtime authority |
| SC-DEC-02 | AOS-3; [изоляция/стратегия/профиль](02_Architecture.md#first-core-build-boundary); LOCAL_FIRST/HD-12; B1 и budget у Development | HUMAN_ACCEPTED_FACT для policy. OPEN только implementation-time binding: branch/worktree/base, actual OS/runtime/architecture, adapter, paths, конечные queue/resource numbers и commands. Агент выбирает/наблюдает их в принятых пределах, без повторного product выбора |
| SC-DEC-03 | [Codex-first](02_Architecture.md#scaffold-core-host), HD-11/23/24; durable state и обязательный [resume proof](03_Development.md#first-core-autonomy-proof) | HUMAN_ACCEPTED_FACT для host/data/retention/resume requirements. Реальные capture/admission/data routes/wake UNKNOWN; conformance и interruption/resume NOT_RUN |
| SC-DEC-04 | Будущая exact parent task и отдельный runtime launch | NOT_RUN. Ожидается explicit Human authorization: Risk Profile, mutation paths, operations/effects, limits/expiry и текущий допуск. Их этот пакет не выдаёт |

Выбранные policy-level решения SC-DEC-01…03 повторно не запрашиваются. Настройка,
наблюдение и conformance не закрываются словом ACCEPTED. Неожиданный material
conflict или новый external access блокирует только затронутый путь.

[HD-26](03_Development.md#first-core-local-commit) задаёт будущую standing policy
ACCEPT exact first-core candidate → один local Commit; она не является разрешением
Commit сейчас и не относится к этой documentation task. Push/Merge/Release
требуют каждый отдельной явной Human authorization. Technical completion,
Human acceptance, local commit result и runtime readiness остаются разными фактами.
