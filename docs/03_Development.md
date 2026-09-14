---
package: AOS_Project_Knowledge_Baseline
package_revision: R7-RU
updated: '2026-09-13'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: AOS_PRECOMMIT_DOCUMENTATION_CORRECTIONS_R7
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

Ниже сохранён маршрут exact Global Design Package. Его Freeze относится к указанным трём файлам `AOS/`. Для нового scaffold/core документационная задача идёт от current owners к bounded [brief](../workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md); применение этого handoff к runtime предложено как `SCAFFOLD_CORE_DRAFT` и ожидает [SC-DEC-01](00_Core.md#scaffold-core-decisions). Подготовка нового DRAFT не меняет frozen bytes и не предоставляет им новую authority.

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

## 8. Task Brief и Execution Authorization

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
Exact authorized scope, one stage, no hidden next stage, no unrelated cleanup; terminal result → report and stop.

### VALIDATE
Read-only exact candidate. Does not fix. Independent validation required only when risk/task demands it. Переход к отдельному corrector возможен только по full-cycle правилам §10.0, не из полномочий validator.

### REVIEW
Read-only assessment/recommendation. No simulated acceptance or correction.

### DELIVER
Handoff package, not stage or Git permission.

<a id="core-lifecycle-transitions"></a>

### 10.0. Явные lifecycle-переходы полного цикла — SCAFFOLD_CORE_DRAFT R5

Человек выбрал явные переходы исполнения и проверки внутри одной задачи.
Эти правила V3 применяются к явно принятому full-cycle scope S0–K4 и отдельной задаче сборки выбранного модуля по §25; создание
DRAFT, имя lifecycle stage или широкая parent allowlist не включают такой scope
автоматически. Самостоятельная PLAN/VALIDATE/REVIEW task сохраняет свою read-only
границу и не получает correction authority. Для неё действие, требующее выхода
из принятого scope/stage, блокируется до отдельного решения; техническое чтение
и выдача отчёта сами не требуют нового effectful worker.

C-005.lifecycle_stage — исходная стадия задачи, C-012 — текущая. Для запуска уже
подготовленной реализации S0–K4 или выбранного модуля исходная стадия EXECUTE; если принятая full-cycle
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

Документационный цикл избавлен от тяжеловесных инженерных проверок. Шаги 1–7 ниже описывают scoped Global Design publication; их нельзя применять как требование автоматически переписать frozen `AOS/` при новой scaffold/core-задаче. Её текущий authoring route: owner corrections/proposals → один производный brief → документальные checks → конкретный пакет решений. Runtime-применимость нового входа остаётся DRAFT до SC-DEC-01.

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

One active task, one causal change, no unrelated cleanup, inventory before sensitive mutation, explicit scope expansion, changed-file allowlist, atomic commit after separate authorization, docs↔schema↔CLI↔code↔tests consistency, source read-only during extraction, no automatic `git add -A`.

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

Freeze subject; verify environment/import provenance; run targeted checks; wider suite only if relevant; record commands/results; preserve required/optional; classify limitations; inspect diff; verify no validation mutation; stop with one next action.

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

Для scaffold/core подготовлено точное уточнение этого порядка в [Product §17](01_Product.md#scaffold-core-outcome): технические срезы и positive/negative проверки выполняются внутри исходного интервала, а human usability evidence собирается отдельно. Это SCAFFOLD_CORE_DRAFT/SC-DEC-01; оно не объявляет пользовательский dogfood уже выполненным.

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

#### Ограниченное измерение полезности

Сначала один реальный многосоставной вопрос на известном scope, затем небольшой заранее объявленный набор: exact fix; русское описание/английский ID; interface с consumers; current/future difference; resume dirty change; partial observation/ambiguous mapping. Сравнить A — тот же агент с direct search, B — lexical, C — lexical+graph; для одного сложного случая C с/без comparator. Semantic D только при измеренном recall gap.

До запуска фиксируются corpus/snapshot, source access, model/settings, oracle, число повторов и budget. Порядок чередуется, контексты изолированы; подготовка карты/mapping, cold build, refresh, failures/retries и review входят в стоимость. Проверить качество конечной разработки, обязательные source spans/recall, ложные и пропущенные Delta, чтения/байты, человеческие уточнения/время, model usage, latency. Unknown costs не нули; подписочная квота не пересчитывается в деньги по API без основания. При нуле validated results стоимость на результат не определена.

Выигрыш по времени/полным затратам заявляется только без существенной потери качества и mandatory coverage. Предложенные архивом 20% — ориентир для обсуждения pilot, не подтверждённая экономия. Итог ограничен tested scope: benefit / no benefit / inconclusive, без нового lifecycle gate. Неуспешный pilot не запускает бесконечную смену backend.

**Readiness:** проверка документационного переноса не запускает runtime/benchmark/архивные scripts. [Единый brief](../workspace/AOS_GRAPH_RAG_MODULE_IMPLEMENTATION_BRIEF.md) связывает owner sections, compatibility mapping и оставшиеся inputs; actual runtime, installed support, independent validation и экономия — `NOT_RUN`. Будущий агент перед реализацией сверяет current owners и exact revisions, не воспроизводит архивные инструкции AOS-3 как authority.

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

## 24. Автономная разработка scaffold/core — SCAFFOLD_CORE_DRAFT

Этот route применяется после принятия [S0–K4](01_Product.md#scaffold-core-outcome), нужных contracts и отдельного launch. Сейчас он описывает подготовленный контракт будущей разработки. Матрица действий V3 и completion predicate находятся в Architecture §7 и Development §10, а `S0–K4` не являются новыми lifecycle enums.

### 24.1. До первого effect

1. Прочитать Core decisions → Product outcome → [базовые dossiers](06_Features.md#core-first-scope) → Architecture interfaces → этот workflow и производный brief. Старый blueprint используется только для разрешения конкретного вопроса через Reference.
2. Привязать exact task/revision, target/root/worktree/base и принятую contract revision; сохранить observed dirt/ownership и запрещённые paths. Существующий repository не считать новым пустым проектом.
3. Уточнить только существенные отсутствующие входы. Готовые Intent/Spec/Passport и исходные человеческие ответы не проходят повторное интервью ради ceremony.
4. Сформировать конечные acceptance criteria и их dependency order для всего S0–K4. Декомпозиция — работа агента внутри scope; backlog FTR-007 не обязателен. Это не transport queue C-016, выбранная для первого ядра.
5. Bind действующую runtime authority и [host capability](02_Architecture.md#scaffold-core-host), command/environment и допустимую test/probe boundary. Проверить доверенное происхождение input, срок/отзыв, ресурсные ограничения и supported resume.
6. Required host/environment check без Evidence даёт конкретный BLOCKED/NOT_RUN. Нельзя начать S0 под видом проверки собственного ещё не реализованного guard.

Для положительного автономного пути C-005 ссылается на exact заранее принятые C-002/C-003. Генерация новых DRAFT-версий в K1 не делает их accepted и не заменяет source binding задачи. Поэтому проверка intake/spec generation и исполнение по уже принятым входам различаются; недостаточная идея, требующая нового человеческого выбора, не обещает uninterrupted autonomous completion.

### 24.2. Внешний development loop с S0

Внешний host сохраняет task checkpoint и владеет продолжением; worker выполняет одно разрешённое действие и возвращает наблюдения. Fresh action boundary должна соответствовать гарантиям canonical parent/envelope contracts, даже когда host использует своё native представление.

Следующий шаг определяется §10.5: reconcile effect → проверить authority/identity → восстановить state → диагностировать failing check → разрешить material unknown → взять dependency-ready критерий → affected checks → final validation. Действующий scheduler/launcher принадлежит host, не создаётся молча как дополнительный product scope.

После каждого action сохраняются task/revision, candidate, критерии и Evidence, effects, диагностическая signature/level, попытки/resources, actual authority binding и next action. Worker выдаёт factual report и останавливается; checker работает в отдельной validation boundary, host оценивает результат и продолжает ту же task. Обычная correction имеет новое action binding и candidate, но не требует нового product plan.

Порядок реализации — S0 → K1 → K2 → K3 → K4; обязательные support contracts создаются до их первого consumer. Например, K2 уже требует durable state, scope reconciliation и независимой от worker проверки. Неполный промежуточный срез не выдаётся за готовое ядро. Если initial authority покрывает все срезы, их переходы не создают дополнительные Human Gates.

До готовности product controller не требуются команды AOS для выдачи внешней authority, записи первоначального state или запуска локального test harness. Product registry/queue C-015/C-016 создаются по Architecture §6.5, без зависимости от собственного transport; профиль заранее задаёт finite capacity/payload/wait/claim/retry/retention и покрытые service paths. Внешнему host до S0 не приписывается готовая product queue. Внешний host обязан обеспечить эти гарантии своим проверенным способом. Нельзя «для bootstrap» пропустить current authority, candidate identity или evidence collection.

Первый product checkpoint готовится по [initial-state contract](#initial-product-state)
до K2. SC-DEC-04 должен явно покрывать служебную инициализацию; внешний host
доказывает соответствие [набору V3](02_Architecture.md#core-loop-v3), включая
диагностические checks, конфликт владельцев, vocabulary/report и lifecycle admission. V1/V2 conformance не переносится; host должен доказать SC-T21/22 до зависимого запуска.

### 24.3. Прерывание и передача controller

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

<a id="feature-integration-readiness"></a>

## 25. Следующий модуль: автономная сборка и интеграция

Обязательный алгоритм создания/изменения фичи, формирования модуля и проверки
его достаточности — [§25.4](#feature-module-protocol); подключение/удаление —
[§25.5](#module-connection-lifecycle). Он применяется перед зависимой реализацией
и после изменения contracts, а не только при первом добавлении в каталог.

Содержательная read-only проверка достаточности документации проводится по
[§25.7](#feature-documentation-review). Это детализация проверки §25.4, а не
параллельный набор требований, новый lifecycle или разрешение на correction.

Для поздних модулей применяется существующий §6 feature-specific workflow к
каждой входящей фиче на этапе подготовки, затем один общий маршрут разработки:
выбор модуля → достаточные contracts и анализ стыков → единый module brief и
parent authority → автономная сборка/интеграция/check/correction → integrated
review. У модуля из одной фичи это тот же маршрут. Все поздние dossiers
одновременно не перерабатываются.

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


<a id="autonomous-module-development"></a>

### 25.1. Готовность к автономной сборке модуля

Product owner [задаёт результат](01_Product.md#autonomous-module-outcome).
Используются существующие C-contracts и loop V3, без нового lifecycle или
параллельного каталога модулей. Название/состав берутся из выбранной группировки
Features; FTR-ID и ownership сохраняются.

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
остаются сужением исходной authority. Закрытие child не закрывает parent.

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
