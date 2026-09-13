---
document_id: AOS-DEVELOPMENT-COMPLETION-LOOP-DESIGN-R2
status: DRAFT_CORRECTED
authority: PROPOSAL
human_model_decision: ACCEPTED_IN_CURRENT_SESSION
predecessor_sha256: 9307b1b190382eec0fa41cfb95d108cd98a59afa03218a1e18df26d0744053dc
correction_scope: REVIEW-F001..F008
second_review_correction_scope: REVIEW2-F001..F004
third_review_correction_scope: REVIEW3-F001..F003
loop_break_rebuild_scope: STATE_MACHINE_AUTHORITY_CORE
implementation_status: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS — механизм петли разработки до завершения задачи

## 1. Назначение

Механизм обеспечивает продолжение одной поставленной задачи через реализацию,
проверку, диагностику, исправление и восстановление после прерывания до
доказанного технического завершения либо до точной границы, требующей решения
человека.

Петля не создаёт новые полномочия. Она использует исходную задачу, её
разрешённый scope и уже принятые product/architecture contracts. Commit, Push,
Merge, Release, изменение product scope, material architecture, security,
privacy или trust boundary остаются отдельными решениями.

## 2. Результат и не-цели

Механизм должен:

1. продолжать работу после промежуточного результата агента или прерывания;
2. выбирать следующий незавершённый шаг из фактического состояния;
3. отличать внутреннюю проверку от итогового результата задачи;
4. исправлять обычные дефекты внутри исходного разрешённого scope;
5. расширять диагностику, если причина не найдена или Evidence неубедительно;
6. предотвращать повторение действий без прироста информации;
7. завершать задачу только по проверяемому completion predicate;
8. сохранять Evidence, ограничения, `NOT_RUN`, блокеры и следующий шаг.

Механизм не должен:

- считать ответ исполнителя доказательством завершения;
- автоматически расширять writable paths, operations, effects или authority;
- выбирать human-only product/architecture decisions;
- превращать `UNKNOWN`, `BLOCKED` или `NOT_RUN` в `PASS`;
- автоматически выполнять Git delivery или публикацию;
- скрывать исчерпание ресурсов либо бесконечно повторять одну траекторию;
- требовать нескольких агентов для нормальной работы.

## 3. Архитектурный выбор

Выбран сохраняемый контроллер состояния. Исполнитель может меняться между
итерациями, но controller восстанавливает одну и ту же task identity, candidate,
ledger попыток, Evidence и resource usage.

```text
Task Contract
    ↓
Persistent Loop State ←→ Repository / Candidate
    ↓
Next-action selector
    ↓
Executor → Checker → Diagnostic ladder → Corrector
    ↑                                  ↓
    └──────────── refreshed state ─────┘
```

Контроллер управляет переходами и проверяет условия. Coding agent выбирает
обратимый implementation HOW внутри accepted boundaries. Checker проверяет
observable result. Отдельный independent validator, когда он требуется, остаётся
read-only относительно exact candidate и не исправляет его.

## 4. Входной Task Contract

Петля запускается только для одной bounded задачи со следующими полями:

```yaml
task_contract_version: AOS_TASK_CONTRACT_V1
task_id:
task_revision:
lifecycle_stage: PLAN | EXECUTE | VALIDATE | REVIEW
goal:
acceptance_criteria: []
required_checks: []
optional_checks: []
requested_paths: []
prohibited_paths: []
requested_operations: []
prohibited_operations: []
requested_effects: []
prohibited_effects: []
source_and_contract_bindings: []
starting_repository_identity:
parent_task_authority_requirements:
  requested_worker_actions: []
  requested_task_hard_limits:
validation_policy:
  independence_required:
  validator_subject:
  required_environment:
run_allowance:
human_only_boundaries: []
accepted_residual_risk_records: []
```

Task Contract описывает requested boundary и requirements, но не предоставляет
authority и до отдельной выдачи не содержит authorization identity. Отдельный
Parent Task Authorization имеет собственную identity и
фиксирует exact task revision/subject, allowed worker actions,
operations/paths/effects, human-only boundaries, expiry/revocation и
task hard limits. Он создаётся человеком; фактический binding сохраняется в
Loop State без переписывания Task Contract.

Task Contract использует только `requested_*`/`prohibited_*`. `allowed_*`
появляется только в Parent Task Authorization и Stage Envelope. Authorization
не изменяет canonical controller-action graph.
Допустимые значения `allowed_worker_actions` — только `EXECUTE` и `CORRECT`;
пустой список не разрешает effectful dispatch.

```yaml
parent_task_authorization:
  authorization_schema_version: AOS_PARENT_TASK_AUTHORIZATION_V1
  authorization_id:
  authorization_revision:
  task_id:
  task_revision:
  subject_identity:
  allowed_worker_actions: []
  allowed_operations: []
  allowed_paths: []
  allowed_effects: []
  forbidden_operations: []
  forbidden_paths: []
  forbidden_effects: []
  human_only_boundaries: []
  task_hard_limits:
  issued_by_human:
  issued_at:
  expires_at:
  revoked: false
```

`task_hard_limits` в authorization задаются только пользователем или более
строгим host policy.
Их достижение может завершить незакрытую задачу с `FAIL`. `run_allowance` —
конечный рабочий лимит одного запуска, который controller может выбрать внутри
этих границ. Его исчерпание при незавершённой задаче создаёт
`PAUSED_RESOURCE`, сохраняет state и не превращает задачу в terminal `FAIL`.

Authority-поля authorization/envelope fail closed: отсутствующее поле, `null` и пустой список означают
«ничего не разрешено». Неограниченный wildcard запрещён. Любое pattern-based
разрешение должно быть явным, иметь bounded root и проверяться после canonical
path resolution. Требования `prohibited_*` переносятся в forbidden fields
authorization/envelope и всегда имеют приоритет над разрешающими полями.

Изменение goal, acceptance, requested paths/operations/effects или human-only
boundary создаёт новую revision задачи. Оно не маскируется как продолжение.

## 5. Сохраняемое состояние

После каждого material observation, mutation, check или перехода controller
атомарно сохраняет:

```yaml
loop_state_version:
state_machine_version: AOS_COMPLETE_TASK_LOOP_V1
state_revision:
previous_state_digest:
event_head_identity:
task_id:
task_revision:
task_state:
run_state:
run_result:
repository_identity:
candidate_identity:
controller_action:
acceptance_status: {}
required_check_status: {}
check_impact_basis: {}
open_findings: []
material_unknowns: []
diagnostic_state:
attempt_ledger: []
resource_usage:
authorization_state:
parent_authorization_id:
parent_authorization_revision:
parent_authorization_digest:
active_stage_envelope:
active_validation_envelope:
controller_lease:
last_observed_effects: []
next_action:
updated_at:
```

Chat summary, свободный текст отчёта и process memory не являются единственным
владельцем состояния. После прерывания controller сначала сверяет сохранённые
claims с repository/candidate и только затем продолжает работу.

Controller является единственным владельцем controller-action переходов. Lifecycle
stage `PLAN | EXECUTE | VALIDATE | REVIEW` хранится отдельно и не является enum
внутренних действий controller. Worker outputs считаются
непроверенными observations: worker не может напрямую установить task state,
закрыть acceptance criterion или записать `PASS`. Каждый transition проверяет
предыдущий `state_revision` и digest. Реализация использует single-controller
lease либо эквивалентный compare-and-swap; конкурентное или stale обновление
отклоняется и направляется в `RECOVER_STATE`. Каждое принятое событие получает
identity и связывается с предыдущим event head.

## 6. Версионированная state machine

Controller-action matrix `AOS_COMPLETE_TASK_LOOP_V1`:

| `from` | Допустимые `to` |
|---|---|
| `BIND_TASK` | `RECOVER_STATE`, `IDLE` |
| `RECOVER_STATE` | `SELECT_NEXT_ACTION`, `DIAGNOSE`, `IDLE` |
| `SELECT_NEXT_ACTION` | `EXECUTE`, `CHECK`, `FINAL_VALIDATE`, `IDLE` |
| `EXECUTE` | `CHECK`, `DIAGNOSE`, `IDLE` |
| `CHECK` | `SELECT_NEXT_ACTION`, `DIAGNOSE`, `FINAL_VALIDATE`, `IDLE` |
| `DIAGNOSE` | `CORRECT`, `IDLE` |
| `CORRECT` | `CHECK`, `DIAGNOSE`, `IDLE` |
| `FINAL_VALIDATE` | `DIAGNOSE`, `IDLE` |
| `IDLE` | `RECOVER_STATE` после resume event |

Lifecycle stage, controller action, task state и run state являются отдельными
осями:

```text
lifecycle_stage: PLAN | EXECUTE | VALIDATE | REVIEW
controller_action: BIND_TASK | RECOVER_STATE | SELECT_NEXT_ACTION | EXECUTE |
                   CHECK | DIAGNOSE | CORRECT | FINAL_VALIDATE | IDLE
run_state:  RUNNING | PAUSED_RESOURCE | STOPPED
run_result: PASS | FAIL | UNKNOWN | BLOCKED | CONTRACT_VIOLATION | NOT_RUN
task_state: ACTIVE | WAIT_HUMAN | WAIT_EVIDENCE | TECHNICALLY_COMPLETE |
            TASK_FAILED | CANCELLED_BY_HUMAN | CONTRACT_VIOLATION
```

Wait/terminal task state или resource pause переводит controller action в
`IDLE`, а не создаёт transition к имени другой оси. `WAIT_HUMAN` и
`WAIT_EVIDENCE` означают приостановку task; `PAUSED_RESOURCE` относится к run и
сохраняет `task_state: ACTIVE`. Resume event допускает только
`IDLE → RECOVER_STATE`, где authority и mutable facts проверяются заново.

`FAIL`, `UNKNOWN` и `BLOCKED` одного worker/run не закрывают task автоматически.
При исчерпании run allowance controller сохраняет controller/next action, переводит
controller action в `IDLE`, а run state — в `PAUSED_RESOURCE`.

`run: FAIL/UNKNOWN/BLOCKED` не завершает `task: ACTIVE`, если сохраняется
разрешённый и обоснованный следующий шаг. Terminal task state требует
completion predicate, явной отмены, user hard-limit либо Evidence доказанной
невозможности выполнить accepted contract в текущем task scope.

## 7. Основная петля

```text
BIND_TASK
→ RECOVER_STATE
→ SELECT_NEXT_ACTION
→ EXECUTE
→ CHECK
    ├─ PASS и остались criteria → SELECT_NEXT_ACTION
    ├─ PASS и все criteria закрыты → FINAL_VALIDATE
    ├─ FAIL или material UNKNOWN → DIAGNOSE
    └─ missing decision/authority → task WAIT_HUMAN + action IDLE
→ CORRECT
→ CHECK
→ …
→ FINAL_VALIDATE
    ├─ completion predicate true → task TECHNICALLY_COMPLETE + action IDLE
    └─ finding → DIAGNOSE → CORRECT → FINAL_VALIDATE
```

Исчерпание `run_allowance` в любой нетерминальной точке сохраняет next action и
переводит run в `PAUSED_RESOURCE`. Новый run начинает с `RECOVER_STATE`, не
сбрасывая task ledger, diagnostic level или resource usage.

Исполнитель не завершает задачу собственным сообщением `done`. Он возвращает
structured observation, после чего controller заново вычисляет следующий
переход.

### 7.1. Детерминированный выбор следующего действия

Controller выбирает первую применимую категорию в порядке:

1. reconciliation неизвестного результата effectful action;
2. остановка при contract/authority/candidate identity violation;
3. восстановление stale или конфликтующего persistent state;
4. диагностика failing required check;
5. разрешение material unknown, блокирующего acceptance;
6. выполнение незакрытого acceptance criterion с удовлетворёнными dependencies;
7. повтор affected required checks;
8. `FINAL_VALIDATE`, когда остальные required work items закрыты;
9. optional work, только если оно явно включено и не задерживает completion.

Внутри одной категории применяется стабильный порядок declared dependency,
затем Task Contract order. Controller сохраняет причину выбора. Независимая
ветвь не должна бесконечно вытеснять более ранний required blocker.

### 7.2. Parent authority и worker envelopes

Parent Task Authorization ограничивает только effectful worker actions
`EXECUTE`/`CORRECT` и не меняет graph `AOS_COMPLETE_TASK_LOOP_V1`. Controller
создаёт Effectful Stage Envelope после выбора exact разрешённого transition.

```text
Task Contract request
→ Human Parent Task Authorization
→ controller transition по canonical matrix
→ [для CORRECT: Correction Gate]
→ fresh Effectful Stage Envelope
→ worker factual result + consume-before-effect
→ read-only ValidationEnvelope
→ controller recomputes next action
```

```yaml
effectful_stage_envelope:
  envelope_schema_version: AOS_EFFECTFUL_STAGE_ENVELOPE_V1
  envelope_id:
  parent_authorization_id:
  parent_authorization_digest:
  parent_authorization_revision:
  state_machine_version: AOS_COMPLETE_TASK_LOOP_V1
  task_id:
  task_revision:
  candidate_identity:
  state_revision:
  event_head_identity:
  transition:
    from: SELECT_NEXT_ACTION | DIAGNOSE
    to: EXECUTE | CORRECT
  worker_action: EXECUTE | CORRECT
  action_spec_digest:
  correction_gate_id:
  correction_gate_digest:
  allowed_operations: []
  allowed_paths: []
  allowed_effects: []
  forbidden_operations: []
  forbidden_paths: []
  forbidden_effects: []
  attempt_ordinal:
  issued_by_controller_identity:
  issued_at:
  expires_at:
  consumed: false
```

Envelope всегда является сужением текущей Parent Task Authorization. Admission
атомарно проверяет exact state/event/candidate/transition/action digest,
актуальную unexpired/unrevoked parent authorization, scope subset/forbidden
superset, required gate и unused envelope. Envelope потребляется до effect.
Для `CORRECT` gate identity/digest обязательны; для `EXECUTE` отсутствуют.

`CHECK` и `FINAL_VALIDATE` используют отдельный read-only ValidationEnvelope с
exact `{from,to}`, state/event/candidate, required checks и read scope. Он не
содержит mutation operations/effects и не преобразуется в Stage Envelope.
Validator возвращает finding; только controller может направить его в
diagnostics и отдельный corrector.

## 8. Completion predicate

```text
TECHNICALLY_COMPLETE =
    каждое acceptance criterion имеет current Evidence
AND каждый required check имеет current PASS
AND candidate соответствует task revision и allowed scope
AND required Evidence относится к exact current candidate
AND material UNKNOWN отсутствуют
AND required findings закрыты или покрыты exact accepted residual-risk record
AND observed mutations/effects согласуются с execution record
AND persistent state сохранено и может быть восстановлено
```

Закрытие всех child steps не доказывает parent completion. Optional check со
статусом `NOT_RUN` допустим только если он действительно optional и ограничение
явно отражено. Required `NOT_RUN` блокирует `TECHNICALLY_COMPLETE`.

Residual risk считается принятым только при наличии Human Decision Record с
exact actor/source provenance, finding identity, candidate identity, declared
scope и decision value. Свободный текст, recommendation или worker claim не
может заполнить `accepted_residual_risk_records`.

После любой semantic mutation прежний candidate PASS считается stale для всех
затронутых checks. Controller сохраняет для affected set основание: changed
paths, dependency/contract edges, behavior boundary и limitations анализа.
Если material impact нельзя определить убедительно, выполняется более широкий
required check либо сохраняется material `UNKNOWN`; completion блокируется.

## 9. Вход в диагностику

Диагностика обязательна, когда:

- focused, affected или final check возвращает `FAIL`;
- наблюдаемое поведение расходится с contract без локализованной причины;
- failure невоспроизводим, observer может быть неисправен или Evidence неполно;
- предлагаемое исправление основано только на правдоподобии;
- одинаковая failure signature сохраняется после коррекции;
- новая ошибка может быть следствием environment/provenance, а не продукта.

До первой effectful correction сохраняются candidate identity, check/command,
expected/actual behavior, stable error class, failure signature, available
Evidence, начальные гипотезы и confidence.

## 10. Многоступенчатая диагностическая лестница

Диагностика начинается с минимальной достаточной boundary. Переход на следующий
уровень обязателен, если причина не найдена, данные совместимы с несколькими
существенными причинами, observer reliability не подтверждена или confidence
недостаточен для bounded correction.

### D0 — Failure binding и надёжность наблюдения

Проверить exact candidate, команду, окружение, expected/actual result,
воспроизводимость, стабильную failure signature и способность observer увидеть
искомое событие. Для отрицательного Evidence нужен положительный control, если
без него отсутствие сигнала ничего не доказывает.

Выход: локализованный однозначный defect либо переход в `D1` с подтверждённой
failure и перечисленными ограничениями наблюдения.

### D1 — Локальная диагностика

Исследовать изменённый компонент, ближайший stack/data path, локальные
инварианты, affected tests и direct contract violation. Очевидный exact RED или
однозначное нарушение может сразу разрешить bounded correction.

Если остаются несколько material hypotheses либо Evidence не объясняет failure,
переход в `D2` обязателен.

### D2 — Различение гипотез

Сформировать минимальный набор конкурирующих гипотез. Для каждой указать
предсказание и выбрать cheapest safe read-only observation или bounded
experiment, который даст разные результаты хотя бы для двух вариантов.

Повтор проверки с неизменными предпосылками не является экспериментом. Если
результат не различил гипотезы или experiment inconclusive, перейти в `D3`.

### D3 — Расширение на соседнюю причинную boundary

Исследовать ближайшие caller/callee, producer/consumer, state transition,
fixture/oracle assumption, repository-local configuration и declared dependency.
Расширяется область reasoning/read-only inspection, но не mutation scope или
authority.

Если причинная цепочка не замкнута либо Evidence указывает на внешний для
компонента фактор, перейти в `D4`.

### D4 — Environment и system boundary

Проверить import/build provenance, interpreter/runtime, process boundary,
filesystem semantics, concurrency/timing, sandbox/permission, platform и уже
разрешённые adapters. Test double, copied source или platform label не считается
доказательством native/system behavior.

Если локальная/system модель всё ещё не объясняет failure либо следующая
коррекция требует materially distinct mechanism, перейти в `D5`.

### D5 — Trajectory и architecture review

Проверить состоятельность текущего подхода: unresolved guarantee, накопленное
Evidence, оставшиеся совместимые причины, повторение эквивалентных corrections,
осцилляцию candidate, соответствие выбранного mechanism принятым contracts и
наличие различающей альтернативы.

Выход:

- новая falsifiable hypothesis и одна bounded correction;
- решение сменить обратимый HOW внутри исходной authority;
- `WAIT_HUMAN` для material product/architecture/authority decision;
- `WAIT_EVIDENCE`, если разрешённая диагностика исчерпана без достаточного
  Evidence и exact next evidence source известен либо требует внешнего события;
- `WAIT_HUMAN`, если Evidence недостаточно и безопасный следующий источник или
  расширение boundary требует решения человека;
- `TASK_FAILED`, если причина известна, но исправление доказанно невозможно в
  текущей task revision или достигнут установленный человеком task hard limit.

### 10.1. Повторный вход в диагностику

Diagnostic state хранит `failure_signature`, `highest_level_reached`,
`last_level`, eliminated hypotheses, observer state и Evidence identities.

- та же failure signature после correction продолжает работу с последнего
  достигнутого уровня и не повторяет уже inconclusive checks;
- новая stable failure signature открывает новый diagnostic record с `D0`, но
  не сбрасывает task ledger или resource usage;
- изменение candidate или observer требует повторного `D0` только для проверки
  новой identity/reliability; затем работа возвращается не ниже ранее
  достигнутой причинной boundary;
- переход на более ранний уровень требует recorded reason и нового Evidence;
- `D5` для той же trajectory не запускается повторно без нового discriminating
  Evidence или material изменения premises.

Если одна correction устранила исходную signature, но открыла другую, records
сохраняются раздельно и связываются причинной ссылкой вместо переименования
старой failure.

## 11. Diagnostic record и критерий убедительности

Каждый уровень дополняет один record:

```yaml
diagnostic_id:
failure_signature:
level: D0 | D1 | D2 | D3 | D4 | D5
highest_level_reached:
previous_diagnostic_event:
observed_facts: []
observer_reliability:
competing_hypotheses: []
predictions: []
discriminating_checks: []
checks_run: []
evidence_gained:
cause_status: PROVEN | PLAUSIBLE | MULTIPLE_COMPATIBLE | NOT_FOUND
confidence: LOW | MEDIUM | HIGH
scope_of_conclusion:
limitations: []
next_level_reason:
reentry_reason:
proposed_disposition:
```

Mutation разрешает только следующий машиночитаемый gate:

```yaml
correction_gate:
  gate_id:
  gate_version: AOS_CORRECTION_GATE_V1
  state_machine_version: AOS_COMPLETE_TASK_LOOP_V1
  parent_authorization_id:
  parent_authorization_revision:
  parent_authorization_digest:
  task_id:
  task_revision:
  state_revision:
  event_head_identity:
  diagnostic_id:
  failure_signature:
  candidate_before_identity:
  proposed_correction_digest:
  authority_match: true
  cause_status: PROVEN | PLAUSIBLE
  confidence: MEDIUM | HIGH
  material_competing_hypotheses: 0
  correction_class: REVERSIBLE_BOUNDED | REVERSIBLE_DIAGNOSTIC
  falsifiable_prediction_id:
  verification_check_ids: []
  rollback_or_recovery_ref:
  evaluated_by_controller_identity:
  evaluated_at:
  decision: ALLOW | DENY
```

`ALLOW` вычисляется только для `PROVEN + MEDIUM|HIGH + REVERSIBLE_BOUNDED` либо
`PLAUSIBLE + HIGH + REVERSIBLE_DIAGNOSTIC`. Дополнительно обязательны valid
authority/state, ноль material competing hypotheses, prediction, исполнимые
checks и recovery reference. Любое отсутствующее поле или другая комбинация
даёт `DENY`. Gate вычисляется до Stage Envelope и применяется только к exact
authorization/state/diagnostic/failure/candidate/proposed-correction tuple. При
`ALLOW` controller создаёт `CORRECT` envelope с gate identity/digest и
`action_spec_digest`, равным `proposed_correction_digest`. Gate не
переиспользуется для другой mutation.
`LOW`, `MULTIPLE_COMPATIBLE`, `NOT_FOUND`, unreliable observer и
inconclusive check требуют расширения диагностики либо `WAIT_*`; свободная
оценка proportional risk mutation не разрешает.

## 12. Correction loop

Каждая effectful correction фиксирует:

```yaml
ordinal:
candidate_before:
failure_signature:
hypothesis:
evidence_before:
semantic_correction:
affected_paths: []
prediction:
checks_rerun: []
result_after:
information_gain:
candidate_after:
```

Исправление не может менять accepted observable behavior ради зелёного теста.
Если contract невыполним без изменения product/architecture boundary,
dependent branch переходит в `WAIT_HUMAN` с одним decision-ready вопросом.

## 13. Progress и anti-loop

Продолжение требует хотя бы одного признака progress:

- ранее failing required check прошёл без равной или большей regression;
- failure boundary измеримо сузилась;
- различающее Evidence опровергло или materially изменило гипотезу;
- Evidence обосновало materially different bounded correction;
- число существенных совместимых гипотез уменьшилось;
- надёжность observer была доказана или восстановлена.

Не являются progress:

- повтор команды при тех же premises;
- переименование hypothesis или failure;
- materially equivalent patch;
- изменение unrelated paths;
- перенос failure между checks без net reduction;
- объяснение без нового Evidence;
- новый worker или session с тем же состоянием.

Controller сохраняет continuous task ledger. Смена worker, session, hypothesis
или diagnostic level не сбрасывает correction count и resource usage.

Локальный default против повторения одной траектории:

```yaml
max_same_failure_corrections_without_progress: 2
max_no_information_gain_checks_per_diagnostic_level: 2
max_equivalent_trajectory_reentry: 0
```

Эти значения ограничивают повторение без progress, а не число разных полезных
исправлений или discriminating checks. `run_allowance` остаётся конечным для
каждого запуска и возобновляется из persistent state. Только explicit
`task_hard_limits` ограничивают всю задачу.

## 14. Расширение диагностики и authority

```text
broader diagnostic reasoning
!= broader mutation scope
!= broader access authority
```

Диагностическая лестница может читать только уже доступные repository-local
источники и выполнять разрешённые Task Contract observations/experiments.
Необходимость сети, credentials, secrets, нового provider, protected resource,
нового writable path, sandbox expansion или destructive effect переводит
affected branch в `WAIT_HUMAN` с exact missing authority/resource.

Независимые безопасные ветви задачи могут продолжаться, если блокер не является
их material dependency.

## 15. Восстановление после прерывания

`RECOVER_STATE` выполняет:

1. rebind repository root, branch/worktree, HEAD и фактический status;
2. сравнение persisted candidate identity с текущими bytes;
3. сверку recorded effects и attempt ledger с наблюдаемым состоянием;
4. классификацию partial/unknown writes;
5. проверку актуальности task revision и authority;
6. invalidation stale check results;
7. выбор безопасного next action.

Неизвестный результат effectful action сначала reconciled. Слепой повтор
запрещён. Если состояние нельзя установить разрешённым чтением, dependent
branch получает run result `UNKNOWN` или `BLOCKED` и task state
`WAIT_EVIDENCE` либо `WAIT_HUMAN` с exact missing input.

## 16. Final validation и возврат в петлю

`FINAL_VALIDATE` использует exact frozen candidate и полный набор required
checks для текущей task revision. Finding не закрывает задачу и не превращается
в автоматический acceptance.

Если correction покрыта исходным Task Contract, controller создаёт новую
candidate identity, возвращает finding в `DIAGNOSE`, выполняет correction и
запускает fresh affected validation. Если correction требует расширения scope
или human-only decision, выполняется `WAIT_HUMAN`.

Independent validation остаётся отдельным read-only run. Controller может
автоматически маршрутизировать его finding обратно в петлю, но validator не
меняет candidate.

## 17. Результаты run и task

| Scope | Result/state | Условие |
|---|---|---|
| task | `TECHNICALLY_COMPLETE` | Completion predicate доказан для exact candidate |
| run | `PAUSED_RESOURCE` | Исчерпан run allowance; task остаётся `ACTIVE` |
| task | `WAIT_EVIDENCE` | Разрешённая диагностика не дала достаточного Evidence; missing input назван точно |
| task | `WAIT_HUMAN` | Не хватает authority или human-only decision |
| task | `TASK_FAILED` | Исправление доказанно невозможно в task revision либо достигнут human task hard limit |
| task | `CANCELLED_BY_HUMAN` | Человек явно отменил exact task |
| task | `CONTRACT_VIOLATION` | Фактическое действие пересекло запрещённую boundary; effects сохранены для disposition |

`TECHNICALLY_COMPLETE/PASS` не означает Human acceptance и не разрешает Git
delivery. `FAIL`, `UNKNOWN` или `BLOCKED` отдельного worker/run сохраняются как
Evidence и сами по себе не закрывают task. `WAIT_*` и `PAUSED_RESOURCE`
возобновляются через `RECOVER_STATE`. Terminal task возобновляется только через
новую task revision либо явное human disposition.

## 18. Проверочные сценарии механизма

Положительные:

1. локальный defect диагностируется на `D1`, исправляется и проходит final check;
2. две совместимые гипотезы различаются на `D2`, correction подтверждает prediction;
3. причина находится на producer/consumer boundary `D3`;
4. source-run ошибочно принимался за installed execution и различается на `D4`;
5. после прерывания controller восстанавливает partial state без повторной записи;
6. final validation finding возвращается в correction loop и новый candidate проходит;
7. несколько разных дефектов последовательно исправляются при измеримом progress.

Обязательные негативные:

1. повтор unchanged failing command не считается progress;
2. equivalent patch после двух бесполезных corrections блокируется anti-loop;
3. `LOW` confidence не разрешает speculative correction;
4. inconclusive `D2` приводит к `D3`, а не к случайному выбору гипотезы;
5. unreliable observer не позволяет сделать вывод из отсутствия сигнала;
6. диагностическое расширение не добавляет writable paths или network authority;
7. неизвестный результат effectful action не retry-ится до reconciliation;
8. required `NOT_RUN` блокирует completion;
9. stale PASS не переносится на новый candidate;
10. validator не исправляет subject;
11. исчерпание budget сохраняется и не сбрасывается новой session;
12. Git action не выводится из технического PASS.
13. исчерпание run allowance даёт `PAUSED_RESOURCE`, а не `TASK_FAILED`;
14. worker output `PASS` не может самостоятельно закрыть criterion или task;
15. второй controller со stale state revision не может перезаписать state;
16. та же failure signature после correction продолжает достигнутый diagnostic level;
17. новая failure signature начинает отдельный `D0`, не сбрасывая общий ledger;
18. пустые authority allowlists не разрешают mutation;
19. residual risk без exact Human Decision Record не закрывает finding;
20. неизвестный impact mutation расширяет required checks или блокирует completion;
21. next-action selector сначала reconciles unknown effect и required blockers.
22. Task Contract до отдельной human authorization не содержит выдуманную authorization identity;
23. lifecycle stage, controller action, task state и run state не подменяют друг друга;
24. stale state/event head либо revoked/changed parent authorization отклоняет Stage Envelope;
25. `ALLOW` Correction Gate нельзя replay для другого diagnostic, candidate, correction или envelope.
26. различие proposed correction и Stage Envelope `action_spec_digest` даёт `DENY` до mutation.
27. prohibited effect нельзя вернуть через более узкий envelope или action spec.

## 19. Минимальный implementation slice

Первая реализация механизма должна включать:

- versioned Task Contract и persistent Loop State;
- separate task/run state axes и resumable `PAUSED_RESOURCE`;
- separate Parent Task Authorization и derived consumable Stage Envelopes;
- canonical `AOS_COMPLETE_TASK_LOOP_V1` controller-action matrix;
- single-controller/CAS protection и tamper-evident event chain;
- priority-ordered next-action selector;
- ledger observations, checks, diagnostics и corrections;
- уровни `D0…D5` с обязательным escalation predicate;
- diagnostic re-entry по stable failure signature;
- progress/anti-loop evaluator;
- machine-readable Correction Gate evaluator;
- completion predicate evaluator;
- exact residual-risk decision и affected-check Evidence bindings;
- recovery/reconciliation после controlled interruption;
- machine-readable terminal report;
- fixtures для сценариев раздела 18.

Первая реализация не требует daemon, server, database, multi-agent scheduler,
RAG, UI, network provider, CI integration или Git automation.

## 20. Связь с текущими владельцами

- `docs/00_Core.md` владеет authority и Minimal Safety Floor.
- `docs/03_Development.md` владеет общим workflow и stage boundaries.
- `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md` задаёт lightweight implementation
  flow, engineering autonomy и bounded correction.
- `workspace/AOS3_IMPLEMENTATION_READY_DRAFT.md` задаёт будущий AOS-3 target,
  test strategy и implementation sequence.
- AOS-3 `docs/development/03_DEVELOPMENT.md` использован как read-only reference
  для finite same-envelope retry, progress ledger и bounded escalation.

Этот DRAFT предлагает будущую harmonization владельцев. Он не меняет canonical
workflow, не активирует implementation и не переносит authority из reference.

## 21. Критерии принятия дизайна

Дизайн готов к implementation planning, когда человек подтверждает exact
revision и одновременно принимает:

1. persistent controller как владельца continuation state;
2. автоматический возврат final validation finding в diagnostic/correction loop
   внутри исходного Task Contract;
3. обязательное расширение `D0 → D5` при недостаточном Evidence;
4. progress-based anti-loop, конечный run allowance и только human-defined
   task hard limits;
5. completion predicate раздела 8;
6. сохранение Human/Git/protected boundaries.

Review correction `R2` также требует принять разделение task/run limits,
parent/stage authority, single-controller state ownership, diagnostic re-entry,
exact residual-risk binding, impact Evidence и priority selector. Эти уточнения
закрывают `REVIEW-F001…F008`, но требуют повторного review exact R2 bytes.

## 22. Текущий статус

```yaml
design_construction: COMPLETE_R2
design_self_review: PASS
human_review_of_exact_artifact: NOT_RUN
review_findings_addressed:
  - REVIEW-F001
  - REVIEW-F002
  - REVIEW-F003
  - REVIEW-F004
  - REVIEW-F005
  - REVIEW-F006
  - REVIEW-F007
  - REVIEW-F008
implementation_plan: NOT_RUN
runtime_implementation: NOT_RUN
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
```
