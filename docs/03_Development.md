---
package: AOS_Project_Knowledge_Baseline
package_revision: R7-RU
updated: '2026-09-16'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: FIRST_CORE_DEVELOPMENT_PROCESS_SIMPLIFICATION
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_status: HUMAN_ACCEPTED_FACT
current_change_scope: FIRST_CORE_DEVELOPMENT_WORKFLOW_DOCUMENTATION_ONLY
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
audited_source_blob_sha: c60c39b4bee652cde2fd2e38f81dc12b498aa817
active_path: docs/03_Development.md
document_language: ru
technical_identifiers_language: en
document_role: CANONICAL_DEVELOPMENT_WORKFLOW
authority_scope:
- task_workflow
- stage_boundaries
- validation_rules
- reporting_rules
- git_action_boundaries
---

# 03 — Разработка

## 1. Граница статуса

Документ задаёт принятый normative workflow для подготовки и проверки работы. Он не является Task Brief, Execution Authorization или разрешением на конкретную mutation либо Git-operation.

## 2. Сквозная модель проектирования и реализации

Процесс строго разделен на проектирование документации и runtime-реализацию.

### Проектирование документации и область deliverable

Ниже сохранён маршрут exact Global Design Package. Его Freeze относится к указанным трём файлам `AOS/`. Для нового scaffold/core документационная задача идёт от current owners к bounded [brief](../workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md); содержание first-core handoff принято HD-01, а runtime launch отдельно ожидает [SC-DEC-04](00_Core.md#scaffold-core-decisions). Подготовка нового DRAFT не меняет frozen bytes и не предоставляет им новую authority.

```text
Knowledge Baseline
↓
Workspace (Source Synthesis + Drafts)
↓
Pass 1 (Product Model)
↓
Structural Review
↓
Pass 2 (Architecture Contracts + Engineering Workflow Semantics)
↓
Integration Review
↓
Global Design Freeze
↓
Publish to AOS (Deliverable)
```

### Runtime Implementation (Реализация)

Для принятого exact implementation input и отдельной runtime authority:

```text
Implementation Roadmap
↓
Slice
↓
Task
↓
bounded Task Brief
→ repository preflight
→ parent task authority for exact effectful worker actions
→ complete-task controller
→ fresh EXECUTE envelope → smallest scoped implementation → report/stop worker
→ CHECK → DIAGNOSE/CORRECT loop when required
→ separate FINAL_VALIDATE on exact candidate
→ REVIEW
→ human decision
→ separate Commit / Push / Merge / Release
→ handoff and lesson proposal
```

## 3. Семантические различия

Analysis ≠ execution; Plan ≠ implementation; file presence ≠ behavior; readiness ≠ authorization; execution ≠ verification; test PASS ≠ acceptance; CI PASS ≠ approval; verification ≠ commit permission; Commit ≠ Push ≠ Merge ≠ Release; UNKNOWN ≠ OK; NOT_RUN ≠ PASS.

## 4. Условия входа

Feature должна иметь purpose/value, actors, trigger/preconditions, I/O, happy path, states, failures/recovery, dependencies, authority boundaries, acceptance, negative scenarios, unknowns и targeted reference questions.

## 5. Процесс, масштабируемый по риску

### Низкий / trivial

Scope → one reversible change → focused check → concise report. No redundant architecture chain.

### Средний

Explicit acceptance, short plan, relevant regression и handoff.

### Высокий / protected

Pinned baseline, inventory, protected paths, explicit authorization, rollback, Evidence package и human review.

### Критический / destructive / sensitive

Stop-before-action, least privilege, data/provider boundary, recovery plan и explicit human decision.

## 6. Feature-specific documentation package

Для feature, чей exact `feature_id` выбран человеком либо явно привязан к документационной задаче current human instruction или human-accepted artifact, применяется bounded authoring-механика внутри этого canonical workflow:

```text
Selected Feature
↓
Skeleton
↓
Saturation
↓
Harmonization / Review
↓
READY_FOR_HUMAN_REVIEW
```

Это не отдельный lifecycle, не замена Global Design workflow из раздела 11 и не Runtime stage. Механика создаёт reviewable feature-specific documentation package, но не принимает feature или architecture, не разрешает implementation и не предоставляет Git authority.

### Граница package

До authoring агент bind exact `feature_id`, текущий human disposition, цель package, upstream owners/sources, allowed paths и material gaps. Ядро package — feature-specific Feature Contract / Feature Passport. Отдельный Architecture Contract нужен при material boundary/state/ownership или external contract, DRAFT ADR — при decision-ready выборе между значимыми вариантами, engineering handoff/brief — когда принятые product/architecture contracts требуется передать будущей реализации. Product crosswalk или любой из этих элементов выделяется в отдельный artifact только при distinct fact class/owner, independent review boundary или потере однозначности внутри ядра. Один artifact может совмещать несколько логических разделов, но не может смешивать их authority.

Package map, index или review summary остаются derived navigation/Evidence и не становятся владельцами product или architecture facts. DRAFT ADR может подготовить вопрос, варианты, trade-offs и Evidence, но `selected_option` остаётся незаполненным до exact human decision. Engineering artifact может фиксировать принятые contract shapes, examples, constraints, acceptance и negative cases; он не выбирает repository, toolchain, internal structures, storage, adapters, algorithms или иное implementation HOW без accepted upstream decision и не является Execution Authorization.

### Skeleton

Сначала создать целостный каркас всего package: inventory artifacts/sections, role и fact owner каждого элемента, source/provenance, связи, expected outputs, review criteria и видимые `UNKNOWN`/gaps. Каркас должен покрывать обязательные поля feature dossier и требуемые conditional artifacts до глубокой детализации. Пустое место помечается `UNKNOWN`, `NOT_APPLICABLE` или explicit decision request, а не заполняется предположением.

### Saturation

Затем насыщать каркас в порядке authority: current human decisions → accepted canonical sources → current repository observations в разрешённой boundary → targeted research/reference findings → явно помеченные synthesis/inference. Заполнять purpose/users, trigger/preconditions, behavior, I/O, flow/states, failures/recovery, dependencies, constraints, acceptance и negative scenarios только до необходимой feature-specific глубины. Legacy используется read-only для exact gap и не переносит автоматически topology, status, approval или implementation HOW.

### Harmonization / Review

После насыщения снова рассматривать exact artifacts как один package. Проверить vocabulary, provenance, owner boundaries, cross-links, traceability `intent → behavior → contracts → acceptance/negative cases`, согласованность состояний и отсутствие скрытого HOW или authority expansion. Внутри той же authorized documentation task агент может исправлять только bounded defects: терминологию, ссылки, дублирование, formatting и пропуски, однозначно восполнимые из уже authoritative upstream source. Новый scope, material conflict, отсутствующее human-only решение или новая architecture choice требуют explicit finding/decision и не исправляются догадкой.

Harmonization / Review является authoring-фазой, а не независимым `VALIDATE`: bounded corrections здесь допустимы. Если risk требует separate validation, после authoring фиксируется exact candidate, а validator работает read-only и не исправляет subject.

### Readiness gate

Package получает outcome `READY_FOR_HUMAN_REVIEW`, только если:

1. exact subject, inventory, owners, sources и связи определены;
2. обязательные feature-specific fields достаточно насыщены для заявленной human review;
3. необходимость или отсутствие отдельных Architecture/ADR/Engineering artifacts обоснованы;
4. material contradictions отсутствуют, а remaining unknowns видимы и ограничивают только зависимые claims;
5. semantic, cross-document и focused mechanical checks прошли;
6. report перечисляет Evidence, findings, unknowns, `NOT_RUN` и одно следующее human action.

Минимальные checks охватывают exact feature/disposition binding, обязательные dossier fields, owner/source/status markers, rationale conditional artifacts, traceability, explicit unknown/decision requests, Markdown links/fences и отсутствие скрытых authority grants или implementation HOW. Незакрытое human-only decision совместимо с `READY_FOR_HUMAN_REVIEW` только когда package делает exact decision request и не заявляет зависимый от решения вывод; иначе readiness остаётся `BLOCKED` или `UNKNOWN` в затронутой boundary.

`READY_FOR_HUMAN_REVIEW` — package-readiness outcome, а не новый owner document maturity: artifacts сохраняют canonical maturity/status до human decision. Technical `PASS` — Evidence проверки. `PASS ≠ approval`; `READY_FOR_HUMAN_REVIEW ≠ HUMAN_ACCEPTED`; ни один из этих результатов не означает implementation readiness, Execution Authorization или Git permission.

### Targeted reconstruction через feature

1. Bind feature из `06_Features.md`, уже выбранную или явно названную человеком; не изменять её disposition агентом.
2. Подтвердить user/problem/outcome/disposition.
3. Сформулировать exact gaps.
4. Bind legacy repository/ref/SHA/paths read-only.
5. Inspect docs/commands → contracts/schemas → tests/negative fixtures → implementation → reports/plans.
6. Classify findings.
7. Обновить Feature Passport.
8. Не копировать legacy topology.
9. Stop when question answered or scope expands.

## 7. Ленивая декомпозиция

```text
Epic → Stage → Sub-stage only when material → executable Task
```

Child создаётся только по authority boundary, independent validation, material risk, protected operation, distinct acceptance или dependency. Closed children не доказывают parent completion.

**Для общей задачи выбранной версии — DRAFT (§25.0).** Ленивая декомпозиция
сначала формирует внутренние пункты работы и worker actions под одной C-005/C-006.
Переход к следующей части, размер работы или её локальная проверка сами по себе
не требуют самостоятельной task. Если по указанным выше основаниям нужна
отдельная C-005, её effectful запуск требует собственного exact authority binding;
controller не выдаёт ей новую C-006 и не переносит исходную authority молча.
Предусмотренную границу учитывают при подготовке общего входа. Пока допуск
отсутствует, зависимая работа ждёт, независимая в исходном scope продолжается.

## 8. Task Brief и Execution Authorization

<a id="first-core-parent-autonomy"></a>

**Принятая first-core модель — HD-08, HD-09, HD-10.**

- **HD-08:** после согласования одной bounded parent task и её runtime authority
  controller самостоятельно читает разрешённый контекст, планирует обратимую
  работу, реализует, проверяет, диагностирует/корректирует, повторяет affected
  checks и готовит итог. Промежуточные технические stages не требуют нового Human
  approval; material scope/behavior/architecture/authority boundary возвращается
  человеку по HD-25. Одна task без отдельного допуска effects недостаточна.
- **HD-09 — B1:** автоматический выбор следующего child разрешён только внутри
  того же parent при fresh inputs, действующих prerequisites и scope/authority,
  без нового material решения. После completion нельзя самостоятельно взять
  новую независимую цель из общего backlog. Transport queue C-016 не выдаёт
  parent selection; отложенный FTR-007 не prerequisite внутреннего порядка.
- **HD-10:** T2 → T2a/T2b/T2c допускается без Human approval, если parent outcome,
  scope, authority и существенные Product/Architecture решения не меняются.
  Вклад, оставшиеся критерии и состояние частей сохраняются у existing controller.
  Переразбиение не создаёт новый parent или пустой budget.

Task Brief описывает goal/scope/constraints/validation и требования к будущей
Parent Task Authorization. Его paths/operations/effects имеют только
`requested_*`/`prohibited_*` semantics; до отдельной выдачи authorization
identity и `allowed_*` отсутствуют.

Parent Task Authorization создаётся человеком, bind к exact task
revision/subject и ограничивает effectful worker actions (`EXECUTE`, `CORRECT`),
operations/paths/effects, human-only boundaries, expiry и task hard limits. Она
не меняет canonical state-machine graph. Controller выводит из неё более узкий
consumable Effectful Stage Envelope для одного `EXECUTE` или `CORRECT`.
`CHECK`/`FINAL_VALIDATE` получают отдельный read-only ValidationEnvelope с purpose и допустимым сочетанием transition по C-009.

Фактический parent authorization binding сохраняется в Loop State без
переписывания Task Brief. Envelope хранит parent identity/revision/digest,
controller issuer, exact controller transition, state revision/event head,
candidate и action-spec digest; он не приписывается человеку напрямую и не
разрешает Git actions.

В [общем проходе версии](#autonomous-project-development) исходная authority
покрывает согласованные внутренние работы, интеграцию, checks, служебные outputs
и bounded correction в своих пределах. Она не расширяется по мере декомпозиции:
каждый effect требует обычного fresh admission, новый scope — отдельного решения.

<a id="first-core-development-execution"></a>

### 8.1. Разработка первого ядра до согласованного результата

Принято [решением 2026-09-16](00_Core.md#first-core-development-simplification).
При подготовке supervised-разработки единицей согласования является bounded
parent task с результатом, критериями, разрешёнными source/state/scratch paths,
действиями/эффектами, текущим model/data route, сроком и общим конечным бюджетом.
Покрытые внутренние стадии S0–K4, декомпозиция, проверка и обычная correction не
становятся отдельными Human Gates. Явно ограниченный старый grant сохраняет свои
границы; это правило не включает автоматически непокрытые стадии или попытки.

После допуска parent агент самостоятельно исправляет код, тесты, fixtures и
настройки запуска в согласованных пределах, повторяет затронутые проверки и
продолжает к результату. Новое имя временной попытки внутри заранее разрешённого
scratch root — HOW; оно не меняет цель, полномочия и оставшийся бюджет. Используется
одна проверенная конфигурация среды и стабильная область записи; новую sandbox
политику под каждую попытку не создавать без выявленной технической необходимости.
Исправление конфигурации не разрешает расширить доступ или отменить защиту.

| Наблюдаемый исход попытки | Следующее действие внутри действующего допуска |
|---|---|
| Ошибка подготовки; отсутствие целевого эффекта доказано | Сохранить причину, существенные Evidence и частичную историю; исправить настройку и использовать новую изолированную попытку в разрешённом root, с fresh binding и тем же бюджетом |
| Целевой эффект подтверждён | Не повторять эффект; проверить результат и продолжить разрешённый маршрут |
| Исход эффекта неизвестен | Остановить зависимый эффект и сверить фактическое состояние; без слепого повтора, сброса lock/ledger или выдуманного отсутствия эффекта. При неустранённой существенной неопределённости вернуть точный blocker |

Новый каталог не является способом обойти admission, replay barrier, неизвестный
эффект или запрет текущего grant. Обычный fail сам по себе не требует обращения
к человеку. Обращение требуется при существенном Product/Architecture решении,
расширении scope/authority/access, изменении защищённой границы или материального
риска, неустранённой опасной неопределённости, исчерпании бюджета/срока либо
действии, для которого сохранён отдельный Human decision, включая Git/delivery.
При отсутствии нового различающего Evidence повторяющийся цикл останавливается.

Для сопровождения достаточно одного актуального durable состояния задачи,
необходимых результатов проверок и итогового отчёта со ссылками на Evidence.
После material transitions оно обновляется; новые launch/stage документы и
согласования каждого внутреннего шага не требуются. Сохраняются decision-relevant
история, точные bindings и finite budget; число отчётов/тестов не заменяет
работающий сквозной результат и обязательные критерии.

Финальный exact candidate проверяет свежий read-only reviewer. Finding передаётся
отдельному correction executor в пределах parent authority; затем affected checks
и свежая финальная проверка нового candidate. Технический PASS не означает ACCEPT.
Это порядок разработки AOS: C-006A/C-009/C-009A, V3 и требования к создаваемому
продукту не упрощаются. Supervised-сборка и доказательство native conformance /
autonomous resume имеют отдельные результаты; требуемые UNKNOWN/NOT_RUN сохраняются.
Этот раздел сам по себе не разрешает запуск, новые native probes или Git actions.

## 9. Preflight репозитория

Проверить root, worktree, branch, HEAD, baseline, staged/unstaged/untracked, diff, nested repos, symlinks, paths, interpreter/dependencies, sandbox/network/remote, temp boundary, stop conditions, candidate identity, source/destination и credentials/data boundary.

```text
IN_SCOPE_EXISTING | OUT_OF_SCOPE_USER_STATE | ENVIRONMENT_NOISE | GENERATED_DISPOSABLE | UNKNOWN_MATERIAL
```

## 10. Модель стадий Runtime-реализации

Эти стадии применяются исключительно к написанию кода и защищенным операциям. Создание и редактирование документации в `workspace/` не требует прохождения через PLAN, EXECUTE, VALIDATE и REVIEW.

`PLAN | EXECUTE | VALIDATE | REVIEW` — lifecycle stages. Внутренние
`BIND_TASK | RECOVER_STATE | SELECT_NEXT_ACTION | EXECUTE | CHECK | DIAGNOSE |
CORRECT | FINAL_VALIDATE | IDLE` — controller actions версии
`AOS_COMPLETE_TASK_LOOP_V3`. Task state и run state — ещё две отдельные оси.
Одноимённый `EXECUTE` не разрешает подменять lifecycle transition внутренним
действием; canonical `{from,to}` matrix находится в `02_Architecture.md`.

### PLAN
Read-only. Decision-ready Task Brief, risks, validation, stop conditions.

### EXECUTE
Worker выполняет один допущенный stage/action в exact scope и возвращает результат
controller. Для принятой full-cycle parent task остановка worker не требует нового
Human запуска следующего покрытого шага: controller продолжает по §8.1/§10.0.
Самостоятельная single-stage task не получает полномочий следующей стадии;
terminal parent result → report and stop. Unrelated cleanup не разрешён.

### VALIDATE
Read-only exact candidate. Does not fix. Independent validation required only when risk/task demands it. Переход к отдельному corrector возможен только по full-cycle правилам §10.0, не из полномочий validator.

### REVIEW
Read-only assessment/recommendation. No simulated acceptance or correction.

### DELIVER
Handoff package, not stage or Git permission.

<a id="core-lifecycle-transitions"></a>

### 10.0. Явные lifecycle-переходы полного цикла — SCAFFOLD_CORE_DRAFT R5

Человек выбрал явные переходы исполнения и проверки внутри одной задачи.
Эти правила V3 применяются к явно принятому full-cycle scope S0–K4 и отдельной
задаче сборки выбранного модуля по §25. DRAFT-уточнение применения к одной общей
задаче конечной выбранной версии проекта задано в [§25.0](#autonomous-project-development); создание
DRAFT, имя lifecycle stage или широкая parent allowlist не включают такой scope
автоматически. Самостоятельная PLAN/VALIDATE/REVIEW task сохраняет свою read-only
границу и не получает correction authority. Для неё действие, требующее выхода
из принятого scope/stage, блокируется до отдельного решения; техническое чтение
и выдача отчёта сами не требуют нового effectful worker.

C-005.lifecycle_stage — исходная стадия задачи, C-012 — текущая. Для запуска уже
подготовленной реализации S0–K4, выбранного модуля или версии по §25.0 исходная стадия EXECUTE; если принятая full-cycle
задача начинается в PLAN, её первый переход в EXECUTE требует готового принятого
task input, current authority и разрешённого action. Controller не редактирует
исходный C-005 и не повышает DRAFT до accepted. Изменение цели/contract/scope
требует отдельного решения и fresh task/authority binding.

| Событие / controller transition | Исходная → текущая lifecycle | Условия и результат |
|---|---|---|
| SELECT_NEXT_ACTION → EXECUTE | PLAN / EXECUTE / VALIDATE → EXECUTE | Exact принятая task полного цикла; dependency-ready action, fresh preview/current C-006 и C-006A. Из PLAN дополнительно доказана готовность принятого input. Read-only scope не допускает mutation |
| DIAGNOSE → CORRECT | EXECUTE / VALIDATE → EXECUTE | Полный цикл покрывает correction; fresh diagnostic/C-009A, current authority и exact C-006A. Gate сам не меняет stage и не допускает effect |
| Разрешённое в matrix действие → CHECK / FINAL_VALIDATE | EXECUTE / VALIDATE → VALIDATE | Fresh C-009, допустимый purpose/from/to, check/read/output scope; worker не изменяет subject |
| FINAL_VALIDATE → DIAGNOSE при finding | VALIDATE → VALIDATE | Сохранить finding/ledger; diagnosis read-only до отдельного разрешённого CORRECT. Нельзя исправлять из validator |
| FINAL_VALIDATE → IDLE при доказанном completion | VALIDATE → REVIEW | Все условия §10.5 доказаны, review/handoff criterion закрыт. Controller фиксирует TECHNICALLY_COMPLETE; REVIEW не означает Human ACCEPT |
| BIND_TASK, RECOVER_STATE, SELECT_NEXT_ACTION, DIAGNOSE, остановка/IDLE и resume без нового dispatch | Сохранить текущую stage | Не дают mutation authority; новый worker допускается только по строкам выше. Повтор того же stage не создаёт фиктивного lifecycle-перехода |

Таблица дополняет, а не расширяет 26 controller edges Architecture: например,
FINAL_VALIDATE → CHECK или REVIEW → CORRECT не возникают из перечисления стадий.
Диагностика после EXECUTE failure может оставаться в EXECUTE, но сама всё равно
read-only; DIAGNOSTIC CHECK переводит lifecycle в VALIDATE и возвращает action
в DIAGNOSE без закрытия acceptance. Новая implementation/correction после checks
получает явный обратный переход VALIDATE → EXECUTE. Текущее REVIEW не имеет
автоматического выхода к effects; terminal task не открывается заново. Human
NEEDS_CHANGES формирует отдельную последующую task/revision и authority, сохраняя
историю завершённой задачи, а не скрытый resume её terminal record.

Controller — единственный writer lifecycle/controller transitions. Admission
читает исходные C-012 revision/event/candidate/lifecycle, task scope, current
parent и gate при необходимости; определяет целевой stage по этой таблице.
Проверка, consumption C-006A/C-009, изменение lifecycle/controller action и запись
нового state/event составляют одну атомарную операцию. Никакого worker dispatch
до её durable подтверждения. При отказе/конфликте сохраняются исходные stage,
state и unused envelope; локальный проигравший не перезаписывает победителя.

C-012/history хранит before/after stage, причину, task/authority binding и
исходный/новый revision/event tuple. Envelope/gate остаются bound к исходному
состоянию допуска. Worker получает результат admission; observation сверяется
с этим binding и current active action, а не повторно допускается против нового
state. Неизвестный исход публикации сначала reconciled: либо нет допуска и
эффекта, либо один durable admission с consumed envelope. После него отсутствие
worker report не разрешает повторный dispatch. Материализация/locking остаются
HOW, атомарность и наблюдаемость обязательны для product и external host.

Pause/resume и recovery сохраняют lifecycle, ledger и незавершённый admission;
новый owner следует §10.2. Успешный final completion фиксирует REVIEW/task state
и final event согласованно в C-012; worker result не выполняет этот переход.
Проверки — [SC-T21/22](#core-r5-checks), совместимость — [V3](02_Architecture.md#core-loop-v3).

### 10.1. Complete-task controller

Для явно поставленной bounded task сохраняемый controller продолжает работу
между stage workers и sessions до доказанного технического завершения либо до
точной паузы/Human Gate. Controller не является новым источником authority:

```text
Task Contract + parent task authority
→ RECOVER_STATE
→ deterministic SELECT_NEXT_ACTION
→ fresh stage envelope
→ EXECUTE → report/stop worker
→ CHECK
    ├─ PASS + remaining criteria → next action
    ├─ FAIL/material UNKNOWN → DIAGNOSE
    └─ all criteria closed → FINAL_VALIDATE
→ CORRECT by separate worker → fresh affected checks
→ TECHNICALLY_COMPLETE only when completion predicate is proven
```

Parent task authority связывает task revision, subject, allowed worker actions,
paths/operations/effects, expiry/revocation, hard limits и human-only
boundaries. Каждый effectful `EXECUTE`/`CORRECT` получает fresh Stage Envelope и
после factual result останавливается. Consumed, expired, ambiguous или
mismatched envelope не переиспользуется. Checker/validator получает read-only
ValidationEnvelope; finding маршрутизируется controller, но validator не
исправляет candidate.

Admission effectful worker требует совпадения envelope с current controller
action transition, state revision, event head и candidate, а также чтения
актуальной unexpired/unrevoked Parent Task Authorization с совпадающими
identity/revision/digest. Envelope потребляется до effect; lifecycle admission атомарен по §10.0. Он bind exact
`action_spec_digest`; worker не может заменить action другой mutation только
потому, что она помещается в общие allowed paths/operations/effects.

Отсутствующее, `null` или пустое authority field означает отсутствие
разрешения. Forbidden action имеет приоритет. Broader diagnostic reasoning не
расширяет read/mutation scope, network, credentials, provider или protected
effects.

### 10.2. Persistent state, run и task

Controller атомарно сохраняет task/revision, repository/candidate identity,
task state, run state/result, acceptance/check status, impact basis, findings,
unknowns, diagnostic level, attempt ledger, resource usage, authority/envelope
state, observed effects и one next action.

Для общей задачи версии этот state охватывает всю выбранную цель: критерии
частей и общих сценариев, их зависимости, готовые и оставшиеся работы, current
Evidence и stale checks (§25.0). Смена внутреннего шага не обнуляет ledger/resources.
После interruption восстанавливается общий scope и фактические effects, а не
только последняя часть; следующий шаг снова выбирается по §10.5.

Controller — единственный владелец controller-action transition. Worker output считается
непроверенным observation и не может напрямую установить `PASS`, закрыть
criterion или task. State update проверяет previous revision/digest; один active
controller подтверждает каждое изменение из одной исходной revision только один раз; механизм реализации не предписывается. Stale/concurrent update
отклоняется; проигравший controller прекращает dispatch. Продолжение идёт только по [протоколу конфликта](#state-conflict-recovery), без записи поверх state победителя.

```text
task_state:
ACTIVE | WAIT_HUMAN | WAIT_EVIDENCE | TECHNICALLY_COMPLETE |
TASK_FAILED | CANCELLED_BY_HUMAN | CONTRACT_VIOLATION

run_state:
RUNNING | PAUSED_RESOURCE | STOPPED

controller_action:
BIND_TASK | RECOVER_STATE | SELECT_NEXT_ACTION | EXECUTE | CHECK | DIAGNOSE |
CORRECT | FINAL_VALIDATE | IDLE
```

Wait/terminal task state или resource pause переводит только controller action
в `IDLE`; оно не становится controller-action transition к имени task/run
state. Resume переводит `IDLE → RECOVER_STATE`.

`run FAIL/UNKNOWN/BLOCKED` не завершает active task, если существует
обоснованный разрешённый следующий шаг. Исчерпание controller-defined finite
run allowance даёт `PAUSED_RESOURCE`; новый run начинает с reconciliation и не
сбрасывает ledger. Всю task ограничивает только explicit human/host hard limit.

<a id="state-conflict-recovery"></a>

#### Конфликт state и единственный продолжатель

1. Отклонённый stale/concurrent update не меняет authoritative state/event head.
   Проигравший controller прекращает dispatch и завершает свой run; его локальный
   STOPPED не переписывает shared task/run state победителя. Уже допущенный worker
   нельзя считать отменённым лишь из-за конфликта controller.
2. Пока текущий владелец действует, второй controller не продолжает задачу.
   Передача владения должна исключить дальнейший dispatch прежним владельцем;
   механизм выбирается при реализации, гарантии проверяются наблюдением.
3. Новый исключительный владелец перечитывает current state, ledger, authority,
   active envelopes и actual effects. Он дожидается/сверяет in-flight action;
   отсутствие записи результата не доказывает отсутствие effect. Missing/partial
   C-008 не препятствует разрешённой read-only reconciliation: используются
   сохранённый dispatch/envelope binding, ledger и независимые observations target.
   Доказанные наличие/отсутствие effect различаются; недостаточность даёт
   WAIT_EVIDENCE. Новый recovery observation C-010 связан с исходным admission
   и C-012; он не подделывает отсутствующий C-008 погибшего worker.
4. Терминальные TECHNICALLY_COMPLETE/TASK_FAILED/CANCELLED_BY_HUMAN/
   CONTRACT_VIOLATION не возобновляются автоматически. WAIT_HUMAN/WAIT_EVIDENCE
   и resource pause сохраняют свои условия возобновления.
5. Для разрешённого продолжения нетерминальной задачи владелец записывает
   `current action → IDLE` относительно свежей revision, если action ещё не IDLE.
   Допустим отдельный recovery checkpoint `ACTIVE/RUNNING/IDLE`: вместе с ним
   durable сохраняются причина takeover, identity единственного владельца,
   исходный/новый state tuple и ссылки на reconciliation шага 3. Это подтверждённая
   передача продолжения, а не wait, resource pause или completion. Без этих
   bindings произвольный `ACTIVE/RUNNING/IDLE` остаётся невалидным.
   Затем host/controller фиксирует resume event с причиной конфликта и identity
   владельца: `IDLE → RECOVER_STATE`. Новый конфликт записи возвращает к шагу 1.
   Прерывание после публикации recovery checkpoint сохраняет его: следующий
   владелец заново проверяет исключительность и условия шагов 1–4, затем выполняет
   этот resume. Сам checkpoint не разрешает effect или обход current authority.
6. RECOVER_STATE сверяет факты до нового dispatch. Недостаточные observations
   оставляют точный WAIT_EVIDENCE; новая authority не выводится из checkpoint.
   Consumed envelopes и неизвестные effects сохраняются, ledger/resources не
   обнуляются. Завершённый effect не повторяется; новое действие требует fresh
   preview и admission.

<a id="initial-product-state"></a>

#### Первоначальный C-012 и продолжение product task

Создание новой задачи запрашивается явно; отсутствие checkpoint не выбирает этот
режим автоматически. До создания известны валидные C-005/task revision,
source-bound inputs, current target/candidate, current C-006 и покрытые ею
служебные state/evidence paths/operations. Controller проверяет trusted issuer,
expiry/revocation и ownership; это не product effect и не выдача authority.

Создание первого record выполняется как отдельно покрытая операция controller
над служебным состоянием, без требования ещё не существующего Stage Envelope.
Она не допускает product mutation. До записи доказано отсутствие этой task
identity и её прежних effects/ledger в объявленном хранилище; недоступная история
означает UNKNOWN, а не пустоту. Create-if-absent не перезаписывает существующее.

Первый C-012 содержит BIND_TASK/ACTIVE/RUNNING, lifecycle stage из C-005 без автоматической смены (последующие переходы — §10.0), исходную revision/event identity,
исходный candidate, current authority binding, критерии с NOT_RUN, пустой ledger,
отсутствующие envelopes/effects и фактический resource usage. После durable записи
идёт BIND_TASK → RECOVER_STATE → SELECT_NEXT_ACTION. До первого product effect
обязательны обычные preview/admission и fresh C-006A; служебная инициализация их
не заменяет. Формат хранения и способ атомарной публикации остаются HOW.

Повторное создание существующей identity не создаёт вторую задачу и не сбрасывает
первую: результат сообщает существующий binding и необходимость отдельного
resume. При прерванной инициализации сохранённые observations позволяют определить,
был ли опубликован record. Complete record сохраняется; incomplete publication
reconciled в покрытой state boundary без product dispatch. Если доказано, что
публикации/effects не было, допускается повтор create-if-absent с той же identity;
при неопределённости — WAIT_EVIDENCE, без silent reset или удаления следов.
Если валидного C-012 ещё нет, это исход попытки в host/controller report;
для записи статуса не создаётся фиктивный checkpoint существующей задачи.

Resume требует существующего совместимого checkpoint: missing/corrupt/unsupported
record запрещает продолжение effects, сохраняет исходные данные и требует
reconciliation. Это правило относится к product task; первоначальный внешний
development checkpoint обеспечивается host до S0 и не импортируется автоматически.

### 10.3. Многоступенчатая диагностика

**HD-14 — ordinary correction первого ядра.** Defect → diagnosis → bounded
correction → affected re-check → continue выполняется автономно в принятом
parent scope с существующим C-009A и отдельным corrector. Новый Human Gate нужен
лишь при material изменении Product behavior, Architecture Contract, parent scope,
authority, external access, protected boundary, dependency или Risk Profile.
Обычная техническая ошибка сама по себе не требует нового поручения.

**Первичное различение finding — DRAFT.** До correction установить предмет ошибки
по источникам и наблюдениям; это маршрутизация внутри существующего цикла,
не новый gate или lifecycle. Несколько совместимых причин остаются гипотезами
до различающего Evidence, а не автоматически четырьмя findings.

| Предмет ошибки | Различающее основание и следующий шаг |
|---|---|
| Реализация / результат | Достаточное действующее требование нарушено на связанном candidate: ограниченная correction результата по C-009A, затем затронутые acceptance/integration checks |
| Требование | Источники не определяют обязательный исход: классификация А/Б/В по §25.7.7, исправление у owner в разрешённом scope либо решение человека; зависимое поведение не угадывается |
| Проверка | Oracle пропускает запрещённый результат либо отвергает допустимый: отдельный finding о checker/fixture, сохранение исходного subject и критериев; корректировка проверяющего только в своей authority, затем его controls и повтор зависимых проверок subject |
| Инструмент / среда | Наблюдение подтверждает недоступность/неисправность средства проверки или исполнения: показать affected NOT_RUN/UNKNOWN и диагноз среды; не объявлять это автоматически дефектом продукта или требований |

Диагностика начинается с минимальной causal boundary и расширяется, если
причина не найдена или Evidence неубедительно:

1. `D0 — Failure binding`: exact candidate/command/environment, reproducibility,
   stable signature и надёжность observer; negative Evidence требует positive
   control, когда иначе отсутствие сигнала недоказуемо.
2. `D1 — Local`: изменённый компонент, stack/data path, локальные invariants,
   affected tests и direct contract violation.
3. `D2 — Hypothesis discrimination`: material competing hypotheses,
   falsifiable predictions и минимальная различающая read-only проверка либо
   уже разрешённый bounded experiment.
4. `D3 — Adjacent boundary`: caller/callee, producer/consumer, state transition,
   fixture/oracle, repository-local configuration и declared dependency.
5. `D4 — Environment/system`: provenance build/import/runtime, process,
   filesystem, concurrency/timing, sandbox/permission, platform и разрешённые
   adapters.
6. `D5 — Trajectory/architecture`: unresolved guarantee, accumulated Evidence,
   equivalent corrections/oscillation и состоятельность выбранного mechanism.

Переход на следующий уровень обязателен при `MULTIPLE_COMPATIBLE`, `NOT_FOUND`,
unreliable observer, inconclusive check или confidence, недостаточном для
обратимой correction. Mutation разрешает только машиночитаемый `C-009A
Correction Gate` из `02_Architecture.md`.

Различающий read-only check выдаётся как C-009 purpose DIAGNOSTIC:
DIAGNOSE → CHECK → DIAGNOSE. Любой результат уточняет текущий diagnostic record,
сохраняя signature/level/ledger; diagnostic PASS не является acceptance PASS.
Если Evidence разрешает finding без mutation, controller фиксирует причину и
оставшиеся required checks, затем выполняет DIAGNOSE → SELECT_NEXT_ACTION.
Нужные ACCEPTANCE/FINAL проверки запускаются отдельно; неубедительные данные
расширяют уровень либо приводят к WAIT_EVIDENCE по прежним правилам.

Gate вычисляется до выдачи `CORRECT` Stage Envelope. `ALLOW` возможен только в
двух случаях: `PROVEN` + `MEDIUM|HIGH` +
`REVERSIBLE_BOUNDED`, либо `PLAUSIBLE` + `HIGH` +
`REVERSIBLE_DIAGNOSTIC`. Во всех случаях обязательны ноль material competing
hypotheses, valid authority/state, prediction, исполнимые checks и recovery
reference. Любое отсутствующее поле, другая комбинация или `LOW` confidence
даёт `DENY` и переводит работу в следующий diagnostic level либо `WAIT_*`.
Свободная оценка «proportional risk» сама по себе mutation не разрешает. Каждый
gate bind current parent authorization/state/event head, diagnostic ID, failure
signature, candidate-before и proposed correction digest. При `ALLOW`
controller создаёт `CORRECT` envelope с gate identity/digest и тем же
`action_spec_digest`; перенос gate на другой tuple запрещён.

Та же failure signature после correction продолжает последний достигнутый
уровень и не повторяет inconclusive checks. Новая signature начинает новый
record с `D0`, но не сбрасывает общий ledger/resources. Повтор `D5` для той же
trajectory требует нового discriminating Evidence или material изменения
premises.

### 10.4. Progress и anti-loop

**HD-20 — конечный бюджет первого ядра.** Каждая автономная parent task имеет
finite work/resource budget с единицей, расходом и stop condition. Агент выбирает
разумные конечные числа внутри Human constraints и фиксирует их до использования;
не требует от человека технического числа на каждый шаг. Это не назначение
Risk Profile и не право увеличить согласованный hard limit или обнулить историю.
Продолжение оправдывают проверка конкретной correction, доказанный bounded
transient retry, различающая переменная, materially new Evidence либо обоснованный
рост уверенности. При прежней failure boundary без новой информации остановить
affected loop и сообщить диагноз/evidence/blocker; число попыток не progress.
Пороги диагностики ниже не разрешают игнорировать отсутствие information gain.

Progress — failing required check стал PASS без равной/большей regression,
failure boundary сузилась, hypothesis опровергнута/существенно изменена,
уменьшилось число совместимых причин, observer доказан либо Evidence обосновало
materially different bounded correction.

Повтор unchanged command, equivalent patch, переименование hypothesis, новый
worker/session, unrelated edit или explanation без new Evidence progress не
создают. Continuous ledger и resource usage не сбрасываются сменой worker,
session, failure label или diagnostic level. После двух corrections одной
signature без progress дальнейшая mutation прекращается и диагностика
расширяется. Два check одного уровня без information gain также требуют
следующего уровня; полезные различающие проверки этим лимитом не ограничены.

### 10.5. Completion predicate и next action

```text
TECHNICALLY_COMPLETE =
    current Evidence закрывает каждое acceptance criterion
AND каждый required check имеет current candidate-bound PASS
AND candidate соответствует task revision и allowed scope
AND material UNKNOWN отсутствуют
AND required findings закрыты или покрыты exact Human residual-risk decision
AND observed effects reconciled
AND persistent state recoverable
```

В общей задаче версии (§25.0) predicate применяется к её общему subject и всем
согласованным критериям, включая реальные обязательные стыки. Завершённая часть
закрывает лишь доказанные критерии; общий lifecycle остаётся в рабочем цикле,
пока не доказан весь результат. Отдельного completion owner или predicate нет.

После mutation affected checks становятся stale. Impact basis связывает changed
paths, dependency/contract edges, behavior boundary и limitations. Если
material impact не установлен, выполняется broader required check либо
completion блокирует `UNKNOWN`.

Residual risk закрывает finding только по Human Decision Record с actor/source
provenance, finding/candidate identity, scope и decision. Worker claim,
recommendation или свободный отчёт этого не делают.

Next-action priority: reconcile unknown effect → stop contract/authority/identity
violation → recover state conflict → diagnose failing required check → resolve
material unknown → implement next dependency-ready acceptance criterion → rerun
affected checks → final validation → optional work. Внутри категории действует
declared dependency и Task Contract order.

## 11. Жизненный цикл документации и применимость публикации

Документационный цикл избавлен от тяжеловесных инженерных проверок. Шаги 1–7 ниже описывают scoped Global Design publication; их нельзя применять как требование автоматически переписать frozen `AOS/` при новой scaffold/core-задаче. Её текущий authoring route: owner corrections/proposals → один производный brief → документальные checks → конкретный пакет решений. First-core содержание принято HD-01; фактический runtime launch остаётся NOT_RUN до SC-DEC-04.

1. **Workspace**: Source synthesis, research, drafts and superseded working artifacts live in `workspace/`; presence there does not create canonical ownership.
2. **Pass 1 (Product Model)**: Define product goals, boundaries, actors, journeys, feature scope and preserved product decisions at WHAT level. Working output: `workspace/DRAFT_01_PRODUCT_MODEL.md`; published path after all gates: `AOS/01_PRODUCT_MODEL.md`.
3. **Structural Review**: Check product/architecture separation, source traceability and the WHAT / implementation-HOW boundary. Pass 2 starts only after the exact candidate has no material structural conflict.
4. **Pass 2 (Architecture Contracts + Engineering Workflow Semantics)**: Define architecture/state contracts and design-level workflow, authority, validation/evidence, recovery and handoff semantics. Working outputs: `workspace/DRAFT_02_ARCHITECTURE_CONTRACTS.md` and `workspace/DRAFT_03_ENGINEERING_PIPELINE.md`; published paths after all gates: `AOS/02_ARCHITECTURE_CONTRACTS.md` and `AOS/03_ENGINEERING_PIPELINE.md`. Pass 2 does not own schemas, exact I/O, serialization, storage, adapters, toolchain, repository topology or other implementation HOW.
5. **Integration Review**: Check the exact three-file package for consistent vocabulary, traceability, ownership, state/result separation and absence of material cross-document conflicts. A technical PASS is Evidence, not human acceptance.
6. **Global Design Freeze**: Bind exact paths and SHA-256 values after review and explicit human decision. Preserved feature-specific inputs, future implementation decisions and non-blocking global decisions are allowed when explicitly classified; a material unresolved product/architecture conflict blocks Freeze.
7. **Publish to AOS**: Copy the exact reviewed working outputs to `AOS/01_PRODUCT_MODEL.md`, `AOS/02_ARCHITECTURE_CONTRACTS.md` and `AOS/03_ENGINEERING_PIPELINE.md` without content drift. These three published paths are the deliverable subject of that Global Design Freeze. Review, acceptance and Freeze identities are stored separately under `AOS/reviews/`, `AOS/decisions/` and `AOS/GLOBAL_DESIGN_FREEZE.md`.

**Локальные корректировки (Local Corrections)**:
Исправление опечаток, ссылок и форматирования в `workspace/` выполняется без полного ревью-цикла по маршруту: `Short Markdown Task → edit → check → report → stop`.

**Правила публикации deliverable (Handoff)**:
Пакет в `AOS/` передается coding agent'у как read-only Source of Truth только для задачи, привязанной к его exact Freeze identity и fact classes. Coding agent не имеет права изменять документы в `AOS/` самостоятельно. Any post-Freeze content change requires an explicit Reopen, a new review subject and a new Freeze identity. Новая задача не получает его прежнее правило «correction обязательно отдельная task» вместо текущего canonical controller workflow: применимость источника определяется до launch по [Core](00_Core.md#scaffold-core-decisions).

## 12. Отчёт стадии

```yaml
task_id:
task_revision:
lifecycle_stage:
controller_action:
result:
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
parent_authorization_binding:
  status: BOUND | NOT_APPLICABLE | UNKNOWN
  identity:
  revision:
  digest:
  reason:
envelope_binding:
  kind: EFFECTFUL_STAGE | VALIDATION | NONE | UNKNOWN
  identity:
  digest:
  consumption_state: UNUSED | CONSUMED | NOT_APPLICABLE | UNKNOWN
  reason:
Git_operations: {commit: NOT_RUN, push: NOT_RUN, merge: NOT_RUN, release: NOT_RUN}
next_required_action:
stop: true
```

R5: technical result следует [C-009](02_Architecture.md#technical-result-contract).
Lifecycle и controller action — разные поля; report только observation, не writer
stage/task state. Parent binding при BOUND требует exact identity/revision/digest;
это применённая authority, а не расходуемый объект. Для EFFECTFUL_STAGE/VALIDATION
обязательны identity/digest конкретного C-006A/C-009 и наблюдаемое consumption state.
NOT_APPLICABLE допустим для NONE с причиной отсутствия envelope (например,
отдельно покрытая initial-state операция); это не освобождает служебную запись
от authority. Read-only действие без применимого parent использует его
NOT_APPLICABLE с причиной; effectful отсутствие binding не маскируется этим статусом.

При недоступном record identity/binding и consumption остаются UNKNOWN с точным
missing evidence; неизвестность не превращается в UNUSED/false. Один CONSUMED
относится только к своему envelope. Для следующего worker current parent
проверяется снова и выдаётся новый envelope. Старое неоднозначное поле
`authorization_consumed` не принимается как V3 consumption evidence и не
конвертируется автоматически. Partial/missing report допускает независимый
recovery observation по §10.2, но не выдуманный отчёт исходного worker.

<a id="human-effort-report"></a>

### Учёт сопровождения и предложение улучшения — PROPOSAL

При оценке подготовки к автономной работе добавить в этот же отчёт короткий
абзац или таблицу; отдельный журнал и обязательная YAML-схема не нужны.
Смысл показателей принадлежит [Product §13](01_Product.md#13-кандидатные-показатели-успеха--proposal).

| Что записать | Минимальное содержание |
|---|---|
| Граница измерения | Задания/редакции входов, baseline или candidate, условия и покрытие наблюдения; источник каждого фактического значения |
| Участие человека | Минуты подготовки, ответов/координации, проверки, ручных исправлений; сумма без двойного счёта. UNKNOWN по ненаблюдавшимся категориям, не ноль |
| Вмешательства и качество | Причина каждого существенного вмешательства и связанный finding/Evidence: недостающий выбор, пропуск источника, дефект результата/проверки, среда, восстановление. Отдельно вопросы с уже доступным ответом и его locator, обычный HOW, существенные пропуски и ложные блокировки; причина-гипотеза помечается явно |
| Попытки и результат | Все попытки, включая неудачные; известные время агента/tokens/расходы и human cost. Принятые результаты — exact revision и ссылка на human decision; отсутствие данных UNKNOWN. При нуле принятых результатов отношение не определено |

Для будущего сравнения зафиксировать одинаковые задания, исходные состояния,
scope, критерии, модель/инструменты, полномочия и согласованные пределы; показать
порядок и эффект обучения при повторе. Сравнивать полные затраты и качество,
не лучший run. Порог пользы задаётся до измерения; массовые прогоны не следуют
из отчёта. Документальная репетиция сама не измеряет экономию человеческого времени.

Ограниченное предложение улучшения помещается в существующие findings/report:
**наблюдаемая ошибка → точные действия/входы/результаты и C-010 Evidence →
предполагаемая причина → одно изменение инструкции или инструмента у его owner →
проверка пользы на сопоставимом задании и сохранённых отрицательных случаях**.
Указать затронутую границу, ожидаемый эффект, критерий отказа от изменения и
неизвестное. Не нужны скрытые рассуждения модели или новая система логов.
Если наблюдаемого сбоя нет, это гипотеза/контрольный пример, не случившийся incident.
Связь с [FTR-025](06_Features.md#ftr-025--observability-audit-log-память-incidentslessons-и-continuous-improvement)
сохраняет lesson/regression proposal и human review; предложение не становится
доказанным lesson или разрешением менять Core, цели, приёмку и полномочия.

## 13. Контроль изменений (только для Runtime)

*Данные правила относятся исключительно к Runtime Implementation. Они не распространяются на документационные изменения в `workspace/` (создание и редактирование Markdown-документов регулируется документационным workflow и не требует Runtime Execution Authorization).*

One active task, one causal change, no unrelated cleanup, inventory before sensitive mutation, explicit scope expansion, changed-file allowlist, atomic commit after applicable authorization (для первого ядра — scoped HD-26 ниже), docs↔schema↔CLI↔code↔tests consistency, source read-only during extraction, no automatic `git add -A`.

<a id="first-core-local-commit"></a>

### 13.1. Standing policy доставки первого ядра — HD-26

Только для принятого first-core workflow в AOS-3:

```text
READY_FOR_HUMAN_REVIEW
→ explicit Human ACCEPT exact review subject
→ один автоматический local Commit exact accepted candidate
```

Отдельный повторный вопрос «разрешить этот Commit?» не нужен: основание — эта
scoped policy вместе с действительным текущим ACCEPT. PASS/review report не
заменяют ACCEPT. До Commit проверить C-011 origin/subject/action, frozen candidate,
actual branch/worktree/base/index, exact file allowlist и отсутствие unrelated
staged content; будущий branch заранее не выдумывается. Не использовать `git add -A`.
Изменённый candidate требует свежей проверки/принятия, а не переноса старого ACCEPT.

Commit выполняет доступный Git adapter исполнителя как операцию доставки принятого
результата, с отдельным C-014 record; это не выдача Git rights из C-006A и не выбор
полного модуля FTR-015 для ядра. Замкнутый development loop не возобновляется ради
новой независимой цели. Успех Commit подтверждается фактическим commit/tree и
точным составом; потеря ответа требует reconciliation до повтора, не второго
commit и не amend/переписывания истории. Локальная ошибка внутри разрешённого
действия допускает bounded correction/retry только при доказанном отсутствии
уже завершённого эффекта и сохранённой authority.

Push, Merge и Release каждый требуют отдельной explicit Human authorization.
Политика не действует для других repositories/workflows, documentation candidate
notebook или просто принятого плана. Сейчас Git authorization остаётся NONE:
runtime task и exact accepted implementation candidate ещё не существуют.

## 14. Правила реализации (только для Runtime)

*Данные правила относятся исключительно к Runtime Implementation.*

Implement observable behavior, one contract owner, separate analysis/mutation, preview binds apply, atomic/journaled writes, explicit idempotent retry, persistent complete-task state, staged Evidence-first diagnostics, preserve user state, authority defaults false, same strict validator in runtime/tests, stable CLI failures, `--help` no writes, optional failure isolated, no hidden network/provider, no privilege escalation, no silent compatibility, portable links, adapter drift checks, AI-code rationale/ownership/tests/handoff.

## 15. Пять verification gates (для Runtime)

1. Structure.
2. Scope.
3. Acceptance.
4. Regression/smoke.
5. Security/release blockers.

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

## 16. Стратегия тестирования

Unit: schemas/status/path/state/digest/conflict/permission/idempotency, task/run axes, transition/CAS, diagnostic re-entry, progress и completion predicates. Contract: Task Brief, auth false, parent/stage envelope consumption, enums, CLI exits, generated decisions, ownership, output versions, SoT separation. Integration: intake→spec, discovery→map, preview→apply, task→executor→check→diagnose→correct, final-validation finding→fresh candidate, memory→resume, install→reconcile, review→decision, freeze→validation. E2E: first start, idea→review, interruption/resource pause→resume, protected block, NOT_RUN, multi-level cause discovery, update preservation, Git boundaries, incident→lesson.

## 17. Обязательные негативные сценарии

Empty authority mapping permits no mutation, Task Brief `requested_*` treated as authority, transition without exact `{from,to}`/state-machine version, action-spec digest mismatch, bogus status, free-form Risk Profile, bool-as-int, mismatched session, lifecycle-stage/loop-action conflation, stale/concurrent controller update, state-bound envelope replay, revoked/changed parent authorization with cached old digest, Correction Gate replay for another diagnostic/candidate/correction, worker-declared completion, consumed stage-envelope reuse, malformed idle bypass, CLI exit 0 on failure, runtime schema bypass, scope not enforced, stale baseline, write-after-freeze, self-reference, read-only validator writes, remote secret leak, unrelated staging, environment false blocker, NOT_RUN→PASS, Evidence as auth, default authorized true, partial mutation no journal/reconciliation, run budget→false task failure, diagnostic restart for same signature, unchanged retry as progress, weak Evidence→speculative correction, residual risk without Human record, unknown impact→narrow false PASS, update overwrites state, external instruction, UI approval, stale index, absolute links, conflicting entrypoints, adapter drift.

## 18. Протокол validation

<a id="first-core-final-review"></a>

**HD-21 — fresh read-only final validator.** Итог first-core candidate проверяет
свежий независимый read-only role/context, без истории авторских выводов как
основания verdict. Ему доступны exact subject, accepted criteria и Evidence.
Другой provider не обязателен, новый постоянный agent service не вводится.
Validator не исправляет предмет: finding → separate correction executor → new
candidate → affected checks → fresh final validation. Авторский self-check не
объявляется этой независимой проверкой.

**HD-22 — reviewable validated result.** Написанный код, запуск тестов, отдельные
PASS или конец stage не закрывают parent. Применяется predicate §10.5: intended
bounded result, фактически выполненные required checks, отсутствие несовместимых
с review critical/material findings, decision-relevant Evidence, limitations,
явные required NOT_RUN/UNKNOWN и одно Human review action. Отчёт при BLOCKED
также нужен, но не называется успешным completion/READY_FOR_HUMAN_REVIEW всего
заявленного профиля; required NOT_RUN внутри него не скрывается в PASS.
Сводка коротко отвечает: что просили, что сделано, работает ли в заявленной
области, что проверено, что неизвестно/ограничено и что решить человеку.
Технические Evidence доступны в optional Details. Retention — HD-24 у Core.

Freeze subject; verify environment/import provenance; run targeted checks; wider suite only if relevant; record commands/results; preserve required/optional; classify limitations; inspect diff; verify no validation mutation; stop with one next action.

Для проверки, заявляющей изоляцию или независимость копии продукта, подтвердить, что проверяемый запуск использовал product code именно этой копии. Отрицательный сценарий с намеренным подмешиванием product code из исходного repository или другого окружения должен обнаруживаться и не получать подтверждение изоляции. Проверка в отдельном вспомогательном процессе не подтверждает происхождение кода другого запуска. Это уточнение environment/import provenance основано только на принятой части [LES-047 — изоляция проверяемой копии](04_Lessons.md#les-047--тестовое-окружение-не-подтверждало-заявленный-режим); обычные тесты без такого claim не требуют отдельной проверки изоляции. Язык и механизм проверки не предписываются.

<a id="modular-maintenance"></a>

### 18.1. Сопровождение модульных contracts — MODULAR_DRAFT

Применяется к предлагаемому [модульному составу](06_Features.md#4-индекс-каталога). Общие interfaces, owners и области affected consumers заданы в [Architecture](02_Architecture.md#module-contracts). Уточнение процедуры не меняет authority, canonical state machine или исходные feature dispositions.

Маршрут изменения: наблюдаемая проблема → требование и owner contract → consumers и affected scenarios → влияние на совместимость/сохранённые задачи → bounded correction → свежая проверка затронутой области → отчёт и завершение. Для документационной задачи это authoring и документальные checks; runtime actions этим маршрутом не разрешаются.

До правки фиксируются цель, exact paths, затронутая возможность и основание. Для изменения contract нужен список consumers из Architecture и зависимостей dossier: прямые readers, producer, recovery path, сохранённые версии и acceptance/negative cases. Если влияние неизвестно, исследовать соседнюю causal boundary; не выдавать узкий PASS. Производный индекс помогает найти consumers, но не заменяет чтение источника.

После правки повторяются проверки изменённых гарантий и их consumers. Полный пересмотр пакета нужен при изменении общего contract с неопределённым влиянием, новых material cross-document conflicts или нарушении source/owner boundaries; локальная редакция сама по себе не требует полного audit. Подтверждение старого результата не переносится на изменённый subject.

Finding содержит нарушенное требование, ссылку на наблюдение/current candidate, последствие и способ проверки исправления. Предпочтение формулировки или новая возможность вне scope — предложение, а не blocker. Reviewer работает read-only; corrector создаёт новую revision, после чего проверяется исправление и его влияние. Новый существенный дефект сохраняет blocking status независимо от числа review rounds.

Эквивалентная correction или повтор той же проверки без новой информации не считаются progress. Действуют diagnostic/anti-loop правила разделов 10.3–10.4: история, signature и diagnostic level сохраняются; исчерпание проверки одного уровня ведёт к расширению диагностики или точному missing decision/Evidence, а не к бесконечному переписыванию текста. Общие product choices группируются в один decision package, обычные редакционные шаги отдельного approval не требуют.

<a id="modular-documentation-checks"></a>

### 18.2. Документальная проверка композиции

Для MODULAR_DRAFT пакет готов к человеческому рассмотрению, если состав, полные границы возможностей, владельцы, версии, failures/recovery, conditional dependencies и acceptance examples определены. Материальное open decision допустимо только как точный вопрос с ограничением dependent claims; оно не превращается в принятое поведение или implementation readiness.

Проверка проходит `input → contract owner → допустимое действие → result/state → next action`. Это анализ описанного поведения, не симуляция исполнения и не runtime Evidence. Следующая таблица задаёт маршрут проверки; итоговый outcome конкретного прогона хранится в плане/отчёте, а не становится постоянным PASS в этом workflow.

| Case | Вход и проверяемый путь | Ожидаемое документальное разрешение |
|---|---|---|
| MOD-S01 | Простая задача без CI, индекса, installer и patterns; FTR-001/003→006→009/019→010→013/011→012/016 | Required локальные checks и базовая authority остаются; техническое завершение не требует Git или optional modules |
| MOD-S02 | Неопределённый outcome; FTR-001→003 | Материальный вопрос/unknown, без выдуманной спецификации и разрешения |
| MOD-S03 | Ненадёжный observer или competing hypotheses; FTR-011→010, C-009A | D0…D5, DENY speculative correction; при исчерпании Evidence — точный WAIT_EVIDENCE |
| MOD-S04 | Та же failure signature после correction; FTR-010/014/016 | Ledger/уровень не обнуляются; отсутствие progress требует расширения диагностики |
| MOD-S05 | Прерывание с неизвестным effect; C-008→FTR-014→C-012 | Reconciliation до retry; envelope не используется повторно; task не завершена |
| MOD-S06 | Required check отсутствует/stale; FTR-013→011 | Нет aggregate PASS/completion; названы check, subject и missing evidence |
| MOD-S07 | Final validation finding; FTR-011→controller→010→013/011 | Отдельная correction с fresh gate/envelope, новая affected validation |
| MOD-S08 | Нужный модуль отсутствует; условие dossier→FTR-008 | Заблокирован зависимый сценарий; нет скрытого включения, install или authority expansion |
| MOD-S09 | Устаревший индекс; FTR-017→016/002 | Direct-source fallback с coverage; старый индекс не подтверждает current facts |
| MOD-S10 | CI недоступен; FTR-023→011 | Local equivalent лишь если заранее определён; иначе required CI NOT_RUN |
| MOD-S11 | Authority отозвана/actor не доказан при отключённом FTR-021; FTR-012/019→010 | Эффект блокируется базовым admission; optional audit не является обходом |
| MOD-S12 | Старая задача несовместимой версии; C-012→FTR-014 | Inspection если поддержан; resume заблокирован до совместимости/recovery, данные не теряются |
| MOD-S13 | Update конфликтует с user-owned файлом; FTR-004→009/014 | Conflict preview, нет скрытой перезаписи; interrupted effects сохраняются |
| MOD-S14 | Child tasks закрыты, parent criterion не доказан; FTR-007→003/011 | Parent completion не выводится из child count |
| MOD-S15 | Изменён общий contract; owner→consumers из Architecture §6.1 | Видны affected scenarios/versions; fresh checks, неизвестное влияние расширяет проверку |

<a id="module-consistency-checks"></a>

#### Дополнение R4: модуль 005+022 и исправленные стыки

Это документальные сценарии поздних модулей, а не новые required runtime checks
для минимального S0–K4. При выборе соответствующей фичи каждый positive/negative
подслучай получает собственные inputs, oracle и check binding. Сейчас runtime
всех этих сценариев NOT_RUN.

| Case | Вход и проверяемый путь | Ожидаемое документальное разрешение |
|---|---|---|
| MOD-S16 | Вопрос без необходимости ADR; отдельно ADR при отсутствии библиотеки; отдельно pattern search и материальный выбор | No-need rationale завершает запрос, ADR не зависит от библиотеки. Поиск возвращает recommendation без обязательного human gate; материальный выбор идёт через FTR-005, без автоматического исполнения; запрос patterns из FTR-005 не вызывает вложенный ADR cycle |
| MOD-S17 | Deprecated/incompatible pattern; stale C-004; карточка изменена после принятия ADR; отдельно достаточный неизменный прежний выбор | Неприменимое не используется молча, stale subject требует новой оценки. Обновление pattern не меняет ADR; достаточный выбор не требует повторного approval |
| MOD-S18 | Отключить 005+022; отдельно interrupted запись artifact или pending decision | Artifacts/provenance/Evidence сохраняются, ядро читает прежние принятые facts; новые рекомендации недоступны. Partial effect reconciled, pending decision не становится accepted, удаления нет |
| MOD-S19 | C-011 rejection для lesson; отдельно stale/чужой subject и unknown issuer → FTR-025 | Rejection сохраняется без policy mutation; invalid decision не применяется. Первичная запись incident не требует будущего C-011 |
| MOD-S20 | Query существующего/stale/missing индекса; отдельно authorized Build и Refresh, interrupted publication | Query не запускает build/refresh и не пишет cache; direct fallback только в read scope. Build/Refresh меняют лишь покрытый output; incomplete/unknown publication не получает success и не повторяется вслепую |
| MOD-S21 | Read-only conformance; отдельно Migration без authority и Sunset без покрытия callers/разрешения | Check не внедряет adapter, не мигрирует и не удаляет parser. Отсутствие checker ограничивает check. Неразрешённая migration/sunset блокируется; базовая валидация ядра доступна без FTR-030 |
| MOD-S22 | Local Commit без remote и без policy, требующей remote; отдельно policy требует недоступную проверку; затем следующий Git action без authority | Первый Commit не блокируется отсутствием remote; явная required policy сохраняется. Commit не выполняет Push/Merge/Release, каждый следующий action требует своего допуска |
| MOD-S23 | FTR-024 готовит package/version/tag proposal → exact request FTR-015 → C-014; отдельно unknown outcome, stale/mismatched record и отсутствие authority | Preparation не создаёт tag. FTR-015 — единственный исполнитель, один dispatch; FTR-024 принимает только связанный result, не повторяет action. Unknown сначала reconciled, stale result не закрывает package |

Для каждого выбранного dossier проверяется вся сохранённая acceptance/negative list и примеры S1/S2 и предметные N-примеры с привязкой к исходным негативным случаям. Модульные сценарии имеют те же safety rules, что ядро. Проверки invalid inputs для будущего runtime остаются спецификацией: executable fixtures, команды и platform support определяются после соответствующих решений.

Focused checks: paths/scope, Markdown links/fences, YAML parse затронутых blocks и diff whitespace. После изменения общих contracts один раз проверяются семь canonical files, уникальные FTR/LES identities, owner/status boundaries и отсутствие authority promotion. Технический результат не является human acceptance или Global Design Freeze.

## 19. Human review

One document: purpose, before/after, exact paths, Evidence, acceptance, negative cases, findings, NOT_RUN, deviations, decision options и next action.

## 20. Recovery и handoff

Stage failure → worker report/stop, preserve state/logs, classify partial writes and reconcile unknown effects before any retry. Controller retains active task and routes a covered defect through diagnosis and a fresh correction envelope. Validation finding → validator report/stop → controller diagnosis → separate corrector/new candidate → fresh affected validation. Missing Evidence/authority produces `WAIT_EVIDENCE`/`WAIT_HUMAN`; run allowance produces resumable `PAUSED_RESOURCE`. Handoff records repo identity, task/run state, candidate, result, changes, checks, diagnostic level/ledger, blockers, decisions, permissions и deterministic next action. Mutable facts and authority are rechecked on resume.

## 21. Git delivery

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Before each action reverify repo/branch/HEAD/candidate/worktree, applicable policy and exact authority; for Commit include the local index. Remote observation is required only for facts relevant to that action or explicitly required by the applicable policy. A local Commit with no such requirement does not depend on a remote or PR check. Push/Merge/Release retain their action-specific source/target checks. Later relevant mutation invalidates the old binding; an unknown outcome is reconciled against the affected local or remote target before retry.

## 22. Manual dogfood и допуск automation

Measure comprehension, clarification loops, scope drift, authority confusion, time to Evidence/review, handoff quality и Governance overhead. Automate only proven repetition with stable contracts, known failures, fallback/removal and no authority expansion.

<a id="interview-to-tz-pilot"></a>

### 22.1. Interview-to-TZ pilot

До заявления об автономной готовности сценарий проверяется на трёх разных задачах:
учёт оборудования, управление графиками работы и RAG-ответы со ссылками на
источники. Для каждой задачи отдельный человек описывает целевой процесс обычным
языком; новый агент затем читает только проектные файлы и объясняет всю систему.
Это pilot функции AOS: три предметные области используются как fixtures для
интервью и подготовки ТЗ. Pilot заканчивается проверенным проектом ТЗ и не
создаёт, не запускает и не поставляет сами системы учёта, графиков или RAG.
Их разработка возможна позднее только на реализованном и проверенном AOS,
по отдельному утверждённому ТЗ и отдельной команде.

Pilot считается технически успешным только если для всех трёх задач:

1. весь основной путь и хотя бы один существенный отрицательный сценарий дошли
   от интервью до reviewable ТЗ;
2. каждое существенное требование связано с источником и проверяемым примером;
3. рекомендации агента нигде не выданы за исходное решение пользователя;
4. после остановки новый сеанс продолжил с ближайшего пробела без повторного
   опроса закрытых тем;
5. независимый cold review после исправлений не оставил критического пропуска
   в выбранном scope;
6. утверждение связано с exact revision и само не запустило разработку.

Дополнительно измеряются число основных вопросов, активное время человека,
число исправлений на рассмотрении, запросы разработчика на уточнение до первого
vertical slice и найденные позднее пропуски. Эти показатели сравниваются между
задачами и с ручным baseline, но заранее не превращаются в обещание длительности
интервью. Результаты спецификации, conformance отдельного адаптера, usability
и реальная автономная разработка сообщаются раздельно; частичный `PASS` не
повышает общий результат.

Для scaffold/core подготовлено точное уточнение этого порядка в [Product §17](01_Product.md#scaffold-core-outcome): технические срезы и positive/negative проверки выполняются внутри исходного интервала, а human usability evidence собирается отдельно. Это принятое HD-01 уточнение первого ядра; оно не объявляет пользовательский dogfood уже выполненным.

<a id="quality-requirements-verification"></a>

#### Условия качества FTR-003: применение и ограниченная проверка — DRAFT

Предмет — [производное представление](06_Features.md#quality-requirements-behavior) существующих требований, их применимость и передача по [C-002/C-003 → C-005 → C-009](02_Architecture.md#quality-requirements-contract). Это уточнение текущего Spec/Brief flow по §25.4–25.7, без новой фичи, quality schema, отдельной активации или изменения трёхсценарного pilot выше. Предварительная документационная репетиция одного условия не доказывает автономную готовность всего интервью.

QR-C01–12 — контрактные сценарии, не написанные или выполненные runtime tests. Исходные критерии FTR-003/005/006/011 сохраняются. Для каждого отрицательного варианта остальные входы корректны; случаи выполняются по отдельности. Sources/decisions и числа в fixtures искусственные и не принимаются как реальные human decisions/пороги AOS.

| Case | Вход/нарушение | Ожидаемый результат и стык |
|---|---|---|
| QR-C01 | Мелкая правка надписи без новой material concern; отдельно есть применимое product constraint, но quality-раздел отсутствует | Новый раздел/опрос не обязателен; исходное constraint сохраняется в C-002/C-005. Отсутствие раздела не NOT_APPLICABLE и не доказательство полного NFR coverage |
| QR-C02 | Пользователь не знает допустимую потерю данных, а задача выбирает поведение сохранения | Один unknown с affected decision/resolution step; зависимое решение не выдумано. Независимая подготовка ТЗ/read-only PLAN продолжается; специальные Product-правила о непредоставленных данных не заменены общим запретом |
| QR-C03 | Источник говорит только «быстро»; агент записал «200 ms» | Точный порог отвергнут как не происходящий из источника; исходные слова и кандидат понимания сохранены, открытый вопрос видим |
| QR-C04 | Один факт в C-003 и производная строка; отдельно строка содержит независимо изменённый порог | В первом случае один owner/ref, во втором conflict/предложение owner correction. Изменение производной строки не обновляет принятое требование само |
| QR-C05 | Product QR-P@1 действует для всех фич; C-002 предлагает исключение для F1 со ссылкой лишь на draft. Затем fixture даёт применимое decision для F1 | До решения действует QR-P@1; после действительного binding исключение только F1, остальные сохраняют QR-P@1. Чужая revision/scope либо попытка отменить safety не допускают ослабления |
| QR-C06 | Условие взято из ответа/переданного документа; отдельно source locator недоступен или предложение агента выдано за подтверждённое | Сохраняются wording, source/revision и реальный статус; недостаток provenance видим. Нормализация не синтезирует принятие |
| QR-C07 | Рекомендация «Redis» без исходного ограничения; отдельно явное принятое требование использовать совместимый интерфейс; обычная правка без architecture consequence | Рекомендация остаётся solution candidate, исходное условие UNKNOWN; явное constraint не стирается как «неправильное». FTR-005 получает только material вопрос и может вернуть no-need; ADR не создаётся от метки concern |
| QR-C08 | Synthetic QR-P@1: «не менее 95 из 100 ответов поиска ≤500 ms при 20 одновременных пользователях на dataset D@1 в E@1»; declared метод M@1 и пригодный subject известны | C-003 хранит факт, C-002 ссылается, FTR-006 создаёт check с отдельным ID и QR-P@1 ref, условиями D/E/M. Несколько checks могут ссылаться на QR-P@1 без collision. Проверка пустой базы не заменяет заданную; ни число, ни метод не изобретены compiler |
| QR-C09 | У required check нет пригодного метода/запуска; отдельно imported valid check по exact subject с отрицательным результатом | NOT_RUN/FAIL остаются видимыми, aggregate не PASS; запись по схеме кандидата `result` вместо текущего C-009 не принимается молча. Positive действительный набор результатов проходит только по полному C-009, без Human ACCEPT |
| QR-C10 | После C-005 requirement/deviation изменён; отдельно старый документ без quality-полей либо consumer не понимает representation | Зависимый Brief/check binding пересматривается, старый PASS historical. Legacy constraints читаются без обязательного backfill; unsupported представление не отключает требования: supported canonical route либо явный gap |
| QR-C11 | Недоступна runtime FTR-005/011 или representation выключено; отдельно FTR-023 не выбрана | Документальная подготовка продолжается по sources; runtime availability/check остаются UNKNOWN/NOT_RUN. Нет фиктивного запуска, обязательной CI или объявления supporting control невыбранным заново; выключение представления сохраняет Spec/Brief |
| QR-C12 | Прерывание между source и сохранением; новый сеанс; повтор передачи; отдельно FTR-003 и FTR-006 локально корректны, но стык потерял requirement ref/условие | Возобновление читает последнюю подтверждённую revision и сверяет source; не заявляет несохранённый output durable, не повторяет effect без reconciliation. Потеря requirement на стыке не закрывает общий критерий. Quality/decision/validation не создают C-006 или Git authority |

Ожидания задаются по исходным требованиям, независимо от нормализатора/compiler. «Всегда UNKNOWN», пустой список или заполненные поля при потере смысла не проходят QR-C01/05/08 и положительный сквозной путь QR-C12. Два исполнителя могут выбрать разные Markdown layout или методы при сохранении применимых критериев; свобода HOW не разрешает другой порог/нагрузку или silent override.

Следующий bounded experiment после выбора предмета: одна реальная фича, обычно 1–3 существенных условия, без жёсткого потолка при подтверждённой необходимости. Сравнить исходный constraints/acceptance путь с производным представлением на тех же sources; одно условие передать в проект C-005, material architecture question — в need/no-need FTR-005. Результат документационного прохода — reviewable requirement/ref/check plan, а не фактический PASS. Реальное измерение требует пригодных subject/method/environment и отдельного scope на выполнение через текущий workflow, вне notebook runtime.

До эксперимента назвать вопрос, read/output boundary, бюджет и допустимую нагрузку на человека. Измерить найденные существенные unknowns/исправленные решения, повторные/лишние вопросы, clarification loops и затраты оформления/контекста; подготовку представления учитывать. Польза — улучшенное конкретное решение или ранее выявленный material gap при заранее допустимых затратах. «Предотвращённый rework» без наблюдаемого сравнения остаётся гипотезой. При отсутствии пользы оставить обычные constraints/metrics/acceptance, не удаляя требования и не расширяя механизм. Permanent schema/автоматизация требуют отдельного обоснования; текущие pilot/измерения/runtime/independent review — NOT_RUN.

<a id="repository-graph-pilot"></a>

### 22.2. Проектный граф: рабочий цикл и pilot — PROPOSAL

Этот подраздел сохраняет graph-only workflow и приёмку [ТЗ R2](05_Reference.md#repository-graph-tz) как источник дополнительных проверок. Для единого модуля FTR-017 последовательность и общий outcome определены [ниже](#graph-rag-verification); старые Slice 1–3 не являются вторым планом сборки или отдельной Graph Feature. [Назначение](01_Product.md#repository-graph-purpose) и [архитектурный контракт](02_Architecture.md#graph-rag-module-contract) имеют собственных владельцев. Маршрут применяется только к задаче с выбранным graph-assisted context; обычная правка не обязана запускать картографирование. Прямое исследование остаётся положительным маршрутом без графа.

**До задачи:** проверить применимую область карты, запросить context/impact и открыть первичные источники существенных решений. В фиксированном pilot Slice 1 допустим полный rebuild малого scope вместо ещё не реализованного check/refresh; offline query сохраняет `repository_currentness: NOT_RUN`. Найденные ограничения и evidence references включаются в существующий task-local Context Pack по необходимости; выдача карты не заменяет Task Brief, permission или validation criteria.

**После изменения:** выполнить только разрешённый refresh либо rebuild малого scope; проверить semantic diff, новые/удалённые связи, test bindings и pending coverage. Тесты продукта не запускаются неявно. **При handoff:** передать graph digest, observation boundary, compact query и следующий probe как дополнение к сведениям §20; весь payload карты читать не требуется. Bootstrap содержит маршрут к owner/tool instruction, а не копию контракта.

#### Реальный вопрос и oracle до разработки

До Slice 1 задаются exact snapshot/corpus, один реальный вопрос о зависимости, существенные правильные связи, допустимые unknowns и oracle из первичных источников. Reader не определяет собственный правильный ответ. Каждый поддержанный способ обнаружения связи имеет достаточное основание и неоднозначный случай, который должен остаться unresolved.

Кандидат для AOS — «подготовленная задача → preflight → условия допуска исполнения». Вопросы: какие обязательные входы нужны; кто их предоставляет; кто потребляет результат; какие условия окружения существенны; чем проверяется стык. Oracle различает исходный код, утверждение контракта и результат запуска. Условия окружения не объявляются реально выполненными из наличия configuration или test. Это тематический пример из `AOS3-S09`, не выбор FTR/будущей topology и не разрешение защищённого исполнения. При выборе другого сценария он также должен проверять существенный системный стык, а не только известные импорты.

На отдельном примере изменения обязательного входа требуется обнаружить потребителя и необходимую повторную проверку/refresh. Выбранный положительный сценарий при выполненных prerequisites должен давать корректный результат. Корректный отказ проверяется отдельно; инструмент, всегда отвечающий UNKNOWN или отказом, положительную проверку не проходит.

#### Срезы

1. **Полезный ответ:** один язык, одно окружение, небольшой scope и несколько patterns; build, validate, exact query и минимальные context/impact. Coverage, source bindings, безопасная публикация и resource limits присутствуют с первого writer. Full rebuild допустим. Проверяются реальный вопрос/oracle, положительный и отрицательный случаи; общая pagination и optional batch могут быть отложены при честном ограничении pilot и явном отказе на превышении. Выход — ответ, сравнение с обычным поиском и решение о следующем срезе.
2. **Сопровождение доказанного участка:** check, changed/new/deleted sources, selective refresh, partial coverage, NO_CHANGE, worktree binding и recovery/concurrency. Сценарий повторяется после изменения источников. Observation batch включается только при доказанной необходимости.
3. **Повторяемая польза:** полные context/impact/detail с budgets/continuation, нужные feature/contract bindings и сравнение трёх видов задач. Проверяются все применимые критерии выбранной версии; частичный срез не выдаётся за весь контракт.

Это срезы вспомогательного инструмента, а не замена product-first последовательности AOS. Автоматизация допускается после доказанного повторения ручного сценария. Отказ от инструмента должен оставлять возможность продолжить обычную разработку.

#### Приёмка и negative cases

ID в таблице относятся к исходному R2, а не к уже выполненным тестам. Полный перечень fixtures сохранён в [черновике, §§14.1–14.2](../workspace/AOS_REPOSITORY_GRAPH_TZ_R2_DRAFT_2026-09-13.md). Для выбранного среза требуется исполняемая проверка применимых случаев; при данном документационном переносе все запуски остаются `NOT_RUN`.

| Область | Критерии R2 | Обязательная проверка |
|---|---|---|
| Наблюдаемая семантика | AC-01–03, AC-10; N-01–05, N-07 | Пустой repo без выдуманного runtime; правильные typed seeds; направления/parallel edges; test binding без PASS; bounded NOT_FOUND; rename без догадки; rebuild/round-trip сохраняют смысл, types, evidence и uncertainty, а не только counts |
| Выдача и impact | AC-04, AC-13–14; N-09, N-11, N-17–19 | Consumer за artifact найден в поддержанном impact; depth frontier видим; stubs учтены; весь результат доступен по страницам; cursor mismatch и oversized record дают явный отказ |
| Актуальность | AC-05–08; N-06, N-08, N-10, N-12 | Новый consumer при неизменном producer обнаружен либо явно pending; dirty tree при прежнем HEAD обнаружен; partial refresh не повышает непроверенное; source-version mismatch видим; NO_CHANGE не переписывает bytes/mtime; graph-only change не создаёт loop |
| Публикация и worktrees | AC-09, AC-11; N-14–15 | Старый/новый artifact целостен; второй writer или failure не теряет обновление; bindings разных worktrees не смешаны; shared Git metadata не заменяет source delta |
| Полезность и границы | AC-12; N-13, N-16 | Ответ сверяем с primary source; symlink/traversal/instruction не расширяют scope; read/check/query/validate/help без скрытых writes и test execution; graph не выдаёт permission |
| Optional batch | AC-15; N-20 | Stale/conflicting/missing batch не повышает claims; rebuild учитывает exact input либо объявляет ограничение |
| Пределы обработки | AC-16; N-21–22 | Oversized source/graph/batch, сложный input, превышение time/memory дают заявленный failure/partial outcome с сохранностью active graph и явной coverage |

Slice 1 охватывает применимые AC-01–03, AC-09–10, AC-12–13, AC-16 и negatives integrity, untrusted input, source bindings, publication и limits. Неподдержанные продолжение, batch и остальные сценарии остаются явно вне проверенного среза. Graph failure не блокирует прямое исследование; этот fallback также проверяется в pilot.

#### Измерение пользы и стоимости

Сравниваются обычный поиск и graph-assisted поиск на сопоставимых условиях. Oracle не подсказывает ответ измеряемому участнику. Повтор одним агентом уже известной задачи учитывает эффект обучения; допустимы равноценные задачи или честно ограниченный trial, отдельные агенты не обязательны.

Техническая корректность и полезность оцениваются раздельно. Для продолжения нужен начальный сравнительный сигнал: предотвращённый material miss относительно baseline либо снижение суммарных затрат без роста material misses/false positives. Один успешный пример не доказывает универсальной эффективности. Если преимущества не обнаружены или результаты неразличимы, одного technical PASS недостаточно для расширения инструмента.

Для решения о дальнейшем внедрении сравниваются минимум локальная правка, изменение общего контракта и добавление consumer. Измеряются пропущенные/ложные существенные связи, время ориентации и source reads, build/review/refresh/rebuild/исправления карты и сопровождения batch, bytes первой и всех страниц, metadata/evidence overhead, peak memory, cold load и warm query. Указываются revision, corpus, hardware, профиль, selectors/budgets, порядок и число повторений. Initial build cost показывается отдельно и входит в итог на заранее объявленном числе задач; произвольная будущая амортизация не доказывает выгоду.

Начальные цели выдачи принадлежат архитектурному контракту; кандидат latency для warm context — median до 1 секунды на зафиксированной локальной машине и объявленном корпусе масштаба прежней карты. Cold load и полное раскрытие измеряются отдельно. Это гипотеза pilot, не измеренная способность. Превышение требует анализа, а не автоматического перехода к БД или многофайловому storage.

#### Решения перед реализацией и поставка

Для выбранного Slice 1 уточняются repository/worktree и write scope, язык/OS/filesystem, вопрос/corpus/oracle, поддержанные patterns, inputs, schema/interface/error contract и resource profile. Optional batch и миграция прежней карты включаются явно либо остаются вне scope. Это не требование проектировать все срезы заранее. Выбор FTR, архитектуры и execution authority сохраняет существующих владельцев.

Поставка будущей реализации: небольшой tool/module в выбранном repo, машиночитаемый schema contract, fixtures/tests, короткая инструкция в существующем owner, один воспроизводимый example graph и report metrics/limitations. Инженерные способы реализации выбираются внутри разрешённого контракта; отдельные approval для каждого обратимого HOW не добавляются. Нужное Evidence хранится по существующему workflow, а большие временные replay artifacts не входят в active graph.

Если выбрана миграция карты AOS-3, importer доказывает full round-trip, включая допустимые неизвестные поля/статусы и semantic records, либо отказывается от неподдержанного переноса. Наблюдение будущего repo с нуля допустимо; оно не разрешает удаление старой карты. Текущий перенос документации не запускает разработку, pilot, миграцию или Git delivery.

<a id="graph-rag-verification"></a>

### 22.3. Граф RAG: единая сборка, совместимость и проверка пользы — DRAFT

**Аннотация:** проверяем, что установленный модуль помогает реальному агенту найти правильные источники, увидеть объяснимое отличие и продолжить после перерыва. Проверка JSON, отдельного алгоритма или красивая карта этого не доказывает. Сбой необязательного модуля должен оставлять обычную работу AOS доступной.

Предмет — одна FTR-017, один модуль «Граф RAG», две группы критериев G/R в [dossier](06_Features.md#ftr-017-contract). [Протокол §25.4](#feature-module-protocol), [C-015/C-016](02_Architecture.md#graph-rag-module-contract) и §25.5 lifecycle применяются без двух отдельных активаций фич. Один будущий C-005/C-006 parent связывает точный принятый contract, target/effects/profile, criteria/dependencies, limits и resume; один bounded run выполняет доступные внутренние шаги. Это вход будущей сборки, не authority от документа.

| Внутренний outcome | Что доказывается на реальном публичном пути |
|---|---|
| LOCAL_CONTEXT | Обычный запрос → разрешённый capture → exact/lexical fragments → FTR-016 Context Pack → ответ existing host с проверяемыми ссылками; полный граф не требуется |
| LINKED_CONTEXT | Typed neighbors добавляют связанный consumer/test/contract; provenance/directions/limits сохранены; unavailable graph даёт честный fallback |
| TARGET_OBSERVED | Для малого явного target получен объяснённый Delta по достаточному mapped scope, future и непроверенное не названы дефектом; next action не исполняется модулем |
| CONTINUITY_AND_PRODUCT | Dirty/add/delete/rename → новая применимость; scoped save/readback и новая сессия без старого чата; disable/recovery сохраняют core flow; installed journey и измерения |

Срезы — dependency order внутри одного модуля, не новые Human Gates. S1 не закрывает весь модуль. Full completion требует applicable G/R, реально проверенных стыков и общих core regressions на одном candidate. Структурная карта без host generation/context boundary не завершает RAG.

**Сценарии источника.** R3 `GW-T01–72` и `RG-T01–24` — 96 semantic scenario specifications, сохранённых в [архиве](../workspace/sources/AOS_Graph_RAG_Module_R3.zip), `verification/contract_cases.json`. Их связь с каждым из 62 критериев перенесена в dossier: G01–38 ← R3 AC-01–38, R01–24 ← R3 RA-01–24. Notebook graph R2 AC/N — другое пространство имён. Fixtures/harness/schema остаются reference, их AOS-3 operation/type/path bindings необходимо адаптировать к текущему C-015 и actual implementation. Expected observations не являются Evidence. Проверка coverage IDs не доказывает достаточность oracle.

#### Полный installed journey

На disposable subject с точным candidate, объявленным host/OS/versions/read/write profile: установить без зависимости от development-репозитория; задать обычным языком вопрос об изменении экспорта; получить exact contract/code и связанную проверку в bounded packet; existing host действительно получает пакет и даёт source-attributed ответ. Oracle из исходных источников/независимых проверок сверяет ссылки и утверждения, не доверяет самооценке host.

Затем сравнить current requirement с полным mapped source-set: одну запрещённую связь обнаружить, future gap и тест без run не назвать defect/PASS. Изменить файлы без commit, добавить incoming relation и удалить source: следующая выдача обновлена либо честно неполна. Завершить процесс, открыть новую сессию с действительно сохранёнными refs: восстановлены goal/blockers/next action, нет replay unknown action. Выполнить controlled disable и проверить прямой flow FTR-016; user decisions/Evidence не меняются. Synthetic acceptance fixture не является настоящим human approval.

#### Дополнительные проверки совместимости текущего AOS

Каждый вариант строки проверяется отдельно на корректных остальных входах. Для cases определить exact public boundary, independent oracle и Evidence; не возвращать ожидаемые поля по case ID без работы actual SUT.

| Case | Требование/стык и stimulus | Наблюдаемый oracle |
|---|---|---|
| GR-C01 | C-015: valid registration/direct query; отдельно absent/disabled/incompatible interface/generation | Реальный FTR-010 route разрешает только valid; остальные explicit refusal, нет hidden fallback/effects |
| GR-C02 | find/compare/context/check + FTR-009/019: закрытый source, symlink escape, prompt injection, hidden neighbor | Read/effect sentinels и outgoing payload подтверждают scope, отсутствие hidden path/snippet/network/process/model calls и persistent writes; ошибки не раскрывают запрещённое |
| GR-C03 | C-016 refresh/save: permitted command; отдельно missing/revoked authority, wrong subject, expired message, full queue | Dispatch проверяет current binding; допустимый writer сохраняет/readback, отрицательные не меняют destination; ack отдельно от результата |
| GR-C04 | Duplicate command, lost ack, changed payload under same operation, crash/unknown publish | Operation ledger + actual output: нет двойного effect/учёта; mismatch rejected, unknown reconciled, прежняя подтверждённая revision сохранена |
| GR-C05 | C-015 update/disable/remove: pending/in-flight, old generation, required consumer | Drain/reconciliation и held/cancelled messages видимы; нет premature disabled/blind rebind/replay; required consumer без проверенного fallback блокирует remove |
| GR-C06 | Corrupt/unknown cache schema, migration failure, access revoke, purge без authority | Источники/history/Evidence не меняются; old reader поддержан либо отказ; direct fallback доступен; закрытые snippets не выдаются, delete не выводится из disable |
| GR-C07 | FTR-016 integration: mandatory overflow, conflicting owners, current/stale смешение | Реальный Context Pack сохраняет source roles/revisions/constraints/conflicts или явно incomplete; source ranking не повышает authority |
| GR-C08 | FTR-005/007/011/012/014/021 boundaries: Delta, task candidate, test-file-only, interrupted action | Нет второго scheduler/drift registry или нового gate; MODULE payload не превращается в C-009 PASS/human acceptance; owner correction только recommendation |
| GR-C09 | Раздельные feature algorithm PASS при сломанном capture → context → host стыке; отдельно рабочий installed positive | Broken integration не закрывает parent; положительный путь реально выполняется без ручного JSON и без development checkout |
| GR-C10 | Coverage/oracle: top-k miss, new incoming relation, partial parser, ambiguous mapping, future expectation | Independent source-set показывает правильные MATCHED/UNVERIFIED/PLANNED_DIFFERENCE и limitations; нулевой recall/всегда UNKNOWN не проходит positive |

Применимые прежние FTR-017.S1/S2/N01–03 сохраняются. Core regression включает обычный direct-source Context Pack без модуля, раздельные selection/authority/result и отсутствие изменения human/task owners. Effects измеряются независимо: declared expected fields адаптера, static PASS и supplied-values unit tests не подтверждают sandbox/capture/persistence/installed journey.

<a id="graph-rag-impact-verification"></a>

#### Уточнения impact из DIP-R1: GR-DI01–10 — DRAFT

Это контрактные примеры к [FTR-017](06_Features.md#graph-rag-impact-behavior) и [C-015](02_Architecture.md#graph-rag-impact-contract), не исполняемые тесты. Исходные G01–38/R01–24, 96 R3 cases и GR-C01–10 сохраняются. Новый namespace не смешивает DIP AC-01 с R3 AC-01. Runtime/installed execution всех GR-DI — `NOT_RUN`.

Первый полный путь добавляется в LINKED_CONTEXT: разрешённый source → поддержанное PRODUCES/CONSUMES основание → `find/v1` с impact profile → объяснение caller/FTR-016 → host; затем material negative и обычный find без impact. TARGET_OBSERVED и CONTINUITY_AND_PRODUCT используют те же правила в своём scope. Новый parent, scheduler или обязательный selective-refresh этап не создаются. GR-C01–09 продолжают проверять реальную registration, read/effect boundary, C-016 writer, lifecycle и parent completion; таблица ниже уточняет смысл ответов.

| Case | Synthetic stimulus и независимый expected outcome | Критерии FTR-017 |
|---|---|---|
| GR-DI01 | P PRODUCES D, C CONSUMES D, exact provider/version binding: downstream(P) содержит прямого C; upstream(C) — P. Witness содержит обе исходные стрелки, 2 raw hops / 1 dependency step. При изменении D C — прямой consumer candidate; неподходящий аспект immutable historical D не проводит влияние P | G03/G38, R10 |
| GR-DI02 | Обозначение X ⇒ Y означает независимо заданную допустимую зависимость X от Y, обеспеченную fixtures PRODUCES/CONSUMES. B ⇒ A, C ⇒ A, B ⇒ C: downstream(A) direct={B,C}, transitive={}; дополнительный путь до B сохранён. Без B ⇒ A: direct={C}, transitive={B}. Stale короткий путь не вытесняет valid длинный; цикл не включает root и завершается; у двух roots отдельная attribution | G03/G04/G11 |
| GR-DI03 | REFERENCES-only endpoint не зависим; TESTS/VALIDATES возвращают только revalidation candidate. Target B ⇒ A и Observed C ⇒ B не дают смешанного пути A→C. PERMITS не даёт grant; исторический PASS не становится current | G10/G25/G34/G37/G38 |
| GR-DI04 | TRUE/current/required проходит; FALSE не проходит; OPTIONAL/FUTURE/UNKNOWN, evaluation error и conflict не попадают в текущие обязательные sets. Исследовательское продолжение остаётся гипотезой; accepted file с draft relation не повышает authority | G03/G10/G29 |
| GR-DI05 | Одна поддержка требует источники S1+S2, альтернативная — S3. Удаление S1 оставляет связь по S3; удаление также S3 лишает current support. History сохранена. Потеря альтернативы видима, valid witness не обнуляется | G11/G32 |
| GR-DI06 | P1/P2 производят похожий D, C не привязан к provider: нет декартова списка подтверждённых зависимостей. После exact binding к P2 подтверждён только P2. Запрос D.field при entity-only model явно coarse; неизвестный/неоднозначный subject не заменён похожим | G26/G27/G38, R24 |
| GR-DI07 | Partial parser, depth/node/edge cutoff, пустой partial ответ и несколько страниц: corpus/predicate/traversal/presentation различимы, caveats не исчезают. Result-only filter «component» сохраняет intermediate D; raw-hop cutoff не обходится derived step. Hidden D не раскрыт ни путём, ни counts/cursor | G08/G09/G27, R08/R11/R13 |
| GR-DI08 | Same HEAD + новый untracked consumer либо новый resolver binding при старых source bytes: current result требует достаточного recapture. Selective refresh, если реализован, совпадает с bounded full rebuild по semantic result/support/coverage; historical result остаётся historical | G11/G30/G31/G32, R12 |
| GR-DI09 | Повтор exact inputs даёт одинаковый semantic output; valid continuation сохраняет query/profile/policy bindings. Другой view/profile/generation/доступ, bool вместо integer limit, неизвестный enum либо несовместимый old consumer явно отклоняются. Обычный find и разрешённый fallback работают, но fallback не сообщает полный impact | G18/G21/G38, R14/R24; GR-C01/C06 |
| GR-DI10 | Public source→find→context→host positive действительно находит consumer; намеренно REFERENCES-only path исключён. Реальный потребитель теряет view/limitation или выдаёт test PASS — общий путь не проходит даже при unit PASS. Повтор в новом процессе использует проверенные bindings; query не пишет, сохранение отдельно проверяется GR-C03–06 | G12/G17/G19/G23/G35/G37, R18/R20; GR-C07/C09 |

Если case не меняет условие явно, fixture имеет разрешённый полный scope, действительные current/required/TRUE source bindings и конечные budgets, достаточные для ожидаемого пути. В GR-DI01 полный upstream(C) равен direct={D,P}, transitive={}; downstream(P) direct={C}, transitive={}: одно PRODUCES не создаёт D → P. Oracles задаются из вручную проверенного source-set/бизнес-сценария до вызова evaluator. Ответ по case ID, всегда пустые sets/UNKNOWN или граф, генерирующий собственную «истину», не проходят positive cases. Actual runtime defect нельзя вывести из этих topology fixtures; проверка реального эффекта принадлежит соответствующему сценарию приложения. Сравнение пользы ниже дополнительно учитывает ложные impact candidates и пропущенных значимых потребителей, раздельно от точности Delta; подготовка карты не предоставляется экспериментальной группе бесплатно.

#### Ограниченное измерение полезности

Сначала один реальный многосоставной вопрос на известном scope, затем небольшой заранее объявленный набор: exact fix; русское описание/английский ID; interface с consumers; current/future difference; resume dirty change; partial observation/ambiguous mapping. Сравнить A — тот же агент с direct search, B — lexical, C — lexical+graph; для одного сложного случая C с/без comparator. Semantic D только при измеренном recall gap.

До запуска фиксируются corpus/snapshot, source access, model/settings, oracle, число повторов и budget. Порядок чередуется, контексты изолированы; подготовка карты/mapping, cold build, refresh, failures/retries и review входят в стоимость. Проверить качество конечной разработки, обязательные source spans/recall, ложные и пропущенные Delta, чтения/байты, человеческие уточнения/время, model usage, latency. Unknown costs не нули; подписочная квота не пересчитывается в деньги по API без основания. При нуле validated results стоимость на результат не определена.

Выигрыш по времени/полным затратам заявляется только без существенной потери качества и mandatory coverage. Предложенные архивом 20% — ориентир для обсуждения pilot, не подтверждённая экономия. Итог ограничен tested scope: benefit / no benefit / inconclusive, без нового lifecycle gate. Неуспешный pilot не запускает бесконечную смену backend.

**Readiness:** проверка документационного переноса не запускает runtime/benchmark/архивные scripts. [Единый brief](../workspace/AOS_GRAPH_RAG_MODULE_IMPLEMENTATION_BRIEF.md) связывает owner sections, compatibility mapping и оставшиеся inputs; actual runtime, installed support, independent validation и экономия — `NOT_RUN`. Будущий агент перед реализацией сверяет current owners и exact revisions, не воспроизводит архивные инструкции AOS-3 как authority.

<a id="event-diagnostics-verification"></a>

### 22.4. FTR-025: один диагностический путь — DRAFT

Это проверка [ограниченного уточнения](06_Features.md#event-diagnostics-behavior) по §25.4–25.7 и [существующим стыкам](02_Architecture.md#event-diagnostics-contract), а не выбор полной FTR-025 для реализации. До подключения сравнить существующий action report/ledger с требуемым диагностическим ответом; новый writer нужен только при конкретном оставшемся gap. LES-049 обосновывает сохранение безопасной причины, не выбранный формат/сервис. Сначала один action с положительным результатом и воспроизводимым отказом диагностики; parent Incident/Lesson/Regression criteria остаются отдельными.

EV-C01–12 — спецификации проверок, execution NOT_RUN. Sources/IDs/actions и faults в fixtures искусственные, не production data/authority. При future runtime проверках используется actual public action adapter, isolated subject, наблюдение primary invocation/result и разрешённых I/O/output effects; fault injection не заполняет диск пользователя. В каждом отрицательном случае прочие необходимые inputs корректны. Expected values задаются по upstream outcome/binding независимо от logger.

| Case | Стимул | Ожидаемый результат / oracle |
|---|---|---|
| EV-C01 | Один разрешённый action A@1 с безопасными task/run/attempt refs: старт, затем фактический FAIL либо PASS | Пользователь различает A и попытку, начало и исход; correlation сохранена, причина соответствует upstream. Always SKIPPED/пустой журнал не проходит positive |
| EV-C02 | Primary не допущен; отдельно crash после старта без terminal observation | Нет одновременно «завершено» и «не допущено» одной попытке; crash не превращается в синтетический FAIL/PASS; отсутствие записи не доказывает отсутствие action |
| EV-C03 | Disabled/help/read-only/PLAN/VALIDATE/REVIEW; frozen destination при EXECUTE | Пропуск до diagnostic filesystem I/O/enqueue, нет mkdir/cache/lock/write. Snapshot и event capture подтверждают границу; enabled её не обходит |
| EV-C04 | Enabled EXECUTE без связанного destination/write scope; denied primary без отдельного права на запись | Нет скрытого destination/fallback/выданной authority; отказ primary сообщается существующим каналом. Только независимо покрытая запись может сохранить denied observation |
| EV-C05 | Secrets/URL/CR-LF/prompt/exception в raw input, extra field или неподтверждённом ID на реальном adapter | Raw payload не поступает в writer/output/error; вход отклонён или необязательный ID опущен с limitation. Regex/hash не проходят за provenance; обязательная потерянная correlation не даёт positive acceptance |
| EV-C06 | Native run ID не UUID; неоднозначный component; чужой subject; HRR/ACCEPT или несовместимый caller result | Не создаётся новая run identity ради формата; action обозначен exact binding либо gap. HRR/ACCEPT не technical event result; несовместимость ограничивает запись, исходный ответ primary сохраняется |
| EV-C07 | Primary FAIL/PASS/NOT_RUN/UNKNOWN плюс recording failure/limit; отдельно warning channel тоже недоступен | Primary result/exit semantics не меняются; один безопасный warning в совместимом канале, нет JSON pollution/рекурсивной записи/primary retry. При потере канала доставка limitation не заявляется |
| EV-C08 | Подмена destination/link, чужие permissions/data, два worktrees; unsupported profile | Только declared boundary, без изменения external sentinel, tracked/user files/Git. Ни cwd, ни одинаковый branch не объединяют storage; ошибка logger не исправляет чужие данные |
| EV-C09 | Concurrent writers, declared capacity exceeded, interruption/partial write, неизвестное подтверждение | Целые записи либо явный bounded failure; cap не превышен конкурентами. Нет corruption repair/auto-delete/retry; unknown outcome требует owner reconciliation, а не повтор primary |
| EV-C10 | Update incompatible reader/profile; disable/remove с in-flight записью; read missing/partial history | Старые данные не переинтерпретируются/не удаляются; started effects reconciled, ordinary report работает без диагностики. Read не создаёт/не ремонтирует storage; partial history честно ограничена |
| EV-C11 | Mutable diagnostic запись объявлена C-010; required Evidence отсутствует при primary PASS | Нет automatic Evidence/acceptance/root cause/aggregate PASS. Отдельный Evidence owner связывает exact snapshot/subject/limitations; журнал не становится C-012 ledger |
| EV-C12 | Writer unit positive, но реальный adapter теряет action ref, скрывает limitation либо повторяет primary после lost ack; отдельно исправный сквозной путь и новый сеанс | Нарушенный стык не проходит общий критерий. Positive source→adapter→diagnostic channel доступен пользователю; resume сохраняет correlation и сверяет unknown effects без повторного action. Отключение 025 не ломает required core reporting |

Контроль пользы: по одной выбранной проблеме получатель называет action/attempt/outcome и существенное ограничение без raw secrets и скрытого контекста. Если тот же ответ уже даёт existing report/ledger, фиксируется отсутствие основания для дополнительного writer. Коды OPERATION_ERROR/UNCLASSIFIED сами по себе не доказывают диагностическую достаточность для конкретного failure. До эксперимента задать предмет, read/output/effects scope, finite budget, доступную среду и критерий полезного различения. Учитывать задержку/дополнительные I/O, потери при заполнении/отключении и затраты сопровождения; численная экономия пока UNKNOWN.

Проверка структуры описания не заменяет concurrency/security/installed E2E. Для запуска нужны actual target, выбранный action/version, caller result/identity mapping, безопасный channel и поддержанный storage/profile с границами сохранности/retention. Один будущий C-005/C-006 связывает покрытые действия и checks; нет нового logger admission gate или обязательной FTR-021/023/026. Формат/utility/синхронизация выбираются агентом внутри принятых WHAT. Runtime, experiment и independent review — NOT_RUN.

## 23. Цепочка готовности

```text
Detailed Feature Passport ≠ accepted feature
Accepted feature ≠ accepted architecture
Accepted architecture ≠ Task Brief
Task Brief ≠ Execution Authorization
Successful implementation ≠ human acceptance
Human acceptance ≠ Git delivery
```

<a id="scaffold-core-development"></a>

## 24. Автономная разработка scaffold/core — принятый contract

Scope [S0–K4](01_Product.md#scaffold-core-outcome), R7/V3 и policy приняты HD-01…28;
фактический запуск всё ещё требует SC-DEC-04. Матрица V3 и predicate остаются у
Architecture §7 и Development §10; S0–K4 не новые lifecycle enums.

### 24.1. До первого effect

1. Прочитать Core decisions → Product outcome → [базовые dossiers](06_Features.md#core-first-scope) → Architecture interfaces → этот workflow и производный brief. Старый blueprint используется только для разрешения конкретного вопроса через Reference.
2. Привязать exact task/revision, target/root/worktree/base и принятую contract revision; сохранить observed dirt/ownership и запрещённые paths. Существующий repository не считать новым пустым проектом.
3. Уточнить только существенные отсутствующие входы. Готовые Intent/Spec/Passport и исходные человеческие ответы не проходят повторное интервью ради ceremony.
4. Сформировать конечные acceptance criteria и их dependency order для всего S0–K4. Декомпозиция — работа агента внутри scope; backlog FTR-007 не обязателен. Это не transport queue C-016, выбранная для первого ядра.
5. Bind действующую runtime authority и [host capability](02_Architecture.md#scaffold-core-host), command/environment и допустимую test/probe boundary. Проверить доверенное происхождение input, срок/отзыв, ресурсные ограничения и supported resume.
6. Required host/environment check без Evidence даёт конкретный BLOCKED/NOT_RUN для зависимого product effect. Покрытые изолированные native probes и supervised preparation по §24.1a продолжаются; нельзя начать runtime S0 под видом проверки собственного ещё не реализованного guard.

Для положительного автономного пути C-005 ссылается на exact заранее принятые C-002/C-003. Генерация новых DRAFT-версий в K1 не делает их accepted и не заменяет source binding задачи. Поэтому проверка intake/spec generation и исполнение по уже принятым входам различаются; недостаточная идея, требующая нового человеческого выбора, не обещает uninterrupted autonomous completion.

<a id="native-host-bounded-probes"></a>

### 24.1a. Native probes до решения о новом механизме — D1

[Human решение D1](00_Core.md#host-integration-d1) задаёт bounded experiment,
не новый product module. Сначала привязать для каждого probe exact installed
host/interface/version, task/candidate/state, входной допуск, allowed paths/effects,
инъекцию отказа, независимый oracle, timeout/budget и evidence destination.
Непривязанный интерфейс/доступ оставляет зависимый probe `NOT_RUN` с точным gap;
это не FAIL capability. Не требовать от ещё проверяемой capability заранее
доказать саму себя: изолированный probe ограничивается независимо от её результата.

| Probe | Минимальный positive/negative case | Критерий и предел |
|---|---|---|
| NP-01 — admission/state binding | Один native разрешённый effect; отдельно менять по одному candidate/state/current authority до dispatch, повторить тот же native допуск; revoked/expired случаи с действительным источником либо явно обозначенным contract fixture | При совпадении effect выполнен, при mismatch/reuse/отзыве effect отсутствует. Fixture decision не доказывает реальный Human capture; plain sandbox replay не является replay native approval |
| NP-02 — fresh-context continuation | Native trigger запускает новую сессию, которой переданы только locator durable parent state и минимальная инструкция поиска | Без prior chat/ручного «продолжи» обнаружены task, candidate, budget и next safe action; read-only результат. Старый transcript через resume/fork или excludeTurns не доказывает fresh context |
| NP-03 — single continuer | Два task-owned contender предъявляют одну pending operation через штатный маршрут; после завершения первого остаётся устаревший contender | Native boundary допускает не больше одного effectful owner и отклоняет устаревший effect. Наблюдатель не сериализует вызовы собственным lock; contenders не имеют обходного права записи |
| NP-04 — interruption/resume | Реально прервать только disposable task-owned process/session в заранее выбранной точке; native trigger при доступном host запускает fresh continuation | Durable state/budget сохранены; current repository/state сверены, определён безопасный шаг. Ручной старт проверяет recoverability отдельно, не autonomous resume |
| NP-05 — duplicate-effect protection | Разрешить одну append-запись «7»; прерывание до effect и после effect до receipt/checkpoint; повторный native вход той же operation | Подтверждённый effect не повторяется; при доказанном no-effect возможен fresh допуск; при неопределённости WAIT_EVIDENCE. Oracle читает точные bytes и operation evidence; идемпотентная overwrite скрыла бы duplicate |

NP-01…05 уточняют порядок минимальных checks SC-T04/09/21/22 и OSS-C03…05,
не заменяют полный HD-28 или все V3 обязательства. Изолированные положительные
результаты не закрывают сквозной proof. Runtime результат каждого нового NP —
`NOT_RUN` до фактического выполнения; прежние narrow Evidence используются только
при совпадении проверенной гарантии и current binding.

`PASS` требует фактического ожидаемого результата и отрицательного контроля.
`FAIL` native capability требует валидного входа, поддержанного native маршрута,
наблюдаемого нарушения выбранной гарантии и исключения ошибки fixture/привязки;
точные условия и actual/expected сохраняются. Потерянный вывод — `UNKNOWN`,
неисполненный/неподготовленный случай — `NOT_RUN`/`BLOCKED`. Ошибка setup
диагностируется отдельно, не служит основанием permanent control layer.
Обычная bounded correction harness допустима внутри полномочий, но нельзя
«исправить» тест реализацией отсутствующей проверяемой защиты в его driver.

После конкретного native FAIL остановить зависимый путь и вернуть минимальный
недостающий механизм, почему штатного недостаточно, варианты, стоимость/риски и
отдельное Human решение на architecture change. До этого permanent adapter не
вводится. Нет progress/new evidence — остановить соответствующий цикл, без
бесконечного поиска настроек или повторения одинаковых probes.

**Supervised preparation:** можно подготовить входы/изоляцию/dependency order,
команды будущей сборки и проверок, ручные контрольные точки и ограничения.
Runtime-код/scaffolding и запуск сборки не следуют из такой подготовки.
Самостоятельное выполнение внутри одного разрешённого run, ручное восстановление
и полная autonomous readiness — три разных claims. Если позже отдельно разрешена
supervised implementation, её Evidence не повышается до autonomous resume/HD-28.

### 24.2. Внешний development loop с S0

Внешний host сохраняет task checkpoint и владеет продолжением; worker выполняет одно разрешённое действие и возвращает наблюдения. Fresh action boundary должна соответствовать гарантиям canonical parent/envelope contracts, даже когда host использует своё native представление.

Следующий шаг определяется §10.5: reconcile effect → проверить authority/identity → восстановить state → диагностировать failing check → разрешить material unknown → взять dependency-ready критерий → affected checks → final validation. Действующий scheduler/launcher принадлежит host, не создаётся молча как дополнительный product scope.

После каждого material transition сохраняется достаточный checkpoint по
[HD-16/17](02_Architecture.md#first-core-durable-state), включая результат
значимого action; это не отдельный artifact на каждый низкоуровневый вызов.
Worker выдаёт factual report и останавливается, host продолжает ту же parent task.
Обычная correction получает новое action binding/candidate, без нового product plan.

Порядок реализации — S0 → K1 → K2 → K3 → K4; обязательные support contracts создаются до их первого consumer. Например, K2 уже требует durable state, scope reconciliation и независимой от worker проверки. Неполный промежуточный срез не выдаётся за готовое ядро. Если initial authority покрывает все срезы, их переходы не создают дополнительные Human Gates.

До готовности product controller не требуются команды AOS для выдачи внешней authority, записи первоначального state или запуска локального test harness. Product registry/queue C-015/C-016 создаются по Architecture §6.5, без зависимости от собственного transport; профиль заранее задаёт finite capacity/payload/wait/claim/retry/retention и покрытые service paths. Внешнему host до S0 не приписывается готовая product queue. Внешний host обязан обеспечить эти гарантии своим проверенным способом. Нельзя «для bootstrap» пропустить current authority, candidate identity или evidence collection.

Первый product checkpoint готовится по [initial-state contract](#initial-product-state)
до K2. SC-DEC-04 должен явно покрывать служебную инициализацию; внешний host
доказывает соответствие [набору V3](02_Architecture.md#core-loop-v3), включая
диагностические checks, конфликт владельцев, vocabulary/report и lifecycle admission. V1/V2 conformance не переносится; host должен доказать SC-T21/22 до зависимого запуска.

### 24.3. Прерывание и передача controller

**HD-18 — автоматическое продолжение обязательно.** Прерывание → durable state
сохранён → подходящий host вновь доступен → reconciliation/stale detection →
safe next action → автоматическое продолжение. Пользователь не восстанавливает
контекст вручную и не посылает повторно «продолжи». Это требование, не доказанная
возможность Codex. Host должен обнаружить незавершённый parent без прежнего чата.

**HD-19 — real interruption/resume обязателен.** Испытание должно реально прервать
process/session активной задачи, сохранить durable state, открыть fresh/new
session без prior chat context, обнаружить незавершённую задачу, сверить repository
и state, автоматически продолжить с безопасного места без повторения завершённого
material effect. Ручной запуск или наличие checkpoint не PASS. Если selected
Codex host не умеет true wake/resume, capability остаётся unsupported/BLOCKED для
автономного профиля. Его нельзя «доказать» созданием нового controller/daemon;
новый материальный механизм рассматривается по HD-13. Проверка сейчас NOT_RUN.

При supported interruption host инициирует новый run через заявленный trigger и сначала восстанавливает checkpoint. Uncertain effects сверяются с target до retry; resources/ledger не сбрасываются, отозванная authority не восстанавливается из cache. После run allowance — resumable PAUSED_RESOURCE; продолжение возможно только при наличии host resources и исходного task hard limit. Нет ресурса или способа wake — честная пауза с exact next action.

Рабочую разработку можно оставить на внешнем loop до конца S0–K4. Передача product controller — отдельная техническая возможность внутри scope, если предусмотрена принятым brief. Она требует проверенных positive/negative product runs, supported переноса task/authority/ledger, reconciliation, одного active continuation owner и fresh preflight. Если перенос невозможен, внешний route продолжается; нельзя обнулить history или признать новый task завершением старого. Если обязательность передачи выбрана человеком, отсутствие доказательства блокирует этот критерий.

Ручное «продолжи» доказывает только assisted resume. Полное автономное продолжение после остановки host process требует фактического подтверждения выбранного внешнего trigger; наличие записанного next action не равно его запуску.

### 24.4. Check entrypoints и Evidence

До исполнения implementation agent связывает следующие логические операции с фактическими командами выбранного toolchain/host. Это требования к будущим entrypoints, не уже существующие команды:

| Операция | Preconditions и требуемый результат |
|---|---|
| PREPARE | Поддержанный runtime, разрешённые dependency sources и disposable environment; объявленные runtime/dev зависимости установлены без изменения unrelated state |
| START | Exact candidate, минимальная surface/help; видны версия/идентичность, отсутствие скрытого network и durable writes у help/read-only |
| CHECK-SCAFFOLD | PREPARE/START; подтверждены состав/identity, imports/runtime deps, инструкции и отдельный запуск из поддержанного окружения |
| CHECK-CORE | Собранные contracts и fixtures; unit/contract/integration, выбранные SC-T cases и fail-closed aggregation на exact candidate |
| CHECK-HOST | Real selected host и разрешённая probe boundary; admission/denial/interruption/resume подтверждены отдельно от fake adapter tests |
| FINAL-CHECK | Все нужные компоненты доступны; полный интегрированный positive journey, material negative paths и fresh required Evidence для S0–K4 |

Каждый check binding содержит check ID, command/runner, environment/provenance, subject, required/conditional flag, independent oracle, ожидаемый результат, Evidence destination и ограничения. Raw exits сохраняются вместе с canonical result; failure не получает успешный exit, required NOT_RUN не агрегируется в PASS. Test-generated artifacts допускаются в объявленной disposable области; validator не исправляет проверяемый subject. Тестирующий launcher не использует runtime под тестом как единственный oracle собственного результата.

Изменение candidate делает affected Evidence stale. Узкая повторная проверка допустима лишь при известном impact; иначе расширить required проверку либо показать UNKNOWN. Fake/synthetic, installed execution и native/host Evidence помечаются раздельно; один вид не подменяет другой.

<a id="scaffold-core-checks"></a>

### 24.5. Обязательные сценарии scaffold/core

Это спецификация будущих запусков. В документационной работе runtime всех SC-T — NOT_RUN.

| ID / критерий | Дано → действие | Наблюдаемый результат и oracle | Required Evidence / affected scope |
|---|---|---|---|
| SC-T01 — безопасный target | Supported target с unrelated изменениями → preflight; отдельно wrong root и path escape | Точный preview; invalid target отвергнут до эффекта; byte/staging сравнение доказывает сохранность | CHECK-SCAFFOLD; S0, FTR-009/019 |
| SC-T02 — воспроизводимый scaffold | Чистая поддержанная среда → PREPARE/START/CHECK-SCAFFOLD; отдельно missing runtime dependency | Установка/запуск из объявленных inputs; import provenance; missing prerequisite виден как незакрытый check. Проверяется сохранность и на success, и на error | S0; отдельно source и installed claims, если заявлена установка |
| SC-T03 — достаточные inputs | Заранее подтверждённые request/answers/constraints → K1; отдельно пустой/противоречивый input | Смысл и происхождение сохранены в C-001/002/003/005; нет повторной human selection достаточного входа; gap не превращён в approval | CHECK-CORE; FTR-001/002/003/006, сравнение с исходным oracle |
| SC-T04 — admission | Valid authorization/action → разрешённый probe; отдельно stale/revoked/replayed/forbidden input | Positive effect ровно один раз; каждый отрицательный вариант без эффекта. Synthetic record отдельно от настоящей host authority | CHECK-CORE + CHECK-HOST; FTR-006/009/010/019, C-006A |
| SC-T05 — effect и проверка scope | Одна разрешённая запись → исполнение и validation; отдельно unexpected changed path | C-008 соответствует actual diff; exact subject проверен; незаявленный effect исключает успешное завершение | CHECK-CORE; FTR-010/013/011, independent filesystem observation |
| SC-T06 — correction | Воспроизводимый дефект с различающим Evidence → D0…D5/gate/correction/check | Falsifiable prediction, fresh action/candidate, исправленный criterion; слабое Evidence даёт DENY, не speculative patch | CHECK-CORE; FTR-010/011/014, ledger и fresh affected checks |
| SC-T07 — anti-loop | Та же signature, две corrections без progress или два inconclusive checks уровня → следующий выбор | Mutation прекращается/diagnostics расширяется по §10.4; смена worker/session не сбрасывает попытки | CHECK-CORE; controller/ledger; сравнение истории действий |
| SC-T08 — final finding | Exact candidate → итоговый validator находит дефект | Validator ничего не исправляет; отдельные diagnosis/corrector/new candidate и affected final check; прежний PASS не переиспользуется | CHECK-CORE; FTR-010/011/013 |
| SC-T09 — interrupted effect | Отдельные прерывания до effect, после effect и до сохранения результата → fresh process/session; C-008 полный, неполный и отсутствующий — отдельные варианты | Reconciliation по dispatch/envelope/ledger и независимым observations определяет actual effect до retry; доказанные effect/no-effect различаются, недостаточные факты → WAIT_EVIDENCE. Missing C-008 не блокирует исследование и не заменяется выдуманным report; нет повторной записи, потери user state или ложного completion | CHECK-CORE + CHECK-HOST; FTR-014/016, внешнее наблюдение effect и сохранённый ledger |
| SC-T10 — resource pause | Исчерпан конечный run allowance → host trigger/resume; отдельно достигнут task hard limit | Task history сохранена, новый run rebind authority; пределы не обходятся. Самостоятельный wake подтверждается real host event, manual resume явно ограничен | CHECK-HOST; host, FTR-014/016; автоматический resume required для полной автономности |
| SC-T11 — неполная проверка | Required check отсутствует/stale, impact неизвестен либо Evidence недоступно → aggregation/next | Нет PASS/TECHNICALLY_COMPLETE; названы exact missing criterion/evidence и допустимый следующий шаг | CHECK-CORE; FTR-011/008/012, C-009/010 |
| SC-T12 — optional отсутствует | Базовая task без installer/index/CI/patterns → core journey; отдельно required CI без approved equivalent | Основной путь проходит без optional services; отсутствующий required результат остаётся NOT_RUN, guard сохраняется | CHECK-CORE; core consumers, negative capability case |
| SC-T13 — изменение стыка | Изменён обязательный input/version; отдельно модуль отключён с незавершённым effect → consumer/resume | Старый reader отказывает явно; affected consumers обнаружены, state/effects reconciled; migration/удаление не выполняются скрыто | CHECK-CORE; Architecture §6.1/6.4, saved-state fixtures и relevant consumers |
| SC-T14 — единый результат | Достаточная task и разрешённый disposable target → продукт создаёт один файл с заданным содержимым, проверяет и выдаёт review/handoff; controlled defect + resume — отдельные варианты | Real selected adapter меняет только разрешённый файл; oracle сравнивает bytes, Evidence и состояние. Подтверждены все критерии S0–K4, human acceptance не сгенерировано | FINAL-CHECK + CHECK-HOST; весь core journey. Actual controller takeover проверяется дополнительно, если включён в scope |

Дополнение R2 закрывает transition/state findings; все перечисленные подслучаи
обязательны и получают отдельный check binding при реализации.

| ID / критерий | Дано → действие | Наблюдаемый результат и oracle | Required Evidence / affected scope |
|---|---|---|---|
| SC-T15 — диагностический маршрут | Finding → DIAGNOSE → DIAGNOSTIC CHECK → DIAGNOSE; отдельно подтверждена correction, опровергнута необходимость mutation, данные inconclusive | Ledger/signature/level сохраняются; в первом случае fresh gate/corrector, во втором SELECT_NEXT_ACTION и отдельные required checks, в третьем расширение/WAIT_EVIDENCE. Diagnostic PASS не закрывает критерий. Неверный purpose/transition, stale/replayed C-009 отклоняются | CHECK-CORE + CHECK-HOST; FTR-010/011, C-009/009A/012; trace purpose и state |
| SC-T16 — конфликт владельцев | Конкурирующий update во время CHECK; отдельно во время EXECUTE с consumed envelope/unknown effect; затем takeover, terminal state и unresolved wait как отдельные случаи; missing C-008 при сохранённом admission и конфликт/прерывание lifecycle publication | Проигравший не пишет shared state и не dispatch; пока победитель активен второго владельца нет. Свежий владелец использует IDLE/resume/RECOVER_STATE, сохраняет lifecycle/ledger, сверяет admission и target без требования полного C-008; нет частичного переключения или двойного dispatch. Terminal не возобновляется, wait не обходится | CHECK-CORE + CHECK-HOST; FTR-010/014/016, state/event/owner и внешнее наблюдение effects |
| SC-T17 — первое состояние | Явный NEW task с пустой доказанной историей → create; отдельно повтор identity, прерывание до/после публикации, incomplete publication, missing/corrupt record при RESUME | Один исходный C-012, без product effect; BIND_TASK → RECOVER_STATE → SELECT_NEXT_ACTION. Existing не перезаписывается, потерянное не заменяется пустым; прерывание reconciled до продолжения, unknown запрещает dispatch | CHECK-CORE + CHECK-HOST; FTR-010/014/016, C-005/006/012; независимое наблюдение state/effects |
| SC-T18 — совместимость V3 | Согласованный набор V3 → journey; отдельно V1/V2/mixed/unknown records или только V1/V2 host report | V3 проходит positive case, остальные не получают V3 resume/dispatch; supported inspection без effects, исходные bytes сохранены, никакой подмены version/migration | CHECK-CORE + CHECK-HOST; все реальные readers изменённых contracts, host conformance |

SC-T16 дополнительно проверяет takeover из `ACTIVE/RUNNING/CHECK` при полностью
reconciled effect и без wait/resource pause: публикация доказанного recovery
checkpoint `ACTIVE/RUNNING/IDLE` → прерывание → новый единственный владелец →
`RECOVER_STATE`. Положительный вариант сохраняет ledger и не получает ложный
CONTRACT_VIOLATION. Отдельные отрицательные варианты — отсутствующий/подменённый
owner/reconciliation binding и произвольный idle без основания; dispatch запрещён.
Oracle сверяет сохранённые tuples и основания по §10.2, включая FTR-006.N01.

NEW/RESUME в SC-T17 — обозначения входных сценариев, не новые task-state enums.
SC-T05/08 дополнительно наблюдают порядок dispatch: EXECUTE stop до CHECK,
CORRECT — отдельный worker после gate, затем fresh affected checks. SC-T14
включает первый product checkpoint и применимые SC-T15…18; один happy path
не заменяет их негативные варианты. Каждый trace связывает вход, producer,
consumer, допустимый переход, observation и следующий action. Декларация будущего
сценария не является доказательством исполненного runtime.

Для каждого negative case остальные inputs корректны; constant-deny implementation не проходит positive case. Проверка SC-T14 через fake adapter даёт только simulation Evidence и не закрывает real-adapter/host критерий. Утверждение о самостоятельной разработке всего S0–K4 требует отдельной истории внешнего development run; один успешный продуктовый пример доказывает только свой сценарий.

SC-T12/13 не требуют создавать поздние installer/CI/plugin-модули. Отсутствие capability, incompatible record и interrupted optional producer проверяются contract fixtures/test doubles в объявленной test boundary с сохранением реальных core consumers; actual отключение проверяется только для уже включённой capability. Такое Evidence относится к contract handling, а не к работоспособности несуществующего модуля. При дальнейшей интеграции конкретной фичи её реальные стыки проверяются по §25.

<a id="core-platform-checks"></a>

### 24.6. Первая проверка ОС и переносимость

Переносимость обязательна для всего S0–K4. Для первого результата required native
среда — macOS в exact profile SC-DEC-02: OS version, machine architecture, runtime,
filesystem semantics и adapter limits фиксируются до launch. PREPARE/START и
применимые SC-T01…26 выполняются с current Evidence на этом профиле. Одна
конфигурация не доказывает поддержку всех macOS.

Linux/Windows — целевые, пока native checks NOT_RUN. Их отсутствие не блокирует
первое macOS completion, но запрещает claim проверенной поддержки этих ОС.
Contract fixtures для платформенных различий обязательны уже сейчас; test doubles
не заменяют native Linux/Windows Evidence. Все подслучаи ниже получают отдельный
check binding; создание остальных adapters и remote CI не требуется этой задачей.

| ID / критерий | Дано → действие | Наблюдаемый результат и oracle | Required Evidence / affected scope |
|---|---|---|---|
| SC-T19 — платформенные capabilities | Пути с пробелами/Unicode, различия регистра/разделителей; отдельно нет Unix shell/macOS utility, обязательной capability, прав; process termination и прерванная file operation | Нет смены subject/scope или collision loss; declared adapter выполняет поддержанное без обязательной shell-зависимости ядра. Missing capability блокирует только зависимое, независимое чтение доступно; неизвестный effect reconciled, неподтверждённый fallback не запускается | CHECK-CORE + CHECK-HOST для границ host; FTR-002/008/009/010/011/013/014; native macOS и различающие contract fixtures |
| SC-T20 — перенос state и support claim | Поддержанный C-012 из другой среды → inspection; отдельно mismatch paths/permissions/environment/authority, неизвестный effect и отсутствие native Linux/Windows Evidence | Inspection не выполняет resume/effect; mismatch блокирует dispatch без переписывания state/ledger. Fixture PASS не означает native support. Отчёт ограничен проверенным macOS profile, Linux/Windows явно NOT_RUN | CHECK-CORE; FTR-009/010/011/013/014/016, C-012 и current admission bindings |

SC-T14 включает применимые SC-T19/20 и platform limitations. Реализация конкретных
команд, fixtures, storage и переносимого identity mechanism — HOW агента в
принятых границах; он фиксирует bindings до check, не назначает сам host/provider
или новую platform support promise. Платформенные требования не добавляют controller edges; текущие версии и lifecycle
условия задаёт [набор V3](02_Architecture.md#core-loop-v3).

<a id="core-r5-checks"></a>

### 24.7. Vocabulary, report и lifecycle — R5

Каждый перечисленный подслучай получает отдельный check binding; SC-T21/22
обязательны вместе с SC-T01…20, а не заменяют прежние negative cases. Повторяются
на реальном host в его boundary до зависимого запуска и на продукте при готовности
consumers. Fixtures не доказывают соответствие внешнего host.

| ID / критерий | Дано → действие | Наблюдаемый результат и oracle | Required Evidence / affected scope |
|---|---|---|---|
| SC-T21 — Result Contract и report | Отдельно все шесть technical enums через producer → validator → controller → status/review; отдельно HUMAN_REVIEW_REQUIRED, WAIT_HUMAN и неизвестный enum. Два последовательных worker с одной current parent и разными envelopes; отдельно replay, NONE с причиной, неизвестный consumption и старый неоднозначный report | Допустимые значения сохраняются; invalid не конвертируется и даёт отдельный CONTRACT_VIOLATION. Report различает lifecycle/action, exact parent и конкретный envelope. Первый CONSUMED не расходует parent; replay запрещён, UNKNOWN не становится UNUSED, NONE не скрывает непокрытый effect | CHECK-CORE + CHECK-HOST; C-006/006A/008/009/010/012, FTR-006/008/010/011/012/014; oracle — независимое сравнение входных значений/bindings и actual effects |
| SC-T22 — явный lifecycle полного цикла | Принятая task → EXECUTE → CHECK → finding → DIAGNOSE → CORRECT → CHECK → FINAL_VALIDATE → REVIEW; отдельно вход PLAN без достаточного принятого input, standalone read-only task, повтор той же stage, DIAGNOSTIC PASS, final finding, pause/resume, конфликт и прерывание atomic publication, stale state, terminal REVIEW | Lifecycle EXECUTE/VALIDATE меняется только controller в разрешённом scope; отдельный corrector, одна task/revision и непрерывная authority/ledger. PLAN не повышает DRAFT, read-only не получает mutation. Diagnostic PASS не закрывает criterion. Нет частичного stage/action/consumption commit, двойного dispatch или ложного stale из-за собственного admission. REVIEW возникает при predicate, не означает ACCEPT и не открывает terminal task | CHECK-CORE + CHECK-HOST; C-005/006/006A/009/009A/012, FTR-006/010/011/014/016; oracle — source task/authority + before/after state/event/admission и независимые observations target |

SC-T14 включает SC-T21/22 и применимые новые варианты SC-T09/16. Финальный
review показывает отдельно technical result, task/run state и lifecycle;
история внешней разработки S0–K4 требуется независимо от product journey.

<a id="core-transport-checks"></a>

### 24.8. Коннекторы и сохраняемая очередь — R7

C-015/C-016 — обязательная граница первого ядра. Ниже future runtime cases;
каждый перечисленный positive/negative вариант получает отдельный check binding
с exact profile, независимым oracle и Evidence. S0 описывает интерфейсы и
preparation; admission/durability обязательны до queued effect K2, полные
recovery/integration cases закрываются при готовности K3/K4. Нельзя требовать
готовую product queue как prerequisite внешней разработки S0.

| ID | Дано → действие | Результат и oracle | Область |
|---|---|---|---|
| SC-T23 | Совместимые C-015 и direct read; отдельно unknown interface/version, missing capability, disabled module, попытка скрытого effect и initial registry/queue create interrupted | Корректное чтение возвращает exact result без product writes; invalid не вызывает handler. Required missing виден; повтор create не перезаписывает историю. Oracle — independent target/config/filesystem observation и contract binding | FTR-009/010/011/016/019/008; registration/direct mode и bootstrap |
| SC-T24 | Durable enqueue → current admission → один effect; отдельно malformed payload, stale subject/generation, revoked authority, сообщение с вложенным Stage Envelope, event с попыткой выдать permission | Accepted только после durable записи; COMMAND в task получает соответствующий fresh V3 admission, read-only EVENT проходит отдельный маршрут ниже. Старый/подменённый input отклонён без effect, событие не становится authority. Oracle — stored message/admission/ledger и independent effect/result observation | FTR-010/016/019/011/008/012, C-015/C-016 и C-006/006A/009/012 |
| SC-T25 | Duplicate message/operation; отдельно same ID/different payload, crash до/после effect, lost ack, истёкший claim при живом worker, cancel pending/admitted | Нет двойного логического effect или ложного no-effect; исходный result сохраняет свой subject. Unknown сначала reconcile, active owner fenced до takeover. Pending cancellation не races с dispatch; admitted cancel не объявляется успешным без наблюдения. Oracle — operation history и actual target, не только ack | FTR-010/014/016; отдельные lifecycle/transport states |
| SC-T26 | Capacity/payload limit, expiry, retry exhaustion; отдельно missing finite profile, incompatible saved message, module disable/update/remove с pending/in-flight и required consumer | Нет silent drop/unlimited retry; причины и данные сохранены. Новая работа после disable не принята, pending удержана, in-flight reconciled. Migration/удаление не скрыты, required consumer без замены блокирует удаление. Oracle — queue/registration state, saved artifacts и consumer journey | C-015/C-016, FTR-009/010/014/016/019/011; пределы, совместимость и lifecycle |

SC-T24 дополнительно проверяет C-010 event по действующей разрешённой подписке
без активной C-005 и после terminal исходной task: FTR-010 доставляет наблюдение
read-only consumers FTR-008/012, не создаёт фиктивную задачу/envelope и не открывает
terminal task. Result Contract используется без ValidationEnvelope; service
receipts записываются только в отдельно покрытой области. Отдельные negative
варианты: отозванный subscription/read scope, stale binding, недоступная authority
на служебную запись и попытка effectful follow-up без собственной active task и
current authority. Oracle проверяет payload/result, receipts, отсутствие product
mutation и неизменность task/lifecycle state. Две объявленные подписки получают
свои delivery observations; результат одной не закрывает другую.
Отдельный положительный follow-up использует заранее существующую active C-005
и current C-006: controller допускает связанный COMMAND по V3, effect наблюдается
ровно один раз. Доставка события сама не выдаёт полномочий этому COMMAND.

SC-T14 сохраняет все прежние критерии и получает direct read + queued file-effect
варианты в разрешённом disposable target с новым message/operation binding.
SC-T23…26 входят в общий FINAL-CHECK; успешный direct путь не заменяет queued
journey и negative cases. История автономной разработки и работа product queue
доказываются отдельно. Queue claim/ack не агрегируются в технический PASS.

<a id="oss-core-verification"></a>

### 24.9. Контрольные варианты восстановления и host — SCAFFOLD_CORE_DRAFT

Адаптация [RF-13–15](05_Reference.md#oss-reference-adaptation) уточняет способы
проверки SC-T04/09/10/11/13/18/21/22/24. Обязательные исходы уже принадлежат
C-006A/C-010/C-012/C-016 и [host contract](02_Architecture.md#scaffold-core-host).
Это документальные варианты existing checks, не новый набор версий или gate,
не выбор Temporal/LangGraph/OpenHands и не реализация scheduler в notebook.
Все runtime результаты NOT_RUN; до probe нужны exact host/profile и отдельная
покрытая область effects по SC-DEC-04. Библиотечный пример не выдаёт authority.

Для выбранного варианта заранее задать task/subject/version, входное сохранённое
состояние, допустимый next action, наблюдаемые effects и условие отказа. Oracle
берётся из task/owners и независимого наблюдения target, не из вывода worker.
Исторические записи используются без изменения их bytes; проверка совместимости
не повторяет исторические внешние effects. Replay history как у Temporal — один
возможный HOW; AOS не требует event sourcing или конкретного формата history.

| Вариант / existing checks | Контрольный вход и действие | Ожидаемое различение / Evidence |
|---|---|---|
| OSS-C01 / SC-T09/13/18/22 | Завершённая и прерванная истории одной поддержанной contract version; новая реализация reader/controller; сначала read-only восстановление | Восстановлены тот же subject, факты effect, consumption, counters и допустимый следующий переход. Изменение трактовки CONSUMED/terminal не проходит; новые effects при проверке истории отсутствуют. Совместимость history не доказывает реальные dispatch/wake |
| OSS-C02 / SC-T18/21 | Те же файлы читаются без syntax errors, но record имеет V1/V2/mixed/unknown version вместо текущего V3 | Структурное чтение не даёт V3 resume/dispatch; явное ограничение версии, сохранённый оригинал. Успех только на пустой новой task не закрывает saved-state compatibility |
| OSS-C03 / SC-T09/24 | Разрешена одна append-запись строки «7» в изначально пустой disposable файл. Отдельно прерывание до effect; после append, но до receipt/checkpoint. Новый run повторно входит в обработчик | В первом варианте после подтверждённого no-effect и fresh admission запись возможна; во втором подтверждённый append не повторяется. Файл содержит одну строку, ledger связывает исход с той же operation; при недостатке наблюдений WAIT_EVIDENCE. Идемпотентная перезапись «7» сама не выявила бы повтор, поэтому здесь выбран append |
| OSS-C04 / SC-T04/09/21 | В checkpoint сохранён положительный ответ; до ещё не выполненного действия authority отозвана. Отдельно вместо решения передан произвольный resume=true | Нет effect по cached ответу или boolean без trusted origin/subject/scope. Положительный вариант с подлинным current решением должен пройти; безусловный отказ не закрывает admission. Проверяются actual target и current binding, не badge интерфейса |
| OSS-C05 / SC-T10/22 | Процесс исполнителя действительно прекращён в объявленной точке при pending task и доступном остатке бюджета. Срабатывает заранее выбранный внешний trigger; человек не пишет «продолжи» | Новый run восстанавливает ту же task/ledger и current authority; доказан один continuation owner. Отдельный старый/конкурирующий run не получает effect. Memory-only state, ручной перезапуск и одна лишь сохранённая next action не доказывают автономный wake; при отсутствии trigger этот claim BLOCKED/NOT_RUN |
| OSS-C06 / SC-T11/14/22 | Unit tests SDK/tools проходят; требуемый cross-package/integration/host check текущего candidate не выполнен либо относится к другой revision/environment | Required результат остаётся NOT_RUN/stale. Ночной CI старой версии не заменяет current Evidence. Положительный полный путь проверяет выбранный caller → admission → workspace/tool → observation → checkpoint → continuation; конкретный состав affected checks определяется изменённой гарантией |

Повторный вход в node после interrupt у LangGraph — повод проверить расположение
и учёт effect, не разрешение повторить его. Даже действие после точки approval
нужно проверить на crash после effect и до receipt. Наличие persistent state
не доказывает внешний запуск после смерти процесса. LocalWorkspace, контейнер,
API server и самостоятельный continuation — разные возможности: каждый claim
в host binding получает свой проверенный scope. Перечень пакетов OpenHands
не принимается за conformance и не делает optional server обязательным для AOS.

<a id="first-core-autonomy-proof"></a>

### 24.10. Полное эмпирическое доказательство первого ядра — HD-28

Обязательный E2E на exact Codex + macOS profile проверяет всю заявленную
историю автономной разработки, а не только существование компонентов или один
product example SC-T14. Перед запуском нужны SC-DEC-04 и покрытые probe/output
effects; настоящий Human ACCEPT не заменяется synthetic fixture.

```text
Human-approved bounded parent + current authority
→ intake/binding → adaptive internal decomposition → autonomous implementation
→ ordinary correction при необходимом дефекте → material durable checkpoints
→ real interruption → automatic fresh-session recovery без prior chat
→ no duplicate completed material effect → completion predicate
→ exact candidate frozen/bound → fresh read-only final validation
→ READY_FOR_HUMAN_REVIEW → explicit Human ACCEPT → один local Commit
```

Final validation входит в proof predicate; достижение остальных условий перед
freeze не выдаёт преждевременный PASS. После finding — HD-21 с новым candidate.
Технический результат, Human decision и commit result фиксируются раздельно;
terminal development state не отменяет предусмотренный HD-26 шаг доставки.

| Проверяемая граница | Независимое основание / отрицательный контроль |
|---|---|
| Один parent, B1, адаптивные children | Trace с исходными scope/authority/criteria показывает внутренние изменения и переходы без нового Human gate; независимый parent из backlog после завершения не активируется |
| Реализация и обычный дефект | Actual candidate/required checks; controlled ordinary defect проходит diagnosis/correction/re-check без изменения expected ради PASS |
| Durability и restart | Независимое наблюдение material state до/после реального interruption, fresh session без старого чата; actual wake event и один continuation owner, сохранённый budget |
| Unknown effect и stale authority | Завершённый append из OSS-C03 остаётся единственным; stale/revoked/mismatched inputs не дают effect, нехватка Evidence не становится no-effect |
| Final review | Exact frozen subject, fresh read-only context, явные actual check outcomes; намеренный дефект обнаруживается и validator не ремонтирует subject |
| ACCEPT и local Commit | Реальный current C-011, accepted candidate совпадает с commit tree/allowlist; forged/stale/другой subject не допускает Commit, unrelated файлы не включены |
| Предел доказательства | Required NOT_RUN/UNKNOWN не агрегируются в PASS; Push/Merge/Release отсутствуют без отдельных решений, Linux/Windows/другие hosts не считаются проверенными |

Одна доказанная история связывает эти границы и SC-T01…26, OSS-C01…06;
несвязанные synthetic/unit PASS не заменяют общий путь. Fixture human decisions
проверяют отрицательные и контрактные случаи отдельно от настоящего ACCEPT.
Все фактические результаты этого E2E, host conformance, trusted capture и
automatic resume сейчас **NOT_RUN**; поддержка wake и data routes **UNKNOWN**.
Новый обязательный Test Lab, service, scheduler или постоянная agent role не создаются.

<a id="feature-integration-readiness"></a>

## 25. Следующий модуль: автономная сборка и интеграция

Обязательный алгоритм создания/изменения фичи, формирования модуля и проверки
его достаточности — [§25.4](#feature-module-protocol); подключение/удаление —
[§25.5](#module-connection-lifecycle). Он применяется перед зависимой реализацией
и после изменения contracts, а не только при первом добавлении в каталог.

Содержательная read-only проверка достаточности документации проводится по
[§25.7](#feature-documentation-review). Это детализация проверки §25.4, а не
параллельный набор требований, новый lifecycle или разрешение на correction.

Для самостоятельного запуска позднего модуля применяется существующий §6 feature-specific workflow к
каждой входящей фиче на этапе подготовки, затем один общий маршрут разработки:
выбор модуля → достаточные contracts и анализ стыков → единый module brief и
parent authority → автономная сборка/интеграция/check/correction → integrated
review. У модуля из одной фичи это тот же маршрут. Все поздние dossiers
одновременно не перерабатываются.
Внутри заранее выбранной версии подготовленные модули связываются общей задачей
по [§25.0](#autonomous-project-development), без нового ручного запуска каждой части.

Перед runtime выбранная фича имеет observable outcome, actors/inputs/outputs/states/failures/recovery, критерии и негативные случаи. Её contract связывает реальные producers/consumers ядра и модулей, required/conditional inputs, data/state owner, версии и поддержку сохранённых задач, permissions/effects, отказ/отсутствие/отключение и состояние после interrupted operation. Архитектурное решение нужно лишь при существенном изменении принятой boundary; HOW внутри неё остаётся за агентом.

Проверка стыков прослеживает не только именованные inputs, но и основной процесс,
условные входы и acceptance/negative examples. Для фактического чтения contract
должен быть consumer либо явный делегированный маршрут; ссылка в примере сама по
себе не доказывает прямое чтение. Первоначальная подготовка не требует своего
будущего результата. Выбранные 005+022 проверяются и раздельно по FTR, и как
[единый модуль](06_Features.md#architecture-patterns-module); другие объединения
не подразумеваются. Регрессии текущих исправлений — [MOD-S16…23](#module-consistency-checks).

Acceptance включает проверки самой фичи, затронутых стыков и сохранности SC-T14 базового ядра с применимыми negative cases. Проверять все пары модулей без реального взаимодействия не требуется. Изменение core contract сначала готовится у owner с compatibility/impact, а не скрывается в implementation diff модуля. Optional capability не становится обязательной по удобству реализации; необходимый новый input требует явного расширения scope либо ограничения сценария.

Missing critical input даёт конкретное BLOCKED для зависимой реализации. Documentation readiness, actual contract/integration PASS, человеческое принятие и Git delivery остаются разными фактами; новый registry или параллельный lifecycle не создаётся.


<a id="autonomous-project-development"></a>

### 25.0. Общая задача конечной версии проекта — DRAFT

Это применение существующего complete-task controller к
[результату версии](01_Product.md#autonomous-project-outcome), уточнённое по
поручению исправить SYS-01. Оно не создаёт lifecycle, каталог или новые C-contracts
и не активирует выбранный scope по наличию этого текста.

**Короткий вход.** Exact Product Spec/Feature Passports и решения → состав версии,
общие сценарии/критерии и исключения → одна общая C-005 с отдельной C-006 → §10.
До запуска агент связывает каждый общий критерий с требованием, участвующими
частями/интерфейсами, check/oracle и Evidence. Вход включает существенные
архитектурные ограничения, необходимые внешние зависимости, target/host,
data/provider boundaries, разрешённые effects/outputs, limits и supported resume.
Недостающее решение не угадывается; отсутствие доступа учитывается отдельно
от достаточности требований по §25.7. Точный состав AOS остаётся предметом
существующих SC-DEC/MOD-DEC, а состав пользовательского проекта — его ТЗ.

**Два исполнителя.** При создании нового AOS внешний host ведёт общий цикл с S0
по §24; существующий target сначала проходит inventory/rebind, его готовые части
не пересоздаются автоматически. Выбранные модули после ядра могут быть внутренними
работами той же общей task.
При создании пользовательского проекта будущий AOS использует его принятое ТЗ,
проверенную техническую архитектуру и отдельно выданную authority. Подготовка
архитектуры входит в покрытую внутреннюю работу, если она ещё требуется перед
кодом; состав и передача результата определены в [Architecture](02_Architecture.md#architecture-output-handoff).
Обычный HOW не создаёт нового product choice. Внутренние contracts
подключения AOS C-015/C-016 не навязываются компонентам пользовательского проекта.
Для обоих применимы §10, границы checker/corrector и требования к реальному
host continuation; работа продукта и история его разработки проверяются отдельно.

**Внутренняя работа и зависимости.** До старта известны общие критерии,
обязательные стыки и порядок доступности существенных inputs; подробный список
actions уточняется по мере работы (§7). Controller выбирает dependency-ready
действие по §10.5, не просит выбрать следующую уже включённую часть. Backlog
FTR-007 может предлагать порядок, но не владеет state или admission. Отдельная
task по §7 не получает права из общей цели; переход к ней возможен только при
собственном допустимом binding. Такая граница не скрывается обещанием автономности.

Часть, создаваемая внутри выбранного scope, не обязана существовать до старта
всей версии. До её consumer известен contract, а к первому использованию готовы
требуемые реальные inputs и гарантии. Как в §24, support создаётся до первого
зависимого effect. Внешняя dependency вне scope не объявляется внутренней для
обхода readiness. Fixtures допустимы для промежуточных проверок в разрешённой
области, но не закрывают обязательную реальную интеграцию итоговой версии.

**Общее завершение и продолжение.** Критерии модуля AOS по §25.2 входят в критерии
общей C-005; у частей пользовательского проекта критерии следуют его ТЗ,
без автоматического добавления SC-T14 или других проверок самого AOS.
PASS части, в том числе K4 внутри более широкой версии, не переводит общую задачу в terminal REVIEW:
controller продолжает оставшиеся части и стыки, затем применяет §10.5 к current
общему candidate и выдаёт один review package. После mutation действует impact
basis/affected checks; неизвестное влияние не разрешает узкий итоговый PASS.
C-012 сохраняет этот общий остаток работы и ledger (§10.2). Lost effect сначала
reconciled; correction и anti-loop остаются по §10.3–10.4, resource pause не
обнуляет hard limit. Непроверенный resume trigger означает assisted mode.
Новый scope/существенное решение/непокрытый effect останавливает зависимую часть;
самостоятельная read-only task никогда не получает correction authority из §25.0.

**Документальный пример для §25.7.** Условное заранее принятое ТЗ версии содержит
две части: первая сохраняет запись `K=7`, вторая читает именно эту запись и
показывает `7`. В scope входят обе части, их реальный стык и проверки. Это
контрольный вход, не новый модуль/FTR или выбор состава AOS.

| Случай | Ожидаемый вывод и основание |
|---|---|
| Первая часть проверена; вторая ещё не создана | Общая задача ACTIVE, следующий доступный внутренний action выбирает controller без новой C-005/C-006; отсутствие создаваемой второй части до старта не является внешним blocker |
| Обе части локально PASS с fixtures, реальное чтение показывает старое значение `6` | Общий критерий не закрыт; diagnosis → разрешённая correction → affected integration checks. Заполненные ссылки и число PASS не заменяют проверку значения |
| После записи потеряно подтверждение, затем новый run | Сверить admission, target и ledger до повтора; восстановить и незавершённое чтение второй частью. Не начинать первую часть заново и не расходовать ресурс с нуля (§10.2) |
| Весь общий результат доказан; остаётся необязательная идея | §10.5 → общий REVIEW/handoff и stop; идея не возобновляет terminal task. Human ACCEPT/Git/deployment не выводятся из technical completion |

Применять восемь репетиций и обе попытки опровержения §25.7 к общему scope;
SC-T и MOD-A сохраняют свои области, этот пример не заменяет их. Авторский
документальный проход не является independent validation или runtime Evidence.

<a id="architecture-handoff-checks"></a>

**Проверка архитектурного handoff — DRAFT.** Для запроса архитектуры системы
проверить exact ТЗ → целостный документ FTR-005 → FTR-006 и зависимости внутренних
работ controller; при выборе FTR-007 потребителем проверить и его contribution/
dependencies на той же revision. Применимость берётся из scope сценария по
[Architecture](02_Architecture.md#architecture-output-handoff), а не выводится
из наличия/отсутствия установленного backlog. Подготовка C-005 и использование
документа внутри уже принятой task различаются по этому contract; исходная
C-005 не переписывается при передаче. Проверяющий сверяет содержание с источниками,
пропуски и противоречия передаёт на разрешённую correction; validation не меняет
subject. Сохраняются revision результата, метод, исход и ограничения проверки;
после изменения повторяются affected checks по §18.1. Проверка документа не
подменяет последующую проверку реализации или технический completion общей task.

| Контрольный случай | Ожидаемый результат |
|---|---|
| SIM-01.P1 — ТЗ требует сохранения K=7 и чтения именно этой записи; архитектура полна и доступна в exact revision, FTR-007 не выбран | FTR-006 получает документ и учитывает constraints/checks при подготовке Brief; в покрытой общей task controller ведёт зависимость чтения от готовой записи/стыка без переписывания C-005. Handoff завершён без FTR-007 и без нового Human Gate; установка backlog не требуется, общий результат проекта ещё не закрыт |
| SIM-01.P2 — тот же вход, FTR-007 выбран потребителем и доступен в совместимой версии | FTR-006 и FTR-007 используют одну exact revision; предложение порядка FTR-007 сохраняет зависимость чтения от записи, следующий action выбирает controller. Handoff включает проверенную реальную интеграцию с FTR-007 |
| SIM-01.N1 — тот же вход, интеграция с FTR-007 обязательна, но он недоступен либо несовместим; остальные inputs корректны | Зависимая передача BLOCKED; нет общего PASS handoff, подмены fixtures или необоснованной неприменимости. Независимая работа продолжается в scope; если consumer создаётся в нём, он готовится до использования |
| SIM-01.N2 — по отдельности в каждой конфигурации P1/P2 потеряно требование читать именно сохранённую запись либо разрешено чтение до готовности записи/стыка; остальные inputs корректны | Handoff не проходит смысловую проверку. Без FTR-007 потерю выявляют в передаче FTR-006/внутренних зависимостях; с FTR-007 дополнительно сверяют его contribution/dependencies. Само наличие документа или обоих consumers не означает PASS |
| ADR заполнен и выбор применим, но обязательный стык чтения или восстановление записи пропущены | Целостность не подтверждена; зависимая реализация ждёт correction/проверки документа, даже если проверка ADR дала PASS |
| ТЗ изменило требование сохранности после проверки архитектуры; отдельно consumer получил старую revision при корректном текущем документе | В обеих конфигурациях P1/P2 зависимый handoff не подтверждён: переоценить архитектуру, Brief/checks и порядок работ либо исправить передачу stale revision. Прежний PASS не переносится; незатронутые факты не переписываются |
| Нужен целостный документ, но существенное решение отсутствует или required область необоснованно помечена «неприменимо» | Зависимая часть BLOCKED; unknown и точный недостающий input видимы, новое решение не угадывается |
| Существенный выбор уже применимо принят; остальные решения обратимы, optional corpus patterns отсутствует | Подготовить/проверить документ без повторного Human Gate и без обязательного FTR-022; отсутствие ADR само по себе не дефект |
| Самостоятельная правка опечатки либо внешний применимый архитектурный документ до сборки 005+022 | Для опечатки нет обязательной полной архитектуры; внешний документ проверяется по содержанию/источникам без требования сначала построить producer-модуль |
| Save получил acknowledgement, но exact документ недоступен после прерывания | В обеих конфигурациях P1/P2 handoff не подтверждён; восстановление по §10.2 до зависимого использования/повторной записи, без фиктивного PASS |

Это документальные positive/negative cases для изменённого стыка, а не новые
обязательные SC-T для S0–K4 и не runtime Evidence. Реальное сохранение, перенос
inputs в планирование и resume проверяются на выбранной реализации отдельно.

<a id="autonomous-module-development"></a>

### 25.1. Готовность к автономной сборке модуля

Product owner [задаёт результат](01_Product.md#autonomous-module-outcome).
Используются существующие C-contracts и loop V3, без нового lifecycle или
параллельного каталога модулей. Название/состав берутся из выбранной группировки
Features; FTR-ID и ownership сохраняются.

Для самостоятельного запуска это собственная task модуля. Внутри версии по
[§25.0](#autonomous-project-development) требования ниже включаются в общую task;
создаваемые в её scope зависимости готовятся до использования, а не обязательно
до старта всей версии. Повторная выдача parent authority на каждую часть не нужна.

Перед запуском достаточный пакет содержит:

- Exact принятый scope всего модуля и contracts каждой входящей FTR; критерии
  фич и общий observable outcome, исключения и необходимые архитектурные решения.
- Producer/consumer каждого внутреннего и внешнего интерфейса, версии, порядок
  доступности данных, state owner, failure/recovery и поведение при отключении.
- Target/base, принятый core contract, реальные доступные dependencies/adapters,
  environment/data/provider boundaries и проверенный host с continuation trigger.
- Одну parent task C-005/C-006 с явным full-cycle scope: все входящие FTR,
  declared integration changes, tests/fixtures/state/evidence, bounded correction,
  limits/expiry и human-only boundaries. Stage envelopes выдаёт controller;
  новый внутренний шаг сам по себе не требует нового разрешения человека.
- Полную criterion → FTR/interface → check/oracle → Evidence связь и условия
  integrated completion. Агент фиксирует конкретные команды до их исполнения.

Missing material input блокирует запуск зависимой части и заявление о готовности
всего модуля к автономной сборке. Если реальный обязательный consumer ещё не
существует, заранее согласуют ограниченный результат с contract fixtures либо
откладывают полный запуск. Fixtures не доказывают реальную интеграцию отсутствующего
модуля; required integration не исключается агентом ради PASS.

Эта проверка запуска отличается от оценки качества описания по
[§25.7](#feature-documentation-review): ненастроенная среда или отсутствие
execution authority сами по себе не делают требования недостаточными. Если выбор
среды/consumer меняет обязательное поведение, интерфейс, данные или приёмку,
проверяющий указывает зависимое требование как содержательную неопределённость.

### 25.2. Один автономный цикл внутри модуля

Controller самостоятельно выбирает dependency-ready шаги. Декомпозиция на фичи
или workers — внутренняя организация одной цели; постоянные parent task identity,
ledger/resources, criteria и authority binding обеспечивают общий результат.
Если нужны child tasks по §7, их outcomes связаны с parent criteria, а полномочия
не выводятся из одного parent reference: внутренние worker actions получают
суженный envelope общей authority, самостоятельная task требует своего exact
binding по §7/§8. Закрытие child не закрывает parent. В общей версии техническая
проверка модуля закрывает только его критерии; общий цикл продолжается по §25.0.

После каждого effect отдельный checker возвращает observation; обычный дефект
ведёт в D0…D5 и отдельный CORRECT по V3. Между фичами нет обязательного ручного
acceptance. Pause/resume восстанавливает весь module state, проверенные и stale
критерии, actual effects и оставшиеся стыки; новый run не начинает модуль заново.
Непроверенный внешний trigger означает assisted mode, а не полную автономность.

Технический completion требует predicate §10.5 для parent: выполнены критерии
каждой входящей фичи, внутренние journeys и declared внешние интеграции, сохранён
SC-T14 базового ядра с affected negative cases, нет required UNKNOWN/NOT_RUN,
незавершённых effects или потерянного state. Проверки выдачи runtime human decisions
не требуют реального человека внутри технического build run: fixtures остаются
синтетическими; настоящее usability/acceptance наблюдение показывается отдельно.

### 25.3. Сценарии автономности каждого выбранного модуля

Это обязательные будущие проверки module development run. Они дополняют собственные
feature/integration cases и не добавляют поздние модули в обязательный S0–K4.

| ID | Сценарий | Требуемое доказательство |
|---|---|---|
| MOD-A01 | Достаточный согласованный вход → полный build модуля | После начального запуска нет новых человеческих решений, ручного выбора очередной фичи или обычной correction; один review package. История development run доказывает это отдельно от product test PASS |
| MOD-A02 | В составном модуле фичи по отдельности PASS, внутренний стык нарушен | Parent не завершён; агент диагностирует, исправляет в scope и повторяет affected проверки. Для однофичевого модуля аналогично проверяется его declared стык с ядром |
| MOD-A03 | Interruption после effect и между внутренними шагами, затем resource resume | Один continuation owner, общий ledger/criteria/authority, no replay и no reset; продолжение по real host trigger без ручного нового запуска |
| MOD-A04 | Missing material decision или обязательный consumer; отдельно достаточно покрытый обычный дефект | Первый случай не проходит readiness/completion; нет догадок или подмены required integration fixtures. Второй исправляется автономно без лишнего Human Gate |
| MOD-A05 | Модуль собран → его real integration меняет поведение ядра/другого declared consumer | Регрессия блокирует parent completion; после исправления проходят integrated journeys и affected core checks на exact candidate |

Для каждого случая до исполнения известны scope, fixture, независимый oracle,
Evidence destination и ограничения. Фактическая автономность требует трассы
внешней разработки, а не демонстрации только автономного поведения продукта.


<a id="feature-module-protocol"></a>

### 25.4. Алгоритм формирования и проверки фичи/модуля — R7

Агент выполняет этот алгоритм при новой фиче, объединении выбранных FTR,
изменении public contract/эффектов/данных и подготовке удаления. Результат —
достаточные owner sections и один производный implementation brief; новый
каталог или отдельный lifecycle package не создаётся. Достаточность проверяется
по содержанию, не по наличию заголовков. N/A требует причины и не исключает
реально применимый safety/integration criterion.

| Шаг | Действие агента | Проверяемый выход |
|---|---|---|
| 1. Предмет и существующее поведение | Определить new/change/group/remove; прочитать relevant Product/Features, найти дубли и фактических владельцев | Exact предмет, outcome, FTR/disposition и границы. Не объединять/принимать новые фичи за человека |
| 2. Поведение | Заполнить C-002: user/trigger/preconditions/I/O/main flow/states/transitions/failures/recovery/constraints/acceptance/negative cases | Каждое существенное требование имеет source и наблюдаемый результат; неизвестность не заменена выдуманным решением |
| 3. Композиция | Для модуля связать FTR, данные и порядок доступности; для одной фичи проверить её реальные стыки | Producer → contract/version → consumer, data owner и общий outcome. Нет цикла, требующего ещё не созданного результата |
| 4. Подключение | Сформировать C-015 и применимые C-016 exchanges; direct/queued mode, provided/required capabilities, versions/effects/profile | Для каждого входа есть производитель, для выхода — реальный consumer либо explicit external boundary. Нет скрытого чтения чужого storage |
| 5. Жизненный цикл | Описать операции §25.5, данные/сообщения/consumers, migration, interruption и reversibility | Добавление/отключение/удаление проверяемы, unrelated и пользовательские данные сохраняются |
| 6. Semantic readiness | Проследить requirement → FTR/interface → transition → check/oracle → Evidence; отдельно ошибки, disable и shared state. Для содержательной read-only проверки применить [§25.7](#feature-documentation-review) | Findings с exact owner/locator, последствием и предложением correction; существенный пробел содержания ограничивает документальную достаточность, предпосылка запуска — affected implementation; выводы разделены |
| 7. Вход автономной разработки | После согласования inputs связать один C-005/C-006 parent: goal, FTR/contract refs, dependency order, target, paths/effects, checks, limits и host resume | Enough input для одного module build; permission отдельна от заполнения шаблона. HOW/обычная correction не создают новые Human Gates |
| 8. Build и завершение | Действовать по §25.2/V3; после каждого relevant изменения перепроверять affected contracts, consumers и Evidence | Фичи, модуль и declared real integrations доказаны на exact candidate; parent закрывается по §10.5, затем единый review |

Минимальная структура описания: назначение/пользователь/результат; входы/выходы;
состояния/отказы/recovery; зависимости и ownership; эффекты/authority/data;
подключение/версии/lifecycle; acceptance/negative/oracle; материальные unknowns.
Для модуля дополнительно обязательны состав FTR, внутренние связи, совместное
владение только с явно указанным единственным owner и общий outcome. Остальные
facts остаются у своих owners: Product WHAT, Features behavior, Architecture
interfaces, Development algorithm; brief ссылается, не дублирует владельцев.

Структура будущей реализации задаётся ролями: публичный interface, внутренняя
логика, connector/adapter boundary, проверки и документация; storage/migrations —
если есть собственные persistent данные. Агент выбирает folders/classes под
принятый stack, объясняет placement этих ролей; одинаковое дерево каталогов,
plugin framework и storage для каждой фичи не требуются. Отсутствие роли допустимо
только с объяснением неприменимости, а не для сокрытия dependencies/effects.

Author может исправлять обнаруженные дефекты в разрешённом documentation scope
и повторять affected checks. Новый material product/architecture выбор возвращает
точный decision request; independent validator фиксирует finding и не исправляет
subject. Перед runtime запуском агент сверяет current bytes/revisions и повторяет
readiness при drift. Structural PASS не подменяет semantic PASS, actual integration
или authority. Для новой составной фичи каждый FTR и модуль проверяются отдельно.

<a id="module-connection-lifecycle"></a>

### 25.5. Подключение, обновление, отключение и удаление

| Операция | Порядок и условия | Проверка результата/восстановление |
|---|---|---|
| ADD / ENABLE | Проверить accepted C-015, реальных consumers/versions, target и authority; подготовить только разрешённые отсутствующие данные/config; зарегистрировать instance/generation, handlers/queue bindings без обработки новых сообщений; проверить совместимость и затем включить | До enable нет business dispatch; после него проходят declared direct/queued journeys и core regression. Conflict/partial registration даёт inactive/recoverable outcome, не silent overwrite |
| UPDATE | Определить affected interfaces, данные, saved messages, consumers; прекратить новую доставку затронутому binding и reconcile in-flight; выполнить только отдельно покрытую migration; опубликовать новую generation/contract и проверить перед enable | Старые сообщения не перенаправляются молча. Поддержанный old reader либо явный отказ; исходные bytes/history сохранены, partial migration требует recovery. Rollback допустим только по объявленному проверяемому пути |
| DISABLE | Прекратить новые direct business calls/enqueue; ожидающие сообщения явно приостановить; admitted действия остановить только при поддержке и подтверждённом результате, иначе дождаться/reconcile | Состояние draining не выдаётся за полностью disabled до reconciliation; новый effect старой generation не допускается. Read-only inspection данных ядром остаётся доступным, пользовательские artifacts/Evidence сохранены |
| REMOVE IMPLEMENTATION | Сначала определить required consumers/замену и все pending/in-flight operations; disable/reconcile; ожидающие сообщения остаются удержанными с причиной либо явно отменены в scope; снять registration/subscriptions/config bindings и удалить только owned implementation paths | Required consumer без проверенной замены блокирует remove. Нет ссылок на удалённый handler как доступный; незавершённый effect не теряется, re-install не воспроизводит старую очередь автоматически. Данные/история сохраняются |
| DELETE DATA | Отдельно определить datasets, owners, retention/legal/user constraints, backup/recovery и exact delete authority; проверить consumers и незавершённые операции | Не выводить delete из disable/remove, истечения message TTL или выбранного retention срока. Непокрытое/unknown блокируется; исход и ограничения необратимости видны |

Это протокол изменений выбранного implementation target, а не обязательная
реализация полного installer FTR-004 в S0–K4. Если FTR-004 выбран, C-013 связывает
его операции с C-015 ownership/lifecycle. Прямое подключение локальной композицией
входит в тот же протокол. FTR-007 backlog может отсутствовать; queued exchanges
доставляет transport ядра. Lifecycle операций не создаёт новых controller edges
и не предоставляет Git permissions. Внутри заранее принятой module task агент
выполняет покрытые operations автономно; новое protected действие требует
собственной authority, не выдуманного разрешения от module manifest.

<a id="installed-update-development"></a>

#### Обновление установленной копии AOS: последовательность реализации

Для принятого [среза FTR-004](06_Features.md#ftr-004-versioned-update) реализация
в AOS-3 выполняется отдельно от текущего documentation edit. Этот раздел не
разрешает runtime, Git writes, публикацию релиза или сетевое получение пакета.

1. Сверить существующий installer, его ownership, entry/runtime lock, журнал и
   recovery. Зафиксировать профиль ОС/runtime, формат пакета и конкретную пару
   поддержанных версий; неизвестный переход не угадывать.
2. Реализовать локальный путь на двух изолированных пакетах: установка старой
   версии в disposable project → preview обновления → разрешённая подготовка
   рядом → проверка → переключение → post-check. Настройки, задачи, Evidence и
   посторонние файлы входят в preservation oracle. Тестовая новая версия должна
   менять и базовый файл запуска, чтобы не обойти прежнее ограничение entry migration.
3. Проверить сбои до, во время и после переключения; потерю ответа, повтор той же
   операции, конкурентный запуск/update, активную либо unresolved задачу, конфликт
   пользовательского файла и несовместимость данных. Проверить возврат к старому
   коду при совместимых данных; отдельно отказ небезопасного rollback после миграции.
4. Только после локального результата добавить получение пакетов из выбранного
   канала релизов: проверку наличия, получение конкретного artifact, проверку
   происхождения/целостности и передачу в тот же preview/apply. Получение не должно
   обходить уже проверенные локальные условия допуска. Недоступность канала,
   повреждение или подмена пакета оставляют текущую установку работоспособной.
5. Провести независимую проверку изменённых стыков и regression, затем представить
   результат пользователю. Различать локальный update, реальную доставку пакета,
   миграцию данных, Human acceptance и Git/Release delivery: NOT_RUN не становится PASS.

Методы проверки и точные bindings принадлежат implementation task. Проверка
сохранности включает наблюдение разрешённых/запрещённых effects, а не только
равенство файлов до и после. Тестовый сбой или fixture authority не выдаются за
реальный пользовательский update. При уже принятом scope обычные исправления
и повтор затронутых проверок не требуют нового согласования продуктовой схемы.

### 25.6. Проверки протокола агента и первого примера

| ID | Сценарий | Требуемый результат |
|---|---|---|
| MOD-A06 | Агент формирует новую фичу или меняет contract существующей; отдельно duplicate outcome, пропущенный consumer, обязательное поле без смысла, N/A при фактическом storage/effect, drift после предыдущего PASS | §25.4 находит конкретный semantic gap до dependent implementation; исправление в scope и повтор affected checks, material решение не угадывается. Полный валидный input доходит до одного автономного parent run |
| MOD-A07 | Один build 005+022: direct pattern lookup, queued analysis/save, real core integration, затем controlled disable/update/remove с pending/in-flight и required consumer | Нет ручных запусков каждой FTR; no-ADR и отсутствие библиотеки сохраняются, lookup не создаёт recursive ADR. Нарушение стыка при отдельных feature PASS не закрывает parent. Artifacts/provenance/pending decisions сохранены, re-enable не делает blind replay, human-gate fixtures не становятся реальными decisions |

MOD-A06/07 дополняют MOD-A01…05 и применимые MOD-S16…18/SC-T23…26. Положительный
и каждый отрицательный вариант имеют отдельный check binding, declared target,
независимый oracle и Evidence. Readiness самого документа и фактический автономный
module run остаются разными результатами. Остальные модули проходят тот же
протокол по мере выбора; полный backlog сейчас не объявляется подготовленным.

<a id="feature-documentation-review"></a>

### 25.7. Протокол содержательной проверки документации фич и модулей — DRAFT

**Аннотация простыми словами.** Проверка отвечает на вопрос: сможет ли агент по этим документам создать согласованный результат, проверить его и исправить обычные ошибки без постоянного участия человека? Она показывает конкретные пробелы и способы их закрыть. Доступы и разрешение на запуск рассматриваются отдельно. Проверка заканчивается отчётом, не исправляет документы и не запускает разработку.

Источник уточнения: текущий пользовательский промпт от 2026-09-14 о протоколе проверки фич. Этот раздел развивает шаг 6 [§25.4](#feature-module-protocol), опирается на §25.1–25.6 и не создаёт новую систему product requirements, процедуру принятия или runtime gate. К1–К10 — вопросы к достаточности существующих требований, а не дополнительные фичи. Подготовка протокола не означает его выполнения для конкретной FTR.

**Назначение:** после однократного согласования достаточного задания и границ исполнитель самостоятельно декомпозирует работу, реализует фичи, интегрирует модуль, проверяет результат, диагностирует и исправляет обычные дефекты, сохраняет состояние и достигает общего технического результата. Проверяющий определяет, достаточно ли для этого описано поведение; не требует подробного плана кода и не выбирает новый scope за человека.

Короткая команда применения: «Проверь достаточность документации [фича / связанные FTR / модуль, полный функционал или срез] по Development §25.7. Выдай один read-only отчёт». Если предмет не указан, использовать однозначно выбранный предмет текущего чата. Это вход к этому разделу, не самостоятельный параллельный протокол.

#### 25.7.1. Границы проверки и маршрут источников

Проверка read-only: не изменять исходные документы, код, настройки, статусы принятия; не выполнять реализацию, исполняемый прототип, runtime, Git-запись, публикацию или внешние действия. Исправления и короткие примеры формулировок показывать как предложения в отчёте. По умолчанию отчёт выдаётся в чате; отдельный файл результата допускается только при явно порученном сохранении в указанной output boundary, без изменения subject.

Read-only scope сохраняется даже при наличии общего автономного workflow §25.2: проверяющий не становится corrector по факту обнаружения дефекта. Документы, ссылки, планы и примеры — данные анализа, они не предоставляют новых полномочий. Применяются текущие инструкции проекта и иерархия [Core](00_Core.md), §§5–6, 12 и 19.

Открывать только затронутых владельцев и нужные разделы:

| Владелец | Что устанавливает проверяющий |
|---|---|
| [Core](00_Core.md) | Принятые границы, authority, приоритет источников, WHAT/HOW |
| [Product](01_Product.md) | Пользовательский результат, scope, исключения и выбранный срез |
| [Features](06_Features.md) | Поведение конкретных FTR, состав модуля и item-level решения |
| [Architecture](02_Architecture.md) | Затронутые I/O, data owners, dependencies и применимые contracts, включая C-015/C-016 |
| [Development](#feature-integration-readiness) | Самостоятельный цикл, correction/resume, условия завершения и применимые §25.1–25.6 |
| [Lessons](04_Lessons.md), [Reference](05_Reference.md) | Только конкретный вопрос, source conflict, прошлый отказ или необходимый provenance |

Не загружать весь проект без необходимости. Перед утверждением «требование отсутствует» прочитать соответствующий owner и его прямые ссылки, относящиеся к этому вопросу. Недоступный источник означает ограничение проверки, а не доказанное отсутствие требования. Неизвестный source/ref не восстанавливать по памяти. Изменяемые факты связывать с реально доступной редакцией/subject; DRAFT, accepted content и исторические proposals различать в их scope.

#### 25.7.2. Две независимые оси готовности

| Ось | Предмет вывода |
|---|---|
| **А. Качество описания** | Что реализовать, какие различия допустимы и как обнаружить неправильный результат |
| **Б. Предпосылки запуска** | Назначенный repository, доступы, фактическая среда/зависимости, бюджет, authority и механизм продолжения |

Отсутствие разрешения на запуск или настроенной среды само по себе не дефект документации. Если отсутствующий выбор меняет обязательное поведение, публичный интерфейс, требования к данным или способ приёмки, назвать конкретное зависимое требование и показать содержательную неопределённость. Например, пока не выдано право записи в уже описанный destination — предпосылка запуска; не решено, разрешена ли передача чувствительных данных внешнему сервису, а от этого зависит результат — вопрос содержания.

DRAFT сам по себе не снижает качество; accepted сам по себе не доказывает достаточность. Документальная готовность не является доказательством работоспособности реализации, автономности среды, пользовательского принятия продукта или разрешения на реализацию/Git. Предписанные ограничения среды и resume оцениваются как описание в К8; их фактическое наличие — отдельно по оси Б.

#### 25.7.3. Зафиксировать предмет глазами исполнителя

До оценки указать:

- Фичу, связанные FTR или модуль и его точный состав; полный функционал или выбранный срез.
- Общий ожидаемый результат, включённые взаимодействия и исключения.
- Использованные решения чата/owners, доступные версии и точные документы/разделы; прочитанную область и ограничения.

Не запрашивать действующие решения повторно, не выбирать новые фичи/состав/расширение scope. Если предмет нельзя однозначно установить, задать один необходимый вопрос; до ответа продолжать лишь независимую часть проверки. Неуказанный предмет не означает автоматического аудита всего AOS.

Кратко восстановить задание:

> Получаю …; должен создать …; взаимодействую с …; результат считается правильным, когда …; самостоятельно выбираю …; обращаюсь к человеку только при … .

Каждую существенную часть связать с источником. Если формулировку нельзя собрать без догадки, записать конкретный пробел, не дописывать за пользователя желаемое поведение. Для модуля проверить и отдельные FTR, и совместный результат; выборка не выдаётся за полный аудит.

#### 25.7.4. Критерии содержания К1–К10

Все критерии проверяются по смыслу, с применимостью к выбранному предмету. Неприменимость требует короткой причины; существенную фактическую зависимость нельзя скрыть под N/A.

**К1. Назначение и границы**

- Определены пользователь, проблема, trigger и наблюдаемый результат; понятно, что входит и не входит в реализацию.
- Полная фича, выбранный срез и будущие возможности различимы и не подменяют друг друга.
- Общая техническая сборка модуля имеет собственный результат и не закрывается по одному перечню завершённых задач.

**К2. Входы и достаточность постановки**

- Необходимые входы имеют источники и условия доступности; обязательные, условные и необязательные данные различимы.
- Для применимых пустых, неполных, ошибочных, противоречивых и устаревших входов описан исход.
- Понятно, когда продолжать, когда вернуть ограниченный результат и когда уточнять; достаточные прежние ответы не запрашиваются снова.
- Неизвестные данные не превращаются в выдуманные факты.

**К3. Наблюдаемое поведение**

- Основной путь прослеживается от входа до результата, существенные развилки имеют определённые исходы.
- Понятен выход для пользователя/потребителя; описаны значимые состояния и переходы.
- Различимы отсутствие результата, частичный результат и завершение.
- Представление может выбирать агент, если это не меняет обязательное поведение.

**К4. Данные, зависимости и интерфейсы**

- Для каждого используемого входа есть источник, для выхода — потребитель или явная внешняя граница; смысл данных, существенные ограничения и ошибки обмена определены.
- Изменяемое состояние имеет владельца; нет скрытого чтения чужого storage или неявной обязательной зависимости.
- Применимые требования совместимости описаны; порядок доступности данных не требует ещё не созданного результата по циклу.
- Не требовать заранее serialization, классы, файлы или storage, если выбор не меняет согласованное поведение и совместимость.

**К5. Ошибки и восстановление**

- Существенный отказ имеет наблюдаемый исход и объяснение того, какие изменения могли произойти до него.
- Определены допустимые повтор, продолжение, отмена или восстановление; для effects разобраны применимые interruption, duplicate command и unknown outcome.
- Нет молчаливой потери данных, повторного эффекта или ложного завершения; recovery не подразумевает неописанные полномочия или расширение scope.
- Не требовать очередь, миграции, rollback или отдельное хранилище без фактической необходимости; неприменимость обосновать.

**К6. Критерии приёмки и примеры**

- Каждое существенное требование связано со способом проверки, способным обнаружить неправильную реализацию; примеры дают достаточно конкретные входы и ожидаемые свойства результата.
- Есть необходимые положительные, отрицательные и пограничные случаи. Отрицательный пример по возможности изолирует один дефект при корректных остальных входах.
- Реализация, которая всегда отказывает или возвращает пустой результат, не проходит положительный сценарий.
- Наличие поля, текста, схемы или ссылки не подменяет проверку их содержания. Исполняемые тесты не требуются для проведения этого документального аудита; достаточный проверяемый смысл будущего теста требуется.

**К7. Качество смысловых и AI-функций**

Применять, если фича анализирует запрос, пишет спецификацию, сравнивает варианты, рекомендует решение или объясняет результат; иначе обосновать неприменимость.

- Для конкретного входа известны обязательные и недопустимые выводы, сведения-основания и ограничения, которые нельзя пропустить.
- Определено, когда несколько разных ответов правильны, как сохраняется смысл исходных требований и когда нужно признать недостаток данных.
- Есть способ обнаружить убедительный, но неверный ответ: сверка с источниками, обязательными смысловыми свойствами и запрещёнными выводами, а не только с самооценкой агента.
- Слова «качественно», «обоснованно», «полно», «понятно», «варианты сопоставимы» без применимого основания проверки недостаточны. Единственная эталонная формулировка свободного текста не требуется; проверяются смысловые обязательства и допустимые различия.

**К8. Самостоятельность исполнителя**

- Понятно, какие технические решения агент принимает сам; обычная декомпозиция, реализация, диагностика и correction не требуют новых пользовательских решений.
- Существенный product choice отделён от обратимого HOW. Отсутствие подробного плана кода не дефект, если агент может составить его из достаточных требований.
- Есть условие технического завершения и достаточное описание сохранения/продолжения либо точная ссылка на общий workflow.
- Нет обязанности бесконечно улучшать результат при выполненных исходных критериях; вопросы человеку связаны с существенными границами, а не обычным выбором реализации.

**К9. Модуль и интеграция**

- Для модуля определены состав, внутренние связи и общий сценарий; проверяются каждая FTR и совместный результат. Однофичевый модуль также имеет реальные стыки с ядром/потребителями.
- Отдельное прохождение проверок фич не закрывает модуль. Есть способ обнаружить неправильный стык при корректных отдельных компонентах и проверить необходимые взаимодействия с ядром/другими потребителями.
- Учтены применимые отключение, обновление и сохранность данных; тестовые подмены отсутствующих компонентов не доказывают реальную интеграцию.
- Поведение человеческих gates внутри создаваемого продукта допускает синтетические проверки; они не имитируют настоящие полномочия разработки или пользовательское принятие. Для одиночной немодульной фичи совместный состав N/A с причиной, фактические интерфейсы всё равно проверяются по К4/К6.

**К10. Согласованность и доступность требований**

- Нет существенных противоречий между owners; уточнения среза и общие семейные требования можно совместить однозначно.
- Старые примеры и draft proposals не выглядят как текущие принятые решения.
- Исполнитель собирает применимый набор требований по точным ссылкам без устного объяснения автора существенного поведения.
- Не требовать новые документы ради структуры; исправления предлагать у существующих владельцев.

#### 25.7.5. Репетиция исполнения без кода

Мысленно пройти следующие применимые сценарии. Это проверка описанного процесса, не выполненный runtime-тест; для неприменимого случая записать причину.

| № | Сценарий репетиции |
|---|---|
| 1 | Достаточный вход → нормальный результат |
| 2 | Неполный вход → продолжение, ограниченный результат или уточнение |
| 3 | Противоречивый вход → явный исход |
| 4 | Недоступная зависимость → ограниченный результат или остановка |
| 5 | Обычный дефект → диагностика → исправление в разрешённом scope → повторная проверка |
| 6 | Прерывание или повтор операции → восстановление без неподтверждённого replay |
| 7 | Отдельные фичи корректны, стык нарушен → обнаружение; для однофичевого модуля — нарушенный стык с ядром |
| 8 | Завершение → доказательства общего технического результата |

Для каждой строки отчёт содержит следующий шаг исполнителя, документальное основание/locator, оставшуюся существенную догадку или её отсутствие, необходимость вопроса человеку и конкретную причину. Шаг correction описывается мысленно: проверяющий ничего не исправляет. Общая ссылка на workflow достаточна только если она действительно определяет нужный переход, scope и условие результата.

#### 25.7.6. Попытки опровергнуть достаточность

**А. «Две реализации».** Предложить две существенно разные по наблюдаемому поведению реализации, которые могут формально удовлетворить тексту. Если обе допустимы в согласованном scope, это свобода исполнителя, не дефект. Если одна нарушает предполагаемый смысл, а текст её не исключает, показать недостающее правило и последствия. Сам «предполагаемый смысл» не повышать до принятого требования: указать его источник либо необходимое пользовательское решение.

**Б. «Плохая реализация проходит».** Мысленно попробовать пройти критерии шаблонным ответом, пропущенным ограничением, фиктивной интеграцией или формально заполненными полями. Если действующее требование уже исключает вариант, указать найденную защиту/locator, не создавать ложное замечание. Если не исключает, предложить конкретное усиление критерия или примера. Не заменять смысловую проверку подсчётом полей/тестов.

В отчёте сохранить по обеим попыткам конкретный контрпример, найденную защиту либо подтверждённый пробел, источник и вывод. Проверить существенные для выбранного предмета риски; не требовать доказать отсутствие любой мыслимой ошибки.

#### 25.7.7. Классификация замечаний

Каждому замечанию назначить действие и отдельно значимость. Если в одном описании смешаны дефект требований и отсутствие доступа для его проверки, разделить выводы; не размножать один корневой пробел по К1–К10.

| Класс действия | Что требуется | Роль человека |
|---|---|---|
| **А. Восстановить существующий ответ** | Решение уже есть: дать точную ссылку, согласовать текст или устранить дублирование | Не спрашивать принятое решение повторно |
| **Б. Дополнить описание** | Поведение следует из принятых требований, но недостаточно явно/проверяемо выражено | Новое продуктовое решение не нужно; отдельная правка остаётся в своём authorized scope |
| **В. Получить пользовательское решение** | Допустимы варианты с разными последствиями для результата, scope, данных, совместимости или существенной границы | Показать конкретный выбор, варианты, рекомендацию и последствия |
| **Г. Уточнить предпосылку запуска** | Вопрос среды, доступов, бюджета, authority или фактического продолжения, сам по себе не снижающий качество описания | Запросить только действительно необходимое действие человека для запуска; не выдавать за дефект содержания |
| **Д. Оставить агенту** | Допустимый технический HOW внутри согласованных гарантий | Не представлять как blocker и не передавать пользователю |

Значимость различать отдельно:

- **Существенный пробел:** препятствует достаточности обязательного поведения/проверки в объявленном scope; указать зависимое требование и риск неправильного результата.
- **Необязательное улучшение:** полезно, но не препятствует достаточности; не включать в условия готовности.
- **Неустановленная область:** источник недоступен или проверка неполна; требование не объявляется отсутствующим. Назвать locator/границу недоступности и затронутую часть вывода.

Классы Г/Д не должны искусственно создавать BLOCKED по качеству документации. Если обнаружена зависимость обязательного поведения от выбора среды/данных, содержательный вопрос относится к А/Б/В с точным объяснением, а сама настройка остаётся Г. Обычные HOW не требуют отдельного finding; их можно кратко перечислить как допустимую свободу исполнителя.

Перед вопросом человеку найти ответ у владельца и в применимых решениях чата;
достаточный действующий ответ закрывает вопрос по классу А. Если нужен класс В
или конкретное действие человека по Г, одним пакетом сообщить: (1) чего именно
не хватает и где искали; (2) какой результат/шаг зависит от ответа;
(3) варианты и последствия; (4) рекомендацию с причиной;
(5) что можно продолжить независимо. Не приостанавливать независимую разрешённую
работу. Класс Б разрешает дополнение из принятого содержания только в отдельно
покрытом edit scope, а не mutation внутри read-only проверки.

<a id="semantic-review-controls"></a>

**Контроль самого проверяющего — DRAFT, детализация MOD-A06.** Эти восемь входов
проверяют применение К1–К10 и классов А–Д, не создают второй протокол. Все
обязательства и основания открыты исполнителю; новый контрольный вход может
варьироваться, скрытое требование — нет. Здесь заданы ожидаемые выводы, а не
заявлено выполнение тестов. Результат репетиции в отчёте: case → ожидаемый вывод
→ фактический вывод с locator → расхождение/ограничение.

| Контрольный вход | Ожидаемый вывод и основание |
|---|---|
| MOD-A06.a — достаточное описание: [FTR-005.S1 и N01](06_Features.md#ftr-005-semantic-examples), результат учитывает все заданные constraints, UNKNOWN и отсутствие human choice; опечатка получает краткий no-ADR | PASS по проверенной области К6/К7/К8, необязательный подробный design не нужен. Завершить эту проверку; не придумывать ещё обязательные замечания (§25.7.10) |
| MOD-A06.b — в задании сохранения ADR указаны readers старого и нового формата, но не выбрано, какие версии должны читать новый artifact; все доступные owner/решения проверены, ответа нет | Класс В, существенный пробел К4/К6: «совместимый результат» нельзя проверить. Варианты — поддержать оба reader либо только новый с явной потерей доступа старого. В этом примере рекомендовать оба для сохранения доступа, ценой дополнительных проверок совместимости; это предложение, не принятое обязательство. До выбора BLOCKED только зависимое поведение; прочий analysis возможен. Основание: FTR-005, MOD-DEC-02 и §25.7.2 |
| MOD-A06.c — две внутренние реализации хранения, файл либо БД, сохраняют одни и те же согласованные ownership, concurrent-update, recovery и публичные guarantees; в задании нет ограничения на этот HOW | Класс Д, не blocker К4/К8; выбор агенту. Проверить заявленные guarantees при будущей реализации, не потребовать от человека storage engine. Основание: Core §12, Architecture C-012, §25.7.6А |
| MOD-A06.d — описание из .a достаточно, но не назначены repository/host и нет допуска runtime | Класс Г по оси Б, runtime BLOCKED/NOT_RUN; качество прочитанного описания по оси А сохраняет PASS. Основание: §25.7.2, §25.1; не требовать переписывать требования ради доступа |
| MOD-A06.e — [FTR-022.N01](06_Features.md#ftr-022-semantic-examples): все поля заполнены, P@1 объявлен готовым для двух writers без сериализации | Ответ отклонён по К6/К7: явное single-writer ограничение нарушено. Описание достаточно, найденная защита закрывает попытку «плохая реализация проходит»; это дефект ответа, не недостающий выбор. Если checker пропустил его, finding относится отдельно к checker (§10.3) |
| MOD-A06.f — corpus недоступен, задача FTR-005 имеет все обязательные входы для самостоятельного сравнения | Класс А: восстановить ответ §4.3 Features / MOD-S16. Lookup получает limited result с причиной, analysis продолжается без corpus. Нет install или false blocker всего модуля; К2/К4/К9 защищены существующим правилом |
| MOD-A06.g — [MOD-S18: потеря подтверждения save_draft](02_Architecture.md#architecture-patterns-save-recovery), фактический эффект пока неизвестен | К5/К8 достаточно описаны: единственный продолжатель сверяет факты до повтора, dependent effect ждёт Evidence. Нет автоматического replay и выдуманного C-008; найденный эффект не означает Human ACCEPT. Основание: C-012/C-016 и §10.2 |
| MOD-A06.h — отдельные FTR возвращают правильные результаты, но ответ lookup в текущем analysis запускает новый architecture.analyze | Стык не проходит К9 / MOD-S16 / MOD-A07; parent не завершён, требования уже запрещают recursion. Finding относится к интеграции, correction — в покрытом scope, затем affected module checks по §25.2. Не открывать новый product design cycle |

Если контроль выявил ошибку проверяющего, не исправлять одновременно проверяемый
subject ради PASS и не снижать исходные критерии. Зафиксировать отдельно
контрольный вход, ошибочный/ожидаемый вывод и основание; изменение checker требует
своего scope, затем повтор его controls и зависимых проверок. Авторский self-check
документационной правки может исправлять только внесённые ею дефекты; он не
называется независимой validation. Если контроль использован для настройки,
он остаётся regression example, а не независимым доказательством качества.

#### 25.7.8. Карточка существенного замечания

Писать простыми словами; технические термины использовать только для точного locator или объяснения последствия. Локальные IDs замечаний относятся к одному отчёту и не создают новый реестр.

| Поле | Обязательное содержание |
|---|---|
| ID и название | Короткое имя проблемы, класс А–Д, значимость и затронутые К |
| Где | Точный документ/раздел/строка либо иной доступный locator |
| Основание | Короткая цитата либо точное описание пробела; какие owners и прямые ссылки проверены, границы поиска |
| Чего не хватает | Конкретное отсутствующее правило/данные/способ проверки без канцелярита |
| Почему мешает | Ошибка исполнителя, лишний вопрос или два неоднозначных наблюдаемых результата |
| Пример | Короткий вход и возможные исходы, если это помогает понять проблему |
| Варианты исправления | Минимальный достаточный; альтернативный — когда он действительно полезен |
| Рекомендация | Выбранный вариант и причина |
| Нужно ли решение пользователя | Да/нет; если да — точный предмет выбора, без повторения принятых решений |
| Готово, когда | Наблюдаемое условие закрытия finding |

Не ограничиваться «уточнить контракт», «добавить тесты», «описать edge cases»: указать требуемое содержание и, где полезно, короткую формулировку исправления. Новое предложенное поведение явно отмечать как предложение, не принятое решение.

#### 25.7.9. Формат итогового отчёта

Сначала коротко и простым языком ответить: насколько документы позволяют работать самостоятельно; что уже достаточно описано; какие главные пробелы остались; какие вопросы действительно вернут управление человеку. Не использовать проценты готовности или средний балл, скрывающий существенный пробел.

Далее дать семь частей:

1. **Предмет и покрытие.** Точные FTR/модуль/срез, общий результат и взаимодействия, использованные версии/owners/locators, исключения, прочитанная и недоступная область. Восстановленная постановка глазами исполнителя из §25.7.3. Выборку не называть полным аудитом.
2. **Таблица К1–К10.** Для каждого критерия — статус, проверенное основание/locator, ограничения и связанные finding IDs. Для нескольких FTR/модуля должно быть видно, к какой части относится вывод; PASS одной фичи не переносится на другие или на общий стык.
3. **Существенные замечания по влиянию.** Карточки §25.7.8 без повторения одного корневого пробела. Приложить компактные результаты восьми репетиций и обеих попыток опровержения: они показывают основания findings и найденные защиты. Необязательные улучшения и недоступные области обозначить отдельно.
4. **Один пакет пользовательских решений.** Только необходимые нерешённые вопросы класса В: что выбрать, варианты, рекомендация и последствия. Не включать уже принятые решения или обычный HOW. Если таких вопросов нет, прямо написать, что новые продуктовые решения не требуются; вопросы фактического запуска остаются в части 6.
5. **Ограниченный пакет предлагаемых исправлений.** Цель, точные owner-разделы, конкретное содержание изменений/короткие примеры, что не менять и условия проверки. Это предложение отдельной правки, не разрешение выполнить её в текущем read-only проходе.
6. **Предпосылки запуска.** Отдельно перечислить существенные repository/environment/access/budget/authority/continuation inputs, их известность, ответственного и влияние на запуск. Не снижать за них качество описания; при влиянии выбора на поведение сослаться на соответствующий содержательный finding.
7. **Итог достаточности.** Одна из формулировок ниже с точным scope и существенными ограничениями. Подтверждённые дефекты и непроверенные области могут присутствовать одновременно — показать оба факта.

Статусы таблицы относятся **только к документальной проверке**; это не запись C-009 runtime verdict или изменение статусов принятия:

| Статус | Когда использовать |
|---|---|
| **PASS** | Применимое содержание прочитано, проверено по смыслу и достаточно в заявленной области |
| **BLOCKED** | Подтверждён существенный пробел содержания; нужен конкретный finding и его влияние |
| **NOT_RUN** | Проверить применимое содержание не удалось; указать недоступный источник/ограничение и не делать вывод об отсутствии требования |
| **Неприменимо** | Критерий или отдельный сценарий не относится к предмету; дать короткую фактическую причину |

Если внутри критерия есть подтверждённый дефект и непроверенная существенная часть, указать BLOCKED с finding и отдельно NOT_RUN-область, не скрывать одно другим. Частичная неприменимость не исключает проверку оставшихся пунктов критерия. Незначительное замечание не превращает достаточный критерий в BLOCKED.

Допустимые итоговые формулировки:

- **«Документация достаточна для автономной реализации в указанном scope».** Обязательное содержание проверено и достаточно, существенные смысловые догадки не нужны. Фактические предпосылки запуска могут быть ещё не выполнены и перечислены отдельно.
- **«Нужна доработка документации».** Есть хотя бы один подтверждённый существенный пробел содержания; назвать необходимые исправления/решения. Непроверенные области, если есть, добавить явно.
- **«Достаточность не установлена из-за неполной проверки».** Подтверждённых существенных дефектов может не быть, но непроверенная обязательная область не позволяет подтвердить достаточность. Не выдавать её за обнаруженный дефект.

#### 25.7.10. Условие завершения проверки

Достаточность подтверждается, когда существенное обязательное поведение определено, оставшиеся различия — допустимая свобода исполнителя, критерии обнаруживают неправильный результат, реальные стыки и общий результат проверяемы, необходимые пользовательские решения известны и обычная реализация/correction не требуют ручного управления. Если незакрытый пользовательский выбор определяет разные обязательные результаты, одного списка вариантов недостаточно для положительного итога; указать зависимое требование.

Не требуется устранять любую мыслимую неопределённость или заранее писать Engineering Design. Открытые обратимые HOW и необязательные улучшения не препятствуют завершению проверки. Существующее достаточное правило, найденное у owner, закрывает предполагаемое замечание ссылкой, а не новым дублирующим требованием.

Выполнить один законченный содержательный проход и выдать отчёт; не переходить автоматически к correction, новому проектированию или реализации. Завершённый отчёт может содержать BLOCKED/NOT_RUN и не обязан объявлять документы достаточными. Проверку без отдельного основания не называть независимой от автора.

Если позже поручена правка, исправлять согласованные findings у их owners и повторять затронутые checks. Новое существенное обнаружение сообщать явно; стилистические предпочтения и необязательные улучшения не запускают бесконечную переработку. Действуют прежние boundaries author/validator, полномочия текущей задачи и общий workflow; этот протокол не выдаёт authority и не требует согласования каждой обычной технической коррекции будущего исполнителя.

Один и тот же сбой без новых сведений не начинает проверку заново: применяются
§10.3–10.4 с сохранёнными signature/ledger и ресурсными пределами. Необязательная
идея остаётся предложением вне completion criteria и не возобновляет завершённую
проверку или terminal task; общий владелец completion остаётся прежним (§10.5).


<a id="ux-pages-verification"></a>

### 25.8. FTR-032: подготовка и проверка dual-surface пути — DRAFT

Это применение §25.1–25.7 и existing controller к
[модели FTR-032](06_Features.md#ftr-032-contract), не новый lifecycle/gate.
[Product](01_Product.md#ux-pages-product) владеет результатом,
[Architecture](02_Architecture.md#ux-pages-contract) — subject/стыками,
[brief](../workspace/AOS_UX_PAGES_MODULE_IMPLEMENTATION_BRIEF.md) даёт короткий вход.
Проверка документации не запускает browser/runtime и не пишет product decisions.

**Перед отдельной реализацией** связать scope, обязательные criteria/checks, exact
schema/profile и разрешённые effects с C-005/C-006. Новый исполнитель получает
owners по brief; старые D02/D03 не подставляются как неявное ТЗ. До генерации
страницы определить expected requirements из выбранных sources, один controlled
normal/error scenario и отрицательные inputs. Детальные implementation choices
остаются агенту, material questions — DS-O01…05. Внешний host начинает сборку
по §25.2 без работающей версии собственного viewer; реальные interactions и
consumers должны быть готовы к зависимым итоговым checks.

**Один проход внутри разрешённой задачи:** прочитать owners/страницы → создать или
исправить owning page по exact base → read-only CHECK → построить derivative
представления/index отдельным покрытым действием → проверить допустимый preview
и scenario → показать factual diff/review → записать human decision только через
FTR-012 при настоящем пользовательском действии → обновить index → экспортировать
task-scoped pack. Нельзя обязать новое принятие каждого внутреннего build action:
настоящий user review относится к продуктовой операции/пилоту, а технические
проверки decision boundary используют явно синтетические fixtures.

Checker не обновляет source/status. Дефект contract, checker, implementation и
среды различаются по §10.3: observation → diagnosis → допустимый CORRECT с fresh
binding → affected check. Повтор без новых сведений расширяет диагностику по §10.4,
не создаёт бесконечную переработку UX. При прерывании §10.2 восстанавливает page
revision, external record/effect, проверенные/stale claims, ledger и следующий
шаг; после неизвестной записи сначала reconciliation. Failed index rebuild не
требует повторного Human Decision. Один continuation owner и текущая authority
сохраняются, реальный автоматический resume отдельно доказывается.

| Проверяемый предмет | Метод / Evidence и граница вывода |
|---|---|
| Structure/schema и expected set | Strict read/normalization, источники требований → mapping/gaps; positive и negative cases DS-T01–04/22. Schema PASS не доказывает смысл, interaction или пригодность preview |
| Human/Engineering и completeness | Сопоставить оба представления с одним snapshot, проверить semantic claims/unknowns по §25.7; DS-T05/15–17/21. Модель «две реализации» допускает разный renderer/parser с теми же guarantees |
| Preview boundary | На exact declared host/browser/profile проверить DS-T10/13/14, включая ресурсы, forms/navigation, host messages, script/runtime, paths/symlinks и outer controls; статический поиск запрещённых строк недостаточен |
| Render/behavior/accessibility | Объявленные одинаковые viewport/conditions для before/after; отдельные проверки клавиатуры/фокуса/названий и DS-T11/12. DOM/state graph, проигрывание и browser test — разные claims; автоматический check не объявляется полной accessibility evaluation |
| Decisions/recovery/consumers | DS-T06–09/18/19, interrupted page/index/pack write, real C-011/C-012/C-016 integrations; FRONTEND/INTEGRATION readiness на точном запросе. Fixture approval не реальный ACCEPT; frontend без API допустим лишь при достаточном UX |
| Общее техническое завершение | Требуемые части и стыки выбранной C-005 проверены по §10.5/§25.2, нет required gaps/unknown effects; отдельные PASS или полностью заполненный report не закрывают весь путь |

Все DS-T — designed tests, сейчас runtime NOT_RUN. Неприменимость конкретного
сценария требует основания в выбранном scope; declared interactive capability
не исключается ради PASS при отсутствии среды. Для authoring/review без preview
безопасная часть остаётся доступной, ограничение общего результата видно.
EXPORT_CONTEXT не требует успеха ещё не реализованных integration/E2E; он требует
достаточного входа для них. Смена source/page/runtime/assets/converter/decision
инвалидирует зависимые выводы; сохраняются unaffected facts, исторические records
и Evidence. Неизвестное влияние не даёт узкий итоговый PASS.

<a id="oss-ux-verification"></a>

**Воспроизводимые UX-проверки по RF-18 — DRAFT.** Метод Storybook адаптирован к
DS-T11/12/20/21 и [DS-PM01–05](06_Features.md#ux-pages-open-decisions), без выбора
framework. Сначала задать source/page revision, исходные props/view model,
mock inputs, viewport и последовательность действий, затем ожидаемые текст,
состояние и аргументы handoff. Reference — [RF-18](05_Reference.md#oss-reference-adaptation).
Все варианты ниже документальные, runtime NOT_RUN; новые browser/network/writes
этот текст не разрешает. Simulation остаётся в approved preview boundary.

| Вариант | Контроль и заранее заданный oracle | Что не засчитывается |
|---|---|---|
| DS-REF01 | В editor выбрать второй шаблон, ввести отличный от шаблона текст, открыть preview; сравнить видимый текст и данные передачи со значениями формы | Успешный render, наличие кнопки или один вызов callback с неправильными аргументами |
| DS-REF02 | На тех же исходных данных отдельно пройти success и error → retry; проверить сохранение введённого и отсутствие второй логической карточки. Следующий case начинается с чистой fixture | PASS за счёт state/spy результата предыдущего case; error с ложным created; один только screenshot без проверки поведения |
| DS-REF03 | Клавиатура, видимый focus, доступные названия, сообщение об ошибке; отдельно автоматический DOM-check с результатом incomplete | Отсутствие автоматических violations не закрывает ручные задания и incomplete. Результаты по методам раздельны; тест без мыши должен действительно пройти путь |
| DS-REF04 | FRONTEND проверяется на mocks; отдельно выбранный INTEGRATION путь с фактическим API/результатом и свежим Evidence | Вызов mock не доказывает сохранение/доставку/решение человека. При недоступном обязательном API integration NOT_RUN; пригодность frontend pack оценивается в его собственном scope |

Checks используют пользовательские роли/названия controls и фактический результат;
конкретный runner/assertion library — HOW. Эти варианты уточняют наблюдения,
не заменяют real usability pilot или проверку security boundary. Derived test
output не меняет страницу/decision record, а ложный успех относится к checker.

**Минимальный пользовательский пилот — PROPOSAL, не поручение запуска.** Одна
выбранная feature, одна форма и связанная страница, обе поверхности, ограниченная
симуляция, одна коррекция с diff, одно реальное решение через существующий канал
и один FRONTEND pack. При недоступной preview среде выполняется лишь безопасный
срез с явным NOT_RUN полного пути. Новый framework/server не нужен по умолчанию.

Предложение R2: три непрограммиста по два малых задания и две отдельные инженерные
сессии по разным заданиям. Expected behavior и один намеренный gap задать заранее,
записать порядок, инструменты и помощь модератора. Наблюдать способность найти
страницу, пройти normal/error, запросить изменение и понять scope решения; инженер
должен обнаружить gap и его последствия без прежнего чата, не выдумывая требований.

Порог для согласования, не отраслевой стандарт: минимум 5/6 человеческих заданий
без вынужденного открытия YAML/hash/CLI, 2/2 инженерных разбора с обнаружением gap,
ноль false-acceptance случаев. Сообщать успешные/выполненные задания отдельно с
помощью и без, время/ошибки и ограничения малой выборки; не переводить в 9/10.
Участники, выбор task, бюджет и разрешения не назначены этим proposal. Подлинную
независимость инженерных сессий подтвердить перед таким claim; авторская смена
перспективы её не заменяет.

В существующем отчёте §12 фиксировать стоимость всего цикла: подготовка, генерация,
правки, human review и context handoff, неудачные попытки, помощь/вмешательства и
принятый UX scope. Принятие UX не означает принятие всего приложения. Человеческое
время на принятый результат — по Product §13; неизвестное не равно нулю, при нуле
принятых результатов отношение не определено. Security/schema/behavior/usability
выводы раздельны, результаты и экономия сейчас NOT_RUN/UNKNOWN. Пилот не заменяет
историю автономной разработки модуля MOD-A01…05 и реальный host continuation.

<a id="rbac-abac-verification"></a>

### 25.9. FTR-031: подготовка и проверка доступа к полям — DRAFT

Применение §25.4–25.7 к [FTR-031](06_Features.md#ftr-031-contract), не новый
протокол. [Product](01_Product.md#rbac-abac-product) задаёт результат,
[Architecture](02_Architecture.md#rbac-abac-contract) — application binding/стыки,
[brief](../workspace/AOS_RBAC_ABAC_MODULE_IMPLEMENTATION_BRIEF.md) — маршрут чтения.
Создание модуля coding agent и настройка работающего приложения его пользователем
различаются: C-005/C-006/controller относятся к первому процессу; второй проверяет
MANAGE_FIELD_ACCESS host и не получает AOS authority от успешного apply.

Перед coding plan собрать выбранные бизнес-сценарии и independent expected
outcomes, каталог/модель и inventory реальных путей к сущности. Для каждого пути
из Architecture указать binding enforcement либо проверяемый отказ. Обязательный
для приложения канал не исключается агентом ради PASS. Schema/fixtures получают
один supported contract; отсутствующие EXAMPLE/SCENARIOS не восстанавливаются по
названиям. До запуска известны target, scope, effects/outputs, checks/oracles,
finite limits и host continuation по §25.1. Parser/framework/storage остаются HOW.

Собирать по порядку доступности: host identity/object/catalog/store contracts →
field decision и защита серверных путей → editor/preview/apply → integrated check.
Первый store/каталог не требует работающего редактора, bootstrap admin даёт host.
Точный порядок внутренних работ выбирает агент; защита обязательна до открытия
соответствующего пути. Один C-005/C-006 и существующий §10/§25.2 охватывают создание
выбранного компонента и интеграций; обычная correction не требует нового product
выбора. Если компонент внутри пользовательского проекта, действует §25.0: C-015/
C-016 и SC-T14 ядра AOS не становятся тестами его прикладных запросов. Если работа
затрагивает само ядро, проверяются действительно affected core paths.

| Группа | Метод и независимое основание | Предел результата |
|---|---|---|
| POLICY — RA-T01–08 | Бизнес-сценарии → ожидаемые ALLOW/DENY с причиной; отдельно комбинации ролей, операций, scope, false/error и несовместимые inputs | Expected values не генерируются тем же evaluator из тех же grants; совпадение schema и evaluator не доказывает бизнес-истину |
| ENFORCEMENT — RA-T09–17 | Прямые вызовы реальных API, наблюдение response bytes и доменных effects; каждый endpoint/serializer из binding имеет положительный путь либо проверенный отказ | UI masking, mock serializer и локальный evaluator PASS не доказывают серверное применение; защищённый write не оставляет partial effect |
| ADMIN — RA-T18–23 | Actual active revision/history/change event, current admin scope; conflict, потеря ответа, rollback, drift и отключение по Architecture | Доказательство отсутствия эффекта требует наблюдения host, не отсутствия ответа; имя роли не доказывает admin permission |
| UX — RA-T24/25 и RA-U01–06 ниже | Непрограммист выполняет задания на безопасных искусственных данных и объясняет итог; результат сравнивается с заранее заданным бизнес-смыслом | Авторская репетиция документа не является usability trial; отсутствие ошибок evaluator не доказывает понятность матрицы |
| Общий результат — RA-T26 | Изменить правило → проверить пример → применить → наблюдать новые права в реальном API/UI → отказной тест и сохранённая revision | Один editor или постоянный DENY не закрывает путь; корректные части при обходном endpoint не дают общий PASS |

POLICY-примеры [RA-REF01–04](06_Features.md#rbac-reference-semantics) уточняют
RA-T03/06 по методу RF-16: false, error и неиспользуемый attribute дают разные
ожидаемые выводы. Подмена этого oracle семантикой стороннего evaluator не
является успешной адаптацией; all-DENY также не проходит положительные случаи.

**Применимость протокола совместимости.** Шаги §25.4 выполняются для одного
FTR-031 и его host-приложения. C-015 registration, C-016 delivery/ack и queue
generations неприменимы к этому runtime по §25.0; их отсутствие не исключает
проверку реальных interfaces, версий, data/effects и lifecycle из Architecture.
Change event не считается очередью. Если позднее предложено подключение к самому
ядру AOS, оно требует отдельного contract scope, а не наследует этот вывод.

| Шаги §25.4 / применимый контроль | Основание и проверка для FTR-031 |
|---|---|
| 1–2: предмет и поведение | Product + dossier: прикладные поля, DEFERRED/DRAFT, RA-T01–25; нет дублирования FTR-019 и нового объединения с FTR-032 |
| 3–4: композиция, interfaces и versions | Architecture §10.3: host producers → evaluator/adapter → serializer/domain/store; RA-C01/05 и RA-T09–17 проверяют совместимость и обходы. При достаточных host contracts первый editor не нужен для bootstrap store |
| 5: lifecycle | Все операции ADD/ENABLE, UPDATE, DISABLE, REMOVE, DELETE DATA из Architecture; RA-C02–04 вместе с RA-T18–23. Required consumer нельзя объявить optional ради удаления |
| 6: semantic readiness / MOD-A06 | К1–К10 и реальные consumer paths; RA-T09/16/26 отвергают unit PASS с неправильным serializer. RA-C04 различает потерю ответа и отсутствие эффекта. Runtime отказ не равен качественной неполноте документации |
| 7–8: автономная сборка / MOD-A01–05 | Один parent выбранного приложения по §25.0/§10.5, текущие criteria/authority/ledger и real integrations. MOD-A02 проверяет стык с host, MOD-A05 — регрессию его обязательных сценариев; C-015/C-016-специфическая часть MOD-A07 для 005+022 сюда не переносится |

RA-C01–05 — проверки интеграции/lifecycle по existing protocol, не отдельный gate.
Для Evidence каждого выполненного случая связать exact module candidate,
host/adapter и model/catalog versions, policy revision, request/subject, проверенный
путь, метод, ожидаемое/наблюдаемое и фактические effects. Прежний PASS другого
набора не переносится. Несовместимость блокирует affected path; корректные
независимые paths не становятся ошибочными автоматически. Техническое завершение
всё равно требует всех обязательных сценариев выбранного приложения.

Локальные RA-* введены при адаптации сообщения и не объявляются IDs отсутствующего
SCENARIOS.yaml. Все runtime/security/usability проверки NOT_RUN. Ошибка реализации,
требования, checker или среды различается по §10.3; ненадёжный oracle исправляется
отдельно, критерии не ослабляются. Повтор без новых сведений использует §10.4,
interruption — §10.2 с общим ledger/authority и actual effects. Finished tasks
не возобновляются из-за необязательного улучшения.

**Шесть пользовательских задач — PROPOSAL пилота.** Основа —
[документальный fixture](06_Features.md#rbac-abac-cases). Каждый вариант стартует
от своей явно изменённой копии; настройки реального приложения не затрагиваются.

| ID | Задание / изменённый начальный draft | Заранее заданный результат |
|---|---|---|
| RA-U01 | editor.UPDATE title дан без условия; настроить «редактор меняет только своё» | D1 разрешён, D2 запрещён; OWN_RECORD виден |
| RA-U02 | У editor добавлен READ internal_notes; закрыть внутренние заметки | Для U1 нет READ notes; manager сохранён |
| RA-U03 | У editor отсутствует SET_ON_CREATE external_code; разрешить заполнение при создании | SET_ON_CREATE разрешён, UPDATE по-прежнему недоступен по каталогу |
| RA-U04 | Проверить изменение D3.title | Запрет по LOCKED понятен; дополнительная роль не снимает ограничение |
| RA-U05 | Снять editor.READ title у U1 с editor+viewer и объяснить итог | READ сохраняется от viewer; «не выдано этой ролью» не принято за общий запрет |
| RA-U06 | Бизнес-правило «notes только manager»; намеренно добавлен viewer.READ notes | Найти и убрать ошибочный grant, проверить combined result; расширение не осталось незамеченным |

Предложенный критерий из источника: все шесть задач завершены без редактирования
кода, ни одно намеренное ошибочное расширение не пропущено. Фиксировать итоговую
матрицу, ошибки, обращения за помощью, время и ограничения выборки в существующем
отчёте §12; состав участников/первое приложение не назначены. Не приписывать этим
заданиям реальные результаты. Для оценки пользы учитывать также подготовку,
correction и интеграцию по Product §13; неизвестные значения не заменять нулями.

Перед техническим завершением §10.5 проверяет current candidate, все обязательные
пути binding, критерии фичи/реальных стыков, reconciled effects и сохранённый state.
При изменении grants/catalog/security bindings/roles/adapter/response повторить
затронутые POLICY/ENFORCEMENT/ADMIN/UX проверки; неизвестное влияние расширяет
проверку или ограничивает итог. Смена примера не доказывает новую runtime revision.

<a id="recovery-verification"></a>

### 25.10. Recovery / FTR-033 — подготовка, совместимость и проверка DRAFT

Применение §25.4–25.7 к [Recovery](06_Features.md#ftr-033-contract), не новый
протокол и не полномочия на pilot. Две разные задачи: создание самого модуля
по §25.1/§10 и работа будущего модуля над existing project. Успех второй не
доказывает автономную историю первой, а HANDOFF_PREPARED не завершает ремонт.

**Будущее использование.** Static discovery/assessment — bounded PLAN с отчётом
и stop; human disposition отдельно, подготовка handoff в следующей разрешённой
PLAN task. Стадии и их permissions принадлежат текущему workflow, recovery_state
их не заменяет. Классы STATIC_OBSERVATION / EXECUTABLE_OBSERVATION / TARGET_MUTATION
не Risk Profiles. В static scope последние два не допускаются. Служебные output
effects должны входить в task boundary и идти по Architecture admission; название
PLAN не предоставляет write authority. Handoff null refs запрещают перенос
разрешения текущего отчёта на будущие команды/ремонт/Git.

Для queued persistence/delivery §10.0 и C-006A запрещают dispatch effectful
COMMAND из standalone PLAN. Проверить отдельный действующий service task/stage
binding только на external outputs; не переходить в EXECUTE по одному желанию
сохранить отчёт. Разрешённое документальное сохранение по §9 — другой путь,
не proof C-016 integration. При отсутствии поддержанного пути — transient/blocked
output с ограничением. Профиль будущего runtime обязан назвать этот путь и его
authority; он не расширяет read-only границу исходного проекта. Разработка самого
модуля по §25.1 остаётся своей task и не является service authority его пользователя.

Budget задаётся до run с единицей/значением и stop behavior. На исчерпании или
stop не начинать следующую discovery/tool работу; допустим только заранее
покрытый путь сохранения/отчёта о фактическом состоянии. Если persistence тоже
запрещён/недоступен, сообщить transient/потерянную часть, не обходить запрет ради
durability. Не резервировать себе новый budget автоматически. Повтор без новых
данных — §10.3–10.4, unknown effect/resume — §10.2, validation не исправляет subject.

**Следующая executable observation — отдельная задача.** До запуска фиксируются
exact command/entrypoint/cwd/subject, synthetic inputs, trusted tool origin,
environment, write/network allowlist, credentials/data boundary, конечные limits,
stop/cancel и ожидаемое наблюдение. Копия проекта сама не доказывает confinement.
Нет пригодного provider → NOT_RUN, независимый Assessment возможен. Реализация
reader/schema/test adapter — работа будущей покрытой сборки до их зависимого
применения, а не требование заранее создать продукт ради implementation planning.

**Совместимость и порядок сборки.** Intake/claim contracts → safe reader/import и
storage/origin interfaces → Assessment/state projection → handoff/receiver → real
integrated cases. Код scanner/executor/Project Memory не дублировать: использовать
объявленные capability boundaries. Нет runtime dependency от установки файлов
AOS в source root. Для runtime-модуля, однако, C-015/C-016 и реальные consumers
проверяются по [Architecture §10.4](02_Architecture.md#recovery-contract).

| §25.4 / контроль | Применение, наблюдаемый результат и отрицательный пример |
|---|---|
| 1–2: предмет/поведение | Product + dossier: FTR-033, DEFERRED/DRAFT, source unchanged, Assessment → один PLAN. REC-AC-001…012 и REC-POS-001…003 исключают пустой отчёт/постоянный отказ при достаточном входе |
| 3–4: стыки | C-001/002/003/005/006/007/009/010/011/012 + C-015/C-016 карта в Architecture. Корректный export с неверным receipt или недоступным required ref не даёт HANDED_OFF (REC-NEG-020/026/028) |
| 5: lifecycle | ADD/UPDATE/DISABLE/REMOVE/DELETE DATA; pending/in-flight/old versions и required consumers не N/A при фактических sidecar/queue effects; REC-C01–03 и output/replay REC-C04–07 ниже |
| 6: semantic readiness / MOD-A06 | К1–К10, восемь репетиций и обе попытки опровержения; fake C-011, stale manifest, скрытый execution и score не проходят REC-NEG-001…030. Defined records не заменяют достоверность их contents |
| 7–8: module build / MOD-A01–05 | Exact accepted scope/profile, target, parent C-005/C-006, limits/continuation и реальный host. MOD-A02/05 проверяют reader→Assessment→decision→receiver и affected core regression. Контроллер закрывает общую task по §10.5, не по числу файлов |

Designed compatibility cases (runtime NOT_RUN):

| ID | Вход / ожидаемый результат |
|---|---|
| REC-C01 | Совместимые C-015/record/reader/receiver versions → REC-POS-001. Unknown/mixed version либо partial ADD → нет business dispatch, поддержанное inspection без conversion, данные сохранены |
| REC-C02 | UPDATE/DISABLE с pending save и in-flight handoff → новые calls закрыты, pending удержаны, effect/receipt выяснены до перехода; old generation не replay на новый handler |
| REC-C03 | REMOVE при required consumer без замены → BLOCKED; после покрытой замены/disable/reconciliation удалить только owned implementation. Пакет/decisions/source сохраняются; DELETE DATA отдельно, reinstall не повторяет очередь |
| REC-C04 | Standalone PLAN пытается отправить save COMMAND → нет effectful dispatch/записи из его authority. Отдельный разрешённый service EXECUTE может сохранить только external output, без target writes; документальное сохранение не объявляется C-016 runtime PASS |
| REC-C05 | Assessment B1 рекомендует S1, содержит S2; общее ACCEPT без выбранного next objective → не PREPARING_HANDOFF. Подлинный выбор S2+N2 по B1 сохраняет именно S2+N2; смена рекомендации S1 не меняет его, enum C-011 не расширен |
| REC-C06 | Пакет P1 передан, ответ потерян; redelivery того же operation → тот же receipt, не новая task. Ack без inputs check, receipt P0/другого receiver или тот же operation с P2 → не HANDED_OFF P1. Новый PLAN не запускается от receipt |
| REC-C07 | Два writer от output revision O1 при неизменном source HEAD; первый сохранил O2 → второй не затирает O2, получает conflict/reconciliation. Проверка source identity не подменяет expected output base; unknown save не повторяется с новым operation ID |

**Методы и Evidence.** Тесты проектируются на disposable fixtures из dossier:
Git staged/unstaged/untracked и directory, conflicting README/checks, два manifest,
external link, sentinel, test-only/forged C-011, interrupted writer, unavailable
receiver/provider. Ожидания заданы до implementation. Harness наблюдает
target_write_events, target_code_execution_events, network_events, disclosed_payloads,
complete revisions и exact receipts. Поиск строк в summary и before/after equality
не доказывают отсутствие временных/внешних effects. Actual API/handler journeys
и реальные storage/origin/receiver adapters нужны для integrated completion;
stub/ручной walkthrough подтверждают только свою ограниченную область.

Каждое выполненное наблюдение содержит purpose/method, module/contract/subject
revision, environment/coverage, expected/actual, Evidence и ограничения. Import
старого PASS сохраняет старый checked subject; проверка импорта не означает
повтор теста. Смена source/index/untracked/contract/consumer/decision/permission
делает affected выводы неприменимыми до recheck, не обнуляя unrelated conclusions.

**Ограниченный pilot — PROPOSAL.** Один отдельно выбранный не-AOS проект и вопрос,
safe static read, external workspace, без target commands/mutations. Owner intake
→ Assessment → понимание → exact direction/next objective decision → MMB/handoff
→ свежий исполнитель проверяет inputs следующего PLAN без чата автора.
Он открывает нужные refs и rechecks mutable facts, не пересканирует всё по умолчанию.
Это не обязательный multi-agent runtime и не доказательство исправления проекта.

Владелец по default summary без технической подсказки должен объяснить: (1) scope
исследования/NOT_RUN; (2) препятствие и степень установления причины; (3) следующий
результат/альтернативу; (4) смысл решения и что не разрешено; (5) stop/resume.
Критерий candidate: все пять сохраняют смысл, нет путаницы «найдено=работает»,
«направление=authority», «handoff=исправлено». Ошибка понимания ведёт к исправлению
формулировки/дизайна в покрытой correction, не снижению критерия. Успех знакомого
с AOS владельца не обобщается на новых пользователей; contrasting case отдельно.

В существующем отчёте §12 фиксировать время до понятного Assessment, material
questions, прочитанный/переданный контекст, доступные расходы, claims без основания,
ложную проверенность, помощь/ошибки понимания, успех handoff и повторное широкое
чтение. Человеческое время на принятый результат — по Product §13; UNKNOWN не ноль,
без принятых результатов отношение не определено. Эффект ремонта/экономию измерять
по отдельно выполненному slice; здесь NOT_RUN. Safety counts сообщать отдельно,
не компенсировать неразрешённый эффект удобным интерфейсом.

Документальная проверка, pilot, runtime tests, независимый review и автономная
сборка имеют раздельные выводы. Открытые REC-O не заполняются догадкой; после
ограниченной проверки/правки — report и stop без автоматического запуска pilot.
