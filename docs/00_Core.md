---
package: AOS_Project_Knowledge_Baseline
package_revision: R7-RU
updated: '2026-09-13'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: AOS_MODULE_PROTOCOL_CONNECTORS_QUEUES_R7
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_status: SCAFFOLD_CORE_DRAFT
current_change_agent_review: PASS
current_change_agent_review_scope: DOCUMENTATION_AUTHOR_SELF_CHECK
current_change_human_review: NOT_RUN
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

Технический vocabulary принадлежит [Result Contract C-009](02_Architecture.md#technical-result-contract).
R5 устраняет прежнее включение HUMAN_REVIEW_REQUIRED в technical result:
это значение зрелости документа, а ожидание runtime-решения выражает WAIT_HUMAN.
Ни то ни другое не является technical PASS или human decision. Уточнение R5
остаётся частью SCAFFOLD_CORE_DRAFT до принятия exact revision; старые records
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
- automatic commit/push/merge/release;
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

Для нового scaffold/core подготовлено scoped уточнение [порядка S0–K4 и dogfood](01_Product.md#scaffold-core-outcome). Оно остаётся SCAFFOLD_CORE_DRAFT до SC-DEC-01; этот стратегический baseline не считается молча отменённым документационной правкой.

## 15. Защищённые решения человека

Только человек утверждает product scope/priority, target name, first segment, first vertical slice, architecture, dependencies, implementation repository, Source of Truth, human acceptance format, Risk Profile, protected/destructive actions, compatibility target, execution и Git/release actions.

## 16. Текущие направления

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

## 20. Scaffold/core: применимость решений и граница запуска

Статус новых уточнений — `SCAFFOLD_CORE_DRAFT`. Текущая инструкция человека разрешает выполнение документационного плана и подтверждает направление «автономная разработка scaffold и ядра; поздние фичи готовятся отдельно». Она не принимает автоматически 13 CORE-семейств, target/stack, host и runtime authorization. Прежние принятые facts сохраняют свою область; audit и self-check не расширяют её.

| Предмет | Основание и текущее применение |
|---|---|
| Владение Product Spec/Passport и первый product slice | X1 record фиксирует `X1-DR-001=A` и `X1-DR-002=A`: cross-feature facts в Spec, feature behavior в Passport; FTR-001 до reviewable, human-confirmed Intent. Исходный X1 selection сохраняется. Исходное подтверждение не подменяет trusted capture будущего runtime и не выбирает весь новый core |
| Frozen Global Design / portable package | Exact документация принята в исходных fact classes. Portable acceptance явно сохраняет `implementation_repository: UNASSIGNED` и отсутствие roadmap activation. Freeze не отменяется |
| AOS-3 / Python / local monolith / local persistence | Прежний blueprint сообщает о таких решениях и ссылается на принятую migration map. Это основание предлагаемого профиля, а не текущий task binding к репозиторию. Современный target/branch/состояние и применимость профиля к новому scope ещё не установлены |
| Новый модульный состав | Человек выбрал группировку FTR-005+022 в модуль «Архитектурные решения и patterns». Остальной состав и полные contracts остаются в [MOD-DEC-01](01_Product.md#modular-decisions); выбор группировки не меняет исходные X1 dispositions и не расширяет S0–K4 |
| Workflow | Canonical complete-task semantics уже описаны. Предложение раннего внешнего loop и нового handoff уточняет их применение к scaffold, а не объявляет существующим host или AOS runtime |

Exact locators, bindings и ограничения доказательств находятся у [Reference](05_Reference.md#scaffold-core-sources). В частности, X1 record сохраняет собственную оговорку о raw-record confirmation; совпадение bytes её не снимает. Здесь не создаётся новое свидетельство человеческого сообщения.

Человек задал требование максимальной переносимости между ОС и использование
macOS для себя; затем явно выбрал вариант «macOS первой»: переносимая архитектура
обязательна, Linux/Windows — целевые платформы с последующим подтверждением.
Это закрывает только требование переносимости и порядок проверки ОС в SC-DEC-02.
Повторное решение по ним не требуется. Версии ОС/runtime, target, adapter, host
и полномочия этим выбором не определены. Product owner — [переносимость](01_Product.md#core-os-portability).

Человек потребовал автономную сборку каждого выбранного модуля целиком,
включая его внутренние фичи и стыки, без промежуточного управления человеком
после согласования входного пакета. Требуемый результат определён у
[Product](01_Product.md#autonomous-module-outcome), готовность и исполнение — у
[Development](03_Development.md#autonomous-module-development). Это направление
не принимает автоматически contracts всех модулей и не выдаёт runtime authority.

Человек выбрал явные lifecycle-переходы внутри одной автономной задачи.
Их конкретный contract R5/V3 описан в [Development](03_Development.md#core-lifecycle-transitions);
выбор модели не означает принятия всего набора contracts или runtime launch.

Человек выбрал смешанный обмен: быстрые read-only запросы через коннектор,
команды с эффектами/отложенная работа и события через сохраняемую очередь.
Минимальные локальные коннекторы и очередь входят уже в первое ядро. R7
уточняет обязанности существующих 13 core-семейств; FTR-007 backlog, полный
installer и plugin framework не становятся обязательными. Требование и сроки
выбраны; конкретные C-015/C-016 и расширенный handoff остаются DRAFT до принятия.
Их owners — [Product](01_Product.md#core-connector-outcome) и
[Architecture](02_Architecture.md#module-connector-queue); способ хранения,
toolchain, численные limits и target не выбираются этим решением.

Оставшиеся решения сгруппированы ниже. Это вопросы для принятия подготовленного результата, не выданные агентом разрешения. Product scope принадлежит Product/Features, interfaces — Architecture, запуск — Development.

| Вопрос | Рекомендация | Альтернатива и последствие | Требуемый ответ / срок | Статус |
|---|---|---|---|---|
| SC-DEC-01 — scope и contracts | Принять минимальные 13 CORE-семейств, S0–K4, текущий handoff R7, C-015/C-016 и [набор V3](02_Architecture.md#core-loop-v3); внешний development loop с S0, UX dogfood отдельно | X1-only сохраняет меньший scope, но не закрывает полный core loop; frozen bytes не меняются | ACCEPT/изменения для exact owner/brief revision до runtime launch по этому набору | WAIT_HUMAN; документационная реализация не означает принятие |
| SC-DEC-02 — target и профиль | Указать implementation repository/worktree/base; предложены local modular monolith, Python 3.12+, CLI и минимальный локальный execution adapter с переносимым интерфейсом. macOS проверяется первой, переносимость обязательна | Другой target/stack/adapter требует проверки contracts; существующий AOS-3 требует inventory без пересоздания. Linux/Windows подтверждаются позднее; public release не требуется | Exact target/base, версия macOS/runtime и архитектура машины, adapter/средство исполнения, dependency policy, support limits, finite queue profile и state/evidence paths до launch; check commands фиксирует агент до check | OPEN по перечисленным параметрам; переносимость и порядок ОС уже заданы человеком |
| SC-DEC-03 — host и данные | Сначала оценить имеющийся host на V3; выбрать проверяемые capture/admission/checkpoint/continuation. Предложение data policy: только объявленные task inputs, recipients и state/evidence paths, без неразрешённых secrets/external effects | Другой host требует своей проверки; manual resume даёт assisted mode, не полную автономность. LOCAL_ONLY продукта не определяет data flow coding host | Identity host, trusted capture, resume mechanism, providers/recipients, разрешённые данные/доступ и retention до conformance probes и launch | OPEN; пригодность текущего host UNKNOWN. Выбор не равен доказательству conformance |
| SC-DEC-04 — runtime launch | После принятия exact brief и fresh preflight выдать отдельно Risk Profile, paths/operations/effects, limits/expiry и human-only boundaries; включить покрытую служебную инициализацию state, регистрации и очереди | Более узкая authority блокирует только непокрытые действия; Git/release остаются отдельно | Конкретная task/revision и отдельная current authorization непосредственно перед runtime launch | NOT_RUN; полномочия и Risk Profile этим документом не выданы |


Техническое завершение интервала не включает human acceptance продукта. Проверка поведения capture/decision использует явно синтетические fixtures отдельно от настоящих решений. Если runtime взаимодействует с реальным человеком, его ответ должен поступить по принятому каналу; агент не генерирует его ради прохождения E2E.

Обратимые классы, algorithms, internal schemas, storage mechanisms и test organization выбирает coding agent в принятых границах. Новый service/provider, dependency вне согласованной политики, другой public contract либо security boundary требует отдельного решения. Находка обычного дефекта ведёт в разрешённую correction; она не требует повторного принятия всего проекта.
