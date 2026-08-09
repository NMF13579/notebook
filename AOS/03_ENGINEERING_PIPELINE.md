# 03 — Engineering Workflow & Contract Semantics

## UPSTREAM_ALIGNMENT
* **Aligned claims:** Границы, установленные в Product Model (напр. разделение Commit ≠ Push ≠ Merge ≠ Release, и разделение Evidence и approval), строго соответствуют Engineering workflow. Концепции Task Brief и Authorization из Architecture корректно транслируются в Engineering Contracts.
* **Upstream-only claims:** Сценарии J-001..J-007, абстрактные архитектурные слои (L1-L5) и компоненты не дублируются в workflow. Документ описывает design-level semantics защищённой работы и контрактные границы, а не implementation mechanics.
* **UPSTREAM_FINDING:** NONE.

## 1. Protected Work Stage Semantics
Стадии задают наблюдаемые границы защищённой работы. Они не определяют algorithms, schemas, storage, adapters или другие implementation mechanics.
* **PLAN**
  * **Purpose:** Read-only стадия для формирования плана задачи.
  * **Produced result:** Decision-ready Task Brief, risks, validation, stop conditions.
* **EXECUTE**
  * **Purpose:** Выполнение работы в строгих границах.
  * **Entry condition:** Exact authorized scope (наличие явной Execution Authorization).
  * **Safety / stop boundary:** Выполняется как одна стадия (one stage), без скрытых переходов на следующую стадию, без посторонней очистки (no unrelated cleanup). При терминальном результате — формируется отчет и происходит остановка (report and stop).
* **VALIDATE**
  * **Purpose:** Сбор независимых доказательств и запуск проверок.
  * **Entry condition:** Точный неизменяемый кандидат (Read-only exact candidate). Стадия не вносит исправлений (Does not fix).
  * **Safety / stop boundary:** Независимая валидация требуется только при соответствующем риске. Запрещены скрытые мутации (correction) внутри валидации.
* **REVIEW**
  * **Purpose:** Предоставление результатов на проверку человеку (Read-only assessment/recommendation).
  * **Safety / stop boundary:** Запрещены симуляция принятия решения (no simulated acceptance) или исправления.

*(Примечание: DELIVER не является стадией пайплайна, а относится к семантике передачи данных — Handoff).*

## 2. Delivery / Handoff Semantics
* **Purpose of Handoff:** Handoff package — это не стадия пайплайна и не разрешение на Git-операции, а безопасная передача контекста.
* **Preservation of state:** Handoff фиксирует repo identity, task/candidate, result, changes, checks, blockers, decisions, permissions и next action. Мутирующие факты перепроверяются при возобновлении (resume).
* **Git Delivery Boundaries:** Edit ≠ Commit ≠ Push ≠ Merge ≠ Release. Каждое действие требует отдельной перепроверки (reverify repo/branch/HEAD/candidate/worktree/remote/auth).
* **Separation Rules:** `PASS ≠ approval`, `Evidence ≠ approval`, `NOT_RUN ≠ PASS`. Успешная передача контекста или успешное прохождение тестов не заменяет явного решения человека.

## 3. Engineering Workflow Contracts C-005..C-014
Определяют design-level semantics артефактов, authority и handoff boundaries (WHAT / BOUNDARIES). Точные schemas, I/O, lifecycle mechanics, storage, producer/consumer, serialization и implementation APIs — **[UNKNOWN]** или **[NOT_SPECIFIED_AT_THIS_LEVEL]** и не принадлежат этому документу.
* **C-005 Task Brief:** Описывает goal/scope/constraints/validation. Не предоставляет разрешений на выполнение.
* **C-006 Execution Authorization Record:** Создаётся отдельно человеком, жёстко привязан к точной задаче (bind to exact task/subject), ограничен стадией/операциями/путями, имеет таймер/счетчик (expiry/consumption) и не разрешает Git-действия.
* **C-007 Preflight / Preview:** Фиксирует exact repository/worktree/branch/HEAD/baseline/status/diff, планируемые действия и конфликты.
* **C-008 Execution Record:** Отчет о мутациях (Starting identity, auth identity, actual mutations, side effects, limitations, stop reason).
* **C-009 ValidationEnvelope:** Агрегирует результаты (required/optional checks, NOT_RUN, limitations, fail-closed aggregation).
* **C-010 Evidence Record:** Единица доказательства (Evidence kind, method/command, result, locator/digest, limitations).
* **C-011 Human Review / Decision:** Записывает опции и явное решение человека (explicit human decision). Сгенерированное (симулированное) решение недействительно.
* **C-012 Project Memory / Handoff:** Сохраняет принятые решения, blockers, состояние авторизации и одно следующее действие (one next action).
* **C-013 Install / Update Manifest:** Управляет ownership classes, operations, preview binding, conflicts.
* **C-014 Git Delivery Record:** Раздельные записи (Separate records) для Commit, Push, Merge и Release.

## 4. Validation & Evidence
* **Verification Gates (для Runtime):** 1. Structure, 2. Scope, 3. Acceptance, 4. Regression/smoke, 5. Security/release blockers.
* **Validation Protocol:** Freeze subject → verify provenance → run targeted checks → wider suite if relevant → record commands/results → preserve required/optional → classify limitations → inspect diff → verify no validation mutation → stop with one next action.
* **Strict Separation:** Если находка (finding) требует изменения проверяемого кода (subject) — это инициирует отдельную задачу на коррекцию (EXECUTE scope). Валидация не вносит изменений.

## 5. Failure & Recovery
* **Execution Failure:** Приводит к остановке (stop), сохранению состояния и логов (preserve state/logs), классификации частичных записей (partial writes).
* **Stop Behavior:** Автоматические повторные попытки (auto-retry) строго запрещены, если сбой изменяет scope, identity, permissions или требования к решениям человека.
* **Recovery:** Исправление ошибок (correction) выносится в отдельную задачу. Точная механика отката (rollback) или транзакционности **[NOT_SPECIFIED_AT_THIS_LEVEL]**.

## 6. Engineering Traceability
Подтверждённые связи (от намерений до контрактов реализации):
* `Product semantic (Explicit authorization)` → `Architecture (Execution permission owner)` → `Engineering Stage (EXECUTE entry)` → `Contract (C-006 Execution Authorization Record)`.
* `Product semantic (Human verdict)` → `Architecture (Human decision owner)` → `Engineering Stage (REVIEW exit)` → `Contract (C-011 Human Review / Decision)`.
*(Остальные полные графы маппинга — NOT_SPECIFIED_AT_THIS_LEVEL).*

## 7. Preserved UNKNOWN
Следующие implementation decisions сохраняются как UNKNOWN и должны быть разрешены до зависящей от них реализации. Они не блокируют design foundation и не входят в ownership этого документа:
* Exact schemas, exact I/O, serialization, storage для всех C-005..C-014.
* Точные Producer / Consumer для артефактов.
* Implementation adapters, CI implementation, release implementation.
* Language/toolchain, implementation repository, persistence механика.
* Exact contract lifecycle и точный граф переходов между стадиями.
* Exact handoff data format.
